import requests
from bs4 import BeautifulSoup

url = "https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}"
target_url = url.format(1)   #{}のなかにページ数が入る記述
print(target_url)
r = requests.get(target_url)
soup = BeautifulSoup(r.text, "html.parser")
contents = soup.find_all("div", class_= "cassetteitem")
print(len(contents))
content = contents[0]
#print(content)
detail = content.find("div", class_="cassetteitem-detail")
table = content.find("table", class_="cassetteitem_other")
title = detail.find("div", class_="cassetteitem_content-title").text
address = detail.find("li", class_="cassetteitem_detail-col1").text
access = detail.find("li", class_="cassetteitem_detail-col2").text
age = detail.find("li", class_="cassetteitem_detail-col3").text
print(title, address,access,age)
tr_tags = table.find_all("tr",class_="js-cassette_link")
tr_tag = tr_tags[0]