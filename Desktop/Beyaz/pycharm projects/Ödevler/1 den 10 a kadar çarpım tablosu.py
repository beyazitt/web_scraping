print(""""
Bir Sayıya Tuşa Basın ve Çarpım Tablosunu Görün...
""")
while True:
    a = input()
    b = 0
    for i in range(0,11):
        for x in range(0,11):
            b = i * x
            print("{} kere {},{} eder.".format(i,x,b))

