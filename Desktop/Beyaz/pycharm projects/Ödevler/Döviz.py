import requests
from bs4 import BeautifulSoup
import sys
import time
url = "https://www.doviz.com/"
response = requests.get(url) #Get fonksiyonu sayfanın özelliklerini verir.
html_içeriği = response.content
soup = BeautifulSoup(html_içeriği,"html.parser")
Altın = 0
USD = 0
Borsa = 0


for i in soup.find_all("span",{"data-socket-key":"gram-altin","data-socket-attr":"s"}):
    for j in i:
        Altın = j
        print(j)
for i in soup.find_all("span",{"data-socket-key":"USD","data-socket-attr":"s"}):
    for j in i:
        USD = j
        print(j)
for i in soup.find_all("span",{"data-socket-key":"XU100","data-socket-attr":"s"}):
    for j in i:
        Borsa = j
        print(j)
while True:

    print("Gram Altın = {}".format(Altın))

    print("USD = {}".format(USD))

    print("BORSA = {}".format(Borsa))

    print(""""
      Lütfen İşlem Seçiniz:
      1) Param İle Kaç Gram Altın Alabilirim?
      2) Param Kaç USD'ye eşit?
      3) Tayyip ne zaman ölür?
      4) Her bir basış hükümete bir beddua...
    """)

    işlem = int(input("Lütfen işlem seçiniz:"))
    if (işlem == 1):
        a = int(input("Lütfen paranızı giriniz"))
        b = a // Altın
        print("Hesaplanıyor...")
        time.sleep(2)
        print("Paranız ile tam {} altın alabilirsiniz.".format(b))
        time.sleep(2)
    elif(işlem == 2):
        a = int(input("Lütfen paranızı giriniz"))
        print("Hesaplanıyor...")
        time.sleep(2)
        print("Paranız tam {} Amerikan Dolarına eşit".format(a / USD))
        timeçsleep(2)
    elif(işlem == 3):
        print("Umarım en kısa zamanda olurrrrr...")
        time.sleep(2)
    elif(işlem == 4):
        print("Kahrol tayyip al sana bombe")
        time.sleep(2)
    else:
        print("Hatalı işlem girdiniz")
        continue



