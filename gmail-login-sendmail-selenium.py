import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

# 웹드라이버(웹 브라우저) 시동 // wait 만들어준다.
driver = webdriver.Chrome('./chromedriver')
wait = WebDriverWait(driver, timeout=5)

# 구글 로그인 사이트로 이동
driver.get('https://accounts.google.com/')

# 아이디를 치고 넥스트 버튼을 클릭
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#identifierId').send_keys('ksoongon97')
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '#identifierNext > div > button').click()

# 패스트워드 치고 넥스트버튼 대신 엔터치고 로그인 한다.
# wait.until(EC.element_to_be_selected(
#     driver.find_element(By.CSS_SELECTOR,
#                         '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')))
time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')\
#     .send_keys('1q2w3e4r##', Keys.ENTER)
login_chain = ActionChains(driver)
login_chain.send_keys('1q2w3e4r##').key_down(Keys.ENTER).perform()
login_chain.reset_actions()

# 지메일 화면으로 이동
print('지메일 화면으로 이동')
time.sleep(3)
driver.get('https://mail.google.com/mail/u/0/#inbox')

# 메일쓰기 버튼 클릭
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div').click()

# 메일쓰기 수행
time.sleep(2)
driver.get_screenshot_as_file('gmail.png')
print('screenshot ok..')
write_mail_action = ActionChains(driver)
(
    write_mail_action
    .send_keys('ksoongon97@gmail.com')        # 보내는 사람
    .key_down(Keys.TAB).key_down(Keys.TAB)    # 다음으로 탭 두번 쳐 줘야됨
    .send_keys('제목입니다2.')
    .key_down(Keys.TAB)
    .send_keys('본문입니다.')
    .key_down(Keys.TAB)
    .key_down(Keys.ENTER)
    .perform()
)
print('메일쓰기 완료')

# 인박스에 메일을 스크래핑 하기위해 현재 페이지의 소스를 가져온다.
time.sleep(2)
html = driver.page_source
# 파싱을 위한 뷰티풀숩 객체로 만든다. 드라이버(웹브라우저)는 종료
soup = BeautifulSoup(html, 'lxml')
driver.close()

print(soup)
