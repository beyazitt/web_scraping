print(""""
1'den 100'e kadar olan çift sayıları görmek için bir tuşa basın.
****************************************************************
""")
a = input()
liste = list()
liste = [i for i in range(1,101) if i%2 == 0]
print(liste)