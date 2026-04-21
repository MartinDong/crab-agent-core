function extractApiKeys() {
  const patterns = [
    /bce-v3\/AL[^\s"'<>]+/g,
    /bce-v3\/AL[^\s]+?/g,
    /bce-v3\/AL[a-zA-Z0-9\-_\/]+/g
  ];
  
  const allMatches = [];
  const sources = [
    document.documentElement.innerHTML,
    document.documentElement.textContent,
    document.body.innerHTML,
    document.body.textContent
  ];
  
  const scripts = document.querySelectorAll('script');
  scripts.forEach(script => {
    sources.push(script.textContent);
    if (script.src) {
      try {
        sources.push(script.getAttribute('src') || '');
      } catch (e) {
        // Ignore errors
      }
    }
  });
  
  for (const pattern of patterns) {
    for (const source of sources) {
      const matches = source.match(pattern) || [];
      allMatches.push(...matches);
    }
  }
  
  return [...new Set(allMatches)];
}

function isValidApiKey(key) {
  let cleanedKey = key.trim();
  cleanedKey = cleanedKey.replace(/^['"]+|['"]+$/g, '');
  cleanedKey = cleanedKey.replace(/^[\[\]{}(),;:.]+|[\[\]{}(),;:.]+$/g, '');
  
  if (cleanedKey.includes('ALTAK-') || cleanedKey.includes('ALTAKSP-')) {
    return false;
  }
  const asteriskCount = (cleanedKey.match(/\*/g) || []).length;
  const totalLength = cleanedKey.length;
  if (asteriskCount > totalLength * 0.5) {
    return false;
  }
  if (cleanedKey.includes('...')) {
    return false;
  }
  if (cleanedKey.length < 20) {
    return false;
  }
  return true;
}

function scanPage() {
  const keys = extractApiKeys().filter(isValidApiKey);
  if (keys.length > 0) {
    chrome.runtime.sendMessage({ type: 'ADD_KEYS', keys });
  }
}

function debounce(func, wait) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
}

const debouncedScan = debounce(scanPage, 500);

document.addEventListener('DOMContentLoaded', debouncedScan);
window.addEventListener('load', debouncedScan);

const observer = new MutationObserver(debouncedScan);
observer.observe(document.body, {
  childList: true,
  subtree: true,
  characterData: true
});

debouncedScan();
