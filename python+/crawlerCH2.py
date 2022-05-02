import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)

*--
file = open("daum.html","w")
file.write(response.text)
find.close()

print(soup.title)
print(soup.title.string)
print(soup.span)
print(soup.findall('span'))
--*
