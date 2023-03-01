print(""""
*********************************************
Armstrong Sayısı Bulma Programına Hoşgeldiniz
*********************************************
""")
while True:
    b = 0
    liste = list()
    a = input("Lütfen bir sayı giriniz:(Çıkmak için q ya basın.)")
    c = len(a)
    if (a == "q"):
        print("Programdan çıkılıyor....")
        break
    else:
        for i in a:
            liste.append(i)
        for j in liste:
            b  += int(j) ** c
    if (int(a) == b):
        print("Tebrikler, bir armstrong sayısı girdiniz:",a)
    else:
        print("Malsınız, bu bir armstrong sayısı değil:",a)