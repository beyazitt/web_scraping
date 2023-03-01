import sys
from PyQt5 import QtWidgets #Pencere ve butonlar burada

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    okay = QtWidgets.QPushButton("Tamam")

    cancel = QtWidgets.QPushButton("İptal")

    v_box = QtWidgets.QVBoxLayout()

    v_box.addWidget(okay)

    v_box.addStretch()

    v_box.addWidget(cancel)


    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 1")

    pencere.setLayout(v_box)

    pencere.show()

    sys.exit(app.exec_())  #Bunun sayesişnde Çarpı tuşuna basmadığımız sürece uygulama çalışır.

Pencere()
