<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="tourDTO.*" %>
<%@ page import="tourVO.*" %>
<%
String loc = request.getParameter("loc");
String nav_week = request.getParameter("nav_week");
if(loc == null) loc = "군산";
if(nav_week == null) nav_week = "1";
naverDTO nav_dto = new naverDTO();


String w_pic = nav_dto.Read(loc, nav_week);

naverVO nav_vo = new naverVO();
nav_vo.setW_place(loc);
nav_vo.setW_week(nav_week);
nav_dto.setNav_vo(nav_vo);


if(w_pic != null && nav_dto.load_graphElement() == true)
{
	out.print(w_pic);
	out.print("<<SEP>>");
	out.print(nav_vo.getN_word());
	out.print("<<SEP>>");
	out.print(nav_vo.getN_fre());
}

%>