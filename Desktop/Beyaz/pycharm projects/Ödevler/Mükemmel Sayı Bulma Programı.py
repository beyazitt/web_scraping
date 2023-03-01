print(""""
****************************
Mükemmel Sayı Bulma Programı
****************************
""")
while True:
    b = 0
    a = input("Lütfen sayıyı giriniz:(Çıkmak için q ya basınız.)")
    if (a == "q"):
        print("Programdan çıkılıyor.....")
        break
    else:
        a = int(a)
        for i in range(1,a):
            if (a % i == 0):
                b += i
            else:
                continue
    if (a == b):
            print("Tebrikler, Mükemmel sayı girdiniz.:", a)
    else:
            print("Malsınız.Girdiğiniz sayı:", a)



