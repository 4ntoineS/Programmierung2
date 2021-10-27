from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setMinimumWidth(640)
        #self.setMinimumHeight(480)
        self.setWindowTitle("Dies ist ein Fenster")
        self.show()


        layout1 = QVBoxLayout()                    ## QHBoxLayout -> boutons alignés à l'horizontal / QVBoxLayout -> à la verticale

        label = QLabel("Hello World")             ## text
        edit = QLineEdit()                        ## zone de text
        button3 = QPushButton("Abbrechen")        ## bouton
        calendar = QCalendarWidget()

        layout1.addWidget(label)                  ## ajouter les boutons au layout
        layout1.addWidget(edit)
        layout1.addWidget(button3)
        layout1.addWidget(calendar)

        center = QWidget()                         ## besoin d'une "zone" pour afficher les boutons
        center.setLayout(layout1)                          
        self.setCentralWidget(center)               


app = QApplication([])
fenster = Fenster()
fenster.raise_()
app.exec()