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
        checkbox = QCheckBox()
        self.name = QLineEdit()

    
        #Widgets in layout hinzufügen
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(checkbox)
        layout.addWidget(self.name)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        ##----------------------------------------

        button1.pressed.connect(self.Knopf1)
        button2.clicked.connect(self.Knopf2)
        checkbox.stateChanged.connect(self.MycheckBox)



    def Knopf1(self):
        print("Line edit has value: " + self.name.text())

    def Knopf2(self):
        self.name.setText("Hello World")

    def MycheckBox(self, state):
        if state == Qt.CheckState.Checked:       
            print("CheckBox checked")
        else:
            print("CheckBox not checked")

app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()
