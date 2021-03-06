drop table course;
create table course
(
	c_no int primary key not null auto_increment,
	c_place varchar(200) not null,
	c_add 	varchar(200) not null,
	c_x 	float(20,15) not null,
	c_y 	float(20,15) not null,
	c_city 	varchar(100)
	
);

drop table bar;
create table bar
(
	b_no int primary key not null auto_increment,
	b_word 	varchar(100) not null,
	b_fre 	int not null,
	b_sep 	int not null,
	b_place varchar(200) not null,
	b_week int 
);

drop table word;
create table word
(
	w_no int primary key not null auto_increment,
	w_place varchar(200) not null,
	w_pic 	varchar(200) not null,
	w_sep 	int not null,
	w_insP  varchar(50),
	w_week int
);



drop table wc;
create table wc
(
	wc_no int primary key not null auto_increment, 
	wc_local varchar(200) not null, 
	wc_place varchar(200) not null, 
	wc_location varchar(200) not null, 
	wc_explain text not null, 
	wc_relate varchar(200) not null
	
);

drop table compare_wd;
create table compare_wd
(
	co_no int primary key not null auto_increment,
	co_place varchar(50) not null,
	co_word1 varchar(50) not null,
	co_word2 varchar(50) not null,
	co_rr float(20,15) not null,
	co_idf float(20,15) not null,
	co_pos varchar(50) not null

);




