from PyQt5.QtWidgets import *
from PyQt5.uic import *


def hello():
    print("Button clicked")


app = QApplication([])

fenster = loadUi("C:/Users/antoi/Desktop/Programmierung2/GUI/Kap_8/Theorie/gui_test1.ui")
fenster.show()

fenster.lineEdit.setText("Es funktionniert")
fenster.pushButton.clicked.connect(hello)

app.exec()