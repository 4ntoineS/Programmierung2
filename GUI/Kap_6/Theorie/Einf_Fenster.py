from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(640)
        self.setMinimumHeight(480)
        self.setWindowTitle("Dies ist ein Fenster")
        self.show()

app = QApplication([])
fenster = Fenster()
fenster.raise_()
app.exec()