from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Bsp")
        layout = QVBoxLayout()

        buttons = []

        buttons.append(QPushButton("QMessage Box : Information"))
        buttons.append(QPushButton("QMessage Box : about"))
        buttons.append(QPushButton("QMessage Box : Warning"))
        buttons.append(QPushButton("QMessage Box : Critical"))
        buttons.append(QPushButton("QMessage Box : ça geht?"))
        buttons.append(QPushButton("QMessage Box : Studium"))
        buttons.append(QPushButton("Open dialog"))
        buttons.append(QPushButton("Open multiple dialogs"))
        buttons.append(QPushButton("Save dialog"))
        buttons.append(QPushButton("10"))

        buttons[0].clicked.connect(self.button1_clicked)
        buttons[1].clicked.connect(self.button2_clicked)
        buttons[2].clicked.connect(self.button3_clicked)
        buttons[3].clicked.connect(self.button4_clicked)
        buttons[4].clicked.connect(self.button5_clicked)
        buttons[5].clicked.connect(self.button6_clicked)
        buttons[6].clicked.connect(self.button7_clicked)
        buttons[7].clicked.connect(self.button8_clicked)
        buttons[8].clicked.connect(self.button9_clicked)
        buttons[9].clicked.connect(self.button10_clicked)


        style = """QPushButton {font-size: 16px; background-color: #00AA00; }
                    QPushButton:pressed {font-size: 16px; background-color: #AA0000; }"""

        for button in buttons:
        
            button.setStyleSheet(style)
            layout.addWidget(button)



        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()


    def button1_clicked(self):
        QMessageBox.information(self, "Information", "Text")

    def button2_clicked(self):
        QMessageBox.about(self, "About", "Salut")

    def button3_clicked(self):
        QMessageBox.warning(self, "Warning", "Error 404")

    def button4_clicked(self):
        QMessageBox.critical(self, "Critical", "System Error: Das Programm muss beendet werden")
        self.close()  #schliesst Main Window

    def button5_clicked(self):
        answer = QMessageBox.question(self, "Question", "ça geht?", QMessageBox.Yes, QMessageBox.No)

        if answer == QMessageBox.Yes:
            QMessageBox.information(self, "Antwort", "Super!")

        else:
            QMessageBox.critical(self, "Antwort", "Schade")
            self.close()

    def button6_clicked(self):
        answer = QMessageBox.question(self, "Question", "musst du studieren?", QMessageBox.Yes, QMessageBox.No)

        if answer == QMessageBox.Yes:
            QMessageBox.about(self, "Antwort", "Warum bist du dann da?")
            self.close()

        else:
            QMessageBox.critical(self, "Antwort", "Doch")
            self.close()

    def button7_clicked(self):
        dateifilter = "Textdatei (*.txt *.ttt);; Python File (*.py)"
        path = QStandardPaths.standardLocations(0)

        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", path, dateifilter)

        QMessageBox.information(self, "File", f"<h1>{filename}</h1><h2>{filter}</h2>")
    
    def button8_clicked(self):
        filenamen, filter = QFileDialog.getOpenFileNames(self, "Datei öffnen", "", "Python File (*.py)")

        QMessageBox.information(self, "File", f"<h1>{filenamen}</h1><h2>{filter}</h2>")
    

    def button9_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Save", "", "Python File (*.py)")
        print(filename, filter)
    
    def button10_clicked(self):
        QMessageBox.information(self, "Information", "Text")



app = QApplication([])
fenster = Fenster()
app.exec()
