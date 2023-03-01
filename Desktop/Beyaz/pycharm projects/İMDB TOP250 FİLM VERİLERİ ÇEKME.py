import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/"

response = requests.get(url)
print(response)
html_içeriği = response.content
soup = BeautifulSoup(html_içeriği,"html.parser")

a = float(input("Rating giriniz:"))
başlıklar = soup.find_all("td", {"class":"titleColumn"})
ratingler = soup.find_all("td", {"class":"ratingColumn imdbRating"})
print(len(başlıklar),len(ratingler))
for baslık,rating in zip(başlıklar,ratingler):
    baslık = baslık.text
    rating = rating.text
    baslık = baslık.strip( )
    baslık = baslık.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n", "")
    if float(rating) > a:
        print("Film ismi: {} Filmin Ragitngi : {}".format(baslık,rating))

#    print("Başlık:",baslık)
#    print("Rating:",rating)
#for i in soup.find_all("td", {"titleColumn"}):
#    print(i.text)
#    print("**********************")