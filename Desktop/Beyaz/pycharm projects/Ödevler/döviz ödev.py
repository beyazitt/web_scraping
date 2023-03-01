import os
import sys
import requests
from bs4 import BeautifulSoup
import time
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QApplication, QLabel, QPushButton, QTextEdit, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QAction, qApp, QMainWindow

url = "https://www.doviz.com/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

dolar = 0

euro = 0

sterlin = 0

bist100 = 0

bitcoin = 0

gumus = 0


class Uygulama(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.dolar = QPushButton("Dolar")
        self.euro = QPushButton("Euro")
        self.bist = QPushButton("Bist100")
        self.sterlin = QPushButton("Sterlin")
        self.btc = QPushButton("Bitcoin")
        self.gumus = QPushButton("Gümüş")
        self.dolar.clicked.connect(self.dolaricintl)
        self.euro.clicked.connect(self.euroicintl)
        self.bist.clicked.connect(self.bisticintl)
        self.sterlin.clicked.connect(self.sterlinicintl)
        self.btc.clicked.connect(self.btcicintl)
        self.gumus.clicked.connect(self.gumusicintl)

        self.yazi_alanidolar = QLabel("")
        self.yazi_alanieuro = QLabel("")
        self.yazi_alanibist = QLabel("")
        self.yazi_alanisterlin = QLabel("")
        self.yazi_alanibtc = QLabel("")
        self.yazi_alanigumus = QLabel("")

        self.sayialanidolar = QTextEdit()
        self.sayialanieuro = QTextEdit()
        self.sayialanibist = QTextEdit()
        self.sayialanisterlin = QTextEdit()
        self.sayialanibtc = QTextEdit()
        self.sayialanigumus = QTextEdit()

        h_box = QHBoxLayout()
        h_box.addWidget(self.dolar)
        h_box.addWidget(self.euro)
        h_box.addWidget(self.bist)
        h_box.addWidget(self.sterlin)
        h_box.addWidget(self.btc)
        h_box.addWidget(self.gumus)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.yazi_alanidolar)
        h_box2.addWidget(self.yazi_alanieuro)
        h_box2.addWidget(self.yazi_alanibist)
        h_box2.addWidget(self.yazi_alanisterlin)
        h_box2.addWidget(self.yazi_alanibtc)
        h_box2.addWidget(self.yazi_alanigumus)

        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.sayialanidolar)
        h_box3.addWidget(self.sayialanieuro)
        h_box3.addWidget(self.sayialanibist)
        h_box3.addWidget(self.sayialanisterlin)
        h_box3.addWidget(self.sayialanibtc)
        h_box3.addWidget(self.sayialanigumus)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addLayout(h_box2)
        v_box.addStretch()
        v_box.addLayout(h_box3)

        self.setLayout(v_box)

        for i in soup.find_all("span", {"data-socket-key": "USD", "data-socket-attr": "s"}):
            for j in i:
                self.yazi_alanidolar.setText(j)
        for i in soup.find_all("span", {"data-socket-key": "EUR", "data-socket-attr": "s"}):
            for j in i:
                self.yazi_alanieuro.setText(j)

        for i in soup.find_all("span", {"data-socket-key": "GBP", "data-socket-attr": "s"}):
            for j in i:
                self.yazi_alanisterlin.setText(j)
        for i in soup.find_all("span", {"data-socket-key": "XU100", "data-socket-attr": "s"}):
            for j in i:
                self.yazi_alanibist.setText(j)

        for i in soup.find_all("span", {"data-socket-key": "bitcoin", "data-socket-attr": "s"}):
            for j in i:
                self.yazi_alanibtc.setText(j)

        for i in soup.find_all("span", {"data-socket-key": "gumus", "data-socket-attr": "s"}):
            for j in i:
                self.yazi_alanigumus.setText(j)






        self.setWindowTitle("Döviz Çevirici")
        self.show()

    def dolaricintl(self):



    def euroicintl(self):
        pass

    def bisticintl(self):
        pass

    def sterlinicintl(self):
        pass

    def btcicintl(self):
        pass

    def gumusicintl(self):
        pass












app = QApplication(sys.argv)

uyg = Uygulama()

sys.exit(app.exec_())


while True:

    timer = 1
    time.sleep(1)
    timer = 0

    if (timer == 0):

        for i in soup.find_all("span", {"data-socket-key": "USD", "data-socket-attr": "s"}):
            for j in i:
                dolar = j

        for i in soup.find_all("span", {"data-socket-key": "EUR", "data-socket-attr": "s"}):
            for j in i:
                euro = j

        for i in soup.find_all("span", {"data-socket-key": "GBP", "data-socket-attr": "s"}):
            for j in i:
                sterlin = j

        for i in soup.find_all("span", {"data-socket-key": "XU100", "data-socket-attr": "s"}):
            for j in i:
                bist100 = j

        for i in soup.find_all("span", {"data-socket-key": "bitcoin", "data-socket-attr": "s"}):
            for j in i:
                bitcoin = j

        for i in soup.find_all("span", {"data-socket-key": "gumus", "data-socket-attr": "s"}):
            for j in i:
                gumus = j

        timer = 1





