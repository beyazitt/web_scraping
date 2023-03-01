def asal_sayı(a):
    toplam = 0
    for i in range(1,a+1):
        if (a % i == 0):
            toplam += i
        else:
            continue
    if (toplam == 1):
        print("{} sayısı asal değildir.".format(a))
    elif (toplam == a + 1):
        print("{} sayısı asaldır.".format(a))
    else:
        print("{} sayısı asal değildir.".format(a))
a = int(input("Bir sayı giriniz."))
asal_sayı(a)