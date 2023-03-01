#print("Murat","Ali","Veli", sep = "\n" )


#print(35,43,54,2000,sep = "/")


#print(*"ŞEFTALİ",sep = "/")



#a=3
#b=4
#print("{} + {} 'nin toplamı {}'dır.".format(a,b,a+b))
# 'pyformat.info'  sitesinden format fonsiyonunun çeşitlerine bakabilirsin.




#Liste oluşturma
#liste = [3.15,"Merhaba",5,25]
#print(type(liste))

#liste = list()
#print(len(liste))  "Listenin eleman sayısını verir."
#liste = [1,2,3,4,5,6,7,8,9,10]
#print(liste[:5])

#liste1 = [1,2,3]
#liste2 = [4,5,6]
#liste3 = liste1 + liste2
#liste3[3] = "a"
#print(liste3)

#liste=[1,2,3,4,5,6]
#liste.append(5)
#print(liste)
#liste.pop(2)
#print(liste)

#liste=[1,56,2,-3,255]
#liste.sort()   Sıralama yapar, eğer sayıysa küçükten büyüğe, eğer string ise alfabetik sıralar.
#print(liste)
#liste.sort(reverse = True)
#print(liste)


#liste=[[1,2],[2,3],[3,4]]
#print(liste[1][0])



#Tuple(Demetler)
#a = (1,1,1,1,1,2,2,5,6,7,8,8)
#print(type(a))
#print(a.count(1))
#Count metodu parantez içinde verilen sayının demetin içinde kaç defa geçtiğini sayar.

#a=("Python","C","Java")
#print(a.index("Python"))
#print((a.index("R"))
#İndex fonksiyonu parantez içinde verilen stringin hangi index de olduğunu söyler. Eğer ki tuple da yoksa error verir.

#b = (1,2,3,4,5)
#b[-1] = 4
#print(b)
#Tuple lar değiştirilemez.





#Dictionaries
#a = {"bir":1,"iki":2,"üç":3,"dört":4}
#print(type(a))
#print(a["bir"])
#a["beş"] = 5
#print(a)

#b = {"Market":["Migros","Gimsa","Ankargorss"],"Avm":[[1,2,3],[5,6]]}
#(b)
#print(b["Avm"][1][0])


#b = {"Market":["Migros","Gimsa","Ankargorss"],"Avm":[[1,2,3],[5,6]]}
#b["Avm"][0][1] += 2
#print(b)




#a = {"bir":1,"iki":2,"üç":3,"dört":4,"beş":11}
#print(a.keys())
#keys , anahtar değerlerini liste içinde verir.

#print(a.values())
#values , anahtarlara karşılık gelen değerleri liste içinde verir.

#print(a.items())
#items anahtara karşılık gelen değerleri tuple içine alır ve bütün tuple ları liste içinde verir.











#Kullanıcıdan girdi alma(input() fonksiyonu)
#input("Lütfen bir sayı giriniz")
#print(""""
#*****************
#Hesap Makinesi Programı

#İşlemler;

#1. Toplama İşlemi

#2. Çıkarma İşlemi

#3. Çarpma İşlemi

#4. Bölme İşlemi

#*****************
#""")

#a = int(input("Birinci Sayı:"))
#b = int(input("İkinci Sayı:"))
#işlem = input("İşlemi Giriniz")
#if işlem == "1":
#    print("{} ve {} nın toplamı {}'dır.".format(a,b,a+b))

#if işlem == "2":
#    print("{} ve {} nın farkı {}'dır.".format(a,b,a-b))

#if işlem == "3":
#    print("{} ve {} nın çarpımı {}'dır.".format(a,b,a*b))

#if işlem == "4":
#    print("{} ve {} nın bölümü {:.2f}'dır.".format(a,b,a/b))
#else:
 #   print("Geçersiz İşlem")








#LİSTE COMPREHENSİON
#liste3 = [1,2,3,4,5,6]
#liste4 = [i for i in liste3]
#print(liste4)


# = [2,4,6]
#liste1 = [i * 2 for i in liste]
#print(liste1)



#liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
#liste2 = list()
#for i in liste:
#    for j in i:
#        liste2.append(j)
#print(liste2)
#or
#liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
#liste1 = [j for i in liste for j in i]
#print(liste1)










#FONKSİYONLAR
#def selamla():
 #   print("Merhaba", "\nNasılsınız?")
#selamla()




#def karekök(a):
#    print("a nın karekökü {:.0f} dır".format(a ** (1/2)))
#karekök(16)


#def bilgiler(ad = "Bilgi yok", soyad = "Bilgi yok", numara = "Bilgi yok"):
#    print("Ad:",ad, "Soyad",soyad, "Numara", numara)
#bilgiler(numara=230015)


#def toplama(*a):
#    toplam = 0
#    for i in a:
#        toplam +=i
#    print(toplam)
#toplama(1,2,3,4)




#ikiyleçarp = lambda x : x * 2
#print(ikiyleçarp(3))



#def asal_sayı(a):
#    toplam = 0
#    for i in range(1,a+1):
#        if (a % i == 0):
#            toplam += i
#        else:
#            continue
#    if (toplam == a + 1):
#        print("{} sayısı asaldır.".format(a))
#    else:
#        print("{} sayısı asal değildir.".format(a))
#asal_sayı(6)



#def tam_bölenler(a):
#    liste = list()
#    for i in range(1,a+1):
#        if(a%i==0):
#            liste.append(i)
#        else:
#            continue
#    return liste
#while True:
#    a = input("Bir sayı giriniz:")
#    if(a == "q"):
#        break
#    else:
#        a = int(a)
#    print(tam_bölenler(a))

























#MODÜLLER
#import math
#import math as matematik
#print(math.factorial(9))
#print(math.floor(20.5))
#print(math.ceil(8.8))




