from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.uic import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:/Users/antoi/Desktop/Programmierung2/GUI/Kap_8/Theorie/webwindowgui.ui", self)

        self.show()

        self.pushButton.clicked.connect(self.loadPage)



    def loadPage(self):
        htmlcode = """
        <h1> Hello World<\h1>
        ksedjasdbggsdfjok<\br>
        fgdhg
        """

        #self.webEngineView.setHtml(htmlcode)

        #self.webEngineView.load(QUrl("https://www.fhnw.ch/de/"))
        self.webEngineView.load(QUrl("https://www.google.ch/maps/@46.7795251,8.3728815,9z"))


app = QApplication([])
fenster = Browser()

app.exec()
