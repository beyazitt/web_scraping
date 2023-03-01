import os
bütün_dosyalar = list()
mp3_dosyaları = list()
txt_dosyaları = list()
pdf_dosyaları = list()
mp3_sözlük = {}
txt_sözlük = {}
pdf_sözlük = {}
#print(os.listdir())

with open("C:/Users/bbeya/Desktop/mp3_dosyaları.txt","a",encoding="utf-8") as file:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/bbeya/Desktop"):
        for i in dosya_isimleri:
            if(i.endswith(".mp3") == 1):
                file.write("{} - {}\n".format(klasör_yolu,i))
with open("C:/Users/bbeya/Desktop/pdf_dosyaları.txt","a",encoding="utf-8") as file:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/bbeya/Desktop"):
        for i in dosya_isimleri:
            if(i.endswith(".pdf") == 1):
                file.write("{} - {}\n".format(klasör_yolu,i))
with open("C:/Users/bbeya/Desktop/txt_dosyaları.txt","a",encoding="utf-8") as file:
    for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/bbeya/Desktop"):
        for i in dosya_isimleri:
            if(i.endswith(".txt") == 1):
                file.write("{} - {}\n".format(klasör_yolu,i))





