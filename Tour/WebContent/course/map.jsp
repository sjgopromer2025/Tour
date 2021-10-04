<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ include file="../include/head.jsp"%>
<%
request.setCharacterEncoding("UTF-8");

String place = request.getParameter("place");
String data = request.getParameter("data");

if(place == null || place.equals("") || data == null || data.equals(""))
{
  response.sendRedirect("../main/main.jsp");
}
%>
<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=4bd65ce2e22f171c4f6a67f3ad9f60e5"></script>
<script src="../JS/loadmap.js" charset="UTF-8"></script>
<script>
$(document).ready(function() {
	loadMap("<%=place%>","<%=data%>");
});
</script>
<tr>
	<td align="center">
		<%=place %> 여행
	</td>
<tr>
<tr>
	<td align="center">
		<div id="map" style="width:1080px;height:680px;"></div>
	</td>
<tr>

<%@ include file="../include/tail.jsp"%>