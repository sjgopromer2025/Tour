from bs4 import BeautifulSoup as bt
import urllib.request
import os
import pandas as pd
import requests

#iframe 제거 후 blog.naver.com 붙이기
def get_iframe(url):
    #티스토리 블로그가 껴있어서 네이버 블로그만 골라냄
    if "naver" in url:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
        res = requests.get(url, headers=headers)
        res.raise_for_status() # 문제시 프로그램 종료
        soup = bt(res.text, "lxml") 
        src_url = "https://blog.naver.com/" + soup.iframe["src"]
    else:
        src_url = ""
        print("네이버 블로그 아닌뒈")    
    return src_url
    
    return src_url
#텍스트 스크래핑
def text_scraping(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status() # 문제시 프로그램 종료
    soup = bt(res.text, "lxml") 
    
    #내용가져옴
    if soup.find("div", attrs={"class":"se-main-container"}):
        text = soup.find("div", attrs={"class":"se-main-container"}).get_text()
        text = text.replace("\n","") #공백 제거
        #print("블로그")
        return text
    else:
        return "확인불가"

api_title = "API_군산 여행(20211007)"
csv = ".csv"
df = pd.read_csv(api_title + csv)    
web_df = pd.DataFrame(columns=("Title", "Description", "Postdate", "Link")) 
rowno = 0


for i in range(0,len(df)):
    print(i)
    web_list = []
    
    url = df['Link'][i]
    title = df['Title'][i]
    postdate = df['Postdate'][i]
    #print(url)
    src_url = get_iframe(url)
    #네이버 블로그가 아닐경우에는 continue
    if(src_url == ""):
        continue
    #print(src_url)
    text = text_scraping(src_url)
    #print(text)
    #print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    if (text == "확인불가"):
        continue
    web_list = [title, text, postdate, src_url ]
    web_df.loc[rowno] = web_list
    rowno += 1

print(web_df)
web_df.to_csv("BS_" + api_title + ".csv",encoding="utf-8")


os.system("notepad.exe BS_API_군산 여행(20211007).csv")

