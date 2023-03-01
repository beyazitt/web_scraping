def sayının_okunuşu(a):
    onlar_basamağı = {"1":"on","2":"yirmi","3":"otuz","4":"kırk","5":"elli","6":"altmış","7":"yetmiş","8":"seksen","9":"doksan"}
    birler_basamağı = {"1":"bir","2":"iki","3":"üç","4":"dört","5":"beş","6":"altı","7":"yedi","8":"sekiz","9":"dokuz"}
    while True:
        b = str(input("Lütfen 2 basamaklı bir sayı giriniz:"))
        liste = list(b)
        if True:
            return onlar_basamağı[liste[0]] + birler_basamağı[liste[1]]
            continue

print(sayının_okunuşu(45))


