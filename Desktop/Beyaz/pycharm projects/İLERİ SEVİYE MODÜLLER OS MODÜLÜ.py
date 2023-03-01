import os
from datetime import datetime
#print(dir(os))

#print(os.getcwd()) #Bulunduğu dizini gösterir.
#os.chdir("C:/Users/bbeya/Desktop") #Bulunduğu dizini değiştirir
#print(os.getcwd())


#print(os.listdir()) #Bulunduğu dizindeki dosyalar listelenir.
#for i in os.listdir():
#    print(i)



#print(os.getcwd())

#os.mkdir("Deneme1") #Bulunduğu klasöre Deneme1 adlı klasör oluşturdu.
#os.makedirs("Deneme2/Deneme3") #Klasör içine klasör oluşturdu.(içiçe klasörler)

#os.rmdir("Deneme2/Deneme3") # Deneme2 nin altındaki Deneme3 silindi.
#os.removedirs("Deneme2/Deneme3") #Hem Deneme 2 hem de Deneme3 silindi.

#os.rename("test.txt","test2.txt") #Dosyanın adı değişti.

#print(os.stat("test2.txt")) #Dosya verilerini verir.
#print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) #Dosyanın değiştirilme zamanını verir.

#for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("c:/Users/bbeya/Desktop"):
#    for i in dosya_isimleri:
#        if (i.endswith(".txt")):
#            print(i)




