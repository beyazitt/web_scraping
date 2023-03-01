import time
class Bilgisayar():
    def __init__(self,bilgisayarın_durumu = "Açık ",bilgisayarın_şarjı = 70,bilgisayarın_sesi = 45 ,bilgisayarın_işlemcisi = "İntel",bilgisayarın_ekran_kartı= "GeForce 1050"):
        self.bilgisayarın_durumu = bilgisayarın_durumu
        self.bilgisayarın_şarjı = bilgisayarın_şarjı
        self.bilgisayarın_sesi = bilgisayarın_sesi
        self.bilgisayarın_işlemcisi = bilgisayarın_işlemcisi
        self.bilgisayarın_ekran_kartı = bilgisayarın_ekran_kartı
    def bilgisayarı_aç(self):
        if(self.bilgisayarın_durumu == "Açık"):
            print("Bilgisayar zaten açık.")
        else:
            print("Bilgisayar açılıyor..")
            time.sleep(3)
            self.bilgisayarın_durumu = "Açık"
            print("Bilgisayarın Durumu :",self.bilgisayarın_durumu)
    def bilgisayarı_kapat(self):
        if (self.bilgisayarın_durumu == "Kapalı"):
            print("Bilgisayar zaten kapalı.")
        else:
            print("Bilgisayar kapatılıyor..")
            time.sleep(3)
            self.bilgisayarın_durumu = "Kapalı"
            print("Bilgisayarın Durumu :", self.bilgisayarın_durumu)
    def ses_ayar(self):
        while True:
            cevap = input("Ses açmak için '+' ya , kısmak için '-' ye basın.")
            if (cevap == "-"):
                if(self.bilgisayarın_sesi != 0):
                    self.bilgisayarın_sesi -= 1
                    print("Bilgisayarın Sesi:", self.bilgisayarın_sesi)
                else:
                    print("Bilgisayarın Sesi '0'")
            elif (cevap == "+"):
                if (self.bilgisayarın_sesi != 100):
                    self.bilgisayarın_sesi += 1
                    print("Bilgisayarın Sesi:", self.bilgisayarın_sesi)
                else:
                    print("Bilgisayarın Sesi '100'")
            else:
                print("Ses Ayarlandı",self.bilgisayarın_sesi)
                break
    def şarj_durumu(self):
        while True:
            cevap = input("Şarj olması için '+' ya basın.")
            if (cevap == "+"):
                if (self.bilgisayarın_şarjı != 100):
                    self.bilgisayarın_şarjı += 10
                    print("Bilgisayarın şarjı:",self.bilgisayarın_şarjı)
                else:
                    print("Şarjı Zaten Dolu:",self.bilgisayarın_şarjı)
            else:
                break
    def işlemci_değişimi(self):
        cevap = input("Yeni işlemcinizi yazınız:")
        self.bilgisayarın_işlemcisi = str(cevap)
        print("İşlemci optimize ediliyor....")
        time.sleep(3)
        print("Yeni işlemciniz:",self.bilgisayarın_işlemcisi)
    def yeni_ekran_kartı(self):
        cevap = input("Yeni ekran kartını yazınız:")
        print("Ekran kartı güncelleştirmesi yapılıyor...")
        time.sleep(3)
        self.bilgisayarın_ekran_kartı = str(cevap)
        print("Yeni ekran kartınız:",self.bilgisayarın_ekran_kartı)
    def özellikler(self):
        print("Bilgisayarın durumu : {}\nBilgisayarın şarjı: {}\nBilgisayarın sesi : {}\nBilgisayarın İşlemcisi : {}\nBilgisayarın ekran kartı : {}".format(self.bilgisayarın_durumu,self.bilgisayarın_şarjı,self.bilgisayarın_sesi,self.bilgisayarın_işlemcisi,self.bilgisayarın_ekran_kartı))
    def __del__(self):
        print("Bilgisayarınız satıldı...")

bilgisayar = Bilgisayar()
print(""""
Bilgisayar Sınıfı


1. Bilgisayarı Aç
2. Bilgisayarı Kapat
3. Ses Ayar
4. Şarj Durumu
5. İşlemci Değişimi
6. Ekran Kartı Değişimi
7. Bilgisayar Özellikleri
Çıkmak için 'q' ya basınız.
""")
while True:
    işlem = input("Lütfen işlem seçiniz:")
    if (işlem == "q"):
        print("Programdan çıkılıyor...")
        time.sleep(3)
        break
    elif (işlem == "1"):
        bilgisayar.bilgisayarı_aç()
    elif (işlem == "2"):
        bilgisayar.bilgisayarı_kapat()
    elif(işlem == "3"):
        bilgisayar.ses_ayar()
    elif(işlem == "4"):
        bilgisayar.şarj_durumu()
    elif(işlem == "5"):
        bilgisayar.işlemci_değişimi()
    elif(işlem == "6"):
        bilgisayar.yeni_ekran_kartı()
    elif(işlem == "7"):
        bilgisayar.özellikler()
    else:
        print("Hatalı işlem seçimi")


