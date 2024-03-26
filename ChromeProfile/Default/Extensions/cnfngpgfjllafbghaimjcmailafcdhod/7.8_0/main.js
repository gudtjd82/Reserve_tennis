function localizeHtmlPage()
{
    //Localize by replacing __MSG_***__ meta tags
    var objects = document.getElementsByTagName('html');
    for (var j = 0; j < objects.length; j++)
    {
        var obj = objects[j];

        var valStrH = obj.innerHTML.toString();
        var valNewH = valStrH.replace(/__MSG_(\w+)__/g, function(match, v1)
        {
            return v1 ? chrome.i18n.getMessage(v1) : "";
        });

        if(valNewH != valStrH)
        {
            obj.innerHTML = valNewH;
        }
    }
}


// 글자 수 계산 함수
function calculateLength() {

	var textarea = document.getElementById("mystr");
	var text = textarea.value;
	var length2 = text.length;

	// 공백 제외
	text = text.replace(/\s/g, "");
	var length1 = text.length;

	document.getElementById("cnt_char1").innerText = length1.toLocaleString();
	document.getElementById("cnt_char2").innerText = length2.toLocaleString();
}


chrome.runtime.onMessage.addListener(function (request, sender) {
  if ( request.action == "releaseDrag") {

    var lbl_message = document.getElementById("lbl_message");
    lbl_message.innerText = request.source;

  }
});

document.addEventListener("DOMContentLoaded", function () {

	// 지역언어 표시
	localizeHtmlPage();

	// 버전정보 표시
	document.getElementById("span_version").innerText = chrome.runtime.getManifest().version;

	// 단축키정보 표시
	chrome.commands.getAll(function(commandinfo) {
		commandinfo.forEach(function (item, index, array) {
			if ( item.name === "releasedrag") {
				document.getElementById("span_shortcut").innerText = item.shortcut.length === 0 ? chrome.i18n.getMessage("string008") : item.shortcut;
			}
		});
	});

	// 단축키버튼
	var btn_shortcut = document.getElementById("btn_shortcut");
	btn_shortcut.addEventListener("click", function() {
		chrome.tabs.create({ url: "chrome://extensions/shortcuts" });
	});

    var btn_show_click = document.getElementById("btn_show_click");
    var btn_hide_click = document.getElementById("btn_hide_click");

    btn_show_click.addEventListener("click", function() {
        document.getElementById("box_char").style.display = "block";
        btn_show_click.style.display = "none";
        chrome.storage.sync.set({ "dragfreestorage2": { "showbox": "1" } });
    });

    btn_hide_click.addEventListener("click", function() {
        document.getElementById("box_char").style.display = "none";
        btn_show_click.style.display = "block";
        chrome.storage.sync.set({ "dragfreestorage2": { "showbox": "0" } });
    });

	// Click 버튼
	var btn_click = document.getElementById("btn_click");
	btn_click.addEventListener("click", function() {


		chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
			chrome.tabs.sendMessage(tabs[0].id, {greeting: "releasedragandmagicbutton"});
		});

		document.getElementById("lbl_message").innerText = chrome.i18n.getMessage("string010");
	});

	// 광고보기 버튼
	var btn_ad = document.getElementById("btn_ad");
	btn_ad.addEventListener('click', function() {
		chrome.tabs.create({ url: 'http://adv.kongmemo.com' });
	}, false);

    // 저장하기 버튼
    var btn_save = document.getElementById("btn_save");
    btn_save.addEventListener("click", function () {

        var radio_always_1 = document.getElementById("radio_always_1");

        chrome.storage.sync.set({ "dragfreestorage": { "always": radio_always_1.checked ? "1" : "0" } }, function () {
 
			if ( radio_always_1.checked ) {

				chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
					chrome.tabs.sendMessage(tabs[0].id, {greeting: "releasedragandmagicbutton"});
				});

			}
			
            location.href = "main.html";
        });

    });


    // 이벤트 리스너 추가
	var textarea = document.getElementById("mystr");
    textarea.addEventListener("input", calculateLength);


    chrome.storage.sync.get("dragfreestorage", function (items) {
        
		var radio_always_1 = document.getElementById("radio_always_1");
        var radio_always_0 = document.getElementById("radio_always_0");

		try
		{
			var dragfree_always = items["dragfreestorage"].always;

			var use_always = dragfree_always === undefined || dragfree_always === "0" ? false : true;
			radio_always_1.checked = use_always;
			radio_always_0.checked = !use_always;

			document.getElementById("div_click").style.display = radio_always_1.checked ? "none" : "block";


		}
		catch (exception)
		{
			radio_always_1.checked = false;
			radio_always_0.checked = true;
		}

    });

    chrome.storage.sync.get("dragfreestorage2", function (items) {
        
        try {
            var showbox = items["dragfreestorage2"].showbox;
            var is_showbox = showbox === "1";
            document.getElementById("box_char").style.display = is_showbox ? "block" : "none";
            btn_show_click.style.display = is_showbox ? "none" : "block";
        }
        catch (exception) {
            // 기본값 설정
            btn_show_click.style.display = "block";
            document.getElementById("box_char").style.display = "none";
        }

    });



});