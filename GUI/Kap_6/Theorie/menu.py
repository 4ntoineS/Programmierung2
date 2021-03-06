from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        menubar = self.menuBar()

        filemenu = menubar.addMenu("File")
        editmenu = menubar.addMenu("Edit")
        viewmenu = menubar.addMenu("View")

        open = QAction("Open", self)
        save = QAction("Save", self)
        quit = QAction("Exit", self)

        quit.setMenuRole(QAction.QuitRole)

        filemenu.addAction(open)
        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

        open.triggered.connect(self.doOpen)
        quit.triggered.connect(self.doClose)

        self.show()

        ##------------------------

    def doOpen(self):
        print("Open data")

    def doClose(self):
        exit(0)

app = QApplication([])
fenster = Window()
fenster.raise_()
app.exec()
