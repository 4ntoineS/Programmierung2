from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Bsp")
        layout = QVBoxLayout()

        button1 = QPushButton("QMessage Box : Information")
        button2 = QPushButton("QMessage Box : about")
        button3 = QPushButton("QMessage Box : Warning")
        button4 = QPushButton("QMessage Box : Critical")
        button5 = QPushButton("QMessage Box : Warning")

        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)
        button3.clicked.connect(self.button3_clicked)
        button4.clicked.connect(self.button4_clicked)
        button5.clicked.connect(self.button5_clicked)

        style = """QPushButton {font-size: 16px; background-color: #00AA00; }
                    QPushButton:pressed {font-size: 16px; background-color: #AA0000; }"""

        button1.setStyleSheet(style)
        button2.setStyleSheet(style)
        button3.setStyleSheet(style)
        button4.setStyleSheet(style)
        button5.setStyleSheet(style)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()


    def button1_clicked(self):
        QMessageBox.information(self, "Titel", "Text")

    def button2_clicked(self):
        QMessageBox.about(self, "Titel", "Salut")

    def button3_clicked(self):
        QMessageBox.warning(self, "Warning", "Error 404")

    def button4_clicked(self):
        QMessageBox.critical(self, "Critical", "System Error: Das Programm muss beendet werden")
        self.close()  #schliesst Main Window

    def button5_clicked(self):
        QMessageBox.information(self, "Titel", "Text")



app = QApplication([])
fenster = Fenster()
app.exec()
