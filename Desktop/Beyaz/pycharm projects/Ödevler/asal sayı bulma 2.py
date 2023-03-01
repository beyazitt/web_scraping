def asal_sayı(a):
    if(a==1):
        return False
    if(a==2):
        return True
    for i in range(2,a):
        if(a%i == 0):
            return False
    return True
while True:
    a = input("Bir sayı giriniz:")
    if(a == "q"):
        break
    else:
        a = int(a)
    if(asal_sayı(a)):
        print("Asaldır.")
    else:
        print("Asal değildir.")
