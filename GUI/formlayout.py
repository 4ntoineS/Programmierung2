from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        layout = QFormLayout()

        #Widgets erstellen
        name = QLineEdit()
        email = QLineEdit()
        alter = QSpinBox()
        button = QPushButton("Send")

        #Widgets in layout hinzufügen
        layout.addRow("Name", name)
        layout.addRow("Email", email)
        layout.addRow("Alter", alter)
        layout.addRow(button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()
