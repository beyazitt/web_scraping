def ebob(a,b):
    i = 1
    ebob = 1
    while(i <= a and i <= b):
        if(a%i == 0 and b%i == 0):
            ebob *= i
        i += 1
    return ebob
sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:",ebob(sayı1,sayı2))
