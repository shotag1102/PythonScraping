from bs4 import BeautifulSoup
import requests

url = "https://www.python.org/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.find_all("h2"))
h2_text_list = []
for i,h2_tag in enumerate(soup.find_all("h2")):
    h2_text_list.append(h2_tag.text)
    print(h2_text_list)