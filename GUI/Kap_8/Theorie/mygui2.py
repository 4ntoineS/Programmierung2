from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

class MeinFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:/Users/antoi/Desktop/Programmierung2/GUI/Kap_8/Theorie/gui_test1.ui", self)

        self.pushButton.clicked.connect(self.button_click)

        self.show()

    def button_click(self):
        print("Hello Wolrd")

app = QApplication([])
fenster = MeinFenster()

app.exec()