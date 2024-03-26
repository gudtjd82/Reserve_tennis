function releaseDetectFunction(isauto) {

		try
		{
			var currentUrl = window.location.toString();
			
			// 다음블로그 처리
			if ( !isauto || currentUrl.indexOf("blog.daum.net") != -1 ) {
				document.addEventListener('mousedown', function(event) {
					event.stopPropagation();
				}, true);
				document.addEventListener('mouseup', function(event) {
					event.stopPropagation();
				}, true);
			}

			var isExcludeSite = 
				currentUrl.indexOf(".google.") != -1 || 
				currentUrl.indexOf(".openai.") != -1 ||  
				currentUrl.indexOf(".twitch.") != -1 ||  
				currentUrl.indexOf(".youtube.") != -1 || 
				currentUrl.indexOf(".afreecatv.") != -1 || 
				currentUrl.indexOf("shopping.naver.") != -1 || 
				currentUrl.indexOf("cloud.naver.") != -1 || 
				currentUrl.indexOf("office.naver.") != -1 || 
				currentUrl.indexOf("mail.naver.") != -1 || 
				currentUrl.indexOf("mail.daum.") != -1 || 
				currentUrl.indexOf(".interpark.") != -1 || 
				currentUrl.indexOf(".11st.") != -1 || 
				currentUrl.indexOf(".gmarket.") != -1 || 
				currentUrl.indexOf(".coupang.") != -1 || 
				currentUrl.indexOf(".wemakeprice.") != -1 || 
				currentUrl.indexOf(".auction.") != -1 || 
				currentUrl.indexOf(".gooroomee.") != -1 || 
				currentUrl.indexOf("map.naver.") != -1 || 
				currentUrl.indexOf("map.kakao.") != -1 || 
				currentUrl.indexOf(".aliexpress.") != -1 ||
				currentUrl.indexOf(".netflix.") != -1 ||
				currentUrl.indexOf(".tving.") != -1 ||
				currentUrl.indexOf(".spotvnow.") != -1 ||
				currentUrl.indexOf(".wavve.") != -1 ||
				currentUrl.indexOf(".coupangplay.") != -1 ||
				currentUrl.indexOf(".disneyplus.") != -1 ||
				currentUrl.indexOf(".primevideo.") != -1 ||
				currentUrl.indexOf(".slack.") != -1 ||
				currentUrl.indexOf(".tmon.") != -1;


			// 구글문서 제외
			if ( !isauto || !isExcludeSite ) {
				document.addEventListener('keydown', function(event) {
					// 엔터키, 백스페이스, Ctrl+엔터의 경우 event.stopPropagation()을 호출하지 않음
					if (!(event.keyCode === 13 || event.keyCode === 8 || (event.ctrlKey && event.keyCode === 13))) {
						event.stopPropagation();
					}
				}, true);
				document.addEventListener('keyup', function(event) {
					// 엔터키, 백스페이스, Ctrl+엔터의 경우 event.stopPropagation()을 호출하지 않음
					if (!(event.keyCode === 13 || event.keyCode === 8 || (event.ctrlKey && event.keyCode === 13))) {
						event.stopPropagation();
					}
				}, true);

				document.addEventListener('dragstart', function(event) {
					event.stopPropagation();
				}, true);
				document.addEventListener('selectstart', function(event) {
					event.stopPropagation();
				}, true);
				document.addEventListener('copy', function(event) {
					event.stopPropagation();
				}, true);

				document.addEventListener('contextmenu', function(event) {
					event.stopPropagation();
				}, true);
		
				var allelements = document.getElementsByTagName("*");
				for (i=0 ; i<allelements.length; i++ ) {
					var elem = allelements[i];
					elem.removeAttribute('oncontextmenu');
					elem.removeAttribute('onselectstart');
					elem.removeAttribute('ondragstart');
					elem.style.setProperty('user-select', 'auto', 'important');
				}
		
				// 모든 iframe 요소를 선택
				var iframes = document.getElementsByTagName('iframe');

				for (var i = 0; i < iframes.length; i++) {
					try {
						// 각 iframe의 내부 문서에 접근
						var innerDoc = iframes[i].contentDocument || iframes[i].contentWindow.document;

						// 내부 문서의 모든 요소를 선택
						var allelements = innerDoc.getElementsByTagName("*");

						for (var j = 0; j < allelements.length; j++) {
							var elem = allelements[j];
							elem.removeAttribute('oncontextmenu');
							elem.removeAttribute('onselectstart');
							elem.removeAttribute('ondragstart');
							elem.style.setProperty('user-select', 'auto', 'important');
						}
					} catch (error) {
						// 동일 출처 정책 위반 등으로 인한 에러 처리
						// console.log("Cannot access iframe content:", error);
					}
				}

			}

		}
		catch (exception)
		{
			//console.log(exception.toString());
		}

}


// 인젝션되면 백그라운드로 통보해줌
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.greeting == "releasedragandmagicbutton") {
        releaseDetectFunction(false);
    }
});



chrome.storage.sync.get("dragfreestorage", function (items) {

    if (items && items["dragfreestorage"]) {
        var dragfree_always = items["dragfreestorage"].always;

        var use_always = dragfree_always === undefined || dragfree_always === "0" ? false : true;
        
        if ( use_always === true ) {
            releaseDetectFunction(true);
        }
    }
});
