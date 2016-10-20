# ---------------------------------------
#
#   Technical Account Manager Tools
#   v.1
#
# ---------------------------------------

# -- Import Dependancies --

# - Core Python Modules
import sys
import json

# - UI Modules -
import MainGUI
import UrlParserGUI
import EditGlobalsGUI
import JSONParserGUI

# - 3rd Party Modules
import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from urllib.parse import urlparse
from urllib.request import url2pathname

# -- Import Dependancies --


# - App Class
class MainGUI(QMainWindow, MainGUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # - Instantiate Parser Widget -
        self.parser = UrlParserGUI()
        self.parser.hide()

        # - Instantiate Formatter Widget
        self.formatter = JSONParserGUI()
        self.formatter.hide()

        # - Instantiate Globals Widget -
        self.globals = GlobalsGUI()
        self.globals.hide()

        # - Show Various Tools and Dialogs
        self.actionUrl_Parser.triggered.connect(self.parser.showSelf)
        self.actionJSON_Parser.triggered.connect(self.formatter.showSelf)
        self.actionGlobals.triggered.connect(self.globals.showSelf)

    # - Parser Sub
    def openParser(self):
        self.parser.showSelf()

    def openFormatter(self):
        self.formatter.showSelf()

    def openGlobals(self):
        self.globals.showSelf()

# - JSON Formatter Window -
class JSONParserGUI(QWidget, JSONParserGUI.JSONParserWIDGET):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # - Set Trigger
        self.pushButton.clicked.connect(self.formatJSON)

    def showSelf(self):
        self.show()

    def formatJSON(self):
        while (True):
            try:
                rawJSON = self.originalJSONWindow.toPlainText()
                formattedJSON = json.loads(rawJSON)
                self.parsedJSONWindow.setPlainText(json.dumps(formattedJSON, indent=4))
                break
            except ValueError:
                self.parsedJSONWindow.setPlainText("Invalid JSON Payload")
                break

# - Url Parser Window -
class UrlParserGUI(QWidget, UrlParserGUI.UrlParserWIDGET):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # - Set Trigger
        self.pushButton.clicked.connect(self.parseUrl)

    def showSelf(self):
        self.show()

    def parseUrl(self):
        self.parsedUrlWindow.clear()
        url = self.originalUrlWindow.toPlainText()
        parsedurl = 'Invalid Url'
        while (True):
            try:
                parsedurl = parsedurl.replace(',', '\n')
                parsedurl = parsedurl.replace('&', '\n')
                # parsedurl = parsedurl.replace('query=\'', 'query=\n')
                parsedurl = str(urlparse(url))
                parsedurl = str(url2pathname(parsedurl))

                break
            except ValueError:
                self.parsedUrlWindow.setPlainText('Invalid Url')
                break

        # report parsed url
        self.parsedUrlWindow.setPlainText(parsedurl)


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