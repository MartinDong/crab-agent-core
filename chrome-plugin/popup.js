document.addEventListener('DOMContentLoaded', () => {
  const keysList = document.getElementById('keysList');
  const noKeys = document.getElementById('noKeys');
  const clearBtn = document.getElementById('clearBtn');

  function loadKeys() {
    chrome.storage.local.get(['apiKeys'], (result) => {
      const keys = result.apiKeys || [];
      keysList.innerHTML = '';
      if (keys.length === 0) {
        noKeys.style.display = 'block';
      } else {
        noKeys.style.display = 'none';
        keys.forEach(key => {
          const keyItem = document.createElement('div');
          keyItem.className = 'key-item';
          
          const keyText = document.createElement('div');
          keyText.className = 'key-text';
          keyText.textContent = key;
          
          const keyActions = document.createElement('div');
          keyActions.className = 'key-actions';
          
          const copyBtn = document.createElement('button');
          copyBtn.className = 'btn btn-success';
          copyBtn.textContent = 'Copy';
          copyBtn.addEventListener('click', () => {
            navigator.clipboard.writeText(key).then(() => {
              copyBtn.textContent = 'Copied!';
              setTimeout(() => {
                copyBtn.textContent = 'Copy';
              }, 2000);
            });
          });
          
          keyActions.appendChild(copyBtn);
          keyItem.appendChild(keyText);
          keyItem.appendChild(keyActions);
          keysList.appendChild(keyItem);
        });
      }
    });
  }

  clearBtn.addEventListener('click', () => {
    chrome.storage.local.set({ apiKeys: [] }, () => {
      loadKeys();
    });
  });

  loadKeys();

  chrome.storage.onChanged.addListener(() => {
    loadKeys();
  });
});
