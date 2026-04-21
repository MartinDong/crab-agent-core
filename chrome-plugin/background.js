function cleanKey(key) {
  let cleaned = key.trim();
  cleaned = cleaned.replace(/^['"]+|['"]+$/g, '');
  cleaned = cleaned.replace(/^[\[\]{}(),;:.]+|[\[\]{}(),;:.]+$/g, '');
  return cleaned;
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'ADD_KEYS') {
    const { keys } = message;
    const cleanedKeys = keys.map(cleanKey).filter(key => key.length > 0);
    chrome.storage.local.get(['apiKeys'], (result) => {
      const existingKeys = result.apiKeys || [];
      const newKeys = cleanedKeys.filter(key => !existingKeys.includes(key));
      if (newKeys.length > 0) {
        const updatedKeys = [...existingKeys, ...newKeys];
        chrome.storage.local.set({ apiKeys: updatedKeys }, () => {
          console.log('API keys stored:', newKeys);
        });
      }
    });
  }
});
