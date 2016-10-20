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
import jsonschema

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

    # - Class Globals
    endpoint = 'http://control.kochava.com/track/json'
    payload = '{"data":"derp"}'
    currentTab = 'Install'

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
        self.installTabValidateButton.clicked.connect(self.validatePayload)
        self.eventTabValidateButton.clicked.connect(self.validatePayload)
        self.customTabValidateButton.clicked.connect(self.validatePayload)
        self.postButton.clicked.connect(self.sendPayload)

    def validatePayload(self):
        if (self.tabWidget.currentIndex() == 0):
            idfa = '"' + self.installTabUserAgentValue.text() + '"'
            ua = '"' + self.installTabUserAgentValue.text() + '"'
            origip = '"' + self.eventTabIPValue.text() + '"'
            appguid = '"' + self.appGUIDValue.text() + '"'

            MainGUI.payload = """{
                                        "data": {
                                            "usertime": "",
                                            "device_ua": %s,
                                            "conversion_data": {
                                                "utm_campaign": "",
                                                "utm_medium": "",
                                                "utm_source": ""
                                            },
                                            "origination_ip": %s,
                                            "device_ids": {
                                                "udid": "",
                                                "mac": "",
                                                "idfa": %s,
                                                "imei": "",
                                                "adid": "",
                                                "odin": "",
                                                "android_id": ""
                                            }
                                        },
                                        "kochava_app_id": %s,
                                        "action": "install"
                                    }""" % (ua, origip, idfa, appguid)
            self.installTabPayloadPreview.clear()
            while (True):
                try:
                    MainGUI.payload = json.loads(MainGUI.payload)
                    self.installTabPayloadPreview.setPlainText(json.dumps(MainGUI.payload, indent=6))
                    break
                except ValueError as ve:
                    self.installTabPayloadPreview.setPlainText('Invalid JSON scrub! \n \n' + str(ve) + '\n \n' + MainGUI.payload)
                    return None

            return MainGUI.payload
        elif (self.tabWidget.currentIndex() == 1):
            appversion = '"1.0"'
            idfa = '"' + self.eventTabUserAgentValue.text() + '"'
            ua = '"' + self.eventTabUserAgentValue.text() + '"'
            deviceversion = '"1.1"'
            eventname = '"' + self.eventTabEventNameValue.text() + '"'
            origip = '"' + self.eventTabIPValue.text() + '"'
            appguid = '"' + self.appGUIDValue.text() + '"'

            MainGUI.payload = """{
                                        "data": {
                                            "app_version": %s,
                                            "device_ids": {
                                                "idfa": %s
                                            },
                                            "device_ua": %s,
                                            "device_ver": %s,
                                            "event_name": %s,
                                            "origination_ip": %s,
                                            "event_data": {
                                                "id": "123",
                                                "name": "Shoes",
                                                "currency": "USD",
                                                "sum": 100
                                            }
                                            },
                                        "action": "event",
                                        "kochava_app_id": %s
                                    }""" % (appversion, idfa, ua, deviceversion, eventname, origip, appguid)
            self.eventTabPayloadPreview.clear()
            while (True):
                try:
                    MainGUI.payload = json.loads(MainGUI.payload)
                    self.eventTabPayloadPreview.setPlainText(json.dumps(MainGUI.payload, indent=6))
                    break
                except ValueError as ve:
                    self.eventTabPayloadPreview.setPlainText('Invalid JSON scrub! \n \n' + str(ve) + '\n \n' + MainGUI.payload)
                    return None

            return MainGUI.payload
        elif (self.tabWidget.currentIndex() == 2):
            MainGUI.payload = """{
                                        "data": {
                                        }
                                    }"""
            self.customTabPayloadValue.clear()
            while (True):
                try:
                    MainGUI.payload = json.loads(MainGUI.payload)
                    self.customTabPayloadValue.setPlainText(json.dumps(MainGUI.payload, indent=6))
                    break
                except ValueError as ve:
                    self.customTabPayloadValue.setPlainText('Invalid JSON scrub! \n \n' + str(ve) + '\n \n' + MainGUI.payload)
                    return None

            return MainGUI.payload

    def sendPayload(self):
        if (self.appGUIDValue.text() != ''):
            newendpoint = self.appGUIDValue.text()
        else:
            newendpoint = MainGUI.endpoint
        newpayload = self.validatePayload()
        self.serverResponseCodeAll.setPlainText('')
        x = 1
        while x <= self.postQtyValue.value():
            while (True):
                try:
                    r = requests.post(newendpoint, newpayload)
                    if (self.serverResponseCodeAll.toPlainText() == ''):
                        self.serverResponseCodeAll.setPlainText(str(r.json))
                    else:
                        self.serverResponseCodeAll.setPlainText(self.serverResponseCodeAll.toPlainText() + '\n' + str(r.json))
                    break
                except ValueError:
                    self.serverResponseCodeAll.setPlainText('Error sending payload! Sorry...')
                    return 1
            x += 1
        return 0


    # - Sub Widgets
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
        rawJSON = self.originalJSONWindow.toPlainText()
        while (True):
            try:
                formattedJSON = json.loads(rawJSON)
                self.parsedJSONWindow.setPlainText(json.dumps(formattedJSON, indent=6))
                break
            except ValueError as ve:
                self.parsedJSONWindow.setPlainText('Invalid JSON scrub! \n \n' + str(ve) + '\n \n' + rawJSON)
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
            try:                # parsedurl = parsedurl.replace('query=\'', 'query=\n')
                parsedurl = str(urlparse(url))
                break
            except OSError as ve:
                self.parsedUrlWindow.setPlainText('Invalid Url \n \n' + str(ve))
                return None
        while (True):
            try:
                parsedurl = str(url2pathname(parsedurl))
                break
            except OSError as ve:
                self.parsedUrlWindow.setPlainText('Invalid Url \n \n' + str(ve))
                return None
        parsedurl = parsedurl.replace(',', '\n')
        parsedurl = parsedurl.replace('&', '\n')
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