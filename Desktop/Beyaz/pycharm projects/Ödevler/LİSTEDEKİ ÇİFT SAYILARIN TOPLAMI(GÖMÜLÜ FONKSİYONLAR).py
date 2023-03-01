from functools import reduce
def çift_sayılar(x):
    if (x%2 == 0):
        return True
    else:
        return False
liste = [1,2,3,4,5,6,7,8,9,10]
filtre = list(filter(çift_sayılar,liste))
print(reduce(lambda x,y: x+y,filtre))
