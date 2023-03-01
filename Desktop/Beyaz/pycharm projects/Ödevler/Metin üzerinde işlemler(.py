with open("C:/Users/bbeya/Desktop/metin2.txt","r+", encoding="Utf-8") as file:
    liste = file.readlines()
    a = list()
    c = str("")
    for i in liste:
        i = i.strip("\n")
        i = i.lstrip("  ")
        i = i.strip(".")
        i = i.strip(",")
        a.append(i)
    for i in a:
        c += i[0]
print(c)