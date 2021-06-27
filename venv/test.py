from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

fp = open("text1", 'r', encoding='utf-8')
text = fp.read()

# 크롬 드라이버
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
dv = webdriver.Chrome(options=options)
dv.get("https://www.naver.com/")


elem = dv.find_element_by_name("query")
elem.send_keys("파파고")
elem.send_keys(Keys.RETURN)

elem = dv.find_element_by_css_selector(".trans_txt._textarea")
elem.send_keys(text)
time.sleep(1)
dv.find_element_by_css_selector(".btn_trans._trans").click()

soup = BeautifulSoup(dv.page_source, "html.parser")
time.sleep(3)
print(soup.select("p.trans_txt._textview")[1].text)




