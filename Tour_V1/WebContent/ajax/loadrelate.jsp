<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="tourDTO.*" %>
<%@ page import="tourVO.*" %>
<%
String word = request.getParameter("word");
String loc = request.getParameter("loc");


compareDTO coDTO = new compareDTO();
compareVO coVO   = new compareVO();

coVO.setCo_place(loc);
coVO.setCo_word1(word);

coDTO.setI_vo(coVO);
if(coDTO.loadWord() == true)
{
	out.print(coVO.getCo_word2());
}else
{
	out.print("결과 값이 없습니다.");
}
%>