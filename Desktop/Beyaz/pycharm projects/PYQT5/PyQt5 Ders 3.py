import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)



    pencere = QtWidgets.QWidget()

    buton = QtWidgets.QPushButton(pencere)

    buton.setText("Burası bir butondur...")

    etiket = QtWidgets.QLabel(pencere)

    etiket.setText("Merhaba Dünya")

    etiket.move(200,30)

    buton.move(190,80) 

    pencere.setWindowTitle("PyQt5 Ders 3")
#    etiket1 = QtWidgets.QLabel(pencere) #Pencere üzerinde etiket oluşturdu.
#    etiket2 = QtWidgets.QLabel(pencere)
#    etiket2.setPixmap(QtGui.QPixmap("205699956_2947434105575333_7552013067211425064_n (1).jpg"))
#    etiket1.setText("Burası bir yazıdır.") #Etiketin üzerine yazı yazar.
#    etiket1.move(200,30)
#    etiket2.move(200,200)

    pencere.setGeometry(800,300,500,500) #Pencere çalıştığındaki yerini değiştirir.
    pencere.show()

    sys.exit(app.exec_())  #Bunun sayesişnde Çarpı tuşuna basmadığımız sürece uygulama çalışır.

Pencere()