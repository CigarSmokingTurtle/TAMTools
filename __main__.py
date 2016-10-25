# ---------------------------------------
#
#   Technical Account Manager Tools
#   v 1.0 bitches!
#
# ---------------------------------------

# -- Import Dependancies --

# - Core Python Modules
import os, sys, inspect

# Set Relative Path
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"pynsist_pkgs")))
if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)
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

        # - Unlock ID Values
        self.eventTabIDSelect1.currentIndexChanged.connect(self.changeEventCombo)
        self.installTabIDSelect1.currentIndexChanged.connect(self.changeInstallCombo)
        self.installTabIDSelect2.currentIndexChanged.connect(self.changeInstallCombo)
        self.installTabIDSelect3.currentIndexChanged.connect(self.changeInstallCombo)
        self.installTabIDSelect4.currentIndexChanged.connect(self.changeInstallCombo)
        self.installTabIDSelect5.currentIndexChanged.connect(self.changeInstallCombo)

        # - Unlock preview for editing
        self.installTabEditCheck.stateChanged.connect(self.installPayloadEdit)
        self.eventTabEditCheck.stateChanged.connect(self.eventPayloadEdit)

    def installPayloadEdit(self):
        if (self.installTabEditCheck.isChecked()):
           self.installTabPayloadPreview.setReadOnly(True)
           self.installTabPayloadPreview.setEnabled(True)
        else:
            self.installTabPayloadPreview.setReadOnly(False)
            self.installTabPayloadPreview.setEnabled(False)

    def eventPayloadEdit(self):
        if (self.eventTabEditCheck.isChecked()):
           self.eventTabPayloadPreview.setReadOnly(True)
           self.eventTabPayloadPreview.setEnabled(True)
        else:
            self.eventTabPayloadPreview.setReadOnly(False)
            self.eventTabPayloadPreview.setEnabled(False)

    def changeEventCombo(self):
        if(self.eventTabIDSelect1.currentText() != '<none>'):
            self.eventTabIDSelect2.setEnabled(True)
            self.eventTabIDValue2.setEnabled(True)
        else:
            self.eventTabIDSelect2.setEnabled(False)
            self.eventTabIDValue2.setEnabled(False)

    def changeInstallCombo(self):
        if (self.installTabIDSelect1.currentText() != '<none>'):
            self.installTabIDSelect2.setEnabled(True)
            self.installTabIDValue2.setEnabled(True)
            if (self.installTabIDSelect2.currentText() != '<none>'):
                self.installTabIDSelect3.setEnabled(True)
                self.installTabIDValue3.setEnabled(True)
                if (self.installTabIDSelect3.currentText() != '<none>'):
                    self.installTabIDSelect4.setEnabled(True)
                    self.installTabIDValue4.setEnabled(True)
                    if (self.installTabIDSelect4.currentText() != '<none>'):
                        self.installTabIDSelect5.setEnabled(True)
                        self.installTabIDValue5.setEnabled(True)
                        if (self.installTabIDSelect5.currentText() != '<none>'):
                            self.installTabIDSelect6.setEnabled(True)
                            self.installTabIDValue6.setEnabled(True)
                        else:
                            self.installTabIDSelect6.setEnabled(False)
                            self.installTabIDValue6.setEnabled(False)
                    else:
                        self.installTabIDSelect5.setEnabled(False)
                        self.installTabIDValue5.setEnabled(False)
                else:
                    self.installTabIDSelect4.setEnabled(False)
                    self.installTabIDValue4.setEnabled(False)
            else:
                self.installTabIDSelect3.setEnabled(False)
                self.installTabIDValue3.setEnabled(False)
        else:
            self.installTabIDSelect2.setEnabled(False)
            self.installTabIDValue2.setEnabled(False)

    def validatePayload(self):
        if (self.tabWidget.currentIndex() == 0):
            idfa = '"' + self.installTabUserAgentValue.text() + '"'
            ua = '"' + self.installTabUserAgentValue.text() + '"'
            origip = '"' + self.installTabIPValue.text() + '"'
            if (self.appGUIDValue.text() != ""):
                appguid = '"' + self.appGUIDValue.text() + '"'
            else:
                appguid = '"kopapa-gwan-s-forge-103d87ps"'

            deviceIDs = '"":""'
            if(self.installTabIDSelect1.currentText() != '<none>'):
                deviceIDs = '"' + self.installTabIDSelect1.currentText() + '":"' + self.installTabIDValue1.text() + '"'
                if(self.installTabIDSelect2.currentText() != '<none>'):
                    deviceIDs = deviceIDs + ',' + '\n' + '"' + self.installTabIDSelect2.currentText() + '":"' + self.installTabIDValue2.text() + '"'
                    if (self.installTabIDSelect3.currentText() != '<none>'):
                        deviceIDs = deviceIDs + ','  + '\n' + '"' + self.installTabIDSelect3.currentText() + '":"' + self.installTabIDValue3.text() + '"'
                        if (self.installTabIDSelect4.currentText() != '<none>'):
                            deviceIDs = deviceIDs + ',' + '\n' + '"' + self.installTabIDSelect4.currentText() + '":"' + self.installTabIDValue4.text() + '"'
                            if (self.installTabIDSelect5.currentText() != '<none>'):
                                deviceIDs = deviceIDs + ',' + '\n' + '"' + self.installTabIDSelect5.currentText() + '":"' + self.installTabIDValue5.text() + '"'
                                if (self.installTabIDSelect6.currentText() != '<none>'):
                                    deviceIDs = deviceIDs + ',' + '\n' + '"' + self.installTabIDSelect6.currentText() + '":"' + self.installTabIDValue6.text() + '"'

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
                                                %s
                                            }
                                        },
                                        "kochava_app_id": %s,
                                        "action": "install"
                                    }""" % (ua, origip, deviceIDs, appguid)
            self.installTabPayloadPreview.clear()
            while (True):
                try:
                    MainGUI.payload = json.loads(MainGUI.payload)
                    self.installTabPayloadPreview.setPlainText(json.dumps(MainGUI.payload, indent=6))
                    break
                except ValueError as ve:
                    self.installTabPayloadPreview.setPlainText('Invalid JSON scrub! \n \n' + str(ve) + '\n \n' + MainGUI.payload)
                    return None

            return self.installTabPayloadPreview.toPlainText()
        elif (self.tabWidget.currentIndex() == 1):
            appversion = '"1.0"'
            idfa = '"' + self.eventTabUserAgentValue.text() + '"'
            ua = '"' + self.eventTabUserAgentValue.text() + '"'
            deviceversion = '"1.1"'
            eventname = '"' + self.eventTabEventNameValue.text() + '"'
            origip = '"' + self.eventTabIPValue.text() + '"'
            if (self.appGUIDValue.text() != ""):
                appguid = '"' + self.appGUIDValue.text() + '"'
            else:
                appguid = '"kopapa-gwan-s-forge-103d87ps"'

            deviceIDs = '"":""'
            if (self.eventTabIDSelect1.currentText() != '<none>'):
                deviceIDs = '"' + self.eventTabIDSelect1.currentText() + '":"' + self.eventTabIDValue1.text() + '"'
                if (self.eventTabIDSelect2.currentText() != '<none>'):
                    deviceIDs = deviceIDs + ',' + '\n' + '"' + self.eventTabIDSelect2.currentText() + '":"' + self.eventTabIDValue2.text() + '"'

            MainGUI.payload = """{
                                        "data": {
                                            "app_version": %s,
                                            "device_ids": {
                                                %s
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
                                    }""" % (appversion, deviceIDs, ua, deviceversion, eventname, origip, appguid)
            self.eventTabPayloadPreview.clear()
            while (True):
                try:
                    MainGUI.payload = json.loads(MainGUI.payload)
                    self.eventTabPayloadPreview.setPlainText(json.dumps(MainGUI.payload, indent=6))
                    break
                except ValueError as ve:
                    self.eventTabPayloadPreview.setPlainText('Invalid JSON scrub! \n \n' + str(ve) + '\n \n' + MainGUI.payload)
                    return None

            return self.eventTabPayloadPreview.toPlainText()
        elif (self.tabWidget.currentIndex() == 2):
            if(self.customTabPayloadValue.toPlainText() == ''):
                MainGUI.payload = """{
                                            "data": {
                                            }
                                        }"""
            else:
                MainGUI.payload = self.customTabPayloadValue.toPlainText()
            self.customTabPayloadValue.clear()
            while (True):
                try:
                    MainGUI.payload = json.loads(MainGUI.payload)
                    self.customTabPayloadValue.setPlainText(json.dumps(MainGUI.payload, indent=6))
                    break
                except ValueError as ve:
                    self.customTabPayloadValue.setPlainText('Invalid JSON, scrub! \n \n' + str(ve) + '\n \n' + MainGUI.payload)
                    return None

            return self.customTabPayloadValue.toPlainText()

    def sendPayload(self):
        if (self.endpointSelector.currentText() != 'Kochava'):
            if (self.endpointValue.text() != ''):
                newendpoint = self.endpointValue.text()
            else:
                newendpoint = MainGUI.endpoint
        else:
            newendpoint = 'http://control.kochava.com/track/json'
        newpayload = self.validatePayload()
        self.serverResponseCodeAll.setPlainText('')
        self.progressBar.setValue(0)
        x = 1
        r = None
        while x <= self.postQtyValue.value():
            while (True):
                try:
                    r = requests.post(newendpoint, json=newpayload)

                    if (self.serverResponseCodeAll.toPlainText() == ''):
                        self.serverResponseCodeAll.setPlainText(str(r.json))
                    else:
                        self.serverResponseCodeAll.setPlainText(self.serverResponseCodeAll.toPlainText() + '\n' + str(r.json))
                        self.progressBar.setValue((100 / self.postQtyValue.value()) * x)
                    break
                except MissingSchema:
                    self.serverResponseCodeAll.setPlainText('Missing Schema Error' + str(MissingSchema))
                    return 4
                except ConnectionError:
                    self.serverResponseCodeAll.setPlainText('Connection Error' + str(ConnectionError))
                    return 5
                except TimeoutError:
                    self.serverResponseCodeAll.setPlainText('Timeout!' + str(TimeoutError))
                    return 6


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