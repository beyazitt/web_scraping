def not_hesapla(satır):
    #satır = satır[:-1]  end="" ile aynı işevi görür. Her satırın sonunda bulunan gizli "\n" karakterini dahil etmez.
    #print(satır,end="")
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)
    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85 ):
        harf = "BA"
    elif (son_not >= 80 ):
        harf = "BB"
    elif (son_not >= 75 ):
        harf = "CB"
    elif (son_not >= 70 ):
        harf = "CC"
    elif (son_not >= 65 ):
        harf = "DC"
    elif (son_not >= 60 ):
        harf = "DD"
    elif (son_not >= 55 ):
        harf = "FD"
    else:
        harf = "DD"

    return isim + "----------->" + harf + "\n"




with open("C:/Users/bbeya/Desktop/dosya.txt","r",encoding="utf-8") as file:
    öğrenciler = []

    for i in file:

        öğrenciler.append(not_hesapla(i))
    with open("C:/Users/bbeya/Desktop/öğrenciler.txt","w",encoding="utf-8") as file2:
        for i in öğrenciler:
            file2.write(i)
