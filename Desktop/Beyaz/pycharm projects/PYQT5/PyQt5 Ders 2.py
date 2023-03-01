import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 2")
    etiket1 = QtWidgets.QLabel(pencere) #Pencere üzerinde etiket oluşturdu.
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("205699956_2947434105575333_7552013067211425064_n (1).jpg"))
    etiket1.setText("Burası bir yazıdır.") #Etiketin üzerine yazı yazar.
    etiket1.move(200,30)
    etiket2.move(0,50)

    pencere.setGeometry(800,300,500,500) #Pencere çalıştığındaki yerini değiştirir.
    pencere.show()

    sys.exit(app.exec_())  #Bunun sayesişnde Çarpı tuşuna basmadığımız sürece uygulama çalışır.

Pencere()