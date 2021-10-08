import os
import sys
import urllib.request
import pandas as pd
import json
import re
from datetime import datetime
#네이버 검색 API서비스 https://developers.naver.com/docs/search/blog/
client_id = "c7ogmUl1bcGAIRW88IBi" 
client_secret = "xeYzPPZiHL"

#실행 할때마다 검색 질의 입력하면 그 검색 질의의 url이 만들어짐.
#query = urllib.parse.quote(input("검색 질의: ")) 
query = urllib.parse.quote("군산 여행") 
input_value = urllib.parse.unquote(query, encoding='utf-8', errors='replace')
today = datetime.today().strftime("%Y%m%d") 

#몇 개인지 세기위해
idx = 0 
#한번에 몇개까지 가지고 오는지
display = 10
start = 1 
end = 10
#정렬(유사도순"sim"//날짜순"date")
sort = "date"

web_df = pd.DataFrame(columns=("Title", "Link", "Description", "Postdate")) 
#가지고 온 정보를 데이터 프레임에 저장
for start_index in range(start, end, display): #satrt 부터 end 까지 스텝을 100개 단위로 가져오기
    #json 형태로 값을 받으므로 결과값이 items에 들어가 있음
    url = "https://openapi.naver.com/v1/search/blog?query=" + query + "&display=" + str(display) + "&start=" + str(start_index) + "&sort" + sort    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    #오류가 나지 않으면 값을 받아옴
    if(rescode==200): 
        response_body = response.read() 
        #딕셔너리 형태로 받아옴
        response_dict = json.loads(response_body.decode('utf-8')) 
        #우리가 필요한 내용은 "items"안에 있으므로 items만 뽑아옴
        items = response_dict['items'] 
        #0부터 items의 수 만큼 가져옴        
        for item_index in range(0, len(items)): 
            #정규표현식설정
            remove_tag = re.compile('<.*?>') 
            #현재 item_index값에 설정해둔 정규표현식을 없애버린 타이틀 가져옴
            title = re.sub(remove_tag, '', items[item_index]['title']) 
            #현재 item_index값에 블로그링크를 가져옴
            link = items[item_index]['link'] 
            #현재 item_index값에 설정해둔 정규표현식을 없애버린 내용을 가져옴
            description = re.sub(remove_tag, '', items[item_index]['description']) 
            #현재 item_index값에 게시물 작성일을 가져옴
            postdate = items[item_index]['postdate'] 
            #만들어둔 데이터 프레임에 넣음
            web_df.loc[idx] = [title, link, description, postdate] 
            #넣은 후 인덱스값 증가
            idx += 1 
    else:
        print("Error Code:" + rescode)

print(web_df)
csv_title = "API_"+input_value+"("+ str(today) +").csv"
web_df.to_csv(csv_title,encoding="utf-8")


os.system("notepad.exe API_군산 여행(20211007).csv")

