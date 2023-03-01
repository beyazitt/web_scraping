import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/hashtag/dizipal"
response = requests.get(url) #Get fonksiyonu sayfanın özelliklerini verir.
#print(response)


html_içeriği = response.content # Sayfanın içeriğini verir.
soup = BeautifulSoup(html_içeriği,"html.parser")
#print(soup.prettify()) # Sayfanın kaynaklarını gösterir.
#print(soup.find_all("a")) #a etiketli sayfanın kaynaklarını gösterir.

#for i in soup.find_all("a"):
    #print(i.get("href")) # a etiketindeki linkleri aldı.
#    print(i.text) #a etiketinin içindeki yazıları aldı.
#    print("*******************************")

 #print(soup.find_all("div",{"class":"css-1dbjc4n"})) #Sadece belirli class daki değerleri alır.
