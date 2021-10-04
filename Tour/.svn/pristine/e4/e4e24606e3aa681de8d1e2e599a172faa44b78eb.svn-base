<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="tourDTO.*" %> 
<%@ page import="tourVO.*" %>
<%
String place1 = request.getParameter("place1"); 
String place2 = request.getParameter("place2");

wcDTO dto = new wcDTO();
wcVO wc1 = dto.Read(place1);
wcVO wc2 = dto.Read(place2);

String place1_info   = wc1.getWc_local()	  +"<<PC1>>" ;
place1_info 		+=  wc1.getWc_location()  +"<<PC1>>" ;
place1_info 		+= wc1.getWc_explain()    +"<<PC1>>" ;  
place1_info 		+= wc1.getWc_relate();

String place2_info   =  wc2.getWc_local()      +"<<PC2>>" ;
place2_info 		+=  wc2.getWc_location()   +"<<PC2>>" ;
place2_info 		+=  wc2.getWc_explain()    +"<<PC2>>" ;  
place2_info 		+=  wc2.getWc_relate();

out.print(place1_info +"<<!MIX!>>" + place2_info);



%>