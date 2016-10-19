# ---------------------------------------
#
#
#
# ---------------------------------------

# -- Import Dependancies --

# - Core Python Modules
import sys

# - UI Modules -
import MainGUI
import UrlParserGUI

# - 3rd Party Modules
import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction

# -- Impost Dependancies --


# - App Class
class MainGUI(QMainWindow, MainGUI.TAMToolsMAINWINDOW):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # - Instantiate Parser Widget -
        self.parser = UrlParserGUI()
        self.parser.hide()

        # - Show Parser Widget
        self.actionUrl_Parser.triggered.connect(self.openParser)

    def openParser(self):
        self.parser.show()

# - Url Parser Window
class UrlParserGUI(QWidget, UrlParserGUI.UrlParserWIDGET):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# -- Main --
if __name__ == '__main__':
    a = QApplication(sys.argv)
    app = MainGUI()
    app.show()


    sys.exit(a.exec_())