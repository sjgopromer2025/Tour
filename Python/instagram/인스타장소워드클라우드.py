# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:23:36 2021

@author: 710
"""
import csv
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from wordcloud import WordCloud
from PIL import Image
from wordcloud import ImageColorGenerator 

stop_words = ['전자담배 슈퍼마켓 정읍점', '전주전자담배마켓', 'Jeonju', '전주혁신도시', '사부작 채집가', '오아시스_익산', '전주한옥마을'
              '객리단길', 'Jeonju, Korea', '전주한옥마을', '스타디움오브독스']  


#수집한 csv파일 불러오기
f = open('정읍.csv','r',encoding="UTF-8")
rdr = csv.reader(f)
place_list =[]
for line in rdr:
    print(line[5])
    
    
        
    if (line[5] != ""):
        place_list.append(line[5])

f.close()

#word for word in instagram_tags if line[5] not in stop_words

#print(len(place_list))

place_list2 = []
for item in place_list:
    if(item not in stop_words):
        place_list2.append(item)

print(place_list2)

print("=================================================================")


#장소 빈도수 출력
place_counts = Counter(place_list2)
place_counts = place_counts.most_common(50)

words = []
count = []
number23 =0
for item in place_counts :
    #print(item)
    
    words.append(item[0].strip())
    count.append(item[1])

print(words)
#print(count)

nouns = [words,count]
df = pd.DataFrame(nouns)
df = df.transpose()
df.columns  = [ "단어", "좋아요수"]




#워드 클라우드 표시용 딕셔너리로 변환
wordlist = {}
for i in range(0,df["단어"].count()):
    #print(df["단어"][i])
    #print(df["빈도수"][i])
    wordlist[df["단어"][i]] = df["좋아요수"][i]
#print(wordlist) 

#워드 클라우드 표시 ========================================

mask_color = np.array(Image.open("mask.jpg"))
image_colors = ImageColorGenerator(mask_color)

wordcloud = WordCloud(font_path = 'gm.ttf',
                      relative_scaling = 0.5,
                      background_color='white',
                      mask = mask_color
                      );
wordcloud.generate_from_frequencies(wordlist)
plt.figure(figsize=(30,30))
plt.imshow(wordcloud.recolor(color_func=image_colors))
plt.axis("off")
plt.savefig("정읍장소워드클라우드.png",dpi=600)
plt.show()
plt.close()
