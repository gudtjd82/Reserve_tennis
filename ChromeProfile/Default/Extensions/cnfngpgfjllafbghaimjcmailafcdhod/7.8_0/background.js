chrome.commands.onCommand.addListener(function (command) {
    if (command === "releasedrag") {

		chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
			chrome.tabs.sendMessage(tabs[0].id, {greeting: "releasedragandmagicbutton"});
		});
	
	}
});