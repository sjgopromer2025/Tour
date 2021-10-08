//$(document).ready(function(){
//	change();
//});


function explain() {
	var selectvalue = $("#jeonbuk").val();
	var text = "";
	if(selectvalue === "군산")
	{
		text = "※군산 워드클라우드는 지역 명소인 초원사진관의 외형을 본 따 만들었습니다.";
		$("#tag_explain").html(text);
	}else if( selectvalue === "부안")
	{
		text = "※부안 워드클라우드는 변산해수욕장에서 자주 볼 수 있는 조개의 외형을 본 따 만들었습니다.";
		$("#tag_explain").html(text);
	}else if( selectvalue === "김제")
	{
		text = "※김제 워드클라우드는 지역 명소인 김제 벽골제 쌍룡의 외형을 본 따 만들었습니다.";
		$("#tag_explain").html(text);
	}else if( selectvalue === "정읍")
	{
		text = "※정읍 워드클라우드는 내장산의 아름다운 단풍잎의 외형을 본 따 만들었습니다.";
		$("#tag_explain").html(text);
	}else if( selectvalue === "완주")
	{
		text = "※완주 워드클라우드는 화산면에서 키운 튼실한 소의 외형을 본 따 만들었습니다.";
		$("#tag_explain").html(text);
	}else if( selectvalue === "익산")
	{
		text = "※익산 워드클라우드는 유네스코 세계문화유산인 미륵사지석탑의 외형을 본 따 만들었습니다.";
		$("#tag_explain").html(text);
	}else if( selectvalue === "임실")
	{
		text = "※임실 워드클라우드는 특산품 임실 치즈의 외형을 본 따 만들었습니다.";
		$("#tag_explain").html(text);
	}else if( selectvalue === "전주")
	{
		text = "※전주 워드클라우드는 지역 명소인 풍남문의 외형을 본 따 만들었습니다.";
		$("#tag_explain").html(text);
	}
}

function change()
{
	var selectjeonbuk = document.getElementById("jeonbuk");

	var selectedValue = selectjeonbuk.options[selectjeonbuk.selectedIndex].value;
	// select element에서 선택된 option의 text가 저장된다.
    var selectedText = selectjeonbuk.options[selectjeonbuk.selectedIndex].text;
	//alert(selectedValue);
	//alert(selectedText);
	$.ajax({
		url: "../ajax/instaload.jsp",
		type: "post",
		dataType: "html",
		data: "word="+selectedValue,
		success : function(data) 
		{
			data = data.trim();
			//alert(data);	
			pic_arr = data.split("<<SEP>>");
			$("#tag").attr("src", "../Instagram/"+pic_arr[0]); //해시태그
			$("#place").attr("src", "../Instagram/"+pic_arr[1]); //장소
			explain();
			i_drawBar(pic_arr[2],pic_arr[3]);
		},
		error: function(request, status, error) 
		{
			alert("error!!!");
		}
	});	
}