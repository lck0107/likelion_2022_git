import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(response.text)


#file = open("daum.html","w") file.write(response.text)
#find.close()

#print(soup.title)
#print(soup.title.string)
#print(soup.span)
#print(soup.findall('span'))

rank = 1

results = soup.findall('a','link_favorsch')

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    rank += 1