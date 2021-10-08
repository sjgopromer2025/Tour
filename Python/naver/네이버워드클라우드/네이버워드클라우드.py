# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:18:03 2021

@author: 711
"""
import matplotlib.pyplot as plt
import pandas as pd
from konlpy.tag import Okt, Hannanum
from matplotlib import rc
from wordcloud import WordCloud
from collections import Counter
from PIL import Image
from wordcloud import ImageColorGenerator
import numpy as np

#파일명이 도시이름+수집날짜 임
loc = "정읍"
date = "20211001"

#수집된 4개의 csv파일을 하나로 합치기
def loadcsv(loc, date):
    file_name = loc+date+".csv"
    df1 = pd.read_csv(file_name)
    df1 = df1
    return df1 


#워드 클라우드를 그려주는 함수
def wordCloud(df):
    palettes = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
    mask_pic = np.array(Image.open('jeongup_word.png'))
    image_colors = ImageColorGenerator(mask_pic)
    wordlist = {}
    #워드 클라우드 표시용 딕셔너리로 변환
    for i in range(0,df["단어"].count()):
        #print(df["단어"][i])
        #print(df["빈도수"][i])
        wordlist[df["단어"][i]] = df["빈도수"][i]
        #print(wordlist)    
    
    #워드 클라우드 표시 ========================================

    wordcloud = WordCloud(font_path = 'HANYGO230.ttf',
                          relative_scaling = 0.5,
                          background_color='white',
                          mask = mask_pic,
                          colormap = "RdPu"
                          );
    wordcloud.generate_from_frequencies(wordlist)
    plt.figure(figsize=(30,30))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(loc+date, dpi=600)
    plt.show()




#4개의 csv파일 합치기 
df1 = loadcsv(loc, date)
#블로그 본문 내용 불러오기
wordCloud(df1)
