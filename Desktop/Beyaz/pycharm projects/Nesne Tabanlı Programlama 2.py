import time

class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgileri_göster(self):
        print("İsim : {}\nMaaş : {}\nDepartman : {} ".format(self.isim,self.maaş,self.departman))
    def departman_değiştir(self,yeni_departman):
        self.departman = yeni_departman
class Yönetici(Çalışan):
    def zam(self,yeni_maaş):
        self.maaş = yeni_maaş
yönetici = Yönetici("Beyazıt Koca",5000,"Yazılımcı")
print(yönetici.bilgileri_göster())
time.sleep(2)
yönetici.departman_değiştir("İnsan Kaynakları")
print(yönetici.bilgileri_göster())
time.sleep(2)
yönetici.zam(9000)
print(yönetici.bilgileri_göster())
time.sleep(2)
class Yönetici(Çalışan):   #Override
    def __init__(self,isim,maaş,departman,kişi_sayısı):
        print("Yönetici Sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı
    def zam(self,yeni_maaş):
        self.maaş = yeni_maaş
    def bilgileri_göster(self):
        print("İsim : {}\nMaaş : {}\nDepartman : {}\nKişi Sayısı : {} ".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
yönetici = Yönetici("Beyazıt Koca",5000,"Yazılımcı",10)
print(yönetici.bilgileri_göster())
time.sleep(3)


class Yönetici(Çalışan):   #Super anahtar kelimesi
    def __init__(self,isim,maaş,departman,kişi_sayısı):
        super().__init__(isim,maaş,departman)
        print("Yönetici Sınıfının init fonksiyonu")
        self.kişi_sayısı = kişi_sayısı
    def zam(self,yeni_maaş):
        self.maaş = yeni_maaş
    def bilgileri_göster(self):
        print("İsim : {}\nMaaş : {}\nDepartman : {}\nKişi Sayısı : {} ".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
yönetici = Yönetici("Beyazıt Koca",5000,"Yazılımcı",10)
print(yönetici.bilgileri_göster())
