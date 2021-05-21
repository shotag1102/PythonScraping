import requests
from bs4 import BeautifulSoup
url = "https://www.python.org/"
r = requests.get(url)
print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.h2.text)
________________________________________________________
import requests
from bs4 import BeautifulSoup
url = "https://tech-diary.net/"
r = requests.get(url)
print(r.text)
soup = BeautifulSoup(r.text,"html.parser")
print(soup.find("h2").text)