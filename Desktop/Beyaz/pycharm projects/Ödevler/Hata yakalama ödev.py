#liste = ["345", "sadas", "324a", "14", "kemal"]
#for i in liste:

#    try:
#        print(int(i))
#    except ValueError:
#        print("Value Error")



def çift_sayı():
    while True:
        try:
            a = int(input("Bir sayı girin ve çift mi değil mi görün:"))
            if ( a%2 == 0):
                print("Bu bir çift sayıdır.")
            else:
                print("Bu bir tek sayıdır.")
        except ValueError:
            print("Lütfen bir sayı girin")

çift_sayı()


