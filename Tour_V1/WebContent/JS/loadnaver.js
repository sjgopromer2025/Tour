//$(document).ready(function(){
//	ch();
//});
function explain() {
	var selectvalue = $("#loc").val();
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




function ch() 
{
	
	$.ajax({
		url: "../ajax/naverok.jsp",
		type: "post",
		dataType: "html",
		data: "loc=" + $("select[name=loc]").val()+"&nav_week=" + $("select[name=nav_week]").val(),
		success : function(data) 
		{
			data = data.trim();
			data_arr = data.split("<<SEP>>"); 
			$("#blog").attr("src", "../nav_image/"+data_arr[0]);
			explain();
			n_drawBar(data_arr[1],data_arr[2]);
			//alert(data);
		},
		error: function(request, status, error) 
		{
			alert("error!!!");
		}
	});	
}	