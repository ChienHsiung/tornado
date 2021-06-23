import requests
import json
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
preload ={"YourLocation":"Hsinchu"}

res = requests.post("http://192.168.0.18:8080/query",headers = headers,data = preload)

session = res.cookies
session_dic = session.get_dict()
print(session_dic)

soup = BeautifulSoup(res.text,'html.parser')

# print(res.text)
# print(soup.text)
# print (soup.contents)
print(soup.select('div ol'))
