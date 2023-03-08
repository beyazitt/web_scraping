import requests
from bs4 import BeautifulSoup

url = "https://www.hdfilmcehennemi.life/category/film-izle/"
gidilecek_url = ""
response = requests.get(url)
print(response)
veriler = dict()
url_list = list()
gecici_depo = list()
a = 0
b = 45
html_içeriği = response.content
soup = BeautifulSoup(html_içeriği,"html.parser")


for i in soup.find_all("h2",{'class':'title px-3'}):
#    print(i)
    i = str(i)
    gecici_depo = i.split(">")
    print(gecici_depo)
    for j in gecici_depo:
        if j.endswith("h2"):
            veriler[a] = j[:-4]
            a += 1
    if a == 28:
        a = 0
        break     
print(veriler)       

for b in range(0,28):


    gecici_depo.append(veriler[b])
    gidilecek_url = "https://www.imdb.com/" + gecici_depo[0]
    print(gidilecek_url)
    gecici_depo.clear()
