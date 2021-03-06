<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ include file="../include/head.jsp"%>
<style>
	.button    
	{
		display: block;
	    margin-left: -5px;
	    padding-left: 20px;
	    background:url(../img/button.png) 0 70% no-repeat;
	    color: #000;
	}
		
	.courseul
	{
	    padding: 0 20px 6px 20px;
        
	}
	th
	{
		color:#FFFFFF;
		cursor : pointer;
		background-size: 550px;
		border-radius: 25px;
		border: 2px solid #73AD21;
		
	}	
	
		
	.courseul > li
	{
		background:url(../img/line_leftobj.png) 0 0 repeat-y;
		line-height: 30px;
   		padding: 10px 0;
   	}		
   	.tableC
   	{
		  border-spacing: 10px;
		  border-collapse: separate;
	}
	.tableC td 
	{
	  width: 30px;
	  border-radius: 25px;	
	 	
	  border: 2px solid #73AD21;
	}
	table
	{
		border-color: white;
	}
</style>
<script src="../JS/course_data.js" charset="utf-8"></script>
<tr>
	<td align="center" >
		<form id="gomapform" name="gomapform" method="post" action="../course/map.jsp">
			<input type="hidden" id="place" name="place">
			<input type="hidden" id="data" name="data">
		</form>
		<table border="0" width="100%" align="center" class="tableC">
			<b><font size=10>힐링여행코스</font></b>
			<tr>
				<th style="width:15%; height:130px; background-image: url(../img/jeonju.jpg)" onclick="javascript:goMap('전주')"><h1>전주 여행</h1></th>
				<th style="width:15%; height:130px; background-image: url(../img/iksan.jpg)" onclick="javascript:goMap('익산')"><h1>익산 여행</h1></th>
				<th style="width:15%; height:130px; background-image: url(../img/gunsan.jpg)" onclick="javascript:goMap('군산')"><h1>군산 여행</h1></th>
				<th style="width:15%; height:130px; background-image: url(../img/jeong.jpg)" onclick="javascript:goMap('정읍')"> <h1>정읍 여행</h1></th>
			</tr>
			<tr>
				<td style="height:280px;" valign="top" >
					<ul class="courseul">
											
						<li>
							<span class="button" id="p_1">전주한옥마을</span>
						</li>
						<li>
							<span class="button" id="p_2">마시랑게</span>
						</li>
						<li>	
							<span class="button" id="p_3">객리단길</span>
						</li>
						<li>
							<span class="button" id="p_4">전주수목원</span>
						</li>
						<li>
							<span class="button" id="p_5">전주한옥레일바이크</span>
						</li>
					</ul>
				</td>
				<td style="height:280px;"valign="top">
				<ul class="courseul">
					<li>
						<span class="button" id="p_6">미륵사지</span>
					</li>
					<li>
						<span class="button" id="p_7">추억담카페</span>
					</li>
					<li>	
						<span class="button" id="p_8">산들강웅포마을</span>
					</li>
					<li>
						<span class="button" id="p_9">성당포구마을</span>
					</li>
					<li>
						<span class="button" id="p_10">블랜드미</span>
					</li>
				</ul>
				</td>	
				<td style="height:280px;"valign="top">
				<ul class="courseul">
					<li>
						<span class="button" id="p_11">초원사진관</span>
					</li>
					<li>
						<span class="button" id="p_12">철길마을</span>
					</li>
					<li>	
						<span class="button" id="p_13">이성당</span>
					</li>
					<li>
						<span class="button" id="p_14">군산근대역사박물관</span>
					</li>
					<li>
						<span class="button" id="p_15">선유도</span>
					</li>
				</ul>
				</td>
				<td style="height:280px;"valign="top">
				<ul class="courseul">
					<li>
						<span class="button" id="p_16">내장산</span>
					</li>
					<li>
						<span class="button" id="p_17">허브원</span>
					</li>
					<li>	
						<span class="button" id="p_18">제이포렛</span>
					</li>
					<li>
						<span class="button" id="p_19">카페새록</span>
					</li>
					<li>
						<span class="button" id="p_20">우화정</span>
					</li>
				</ul>
				</td>
			</tr>
			<tr>
				<th style="width:15%; height:130px; background-image: url(../img/gimje.jpg)" onclick="javascript:goMap('김제')"><h1>김제 여행</h1></th>
				<th style="width:15%; height:130px; background-image: url(../img/wanju.jpg)" onclick="javascript:goMap('완주')"><h1>완주 여행</h1></th>			
				<th style="width:15%; height:130px; background-image: url(../img/imsil.jpg)" onclick="javascript:goMap('임실')"><h1>임실 여행</h1></th>		
				<th style="width:15%; height:130px; background-image: url(../img/buan.jpg)"  onclick="javascript:goMap('부안')"><h1>부안 여행</h1></th>
			</tr>
			<tr>
				<td style="height:280px;"valign="top">
				<ul class="courseul">
					<li>
						<span class="button" id="p_21">미즈노씨네 트리하우스 카페</span>
					</li>
					<li>
						<span class="button" id="p_22">망해사</span>
					</li>
					<li>	
						<span class="button" id="p_23">오늘여기</span>
					</li>
					<li>
						<span class="button" id="p_24">만경향교</span>
					</li>
					<li>
						<span class="button" id="p_25">김제 벽골제</span>
					</li>
				</ul>
				</td>
				<td style="height:280px;"valign="top">
				<ul class="courseul">
					<li>
						<span class="button" id="p_26">아원고택</span>
					</li>
					<li>
						<span class="button" id="p_27">고산자연휴양림</span>
					</li>
					<li>	
						<span class="button" id="p_28">대아저수지</span>
					</li>
					<li>
						<span class="button" id="p_29">송광사</span>
					</li>
					<li>
						<span class="button" id="p_30">위봉산성군립공원</span>
					</li>
				</ul>
				</td>
				<td style="height:280px;"valign="top">
				<ul class="courseul">
					<li>
						<span class="button" id="p_31">치즈테마파크</span>
					</li>
					<li>
						<span class="button" id="p_32">옥정호</span>
					</li>
					<li>	
						<span class="button" id="p_33">애뜨락</span>
					</li>
					<li>
						<span class="button" id="p_34">세심자연휴양림</span>
					</li>
					<li>
						<span class="button" id="p_35">상록수</span>
					</li>
				</ul>
				</td>
				<td style="height:280px;"valign="top">
				<ul class="courseul">
					<li>
						<span class="button" id="p_36">채석강</span>
					</li>
					<li>
						<span class="button" id="p_37">변산반도국립공원</span>
					</li>
					<li>	
						<span class="button" id="p_38">카페마르</span>
					</li>
					<li>
						<span class="button" id="p_39">변산해수욕장</span>
					</li>
					<li>
						<span class="button" id="p_40">내소사</span>
					</li>
				</ul>
				</td>
			</tr>	
		</table>
	</td>
</tr>
<%@ include file="../include/tail.jsp"%>	