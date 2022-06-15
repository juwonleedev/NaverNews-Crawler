import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
html = response.text

# 네이버를 시작 페이지로 버튼 선택 (브라우저 F12의 HTML 태그 보고 id값을 선택해서 넣기)
# id에는 맨 앞에 # 넣기 
soup = BeautifulSoup(html,'html.parser')
word = soup.select_one("#NM_set_home_btn") 

# 내가 원하는 텍스트만 
print(word.text)