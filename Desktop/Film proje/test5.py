import requests
from bs4 import BeautifulSoup


def veriyi_cek():
    
    url = "https://www.hdfilmcehennemi.life/category/film-izle/"
    film_url = ""
    gidilecek_url = ""
    konu = list()
    response = requests.get(url)
    print(response)
    film_isimleri = list()
    a = 0
    uzunluk = 0
    veriler = dict()
    url_list = list()
    gecici_depo = list()
    gecici_depo_2 = list()
    gecici_dict = dict()
    html_içeriği = response.content
    soup = BeautifulSoup(html_içeriği,"lxml")   
#    for i in soup.find_all("h2",attrs={"class":"title px-3"}):
#        film_isimleri.append(i.text)

    for i in soup.find_all("div",attrs = {"class":"poster poster-pop"}):
        gidilecek_url = i.find("a").get("href")
        url_list.append(gidilecek_url)


    for i in range(1,2):
        url_devam = "https://www.hdfilmcehennemi.life/category/film-izle/" + "page/" + str(i) + "/"
        response = requests.get(url_devam)
        html_içeriği_devam = response.content
        soup_devam = BeautifulSoup(html_içeriği_devam,"lxml") 
        for i in soup_devam.find_all("h2",attrs={"class":"title px-3"}):
            film_isimleri.append(i.text)
        print(film_isimleri)
        for i in soup_devam.find_all("div",attrs = {"class":"poster poster-pop"}):
            gidilecek_url = i.find("a").get("href")
            url_list.append(gidilecek_url)

    for i in url_list:
        i = str(i)
        film_url = i
        response_film = requests.get(film_url)
        html_içeriği_devam_film = response_film.content
        soup_devam_film = BeautifulSoup(html_içeriği_devam_film,"lxml") 
        for x in soup_devam_film.find_all("article",attrs = {"class":"text-white"}):
            konusu = x.find("p").text                      
            if a < 28:
                gecici_depo =konusu.split(" ")
                uzunluk = len(gecici_depo)
#                print(gecici_depo)
                for j in gecici_depo:
                    j = str(j)
                    sayi = gecici_depo.count(j)
                    gecici_depo_2.append({j,sayi})
                    for m in range(0 , sayi):
                        index = gecici_depo.index(j)
                        gecici_depo.pop(index)
                    
            else:
                break
            veriler[a] = gecici_depo_2
            gecici_depo_2.clear()
            a += 1
#
            gecici_depo.clear()
            
                
            
            
#            konu.clear()
    a = 0
    print(veriler[10])
        
#    print(film_isimleri)
#    print(konu)

            
            
veriyi_cek()

    



