from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

# 크롬 드라이버
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
dv = webdriver.Chrome(options=options)
dv.get("https://papago.naver.com/")

time.sleep(1)
elem = dv.find_element_by_css_selector(".edit_box___1KtZ3")
time.sleep(1)
elem.send_keys("안녕하세요 저는 케빈입니다")


dv.find_element_by_css_selector(".btn_text___3-laJ").click()

soup = BeautifulSoup(dv.page_source, "html.parser")
time.sleep(3)
# x = soup.select("div.edit_box___1KtZ3.active___3VPGL")
x = soup.select("")

print(x)



