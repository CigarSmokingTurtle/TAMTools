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
import EditGlobalsGUI

# - 3rd Party Modules
import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction

# -- Impost Dependancies --


# - App Class
class MainGUI(QMainWindow, MainGUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # - Instantiate Parser Widget -
        self.parser = UrlParserGUI()
        self.parser.hide()

        # - Instantiate Globals Widget -
        self.globals = GlobalsGUI()
        self.globals.hide()

        # - Show Various Tools and Dialogs
        self.actionUrl_Parser.triggered.connect(self.parser.showSelf)
        self.actionGlobals.triggered.connect(self.globals.showSelf)

    # - Parser Sub
    def openParser(self):
        self.parser.show()

    def openGlobals(self):
        self.globals.show()

# - Url Parser Window -
class UrlParserGUI(QWidget, UrlParserGUI.UrlParserWIDGET):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showSelf(self):
        self.show()

# - Global Editing Window -
class GlobalsGUI(QWidget, EditGlobalsGUI.EditGlobalsWIDGET):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showSelf(self):
        self.show()


# -- Main --
if __name__ == '__main__':
    a = QApplication(sys.argv)
    app = MainGUI()
    app.show()


    sys.exit(a.exec_())