# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:36:35 2021

@author: 733
"""

from collections import Counter
import numpy as np
import re
import pandas as pd
import math
#from nltk import word_tokenize
from konlpy.tag import Okt

#특수문자를 제거한다. [ 시작 ]============================
def remove_spc(wd):
    wd = str(wd)
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    val = re.compile('[^가-힣a-zA-Z]')
    wd = re.sub(pattern, '', wd)
    wd = re.sub(r'\[[^]]*\]', '', wd)
    wd = re.sub(val,' ',wd)
    wd = ' '.join(wd.split())
    return wd
#특수문자를 제거한다. [ 종료 ]============================

#불용어를 제거한다. [ 시작 ]============================
def remove_stopword(wd) :
    stopwords = ['아', '휴', '아이구', '아이쿠', '아이고', '어', '나', '우리', '저희', "앞","1차","내","데","곳","후",'따라',"♀", '의해'
            , '수','을', '를', '에', '의', '가', '으로', '로', '에게', '뿐이다', '의거하여', '근거하여', '입각하여', '기준으로', '예하면',
            '예를 들면', '예를 들자면', '저', '소인', '소생', '저희', '지말고', '하지마', '하지마라', '다른', '물론', '또한', '그리고', '비길수 없다', 
            '해서는 안된다', '뿐만 아니라', '만이 아니다', '만은 아니다', '막론하고', '관계없이', '그치지 않다', '그러나', '그런데', '하지만', '든간에',
            '논하지 않다', '따지지 않다', '설사', '비록', '더라도', '아니면', '만 못하다', '하는 편이 낫다', '불문하고', '향하여', '향해서', '향하다',
            '쪽으로', '틈타', '이용하여', '타다', '오르다', '제외하고', '이 외에', '이 밖에', '하여야', '비로소', '한다면 몰라도', '외에도', '이곳', 
            '여기', '부터', '기점으로', '따라서', '할 생각이다', '하려고하다', '이리하여', '그리하여', '그렇게 함으로써', '하지만', '일때', '할때',
            '앞에서', '중에서', '보는데서', '으로써', '로써', '까지', '해야한다', '일것이다', '반드시', '할줄알다', '할수있다', '할수있어', 
            '임에 틀림없다', '한다면', '등', '등등', '제', '겨우', '단지', '다만', '할뿐', '딩동', '댕그', '대해서', '대하여', '대하면', '훨씬', 
            '얼마나', '얼마만큼', '얼마큼', '남짓', '여', '얼마간', '약간', '다소', '좀', '조금', '다수', '몇', '얼마', '지만', '하물며', '또한', 
            '그러나', '그렇지만', '하지만', '이외에도', '대해 말하자면', '뿐이다', '다음에', '반대로', '반대로 말하자면', '이와 반대로', '바꾸어서 말하면',
            '바꾸어서 한다면', '만약', '그렇지않으면', '까악', '툭', '딱', '삐걱거리다', '보드득', '비걱거리다', '꽈당', '응당', '해야한다', 
            '에 가서', '각', '각각', '여러분', '각종', '각자', '제각기', '하도록하다', '와', '과', '그러므로', '그래서', '고로', '한 까닭에',
            '하기 때문에', '거니와', '이지만', '대하여', '관하여', '관한', '과연', '실로', '아니나다를가', '생각한대로', '진짜로', '한적이있다', 
            '하곤하였다', '하', '하하', '허허', '아하', '거바', '와', '오', '왜', '어째서', '무엇때문에', '어찌', '하겠는가', '무슨', '어디', 
            '어느곳', '더군다나', '하물며', '더욱이는', '어느때', '언제', '야', '이봐', '어이', '여보시오', '흐흐', '흥', '휴', '헉헉', 
            '헐떡헐떡', '영차', '여차', '어기여차', '끙끙', '아야', '앗', '아야', '콸콸', '졸졸', '좍좍', '뚝뚝', '주룩주룩', '솨', 
            '우르르', '그래도', '또', '그리고', '바꾸어말하면', '바꾸어말하자면', '혹은', '혹시', '답다', '및', '그에 따르는', '때가 되어',
            '즉', '지든지', '설령', '가령', '하더라도', '할지라도', '일지라도', '지든지', '몇', '거의', '하마터면', '인젠', '이젠', '된바에야',
            '된이상', '만큼\t어찌됏든', '그위에', '게다가', '점에서 보아', '비추어 보아', '고려하면', '하게될것이다', '일것이다', '비교적', 
            '좀', '보다더', '비하면', '시키다', '하게하다', '할만하다', '의해서', '연이서', '이어서', '잇따라', '뒤따라', '뒤이어', '결국', 
            '의지하여', '기대여', '통하여', '자마자', '더욱더', '불구하고', '얼마든지', '마음대로', '주저하지 않고', '곧', '즉시', '바로', '당장', 
            '하자마자', '밖에 안된다', '하면된다', '그래', '그렇지', '요컨대', '다시 말하자면', '바꿔 말하면', '즉', '구체적으로', '말하자면', 
            '시작하여', '시초에', '이상', '허', '헉', '허걱', '바와같이', '해도좋다', '해도된다', '게다가', '더구나', '하물며', '와르르', '팍',
            '퍽', '펄렁', '동안', '이래', '하고있었다', '이었다', '에서', '로부터', '까지', '예하면', '했어요', '해요', '함께', '같이', '더불어',
            '마저', '마저도', '양자', '모두', '습니다', '가까스로', '하려고하다', '즈음하여', '다른', '다른 방면으로', '해봐요', '습니까', '했어요',
            '말할것도 없고', '무릎쓰고', '개의치않고', '하는것만 못하다', '하는것이 낫다', '매', '매번', '들', '모', '어느것', '어느', '로써',
            '갖고말하자면', '어디', '어느쪽', '어느것', '어느해', '어느 년도', '라 해도', '언젠가', '어떤것', '어느것', '저기', '저쪽', '저것', 
            '그때', '그럼', '그러면', '요만한걸', '그래', '그때', '저것만큼', '그저', '이르기까지', '할 줄 안다', '할 힘이 있다', '너', '너희',
            '당신', '어찌', '설마', '차라리', '할지언정', '할지라도', '할망정', '할지언정', '구토하다', '게우다', '토하다', '메쓰겁다', '옆사람',
            '퉤', '쳇', '의거하여', '근거하여', '의해', '따라', '힘입어', '그', '다음', '버금', '두번째로', '기타', '첫번째로', '나머지는',
            '그중에서', '견지에서', '형식으로 쓰여', '입장에서', '위해서', '단지', '의해되다', '하도록시키다', '뿐만아니라', '반대로', '전후', 
            '전자', '앞의것', '잠시', '잠깐', '하면서', '그렇지만', '다음에', '그러한즉', '그런즉', '남들', '아무거나', '어찌하든지', '같다', 
            '비슷하다', '예컨대', '이럴정도로', '어떻게', '만약', '만일', '위에서 서술한바와같이', '인 듯하다', '하지 않는다면', '만약에', '무엇',
            '무슨', '어느', '어떤', '아래윗', '조차', '한데', '그럼에도 불구하고', '여전히', '심지어', '까지도', '조차도', '하지 않도록', 
            '않기 위하여', '때', '시각', '무렵', '시간', '동안', '어때', '어떠한', '하여금', '네', '예', '우선', '누구', '누가 알겠는가',
            '아무도', '줄은모른다', '줄은 몰랏다', '하는 김에', '겸사겸사', '하는바', '그런 까닭에', '한 이유는', '그러니', '그러니까',
            '때문에', '그', '너희', '그들', '너희들', '타인', '것', '것들', '너', '위하여', '공동으로', '동시에', '하기 위하여',
            '어찌하여', '무엇때문에', '붕붕', '윙윙', '나', '우리', '엉엉', '휘익', '윙윙', '오호', '아하', '어쨋든', 
            '만 못하다','하기보다는', '차라리', '하는 편이 낫다', '흐흐', '놀라다', '상대적으로 말하자면',
            '마치', '아니라면', '쉿', '그렇지 않으면', '그렇지 않다면', '안 그러면',
            '아니었다면', '하든지', '아니면', '이라면', '좋아', '알았어', '하는것도', 
            '그만이다', '어쩔수 없다', '하나', '일', '일반적으로', '일단', '한켠으로는',
            '오자마자', '이렇게되면', '이와같다면', '전부', '한마디', '한항목',
            '근거로', '하기에', '아울러', '하지 않도록', '않기 위해서', '이르기까지', '이 되다', '로 인하여', '까닭으로', 
            '이유만으로', '이로 인하여', '그래서', '이 때문에', '그러므로', 
            '그런 까닭에', '알 수 있다', '결론을 낼 수 있다', '으로 인하여', '있다','같아', '있는데요', '맛있었다', '같습니다', '굉장히', '있었는데',
            '좋습니다', '있고', '계실', '있도록', '있을', '있으며', '있기', '쿠린', '맛있는', '있습니다', '있었어요', '있더라고요', '좋다고', '입니다',
            '아름다', '미친', '있어서', '있는데', '안녕하세요', '없다', '있었다', '같더라구요', '있었는데요', '좋았었어요', '두껍', '그런', 
            '있답니다', '좋다', '좋았습니다', '좋았어요', '아니라', '좋네요', 
            '어떤것', '관계가 있다', '관련이 있다', '연관되다', '어떤것들', '에 대해', 
            '이리하여', '그리하여', '여부', '하기보다는', '하느니', '하면 할수록', '운운',
            '이러이러하다', '하구나', '하도다', '다시말하면', '다음으로', '에 있다', '에 달려 있다',
            '우리', '우리들', '오히려', '하기는한데', '어떻게', '어떻해', '어찌됏어', '어때', '어째서',
            '본대로', '자', '이', '이쪽', '여기', '이것', '이번', '이렇게말하자면', '이런', '이러한', 
            '이와 같은', '요만큼', '요만한 것', '얼마 안 되는 것', '이만큼', '이 정도의', '이렇게 많은 것',
            '이와 같다', '이때', '이렇구나', '것과 같이', '끼익', '삐걱', '따위', '와 같은 사람들',
            '부류의 사람들', '왜냐하면', '중의하나', '오직', '오로지', '에 한하다', '하기만 하면', '도착하다',
            '까지 미치다', '도달하다', '정도에 이르다', '할 지경이다', '결과에 이르다', '관해서는', '여러분', 
            '하고 있다', '한 후', '혼자', '자기', '자기집', '자신', '우에 종합한것과같이', '총적으로 보면', 
            '총적으로 말하면', '총적으로', '대로 하다', '으로서', '참', '그만이다', '할 따름이다', '쿵', '탕탕',
            '쾅쾅', '둥둥', '봐', '봐라', '아이야', '아니', '와아', '응', '아이', '참나', '년', '월', '일', 
            '령', '영', '일', '이', '삼', '사', '오', '육', '륙', '칠', '팔', '구', '이천육', '이천칠', '이천팔',
            '이천구', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '령', '영',"지","전","00",'있으니', 
            '남다른', '있어', '마라', '매운', '있다는', '상당히', '자세한', '좋아하는', '좋아요', '없었어요', '그런지', '좋을',"지금",
            '있다고', '같은', '있던', '같네요', '없는', '있었답니다', '같아요', '있어요', '작은', '좋은', '있는', '행복하기', 
            '있었습니다', '좋았다', '많은' ,'벤다', '구매', '있음', '확인', '짚라인', '인터', '젤라또', '맛있었어요', '아니마', '있죠', '있지요', '샌드위치', '필요합니다', '파운드', '있게', '좋더라구요', '있네요']
    
    
    
    word_list = set(wd)
    for word in word_list:
        if word in stopwords:
            while word in wd: wd.remove(word) 
    return wd    
#불용어를 제거한다. [ 종료  ]============================


#전역변수 지역================================================================================
#파일명이 도시이름+loc+수집날짜 
date1= "20210924"
date2= "20210910"
date3= "20210917"
date4= "20211001"


loc_dict = {
    "군산" : ['이성당', '크리스마스', '경암동', '디저트', '아메리카노', '지린성', '해수욕장', '장자도', '단팥빵', '케이크', '박물관', '새만금', '사진관', '선유도', '신흥동', '칼국수'],
    "익산" : ['미륵사지', '디저트', '익산역', '캠핑장', '아메리카노', '전시관', '드라마', '비빔밥', '케이크', '박물관', '바람개비', '금마면', '교도소', '칼국수', '영등동', '모현동'],
    "부안" : ['바닷가', '진서면', '디저트', '아메리카노', '내소사', '해수욕장', '곰소항', '직소폭포', '생크림', '새만금', '국립공원', '격포항', '변산반도', '칼국수', '바지락', '변산면'],
    "완주" : ['순두부', '수목원', '갤러리', '올레길', '위봉산성', '묵은지', '대둔산', '아메리카노',  '미술관', '닭볶음탕', '박물관', '송광사', '소양면', '송광수', '드라이브', '저수지'],
    "임실" : ['운암면', '국사봉', '디저트', '전망대', '섬진강', '아메리카노', '상록수', '애뜨락', '요거트', '고양이', '다슬기', '칼국수운암면', '드라이브', '칼국수', '고양이', '코티지', '관촌면'],
    "전주" : ['덕진구', '수목원', '떡갈비',  '콩나물', '디저트', '아메리카노', '케이크', '박물관', '막걸리', '피순대', '비빔밥', '칼국수', '초코파이', '전동성당', '완산구'],
    "정읍" : ['케이블카', '브런치', '디저트', '우렁이', '전망대', '아메리카노', '쌍화탕', '구절초', '수성동', '케이크', '국립공원', '정읍사', '내장산', '칼국수', '라벤더'],
    "김제" : ['벽골제', '미즈노', '디저트', '전망대', '아메리카노', '라운드', '금산사', '지평선', '금산면', '트리하우스', '새만금', '베이커리', '드라이브', '저수지', '칼국수', '아리랑']
    }

Okt = Okt()
#전역변수 지역================================================================================
loc_list = ["군산","익산","김제","정읍","완주","전주","임실","부안"]
for loc in loc_list:
    docs1 = pd.read_csv(loc+'tf'+date1+'.csv')
    docs2 = pd.read_csv(loc+'tf'+date2+'.csv')
    docs3 = pd.read_csv(loc+'tf'+date3+'.csv')
    docs4 = pd.read_csv(loc+'tf'+date4+'.csv')
    
    docs = pd.concat([docs1,docs2,docs3,docs4])
    docs =docs.drop(["Unnamed: 0"],axis=1)
    #print(docs.duplicated())
    docs = docs.drop_duplicates()
    total_docs = docs[docs.columns[0]].count()
    print(total_docs)
    
       
    result = []
    total_word = {}
    noun_total_list = []
    
    
    
    keyword = loc_dict[loc]
    
    for docno in range(0,100) :
        print("문서번호 : ", docno)
        raw_text = docs.iloc[docno][0]
        
        #print(raw_text)
        print("[01]--------------------------------------")
        
        #한글,영문,숫자 OR 특수문자 제거 OR [],() 내용 제거
        raw_text = remove_spc(raw_text)
        #print(raw_text)
        
        print("[02]--------------------------------------")    
        
    
        
        word_data = Okt.pos(raw_text)
        #print(word_data)       
        print("[03]--------------------------------------")        
        
        #일반명사 NNG / 고유명사 NNP / 영어 SL / 숫자 SN 선택
        Noun_words = []
        
        for word, pos in word_data:
            if (pos == 'Noun') or (pos == 'Adjective'):
            #if (pos == 'NNG') or (pos == 'NNP') :
                if len(word) != 1 :
                    #if len(word) != 1 and len(word) != 2 :
                    Noun_words.append(word)
                    
        
        #print(Noun_words)
        print("[04]--------------------------------------")
        
        #불용어 정리
        word_data = remove_stopword(Noun_words)
        #print(word_data)       
        print("[04]--------------------------------------") 
        
        
        #단어 목록에서 단어,빈도수로 얻기 
        #row_data = "단어1,단어2,단어1,단어2"
        word_list = Counter(word_data)
        #print(word_list)     
        print("[05-01]--------------------------------------")     
        word_list = word_list.most_common()
        #print(word_list)     
        print("[05-02]--------------------------------------") 
        
        #컬럼 이름 목록을 만든다.
        noun_list  = []
        count_list = []
        for noun in word_list :
            if noun[1] > 5 or  (noun[0] in (keyword)) :
                noun_list.append(noun[0])  #단어
                count_list.append(noun[1]) #빈도수
                noun_total_list.append(noun[0]) # concat 된 컴럼의 총 단어의 개수를 저장한다
            
        #print(noun_list)
        #print(max(count_list, default=-1))
        print("[06]--------------------------------------") 
        #TF를 계산한다.
        max_word_count = max(count_list,default=-1)
        
        
        for n in range(len(count_list)) :
            #TF를 계산한다.
            doc_tf = (0.5 * count_list[n]) / max_word_count
            count_list[n] = doc_tf    
        
        #단어-문서번호 행열을 만든다.
        df = pd.DataFrame([count_list],columns = noun_list)
        #print(df)
        
        #print("[07]--------------------------------------") 
        
        if docno == 0 :
            allWord =  df
        else:
            allWord = pd.concat([allWord,df])    
        
        
        #print(allWord)
        #print("[08]--------------------------------------")         
        
    
    
    tfidf_Word = pd.DataFrame([],index=["단어","TF-IDF"])
    max_rows = allWord[allWord.columns[0]].count()
    for nWord in allWord.columns:
        #전체 문서에서 몇 개의 문서에 해당 키워드가 있는지 갯수 얻기
        nRowCount = allWord[nWord].count()
        doc_idf = math.log(total_docs/(nRowCount+1))
        add_data = { "단어" : nWord, "TF-IDF" : doc_idf }
        tfidf_Word = tfidf_Word.append(add_data, ignore_index=True)


    tfidf_Word = tfidf_Word.dropna()    
    
    tfidf_Word.to_csv(loc+"word_tfidf.csv",encoding="euc-kr")
    break

