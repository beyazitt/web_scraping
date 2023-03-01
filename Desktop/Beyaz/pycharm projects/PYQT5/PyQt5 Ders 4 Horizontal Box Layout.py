import sys
from PyQt5 import QtWidgets #Pencere ve butonlar burada

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    okay = QtWidgets.QPushButton("Tamam")

    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()

 #    h_box.addStretch()  #Dene ve gör

    h_box.addWidget(okay)

    h_box.addStretch()   #Dene ve gör

    h_box.addWidget(cancel)

#    h_box.addStretch()   #Dene ve gör

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 4")

    pencere.setLayout(h_box)

    pencere.show()

    sys.exit(app.exec_())  #Bunun sayesişnde Çarpı tuşuna basmadığımız sürece uygulama çalışır.

Pencere()