import random
import time

class Kumanda():

    def __init__(self,tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["TRT","Show","Star","TV8","NTV SPOR"], kanal = "Show"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

    def tv_aç(self):
        if(self.tv_durum == "Açık"):
            print("Televizyon zaten açık.")
        else:
            print("Televizyon açılıyor")
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapatılıyor")
            self.tv_durum = "Kapalı"
    def ses_ayarları(self):
        while True:
            cevap = input("Sesi azalt: '<'\nSesi arttır: '>'\nÇıkış : çıkış")
            if (cevap == "<"):
                if(self.tv_ses == 0):
                    print("Ses zaten sıfır.")
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif (cevap == ">"):
                if(self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses ayarlandı")
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi...")


    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)

    def sonraki_kanal(self):
        while True:
            a = 0
            cevap = input("Bir sonraki kanala geçmek için '+' ya basın(Çıkmak için 'Exit' yazın.)")
            if ( cevap == "+"):
                a += 1
                self.kanal = self.kanal_listesi[a+1]

                print("Şu anki kanal:", self.kanal)
            else:
                break
    def önceki_kanal(self):
        while True:
            a = 0
            cevap = input("Bir önceki kanala geçmek için '-' ya basın(Çıkmak için 'Exit' yazın.)")
            if ( cevap == "-"):
                if (self.kanal == "TRT"):
                    print("Bir önceki Kanal Bulunmamaktadır.")
                else:
                    a -= 1
                    self.kanal = self.kanal_listesi[a-1]
                    print("Şu anki kanal:", self.kanal)
            else:
                break


    def __len__(self):
        return len(self.kanal_listesi)


    def __str__(self):
        return "Tv Durumu : {}\n Tv Ses: {}\n Kanal Listesi {}\n Şu Anki Kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()
print(""""
Televizyon Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısı Öğrenme
6. Bir Sonraki Kanala Geçme
7. Bir Önceki Kanala Geçme
8. Rastgele Kanala Geçme
9. Televizyon Bilgileri
Çıkmak için 'q' ya basın.
""")
while True:
    işlem = input("İşlemi Seçiniz:")
    if (işlem == "q"):
        print("Program sonlandırılıyor...")
        break
    elif(işlem == "1"):
        kumanda.tv_aç()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarları()
    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        kumanda.sonraki_kanal()
    elif (işlem == "6"):
        kumanda.önceki_kanal()
    elif(işlem == "7"):
        print("Kanal sayısı: ",len(kumanda))
    elif(işlem == "8"):
        kumanda.rastgele_kanal()
    elif (işlem == "9"):
        print(kumanda)
    else:
        print("Geçersiz işlem")

