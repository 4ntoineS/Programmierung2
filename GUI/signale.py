from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        layout = QVBoxLayout()

        #Widgets erstellen
        button1 = QPushButton("button1")
        button2 = QPushButton("button2")
    
        #Widgets in layout hinzufügen
        layout.addWidget(button1)
        layout.addWidget(button2)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        ##----------------------------------------

        button1.clicked.connect(self.Knopf1)
        button2.clicked.connect(self.Knopf2)



    def Knopf1(self):
        print("button 1 selected")

    def Knopf2(self):
        print("button 2 selected")

app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()
