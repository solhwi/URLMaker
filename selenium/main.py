from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

filePath = "https://www.youtube.com/channel/UCLJNGmEfcuugzEjLyZ6mKKw" # 작업할 웹 브라우저 경로 
driver.get(filePath) # 경로의 웹 페이지 오픈

thumbnailClass = "thumbnail" # URL을 추출할 썸네일의 클래스 id 혹은 name - 현재는 id
thumbnailFindTag = By.ID # tag을 By.ID, 혹은 By.CLASS_NAME - 현재는 id

elements = driver.find_elements(thumbnailFindTag, thumbnailClass) # thumbnailClass를 id로 하는 element 전부 find
urlList = []

time.sleep(5)

for elem in elements:
    hrefAttr = elem.get_attribute("href") # element 내에서 하이퍼 링크만 가져옴
    if(hrefAttr != None):
        urlList.append(hrefAttr)
    
driver.close() # 다 쓴 크롬 닫아주고

count = 0

# 현재 폴더에 url.txt 파일 생성 혹은 열기, 문자열 삽입
with open('url.txt', 'w', encoding='utf-8') as f:
    for url in urlList:
        count = count + 1
        f.write(str(count) + "번 영상 : ")

        f.write(url)
        f.write('\n')

