# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:51:10 2021

@author: 733
"""


from collections import Counter
import numpy as np
import re
import pandas as pd
import math
from konlpy.tag import Okt
from konlpy.tag import Hannanum

Okt = Okt()
han = Hannanum()

loc = "부안"

date = "20210924"


docs = pd.read_csv(loc+'tf'+date+'.csv')
total_docs = docs[docs.columns[0]].count()
docs =docs.drop(["Unnamed: 0"],axis=1)


text1 = docs.iloc[0][0]
text2 = docs.iloc[0][0]

nouns1 = Okt.nouns(text1)
nouns2 = han.nouns(text2)

count1 = Counter(nouns1)
count2 = Counter(nouns2)
print("okt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~start")
print(count1.most_common(10))
print("okt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~end")



print("Han~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~start")
print(count2.most_common(10))
print("Han~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~end")




