from Kütüphanesınıfı import *
print("""
********************************
Kütüphane Programına Hoşgeldiniz.
İşlemler:
1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
Çıkmak için 'q' ya basn.

********************************
""")

kütüphane = kütüphane()

while True:

    işlem = input("Yapacağınız işlem:")
    if(işlem=="q"):
        print("Program sonlandırılıyor...")
        break
    elif(işlem == "1"):
        kütüphane.kitapları_göster()
    elif(işlem == "2"):
        isim = input("Hangi kitabı istiyorsunuz ?")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif(işlem == "3"):
        isim = input("Ekleyeceğiniz Kitabın Adını Giriniz:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı:"))
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap Sisteme Ekleniyor....")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap Sisteme Eklendi")
    elif(işlem == "4"):
        isim = input("Sileceğiniz Kitabın Adını Giriniz:")
        print("Kitap Sistemden Siliniyor....")
        time.sleep(2)
        kütüphane.kitap_sil(isim)
        print("Kitap Sistemden Silindi.")
        
    elif(işlem == "5"):
        isim = input("Lütfen baskısını yükselteceğiniz kitabın adını girin:")
        ("Baskı Yükseltiliyor...")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı Yükseltildi.")
    else:
        print("Geçersiz işlem.")
        break








































