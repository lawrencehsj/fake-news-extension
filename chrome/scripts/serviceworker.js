
chrome.tabs.onUpdated.addListener(() => {
    chrome.tabs.query({ active: true, }, function (tab) {
        // get the url of the current window
        console.log(tab[0].title)
        var input = tab[0].title;
        // send a request from content script to extension
        chrome.tabs.sendMessage(tab[0].id, {"message": "got_title"});
        console.log('sent message');
        tabId = tab[0].id;
        chrome.tabs.sendMessage(tabId, {greeting: input}, function(response) {
              console.log(response.farewell);
    });
    });
  });