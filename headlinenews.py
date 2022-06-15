import requests
from bs4 import BeautifulSoup

# solving connection aborted : header 
# 마치 Mozila web browser로 접속 한 것 처럼 만들어주는 header
header = {'User-agent' : 'Mozila/2.0'}

response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.section_sub_txt')

# <p class="section_sub_txt">오후 2시~오후 3시까지 집계한 결과입니다.</p>
print(title)

# 오후 2시~오후 3시까지 집계한 결과입니다.
print(title.text)