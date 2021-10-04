<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../include/head.jsp"%>
<%@ page import="tourDTO.*" %> 
<%@ page import="tourVO.*" %>
<%
wcDTO dto = new wcDTO();	
String image_name = dto.load_name();
%>

<tr>
	<td align="center" style="width: 100%; height:700px;" >	
		<h1>월드컵</h1>
		<p id="cal"></p>
		<div>
			<div style="display:inline-block;">
				<figure class="perfromimg"  id="pause" onclick="javascript:change(0);">
					<img id="image"  class="imgs"  >
						<figcaption >
							<bm id="place1"></bm>
							<hr></hr>
							<p id="local1"></p>
							<p id="location1"></p>
							<p id="explain1"></p>
							<p id="relate1"></p>
						</figcaption>
				</figure>
		</div>
			<div style="display:inline-block;">
				<figure class="perfromimg" onclick="javascript:change(1);" >
					<img id="images" class="imgs"   >
						<figcaption>
							<bm id="place2"></bm>
							<hr></hr>
							<p id="local2"></p>
							<p id="location2"></p>
							<p id="explain2"></p>
							<p id="relate2"></p>
						</figcaption>
				</figure>
			</div>
		</div>
	</td>
</tr>
<tr>
	<td align="center" style="width: 100%;"  >
		<span style="display: none;" id="courselink"><font size="16pt">하이요</font></span>
	</td>
</tr>
<script>

text ="";
var images=[];
var sImages = [];

//var image_name = ["군산선유도해수욕장","군산철길마을","김제벽골제","김제아리랑문학마을","부안직소폭포","부안채석강","완주아원고택","완주위봉사","익산미륵사지","익산바람개비마을","임실사선대 조각공원","임실치즈테마파크","전주동물원","전주한옥마을","제이포렛","허브원"];

var image_name = "<%=image_name %>";
var image_name = image_name.split(",");
image_name.pop();

var cnt=0;
var num=0;
var sNum = 0;
var cnt2=0;
var end = 0;

function show(){

	for(i=0; i<16; i++)
	{
		images[i]= image_name[i]+".png";
	}
	images.sort(function(a,b){return 0.5- Math.random()});
	showImg(num);
}

show(0);		


function getinfo(place1,place2)
{
	
	$.ajax({
		url: "../ajax/worldcupload.jsp",
		type: "post",
		dataType: "html",
		data: "place1="+place1+"&place2="+place2,
		success : function(data) 
		{
			data = data.trim();
			//alert(data);
			Reflect(data);
		},
		error: function(request, status, error) 
		{
			alert("error!!!");
		}
	});		
}

function Reflect(data)
{
	data_arr = data.split("<<!MIX!>>");
	place1 = data_arr[0].split("<<PC1>>");
	place2 = data_arr[1].split("<<PC2>>");
	
	
	$("#local1").html("장소 : " + place1[0]);
	$("#location1").html("위치 : " + place1[1]);
	$("#explain1").html("설명 : " + place1[2]);
	$("#relate1").html("관련어 : " + place1[3]);
	
	$("#local2").html("장소 :" + place2[0]);
	$("#location2").html("위치:" + place2[1]);
	$("#explain2").html("설명 :" + place2[2]);
	$("#relate2").html("관련어 :" + place2[3]);
}




function showImg(num){
	if(end != 1)
	{
		place2 = images[num+1];	
	}else
	{
		place2 ="";
	}
	document.getElementById('image').src=images[num];
	document.getElementById('images').src=place2;	
	cnt2++;
	place1 = images[num].replace(".png","");
	place2 = place2.replace(".png","");	
	getinfo(place1,place2)
	$("#place1").html(place1);
	$("#place2").html(place2);
	
}

function change(n){
	if(cnt2<19)
	{
		cnt++;
		if(n == 0)
			sImages[sNum++] = images[num];
		else
			sImages[sNum++] = images[num+1];
		num+=2;

		if(cnt == images.length/2){
			for(i=0; i<sImages.length; i++){
				images[i] = sImages[i];
				sImages[i] = null;
			}
			if(cnt < 2 )
			{
				text = "우승";
				document.getElementById('cal').innerHTML=text;
				document.getElementById('image').src=images[0];
				$("#images").css('display',"none");
				$("#pause").attr('onclick',"");
				$("#courselink").css('display',"inline");
				num = 0;
				end = 1;
				
			}else
			{
				if(cnt > 2)		
				{	
					text = cnt +"강";
				}else
				{
					text = "결승";
				}
				document.getElementById('cal').innerHTML=text;
				images.splice(cnt);
				cnt = 0;
				num = 0;
				sNum = 0;
			}
		}
		showImg(num);
	}
}



document.getElementById('cal').innerHTML=text;


</script>

<%@ include file="../include/tail.jsp"%>	