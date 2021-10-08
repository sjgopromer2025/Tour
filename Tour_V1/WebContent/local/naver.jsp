<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="../include/head.jsp"%>
<script src="../JS/naver_graph.js" charset="UTF-8"></script>
<script src="../JS/loadnaver.js" charset="UTF-8"></script>
<%
String word = request.getParameter("word");
if(word == null) word = "군산";
%>
<style>
	.analysis
	{
		width: 600px;
		height: 600px;
	}
	
	select > option
	{
		text-align: center;
	}
	
	.head
	{
		background-color: #98E0AD;
		color: #138535;
	}
	
	.TBorder
	{
		border: 1px solid #98E0AD;
		
	}
	
	select
	{
		color:#138535; 
		width: 150px; 
		height: 40px; 
		font-size: 18pt; 
		text-align-last:center; 
		border: 1px solid #138535; 
		border-radius: 15px;
	}
	
	
}
		
</style>
<script>

$(document).ready(function(){
	$("#loc").val('<%=word%>');
	ch();
});

</script>
<tr>
	<td style="width: 100%">
		<table  border="0" style="width: 100%;">
			<caption><h1>지역분석 > 네이버</h1></caption>
			<tr>
				<td colspan="2">
					<select id="loc" name="loc" onchange="javascript:ch();">
						<option value="군산">군산</option>
						<option value="김제">김제</option>
						<option value="부안">부안</option>
						<option value="완주">완주</option>
						<option value="익산">익산</option>
						<option value="임실">임실</option>
						<option value="전주">전주</option>
						<option value="정읍">정읍</option>
					</select>
					<select id="nav_week" name="nav_week" onchange="javascript:ch();">
						<option value="1">9월 둘째주</option>
						<option value="2">9월 셋째주</option>
						<option value="3">9월 넷째주</option>
						<option value="4">10월 첫째주</option>
					</select>
				</td>
			</tr>
			<tr align="center">
				<td class="head" style="width: 40%;">
					<h1>블로그</h1>
				</td>
				<td class="head">
					<h1>그래프</h1>
				</td>
			</tr>
			<tr align="center" >
				<td class="TBorder">
					<br>
					<span id="tag_explain" style="font-size: 13pt;"></span>
					<br>
					<img class="analysis" id="blog">
				</td>
				<td class="TBorder">
					<div id="container_graph" style="width: 100%; height: 100%;"></div>
					<div id="contents_word"></div>
					<font>그래프의 막대바를 클릭하면 연관된 단어들이 표시됩니다.</font>
				</td>
			</tr>
		</table>
	</td>
</tr>
<%@ include file="../include/tail.jsp"%>	