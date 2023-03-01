import math
import time
print(""""
CASIO fx-82MS
Please use "on" as input
to start the program.
Whiiting le program is working,
you can exit by wroff
""")

def hesap_makinası():
        while True:
            try:
                time.sleep(1)
                print("""
                1) Toplama
                2) Çıkartma
                3) Çarpma
                4) Bölme
                5) sin
                6) cos
                7) tan
                8) Karekök
                9) Faktoriyel
                10) log
                11) ln
                """)
                işlem = input("Lütfen yapacağınız işlemi seçiniz....(Çıkmak için off yazınız.)")
                if(işlem == "off"):
                    print("Programdan çıkılıyor......")
                    time.sleep(3)
                    break
                else:
                    işlem = int(işlem)
                if(işlem == 1):
                    a = int(input("İlk Sayıyı Giriniz:"))
                    b = int(input("İkinci Sayıyı Giriniz:"))
                    print("{} ve {} nın toplamı {} dır.".format(a,b,a+b))
                    time.sleep(3)
                elif ( işlem == 2):
                    a = int(input("İlk Sayıyı Giriniz:"))
                    b = int(input("İkinci Sayıyı Giriniz:"))
                    print("{} ve {} nın farkı {} dır.".format(a, b, a - b))
                    time.sleep(3)
                elif (işlem == 3):
                    a = int(input("İlk Sayıyı Giriniz:"))
                    b = int(input("İkinci Sayıyı Giriniz:"))
                    print("{} ve {} nın çarpımı {} dır.".format(a, b, a * b))
                    time.sleep(3)
                elif (işlem == 4 ):
                    a = int(input("İlk Sayıyı Giriniz:"))
                    b = int(input("İkinci Sayıyı Giriniz:"))
                    print("{} ve {} nın bölümü {} dır.Kalan {} dır.".format(a, b, a / b, a%b))
                    time.sleep(3)
                elif (işlem == 5):
                    a = int(input("Derecesini giriniz:"))
                    print(math.sin(a))
                    time.sleep(3)
                elif ( işlem == 6):
                    a = int(input("Derecesini giriniz:"))
                    print(math.cos(a))
                    time.sleep(3)
                elif ( işlem == 7):
                    a = int(input("Derecesini giriniz:"))
                    print(math.tan(a))
                    time.sleep(3)
                elif ( işlem == 8):
                    a = int(input("Karekök almasını istediğiniz sayıyı giriniz:"))
                    print(math.sqrt(a))
                    time.sleep(3)
                elif ( işlem == 9):
                    a = int(input("Faktöriyelini bulmasını istediğiniz sayıyı giriniz:"))
                    print(math.factorial(a))
                    time.sleep(3)
                elif ( işlem == 10):
                    a = int(input("Logaritmasını bulmasını istediğiniz sayıyın tabanını giriniz:"))
                    b = int(input("Logaritmasını bulmasını istediğiniz sayıyıyı giriniz:"))
                    print(math.log(a,b))
                    time.sleep(3)
                elif ( işlem == 11):
                    a = int(input("'e' tabanında logaritmasını bulmasını istediğiniz sayıyın tabanını giriniz:"))
                    print(math.log(a))
                    time.sleep(3)
            except ValueError:
                print("Geçerli bir işlem giriniz.")

a = input("Selam, hoşgeldiniz.")
if(a == "on"):
    hesap_makinası()


