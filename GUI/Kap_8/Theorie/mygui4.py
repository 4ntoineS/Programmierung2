from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

class Umrechnen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:/Users/antoi/Desktop/Programmierung2/GUI/Kap_8/Theorie/gui_test3.ui", self)

        self.createConnects()
        self.show()

    ## -------------------------------------------------------------------------------------------------------    

    def createConnects(self):
        self.umrechnenbutton.clicked.connect(self.umrechnen)
        #self.euroLineEdit.textChanged.connect(self.euroEdit)

    ## -------------------------------------------------------------------------------------------------------    

    #def euroEdit(self, text):
    #    self.umrechnen()

    def umrechnen(self):
        euro = self.euroLineEdit.text()
        try:
            wert = float(euro)
            wert_chf = wert * 1.06
            self.frankenLineEdit.setText(str(wert_chf))
        except:
            self.frankenLineEdit.setText("Ungültiger Wert")


app = QApplication([])
fenster = Umrechnen()

app.exec()