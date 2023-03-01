import sqlite3

connection = sqlite3.connect("kütüphane.db") #KENDİ DOSYAMIZA BAĞLANMA

cursor = connection.cursor() #İMLEÇ OLUŞTURMA

def tablo_oluştur():
    
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    connection.commit()

def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    connection.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    connection.commit()
def verileri_al():
    cursor.execute("Select * from kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri:")
    for i in liste:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim, Yazar from kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri:")
    for i in liste:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("Select * from kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri:")
    for i in liste:
        print(i)
def verileri_güncelle(eski_yayınevi, yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi = ?",(yeni_yayınevi, eski_yayınevi))
    connection.commit()
def verileri_sil(Yazar):
    cursor.execute("Delete from kitaplık where Yazar = ?",(Yazar,))
    connection.commit()
verileri_güncelle("Doğan Kitap","Everest")
verileri_sil("Ahmet Ümit")
verileri_al()
#verileri_al3("Everest")
#verileri_al()
#verileri_al2()
isim = input("İsim:")
yazar = input("Yazar:")
yayınevi = input("Yayınevi:")
sayfa_sayısı = int(input("Sayfa Sayısı:"))
#veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)
connection.close()  
