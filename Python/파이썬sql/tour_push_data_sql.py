# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:26:26 2021

@author: 711
"""

from collections import Counter
import numpy as np
import re
import pandas as pd
import pymysql

#DB연결
conn = pymysql.connect(host = '192.168.0.81', user = 'root' , db='tour' , password = 'ezen', charset='utf8')
#cursor = 가리키다
curs = conn.cursor() 
sql  = "insert into compare_wd (co_place , co_word1 , co_word2 , co_rr , co_idf, co_pos) values (%s,%s,%s,%s,%s,%s)"




loc_dict = {
    "군산" : ['이성당', '크리스마스', '경암동', '디저트', '아메리카노', '지린성', '해수욕장', '장자도', '단팥빵', '케이크', '박물관', '새만금', '사진관', '선유도', '신흥동', '칼국수'],
    "익산" : ['미륵사지', '디저트', '익산역', '캠핑장', '아메리카노', '전시관', '드라마', '비빔밥', '케이크', '박물관', '바람개비', '금마면', '교도소', '칼국수', '영등동', '모현동'],
    "부안" : ['바닷가', '진서면', '디저트', '아메리카노', '내소사', '해수욕장', '곰소항', '직소폭포', '생크림', '새만금', '국립공원', '격포항', '변산반도', '칼국수', '바지락', '변산면'],
    "완주" : ['순두부', '수목원', '갤러리', '올레길', '위봉산성', '묵은지', '대둔산', '아메리카노',  '미술관', '닭볶음탕', '박물관', '송광사', '소양면', '송광수', '드라이브', '저수지'],
    "임실" : ['운암면', '국사봉', '디저트', '전망대', '섬진강', '아메리카노', '상록수', '애뜨락', '요거트', '고양이', '다슬기', '칼국수', '드라이브', '칼국수', '고양이', '코티지', '관촌면'],
    "전주" : ['덕진구', '수목원', '떡갈비',  '콩나물', '디저트', '아메리카노', '케이크', '박물관', '막걸리', '피순대', '비빔밥', '칼국수', '초코파이', '전동성당', '완산구'],
    "정읍" : ['케이블카', '브런치', '디저트', '우렁이', '전망대', '아메리카노', '쌍화탕', '구절초', '수성동', '케이크', '국립공원', '정읍사', '내장산', '칼국수', '라벤더'],
    "김제" : ['벽골제', '미즈노', '디저트', '전망대', '아메리카노', '라운드', '금산사', '지평선', '금산면', '트리하우스', '새만금', '베이커리', '드라이브', '저수지', '칼국수', '아리랑']
    }

loc_list = ["군산","익산","김제","정읍","완주","전주","임실","부안"]
for loc in loc_list:
    path1 = "C:\\Users\\711\\Desktop\\새 폴더\\파이썬20211006\\idf\\"+loc+"word_tfidf.csv"
    path2 = "C:\\Users\\711\\Desktop\\새 폴더\\파이썬20211006\\corr\\corr"+loc+"real.csv"
    
    df = pd.read_csv(path1,encoding=("euc-kr"),index_col=("단어"))
    df = df.drop(["Unnamed: 0"],axis=1)
    df=df.transpose()
    
    df2 = pd.read_csv(path2,encoding="euc-kr")
    df2 = df2.drop(["Unnamed: 0"],axis=1)
    df2 = df2.fillna(999)
    
        
    
    corr = []
    idf = {}
    for i in range(0,len(df2['단어'])):
        word = df2['단어'][i]
        corr.append(df2['단어'][i])
        idf[word] = df[word][0]
        
        
    keyword_list = loc_dict[loc]

    for keyword in keyword_list:
        for seq in range(0,len(df2['단어'])):
            if(df2[keyword][seq] == 999):
                continue
            else :
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(loc)
                print(keyword)
                print(df2['단어'][seq]) # 키워드에 관한 상대 단어
                
                textsql = df2['품사'][seq]
                if(textsql == "Noun"):
                   textsql = "N"
                else:
                   textsql = "A"
                
                print(df2['품사'][seq]) # 키워드에 관한 상대 품사
                print(df2[keyword][seq])  ##corr 상관관계값
                print(idf[df2['단어'][seq]]) ##idf  값
                
                print("0000000000000000000000000000")
                curs.execute(sql,(loc.strip(),keyword.strip(),df2['단어'][seq],df2[keyword][seq],idf[df2['단어'][seq]],textsql))
    


conn.commit()
conn.close()

