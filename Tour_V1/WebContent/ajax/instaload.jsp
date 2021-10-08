<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="tourDTO.*" %>
<%@ page import="tourVO.*" %>
<%
String word = request.getParameter("word");

instaDTO i_dto = new instaDTO(); 
instaVO i_vo   = new instaVO();
i_vo.setW_place(word);

i_dto.setI_vo(i_vo);
if(i_dto.load_w_pic_0() == true && i_dto.load_w_pic_1() == true && i_dto.load_graphElement() == true)
{
	out.print(i_vo.getW_pic_0());
	out.print("<<SEP>>");
	out.print(i_vo.getW_pic_1());
	out.print("<<SEP>>");
	out.print(i_vo.getI_word());
	out.print("<<SEP>>");
	out.print(i_vo.getI_fre());
}



%>