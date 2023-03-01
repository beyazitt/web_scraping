import sys
#print(dir(sys))

#a = int(input("a:"))
#b = int(input("a:"))
#sys.exit() # Programı sona erdirir.Buradan sonraki hiçbir kod çalışmaz.
#c = int(input("c:"))





#stdin stdout stderr

#sys.stderr.write("Bu bir hata mesajıdır\n")

#sys.stderr.flush()

#sys.stdout.write("Bu normal bir yazıdır\n")





#print(sys.argv) #PyCharm dosyasının bulunduğu klasörün yolunu verir.

#for i in sys.argv:
#    print(i)


def kok_bulma(a,b,c):
    delta = b ** 2 - 4 * a * c
    if (delta < 0):
        print("Reel Kök Yok")
    else:
        kok_1 = (- b - delta ** (1/2)) / 2 * a
        kok_2 = ( b - delta ** (1/2)) / 2 * a
        return (kok_1,kok_2)
if len(sys.argv) == 4:
    print("Kök Bulma",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen Doğru Değerler Girin.")
    sys.stderr.flush()

