<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page import="tourDTO.*" %>
<%@ page import="tourVO.*" %>
<%
String place = request.getParameter("place");
String data = request.getParameter("data");


mapDTO dto = new mapDTO();
mapVO vo   = new mapVO();


vo.setCity(place);
vo.setData(data);

dto.setVo(vo);
if(dto.load_map_element()== true)
{
	out.print(vo.getData());
	out.print("<<SEP>>");
	out.print(vo.getLat()); // 위도
	out.print("<<SEP>>");
	out.print(vo.getLog()); //경도
}




%>