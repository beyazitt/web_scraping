class Dosya():
    def __init__(self):

        with open("C:/Users/bbeya/Desktop/metin.txt","r",encoding="Utf-8") as file:
            dosya_içeriği = file.read()
            kelimeler = dosya_içeriği.split()
            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip("")
                i = i.strip(".")
                i = i.strip(",")
                self.sade_kelimeler.append(i)
            for i in self.sade_kelimeler:
                print(i)
    def tüm_kelimeler(self):
        kelimeler_kümesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)
        print("Tüm kelimeler.........")
        for i in kelimeler_kümesi:
            print(i)
            print("******************")
    def kelime_frekansı(self):
        kelime_sözlük = dict()
        for i in self.sade_kelimeler:
            if(i in kelime_sözlük):
                kelime_sözlük[i] += 1
            else:
                kelime_sözlük[i] = 1
        for kelime,sayi in kelime_sözlük.items():
            print("{} kelimesi {} defa geçiyor.".format(kelime,sayi))
    def kelime_varmı(self):
        while True:
            a = input("Lütfen bir kelime girin ve metin içinde var mı kontrol edin, eğer varsa kaç defa söyleyecek olmamız da cabası :):):)")
            if (self.sade_kelimeler.count(a) == 0):
                print("Girdiğiniz kelimeden metinde bulunmamaktadır.")
            else:
                print("{} kelimesi metinde {} defa geçmektedir.".format(a,self.sade_kelimeler.count(a)))
dosya = Dosya()
dosya.kelime_varmı()