#try:
#    a = int("324")
#    print("Program Burada")
#except ValueError:
#    print("Bir hata oluştu")
#print("Bloklar sona erdi!")




#try:
#    a = int(input("Sayı_1"))
#    b = int(input("Sayı_2"))
#    print(a/b)
#except ValueError:
#    print("Lütfen Inputu doğru girin")
#except ZeroDivisionError:
#    print("Bir sayı 0' a bölünemez")





try:
    a = int(input("Sayı_1"))
    b = int(input("Sayı_2"))
    print(a/b)
except ValueError:
    print("Lütfen Inputu doğru girin")
except ZeroDivisionError:
    print("Bir sayı 0' a bölünemez")
finally:
    print("Burası Çalıştı")

