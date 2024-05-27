from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 사용자로부터 키워드 입력 받기
keyword = input("검색할 키워드를 입력하세요: ")

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver", options=chrome_options)

def search_naver(keyword):
    driver.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%84%A4%EC%9D%B4%EB%B2%84")
    time.sleep(2)
    search_box = driver.find_element_by_name("greenbox")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    results = driver.find_elements_by_css_selector("a.news_tit")  # 클래스 이름은 확인 후 수정 필요
    print("네이버 검색 결과:")
    for result in results:
        title = result.text
        link = result.get_attribute('href')
        print(f"제목: {title}\n링크: {link}\n")

def search_daum(keyword):
    driver.get("https://www.daum.net")
    time.sleep(2)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    results = driver.find_elements_by_css_selector("a.f_link_b")  # 클래스 이름은 확인 후 수정 필요
    print("다음 검색 결과:")
    for result in results:
        title = result.text
        link = result.get_attribute('href')
        print(f"제목: {title}\n링크: {link}\n")

def search_google(keyword):
    driver.get("https://www.google.com")
    time.sleep(2)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    results = driver.find_elements_by_css_selector("a h3")  # 제목 태그를 선택
    print("구글 검색 결과:")
    for result in results:
        title = result.text
        link = result.find_element_by_xpath('..').get_attribute('href')  # 부모 태그의 href 속성 추출
        print(f"제목: {title}\n링크: {link}\n")

# 각 검색 엔진에 대해 검색 수행
search_naver(keyword)
search_daum(keyword)
search_google(keyword)

# 브라우저 닫기
driver.quit()