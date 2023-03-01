a = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb".lower()
add = dict()

for i in a:
    if(i in add ):
        add[i] += 1
    else:
        add[i] = 1
for i,j in add.items():
    print("{} harfi {} defa geçiyor.".format(i,j))