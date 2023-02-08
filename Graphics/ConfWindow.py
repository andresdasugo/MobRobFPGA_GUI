from Graphics.confWindow_ import *
from PyQt5.QtWidgets import QMessageBox

from Serial.SerialPorts import scan

import FileManager.FileManager as File

import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConfigWindow(QtWidgets.QDialog, Ui_confWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.show()
        self._load_baud()
        self._load_devices()

    def accept(self):
        logger.info('Saving configurations parameters')
        baud = self.baudParameter.currentText()
        port = self.portParameter.currentText()
        File.create_configuration(data={'baud': int(baud), 'port': port.strip()})
        self.close()

    def _load_baud(self):
        try:
            logger.info('Reading BaudParameters file')
            with open('Setup/BaudParameters.txt', mode='r') as f:
                lines = f.readlines()
                if len(lines) > 0:
                    for line in lines:
                        self.baudParameter.addItem(line.rstrip())
                else:
                    File.log('There are no parameters in the BaudParameters file')
        except FileNotFoundError as e:
            File.log(e)

    def _load_devices(self):
        logger.info('Looking for devices')
        while True:
            devices = scan()
            if len(devices) > 0:
                for device in devices:
                    self.portParameter.addItem(device.rstrip())
                break
            else:
                File.log('No ZigBee device connect')
                ret = QMessageBox.question(self, 'Information', 'There are no connected devices\r\nConnect the device',
                                           QMessageBox.Yes, QMessageBox.Cancel)
                if ret == QMessageBox.Cancel:
                    break
