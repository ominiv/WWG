from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import pandas as pd

csv_test = pd.read_csv('./example1.csv')  #csv파일이름
cat = csv_test['상호명']

driver = webdriver.Chrome("chromedriver.exe")#chromedriver를 사용하기위한 webdriver함수 사용

xyz = []

for i in cat:
 keyword = i #get keyword to search
 driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")##open google image search page
 driver.maximize_window()##웹브라우저 창 화면 최대화
 time.sleep(2)
 driver.find_element_by_css_selector("input.gLFyf").send_keys(keyword) #send keyword
 driver.find_element_by_css_selector("input.gLFyf").send_keys(Keys.RETURN)##send Keys.RETURN


 last_height = driver.execute_script("return document.body.scrollHeight") #initialize standard of height first

 list = driver.find_element_by_css_selector("img.rg_i.Q4LuWd")##thumnails list

 print(list)

 address = 'C:/Users/82109/git/python/naverimg/downloads'# 파일을 저장할 주소를 입력받기

 imgurl = list.get_attribute("src") # get thumnails address list
 time.sleep(1)
 urllib.request.urlretrieve(imgurl,address+"/"+str(keyword)+".jpg") # download images in address folder
 xyz.append(imgurl)

df = pd.DataFrame(xyz)
print(df)
df.to_csv('dlalwl.csv', index=False, encoding='UTF-8')