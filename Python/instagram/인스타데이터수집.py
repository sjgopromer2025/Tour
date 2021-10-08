# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:20:50 2021

@author: 710
"""

#필요 패키지 호출
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import pandas as pd


#검색어 조건에 따른 URL 생성
def insta_searching(word):
    url = "https://www.instagram.com/explore/tags/" + str(word)
    return url

#열린 페이지에서 첫 번째 게시물 클릭 + time.sleep()메소드 시차두기
#로딩을 위해 3초 대기
def select_first(driver):
    first = driver.find_elements_by_css_selector("div._9AhH0"[0])
    first.click()
    time.sleep(3)                                                              

#내용, 작성일, 좋아요 수, 장소, 해시태그 가져오기
#현재페이지 HTML 정보가져오기
def get_content(driver):
    html = driver.page_source                                                
    soup = BeautifulSoup(html, 'lxml')
    
    #본문내용 
    #여러 태그중 첫번째([0]) 태그를 선택
    #첫 게시글 본문 내용이 <div class="C4VMK">
    list2= []
    try:
        #content = soup.select('div.C4VMK > span')[0].text                                          
        list2.append(soup.select('div.C4VMK > span')[0].text)
    except:
        list2.append("")
    
    #해시태그
    #tags = re.findall(r'#[^\s#,\\]+', content)
    list2.append(re.findall(r'#[^\s#,\\]+', list2[0]))
    #print(tags)
    
    #작성일자
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]           
    list2.append(date)
    #좋아요 수
    try:
        like = soup.select('a.zV_Nj')[0].text[4:-1]
        list2.append(like)
        print(like)
    except:
        like = "0"
        list2.append(like)
    
    #장소
    try:
        place = soup.select('div.M30cS')[0].text
        list2.append(place)
        print(place)
    except:
        place = ' ' 
        list2.append(place)
            
    print(list2)
    return list2
    
#첫 번째 게시물 클릭 후 다음 게시물 클릭
def move_next(driver):
    right = driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow')   
    right.click()
    time.sleep(5)
 
#크롬 브라우저 열기
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.instagram.com')
time.sleep(3)

#인스타그램 로그인을 위한 계정 정보
email = 'team.project1'
#input_id = driver.find_elements_by_css_selector('input.2hvTZ.pexuQ.zyHYP')[0]
#input_id = driver.find_element_by_class_name('input._2hvTZ pexuQ zyHYP')

#xpath를 copy하여 로그인하기
input_id = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
#loginForm > div > div:nth-child(1) > div > label > input
input_id.clear()
input_id.send_keys(email)

#xpath를 copy하여 비밀번호 입력
password = 'ezen1234@'
#input_pw = driver.find_elements_by_css_selector('input.2hvTZ.pexuQ.zyHYP')[1]
input_pw = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
input_pw.clear()
input_pw.send_keys(password)
time.sleep(3)

#로그인 버튼 누르기
driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF').click()
time.sleep(3)

#로그인 완료 후 로그인정보 나중에저장하기 클릭하고 넘어가기
driver.find_element_by_css_selector('button.sqdOP.yWX7d.y3zKF').click()
time.sleep(5)

#알림설정 나중에 저장하기 클릭하고 넘어가기
driver.find_element_by_css_selector('button.aOOlW.HoLwm').click()
time.sleep(3)


#게시물을 조회할 키워드 입력 요청
#word = input("검색어를 입력하세요 : ")
#word = str(word)
word ="김제여행"
url = insta_searching(word)

#검색결과 페이지 열기
driver.get(url)
time.sleep(10)

#첫번째 게시물 클릭
driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
time.sleep(3)

#본격적으로 데이터 수집하기
#변수 results 만들기
results = []

#수집 할 게시물 수
target = 500

#게시물 정보 가져오기
for i in range(target):
    try:
       data = get_content(driver)
       results.append(data)       
       move_next(driver)
    except:
       time.sleep(3) 
       move_next(driver)

#크롤링 수집 후 엑셀파일로 저장
#results_df.columns = ['content', 'tags', 'date', 'like', 'place'] 
results_df = pd.DataFrame(columns=['content', 'tags', 'date', 'like', 'place'] )
print(len(results))
rowno= 0
for item in results:
    results_df.loc[rowno] = item
    rowno = rowno + 1    
results_df.to_excel("D:\Instagram\김제여행0927.xlsx")

#크롬드라이버 종료
driver.quit()














 