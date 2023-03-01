def mükemmel_sayı(a):
    liste = list()
    b = 0
    for i in range(1,a):
        if( a%i == 0):
            liste.append(i)
        else:
            continue
    for i in liste:
        b += i
    if(b==a):
        print("{} sayısı mükemmel sayıdır.".format(a))
    else:
        print("{} sayısı mükemmel sayı değildir.".format(a))
        return liste
while True:
    a = input("Bir sayı giriniz.(Çıkmak için q ya basınız.)")
    if (a == "q"):
        break
    else:
        a = int(a)
        mükemmel_sayı(a)

