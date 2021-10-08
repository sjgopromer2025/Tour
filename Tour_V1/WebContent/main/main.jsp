<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../include/head.jsp"%>
<script>
$(document).ready(function() {
	  var swiper = new Swiper(".mySwiper", {
	        slidesPerView: 1,
	        spaceBetween: 30,
	        effect:'fade',
	        loop: true,
	        pagination: {
	          el: ".swiper-pagination",
	          clickable: true,
	        },
	        navigation: {
	          nextEl: ".swiper-button-next",
	          prevEl: ".swiper-button-prev",
	        }
	      });
	});

function goworldcup() {
	document.location = "../worldcup/worldcup.jsp";
}
function golocalpage(id) {
	document.location = "../local/insta.jsp?word="+id;
}

</script>
<style>
.swiper-wrapper > div
{
	cursor: pointer;
}
.pagemovespan > span
{
	background-color : red;
	height: 100px;
	width: 100px;
}
.mainlocal > td
{
	text-align: center;
	
}
.mainlocaltd
{
	background-color : white;  
	border-color: solid 1px #eeeeee;
}
#keyword 
{
  text-transform: uppercase;
  font-size: 20px;
  
  text-decoration: none;
  position: relative;
  display: block;
}
#keyword:hover
 {
  -webkit-transform: scale(1.05);
     -moz-transform: scale(1.05);
      -ms-transform: scale(1.05);
       -o-transform: scale(1.05);
          transform: scale(1.05);  
}

#keyword  {
  -webkit-transition: all 0.1s linear;
          transition: all 0.1s linear;
}
</style>
<tr>
	<td>
		<div class="swiper mySwiper slider">
	      <div class="swiper-wrapper">
	        <div class="swiper-slide bg01" onclick="javascript:goworldcup()">
	    	    <p class="bottomleft">(전주) 한옥마을</p>
	        	<span class="bottomleft2">전북 전주시 완산구 기린대로 99</span>
	        </div>
	        <div class="swiper-slide bg02" onclick="javascript:goworldcup()">
	        	<p class="bottomleft">(군산) 선유도</p>
	        	<span class="bottomleft2">전북 군산시 옥도면 선유남길 34-22</span>
	        </div>
	        	<div class="swiper-slide bg03" onclick="javascript:goworldcup()">
	        	<p class="bottomleft">(완주) 위봉산성</p>
	        <span class="bottomleft2">전북 완주군 소양면 대흥리</span>
	        </div>
        	<div class="swiper-slide bg04" onclick="javascript:goworldcup()">
	        	<p class="bottomleft">(정읍) 내장산</p>
	        	<span class="bottomleft2">전북 정읍시 내장산로 1207</span>
	        </div>
	        <div class="swiper-slide bg05" onclick="javascript:goworldcup()">
	        	<p class="bottomleft">(김제) 지평선 축제</p>
	        	<span class="bottomleft2">전라북도 김제시 부량면 벽골제로 442</span>
	        </div>
	      </div>
	      <div class="swiper-button-next"></div>
	      <div class="swiper-button-prev"></div>
	      <div class="swiper-pagination"></div>
	    </div>
    </td>
</tr>
<tr height="200px">
	<td class="pagemovespan" align="center" width="100%" valign="top">
		<table style="width: 1200px;height: 80px;">
			<tr>
				<h1>키워드</h1>
			</tr>
			<tr class="mainlocal" >
			<%
			String[] loc = {"전주","정읍","김제","군산"};
			String[] loc1 = {"#한국도로공사수목원","#내장산 케이블카","#미즈노씨네 트리하우스","#철길마을"};
			for(int i = 0 ; i < 4 ; i++)
			{
				%>
				<td  class="mainlocaltd" id="mainlocaltd2">
					<a href="javascript:golocalpage('<%=loc[i]%>')" id="keyword"><span style="background-color:#FFF3EB;  border-radius: 25px;" ><%=loc1[i]%></span></a>
				</td>
				<%
			}
			%>
			</tr>
			<tr>
				<%
			String[] Loc = {"완주","임실","부안","익산"};
			String[] Loc1 = {"#아원고택","#옥정호","#변산반도","#교도소세트장"};
			for(int i = 0 ; i < 4 ; i++)
			{
				%>
				<td  class="mainlocaltd" id="mainlocaltd2" align="center">
					<a href="javascript:golocalpage('<%=Loc[i]%>')" id="keyword"><span  style="background-color: #FFF3EB;  border-radius: 25px; "><%=Loc1[i]%></span></a>
				</td>
				<%
			}
			%>
			</tr>
		</table>
    </td>
  
    
</tr>
<%@ include file="../include/tail.jsp"%>	