import requests
from bs4 import BeautifulSoup

# solving connection aborted : header 
# 마치 Mozila web browser로 접속 한 것 처럼 만들어주는 header
header = {'User-agent' : 'Mozila/2.0'}

response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.cluster_text')

# list 
print(titles)

# test of lists - 공백제거 
for title in titles : 
    print(title.text.strip())