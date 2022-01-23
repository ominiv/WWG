import selenium
import inspect, os, platform, time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# waiting function added
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
from urllib.parse import quote_plus
from webdriver_manager.chrome import ChromeDriverManager


os.chdir('C:\\Users\\user\\PJT\\WhereWeGo\\')

#-- Chromedriver loading
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # hide error
current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))

if platform.system() == 'Windows': 
    driver_path = os.path.join(current_folder, 'chromedriver.exe') 
else: 
    driver_path = os.path.join(current_folder, 'chromedriver')
# driver = webdriver.Chrome(driver_path, options=options) 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)


# kakao map 접근
url = 'https://map.kakao.com/?map_type=TYPE_MAP&folderid=4049789&target=other&page=bookmark'
driver.get(url)
print('kakaomap 접근 ...')
time.sleep(3) 

# soup.find('div.FavoriteInformationBundle > div > div > div > strong')[0].text
# tds[0].find('a').text
# tds[0].find('span').text

cnt = 3
ids = ["info.other.favorite.page.no1", "info.other.favorite.page.no2", "info.other.favorite.page.no3"]

# link = driver.find_element_by_css_selector(str('#other\.favorite > ul > li:nth-child('+'2'+') > div.FavoriteInformationBundle > div > div > div.tit_directory > strong > a'))
# link.click()

datas=[]
for i in range(cnt) :
    right = driver.find_element_by_id(ids[i])
    right.click()
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find_all(class_ = 'info_directory')
    time.sleep(1)
    idx = 0
    for td in tds[:len(tds)-2] :
        idx +=1
        link = driver.find_element_by_css_selector(str('#other\.favorite > ul > li:nth-child('+str(idx)+') > div.FavoriteInformationBundle > div > div > div.tit_directory > strong > a'))
        try : 
            link.click()
            WebDriverWait(driver,3).until(EC.alert_is_present())
            result = driver.switch_to_alert()
            print(result.text)
            result.dismiss()
            result.accept()
        except:
            morehtml = driver.page_source
            moresoup = BeautifulSoup(morehtml, 'lxml')
            try:
                memo = td.find('p').text
            except:
                memo = ' '
            try :
                store = td.find('a').text
            except :
                store = ' '
            try :
                address = moresoup.find(class_ = 'address').text
            except :
                address = ' '
            try :
                phone = moresoup.find(class_ = 'phone').text
            except :
                phone = ' '
            try :
                imgUrl = moresoup.find(class_ = 'placeimg')['src']
                jpg = store+'.jpg'
                with urlopen('https:'+imgUrl) as f:
                    with open('./img/' + store + '.jpg','wb') as h: # 이미지 + 사진번호 + 확장자는 jpg
                        img = f.read() #이미지 읽기
                        h.write(img) # 이미지 저장
            except :
                imgUrl = ' '
                jpg = ' '
            datas.append([store, phone, address, memo, imgUrl, jpg])
            print(str(i)+'페이지 / '+ store)

total = pd.DataFrame(datas)
total.columns = ['상호명','전화번호','소재지','설명','imgUrl', 'jpg']
total.to_csv('C:\\Users\\user\\Desktop\\FinalPJT\\kakaomap_zerowaste.csv',encoding='utf-8')


# with urlopen('https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200220_76%2F1582188574257vcc4T_JPEG%2FZ-QxdNLsnG2OWKAucxqq1hCq.jpg') as f:
#     with open('./img/' + '카페 패밀리앤프렌즈' + '.jpg','wb') as h: # 이미지 + 사진번호 + 확장자는 jpg
#         img = f.read() #이미지 읽기
#         h.write(img) # 이미지 저장

# import json
# from urllib.request import urlopen
# location = "서울특별시 은평구 은평로21길 32"
# data = urlopen("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=" + location)
# json = json.loads(data.read())

# latitude = json["results"][0]["geometry"]["location"]["lat"]
# longitude = json["results"][0]["geometry"]["location"]["lng"]

# print latitude
# print longitude


# 출처: https://wkdgusdn3.tistory.com/entry/Python-주소로-위도-경도-검색하기 [장삼의 착한코딩]