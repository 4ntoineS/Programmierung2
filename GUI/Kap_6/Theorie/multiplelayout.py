from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()

        #Widgets erstellen
        button1 = QPushButton("button1")
        button2 = QPushButton("button2")
        button3 = QPushButton("button3")

        #Widgets in layout hinzufügen
        layout1.addWidget(button1)
        layout2.addWidget(button2)
        layout2.addWidget(button3)

        layout1.addLayout(layout2)

        center = QWidget()
        center.setLayout(layout1)

        self.setCentralWidget(center)
        self.show()

app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()
