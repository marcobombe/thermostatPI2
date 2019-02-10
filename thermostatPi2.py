# always seem to need this
import os
import sys

# This gets the Qt stuff
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

# This is our window from QtCreator
import mainwindow_auto


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    # functions for the buttons to call
    def pressedOnButton(self):
        print("Application quit.")
        QtCore.QCoreApplication.instance().quit()

    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)  # gets defined in the UI file

        # Hooks to for buttons
        self.exitButton.clicked.connect(lambda: self.pressedOnButton())


# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()

    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
