from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

class MeinFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:/Users/antoi/Desktop/Programmierung2/GUI/Kap_8/Theorie/gui_button123.ui", self)

        self.button1.clicked.connect(self.button1_click)
        self.show()

    def button1_click(self):
        print("Hello Wolrd")

app = QApplication([])
fenster = MeinFenster()

app.exec()