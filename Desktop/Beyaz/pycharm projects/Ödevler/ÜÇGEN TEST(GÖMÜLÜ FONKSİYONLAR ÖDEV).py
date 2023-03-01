liste = [(3,4,5),(6,8,10),(3,10,7)]
def üçgen_mi(liste):
    if(abs(liste[0]-liste[1]) < liste[2] < abs(liste[0] + liste[1])):
        return True
    elif(abs(liste[0]-liste[2]) < liste[1] < abs(liste[0] + liste[2])):
        return True
    elif(abs(liste[1]-liste[2]) < liste[0] < abs(liste[1] + liste[2])):
        return True
    else:
        return False
print(list(filter(üçgen_mi,liste)))