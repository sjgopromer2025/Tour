//insP가 0이면 태그 클라우드 1이면 장소 클라우드 이미지

delete from word where w_sep = 0;

insert into word
(w_place , w_pic, w_sep, w_insP)
values
('군산', 'i_gunsan_0.png', 0,0),
('김제', 'i_kimje_0.png', 0,0),
('부안', 'i_buan_0.png', 0,0),
('완주', 'i_wanju_0.png', 0,0),
('익산', 'i_iksan_0.png', 0,0),
('임실', 'i_imsil_0.png', 0,0),
('전주', 'i_jeonju_0.png', 0,0),
('정읍', 'i_jeongeup_0.png', 0,0);


insert into word
(w_place , w_pic, w_sep, w_insP)
values
('군산', 'i_gunsan_1.png', 0,1),
('김제', 'i_kimje_1.png', 0,1),
('부안', 'i_buan_1.png', 0,1),
('완주', 'i_wanju_1.png', 0,1),
('익산', 'i_iksan_1.png', 0,1),
('임실', 'i_imsil_1.png', 0,1),
('전주', 'i_jeonju_1.png', 0,1),
('정읍', 'i_jeongeup_1.png', 0,1);




