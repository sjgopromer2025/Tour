<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../include/head.jsp"%>
<script src="../JS/insta_graph.js" charset="UTF-8"></script>
<script src="../JS/loadinsta.js" charset="UTF-8"></script>
<style>
	.analysis
	{
		width: 790px;
		height: 790px;
	}
	
	select > option
	{
		text-align: center;
	}
	
	.container_graph
	{
		width: 850px;
		height: 850px;
	}
	
	.head
	{
		background-color: #FFF3EB;
		color: #FA7937;
	}
	
	.TBorder
	{
		border: 1px solid #FFF3EB;
	}
	
	select
	{
		color:#FA7937; 
		width: 150px; 
		height: 40px; 
		font-size: 18pt; 
		text-align-last:center;
		border: 1px solid #FA7937; 
		border-radius: 15px; "
	}
	
		
</style>
<tr>
	<td style="width: 100%">
		<table  border="0" style="width: 100%">
			<caption><h1>지역분석 > 인스타그램</h1></caption>
			<tr>
				<td colspan="2">
					<select id="jeonbuk" onchange="javascript:change()">
						<option value="gunsan">군산</option>
						<option value="gimje">김제</option>
						<option value="buan">부안</option>
						<option value="wanju">완주</option>
						<option value="iksan">익산</option>
						<option value="imsil">임실</option>
						<option value="jeonju">전주</option>
						<option value="jeongep">정읍</option>
					</select>	
				</td>
			</tr>
			<tr align="center">
				<td>
					<h1 class="head">해쉬태그</h1>
				</td>
				<td>
					<h1 class="head">장소</h1>
				</td>
			</tr>
			<tr align="center">
				<td class="TBorder">
					<br>
					<span id="tag_explain" style="font-size: 20pt;"></span>
					<br>
					<img class="analysis" id="tag" >
					
				</td>
				<td class="TBorder">
					<img class="analysis" id="place">
				</td>
			</tr>
			<tr align="center">
				<td colspan="2">
					<h1 class="head">그래프</h1>
				</td>
			</tr>
			<tr align="center" height="600px">
				<td colspan="2" class="TBorder">
					<div id="container_graph" style="width: 100%; height: 100%"></div>
				</td>
			</tr>
		</table>
	</td>
</tr>
<%@ include file="../include/tail.jsp"%>	