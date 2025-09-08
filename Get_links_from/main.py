import requests as rq
from bs4 import BeautifulSoup

url=input("Enter your link: ")

if("https" or 'http') in url:
    data=rq.get(url)
else:
    data=rq.get("https://"+url)

soup=BeautifulSoup(data.text,"html.parser")
links=[]
for link in soup.find_all('a'):
    links.append(link.get('href'))

print(links)

with open('myLinks.txt','a') as save:
    print(links[:10],file=save)