# 메인 화면
# http://e-lib.sen.go.kr/index.php

# 로그인 화면
# http://e-lib.sen.go.kr/member/login.php

# 마이라이브러리
# - 대출중인 도서
# https://e-lib.sen.go.kr/10_my/book_lend.php?sort=cl_no
# - 즐겨찾기
# http://e-lib.sen.go.kr/10_my/my_book.php
# - 예약중인 도서
# https://e-lib.sen.go.kr/10_my/book_reserve.php

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('D:/Program Files/Chrome/chromedriver')

driver.set_window_size(1300, 950)

driver.get('http://e-lib.sen.go.kr/member/login.php')

# 아이디, 비밀번호 입력
id = 'abc'
pw = '123'
driver.find_element_by_id('member_id_tmp').send_keys(id)
driver.find_element_by_id('member_pw_tmp').send_keys(pw)

# 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="save-btn"]').click()

driver.implicitly_wait(1)
driver.get('https://e-lib.sen.go.kr/10_my/book_lend.php?sort=cl_no')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 책 제목부분 가져오기
# myEBooks = soup.select('ul > li > div.list-body > div.flexbox > a > b')
myEBooks = soup.select('.flexbox > a > b')

with open('title.txt', 'w', encoding='utf-8') as myTitle:    
    for title in myEBooks:
        myTitle.write(title.text + '\n')

driver.quit()