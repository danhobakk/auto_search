from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 사용자로부터 키워드 입력 받기
keyword = input("검색할 키워드를 입력하세요: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
naver_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
daum_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
dc_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
zum_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def search_naver(keyword):
    naver_driver.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query="+keyword+"&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0")

def search_daum(keyword):
    daum_driver.get("https://search.daum.net/search?w=news&nil_search=btn&DA=STC&enc=utf8&cluster=y&cluster_page=1&q="+keyword+"&p=1&sort=recency")

def search_dc(keyword):
    dc_driver.get("https://search.dcinside.com/post/q/"+keyword)

def search_zum(keyword):
    zum_driver.get("https://search.zum.com/search.zum?method=realtime&option=accu&query="+keyword+"&rd=1&cm=tab&co=8")

search_naver(keyword)
search_daum(keyword)
search_dc(keyword)
search_zum(keyword)