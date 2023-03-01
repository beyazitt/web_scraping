#MAP FONKSİYONU


#liste1 = [1,2,3,4]
#liste2 = [5,6,7,8]
#liste3 = [9,10,11,12,13]
#print(list(map(lambda x,y,z : x * y * z,liste1,liste2,liste3)))



#REDUCE FONKSİYONU

from functools import reduce
#print(reduce(lambda x,y : x*y,[1,2,3,4,5]))#1*2 = 2 , 2*3 = 6 , 6*4 = 24, 24*5 = 120
def maksimum(x,y):
    if (x>=y):
        return x
    else:
        return y
#print(reduce(maksimum,[-2,3,1,4]))




#FİLTER FONKSİYONU

#print(list(filter(lambda x : x%2 == 0,[1,2,3,4,5,6,7,8,9,10,11])))


def asal_mi(x):
    i = 2
    if(x == 1):
        return False
    elif (x == 2):
        return True
    while (i<x):
        if( x % i == 0 ):
            return False
        i += 1
    return True
#print(list(filter(asal_mi,range(1,100))))





#ZİP FONKSİYONU

#liste1 = [1,2,3,4,5]
#liste2 = [6,7,8,9,10,11]
#i = 0
#sonuç = list()
#while(i < len(liste1) and i < len(liste2)):
#    sonuç.append((liste1[i],liste2[i]))
#    i += 1
#print(sonuç)



#print(list(zip(liste1,liste2)))



#sözlük1 = {"Kavun":"Yaz","Karpuz":"Yaz","Çilek":"Yaz","Kiraz":"Yaz"}
#sözlük2 = {"Portakal":"Kış","Mandalina":"Kış","Kivi":"Kış"}
#print(list(zip(sözlük1.values(),sözlük2.keys())))


liste = ["Elma","Armut","Kiraz","Muz"]
#i = 0
#sonuç = list()
#while(i<len(liste)):
#    sonuç.append((i,liste[i]))
#    i += 1
#print(sonuç)

#print(list(enumerate(liste))) #Yukarıdaki işlemlerle aynı işi yani listedeki elemanları index değerleri ile beraber verir.




#ALL VE ANY FONKSİYONLARI

def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True

liste =  [True,False,True,False,True]
print(hepsi(liste))
liste2 = [1,2,3,4,5]
print(hepsi(liste2))


def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
print(herhangi(liste))
liste3 = [0,False,0,False]
print(herhangi(liste3))

