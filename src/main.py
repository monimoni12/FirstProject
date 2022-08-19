from selenium import webdriver
from selenium.webdriver.common.by import By

# 초기 설정 (브라우저 실행 및 이동)
browser = webdriver.Chrome()
browser.get("http://python.org")

# Class 이름이 introduction인 태그의 text를 출력
print(browser.find_element(By.CLASS_NAME, 'introduction').text)

# Downloads 텍스트를 가진 요소를 클릭
browser.find_element(By.LINK_TEXT, 'Downloads').click()

# 브라우저 종료
browser.quit()
