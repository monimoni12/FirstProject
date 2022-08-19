import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 초기 설정 (브라우저 실행 및 이동)
browser = webdriver.Chrome()
browser.get("https://eureka.ewha.ac.kr/eureka/my/public.do?pgId=P531005519")

# 브라우저가 로드될 때까지 적당히 기다려 준 뒤 page_source 조회
time.sleep(5)
print(browser.page_source)

# browser.close()