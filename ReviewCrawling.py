# 필요한 라이브러리
import pandas as pd
import time
import requests

from bs4 import BeautifulSoup
from urllib.parse import quote

rawData = pd.read_csv('veganfood_fin.csv') # ,  encoding = 'CP949'
placeList = rawData['상호명'].replace(' ','')
print(placeList)

ratingList = []
review1List = []
review2List = []

for search in placeList :
    # url ="https://map.naver.com/v5/search/"+ quote(search) +"/place/12987519?placePath=%3Fentry%253Dpll&c=14137846.1488029,4516820.9380197,15,0,0,0,dh"
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=" + quote(search)
    req = requests.get(url , headers = {'User-agent' : 'Mozilla/5.0'})
    soup = BeautifulSoup(req.text , 'lxml')

    try :
        # rating = soup.select("#place_main_ct > div > div > div > div.ct_box_area > div.biz_name_area > div > div > a:nth-child(1) > span.rating")[0].text
        rating = soup.select('#place_main_ct > div > section > div > div.default_info_area.booking_review_area > div > span.score > em')[0].text
    except Exception :
        rating = 0
    # print('{} : {}'.format(search , rating))
    ratingList.append(rating)

    try :
        # review1 = soup.select("#place_main_ct > div > div > div > div.ct_box_area > div.biz_name_area > div > div > a:nth-child(1) > span.txt")[0].text
        review1 = soup.select('#place_main_ct > div > section > div > div.ct_box_area > div.biz_name_area > div > div > a:nth-child(1) > span.txt')[0].text
    except Exception :
        review1 = 0
    # print('{} : {}'.format(search , review1))
    review1List.append(review1)

    try :
        # review2 = soup.select("#place_main_ct > div > div > div > div.ct_box_area > div.biz_name_area > div > div > a:nth-child(2) > span.txt")[0].text
        review2 = soup.select("#place_main_ct > div > section > div > div.ct_box_area > div.biz_name_area > div > div > a:nth-child(2) > span")[0].text
        
    except Exception :
        review2 = 0
    # print('{} : {} , {}'.format(search , review1 , review2))
    review2List.append(review2)
    print(search,'/', rating, review1, review2)

print(len(ratingList))
print(len(review1List))
print(len(review2List))

time.sleep(5)

if rawData.shape[0] == len(ratingList) and rawData.shape[0] == len(review1List) and rawData.shape[0] == len(review2List) :
    rawData['rating'] = ratingList
    rawData['review1'] = review1List
    rawData['review2'] = review2List
    rawData.to_csv('veganfood_review.csv' , index = False ) #, encoding = 'CP949'
    # rawData.to_csv('zerowaste_review.csv' , index = False ) #, encoding = 'CP949'
    print('Success')
else :
    print("Error")

rawData['review1'].str.extract('(\d+)')
rawData['review1'].str.replace(pat=r'[ㄱ-ㅣ가-힣]+', repl= r'', regex=True)

#------------------------------------------------------------------------------------------------------
# # 필요한 라이브러리
# import pandas as pd
# import time
# import requests
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from urllib.parse import quote
# import re


# rawData = pd.read_csv('veganfood_fin.csv') # ,  encoding = 'CP949'
# placeList = rawData['상호명'].replace(' ','')
# print(placeList)

# ratingList = []
# review1List = []
# review2List = []

# driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PJT\\WeWantGreen\\chromedriver_win32\\chromedriver.exe') # 웹드라이버가 설치된 경로를 지정해주시면 됩니다.

# rawData['naver_map_url'] = '' 

# for search in placeList:
#     print("이번에 찾을 키워드 :", search)
    
#     try:
#         # naver_map_search_url = f'https://map.naver.com/v5/search/{keyword}/place' # 검색 url 만들기
#         naver_map_search_url ="https://map.naver.com/v5/search/"+ quote(search) +"/place/12987519?placePath=%3Fentry%253Dpll&c=14137846.1488029,4516820.9380197,15,0,0,0,dh"
#         driver.get(naver_map_search_url) # 검색 url 접속, 즉 검색하기
#         html = driver.page_source
#         soup = BeautifulSoup(html, 'lxml')
#         soup = pd.DataFrame(soup)
#         soup.to_csv('./navertest.csv',encoding='utf-8')
#         time.sleep(5) # 중요함
#         cu = driver.current_url # 검색이 성공된 플레이스에 대한 개별 페이지
        
#         res_code = re.findall(r"place/(\d+)", cu)
#         final_url = 'https://pcmap.place.naver.com/restaurant/'+res_code[0]+'/review/visitor#'
        
#         print(final_url)
#         rawData['naver_map_url'][i]=final_url
        
#     except IndexError:
#         rawData['naver_map_url'][i]= ''
#         print('none')

# rawData.to_csv('veganfood_fin_url.csv', encoding = 'utf-8-sig')

