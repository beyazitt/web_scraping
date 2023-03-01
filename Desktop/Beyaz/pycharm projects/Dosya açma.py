#DOSYA AÇMA VE DOSYAYA YAZMA İŞLEMİ


#file = open("C:/Users/bbeya/Desktop/bilgiler.txt","w",encoding="utf-8")
#file.write("Beyazıt Koca, Mustafa Murat Coşkun")
#file.close

#file = open("C:/Users/bbeya/Desktop/bilgiler2.txt","a",encoding="utf-8")
#file.write("Selam \ncanım \n<3")
#file.close


#DOSYA OKUMA İŞLEMİ

#file = open("C:/Users/bbeya/Desktop/LabExam4andSolution (4).txt","r",encoding="utf-8")
#for i in file:
#    print(i)
#file.close()



#READ FONKSİYONU


#file = open("C:/Users/bbeya/Desktop/bilgiler2.txt","r",encoding="utf-8")
#içerik = file.read()
#print("Dosyanın içeriği:")
#print(içerik)
#içerik2 = file.read()
#print("Dosyanın içeriği:")
#print(içerik2)




#READLİNE FONKSİYONU


#file = open("C:/Users/bbeya/Desktop/bilgiler2.txt","r",encoding="utf-8")
#print(file.readline())
#print(file.readline())
#print(file.readline())




#DOSYALARDA KULLANILAN FONKSİYONLAR
#seek() ve tell() fonksiyonları
#seek() fonksiyonu imleci istediğimiz bayta götürür.
#tell fonksiyonu imlecin hangi baytta bulunduğunu söyler.



#with open("C:/Users/bbeya/Desktop/bilgiler2.txt","r",encoding="utf-8") as file:
#    file.seek(5)
#    print(file.read(10))
#    print(file.tell())



#seek() write() r+ kipi


#with open("C:/Users/bbeya/Desktop/bilgiler2.txt","r+",encoding="utf-8") as file:
#    file.seek(10)
#    file.write("Deneme")
#with open("C:/Users/bbeya/Desktop/bilgiler2.txt","r+",encoding="utf-8") as file:
#    print(file.read())

#with open("C:/Users/bbeya/Desktop/bilgiler2.txt","a",encoding="utf-8") as file:
#    file.write("Erkan Akar\n")
#with open("C:/Users/bbeya/Desktop/bilgiler2.txt", "r",encoding="utf-8") as file:
#    print(file.read())

with open("C:/Users/bbeya/Desktop/bilgiler2.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Deniz Akar\n")
    print(liste)
    file.seek(0)
    for i in liste:
        file.write(i)
    print(file.read())



