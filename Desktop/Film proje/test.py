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
ratingler = soup.find_all("td", {"class":"ratingColumn imdbRating"})
basliklar = soup.find_all("a", href=True, attrs={'class':'titleColumn'})
#for i in basliklar:
#    print(i.get("href"))





    

for k in soup.find_all("a"):
    k = str(k)
#    print(k)
    gecici_depo = k.split(" ")
    for j in gecici_depo:
        if j.startswith("href"):
            veriler[a] = j
            gecici_depo.clear()
    a += 1
    if a == 545:
        break
#print(veriler)
for b in range(0,545):
    if b < 45:
        continue
    else:
        gecici_depo.append(veriler[b][7:22])
        gidilecek_url = "https://www.imdb.com/" + gecici_depo[0]
        gecici_depo.clear()
print(gidilecek_url)
#print(gecici_depo)

#print(url_list)
        
#for i in range(0,250):
 #   url2 = url + url_list[i]
 #   print(url2)
        

