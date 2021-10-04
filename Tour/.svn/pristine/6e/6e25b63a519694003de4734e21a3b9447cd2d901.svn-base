function goMap(place)
{
	var pv = 0;
	var text = "";
	
	if(place == "전주")
	{
		pv = 1;
	}else if(place == "익산")
	{
		pv = 6;
	}else if(place == "군산")
	{
		pv = 11;
	}else if(place == "정읍")
	{
		pv = 16;
	}else if(place == "김제")
	{
		pv = 21;
	}else if(place == "완주")
	{
		pv = 26;	
	}else if(place == "임실")
	{
		pv = 31;
	}else if(place == "부안")
	{
		pv = 36;
	}	
	
	for (i = pv ; i < (pv+5); i++)
	{
		//alert($("#p_"+i).html());
		text += $("#p_"+i).html() + ",";
	}
	
	$("#place").val(place);
	$("#data").val(text);
	
	$("#gomapform").submit();
	
}