import random
import time
print(""""
*************************
    SAYI TAHMİN OYUNU  
1-40 ARASINDA TAHMİN EDİN 
*************************
""")

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7
while True:
    a = int(input("Tahmininizi Giriniz:"))
    if ( a < rastgele_sayı):
        print("Doğruluğu kontrol ediliyor.....")
        time.sleep(1)
        print("Doğru bilemediniz. Daha büyük bir sayı söyleyin.")
        tahmin_hakkı -= 1
    elif ( a > rastgele_sayı):
        print("Doğruluğu kontrol ediliyor.....")
        time.sleep(1)
        print("Doğru bilemediniz. Daha küçük bir sayı söyleyin.")
        tahmin_hakkı -= 1
    elif ( a == rastgele_sayı):
        print("Doğruluğu kontrol ediliyor.....")
        time.sleep(1)
        print("Bingo.Doğru bildiniz.")
    if (tahmin_hakkı == 0):
        print("Tahmin hakkınız doldu.")
        print("Sayı:",rastgele_sayı)
        break

