import requests
from bs4 import BeautifulSoup

url = "https://tech-diary.net/python-scraping-books/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
soup.find_all(["h2", "h3"])
h2_h3 = [tag.text for tag in soup.find_all(["h2", "h3"])]
print(h2_h3)
