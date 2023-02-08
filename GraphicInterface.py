#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Graphic Interface for robot control
Author: Robert Limas
Year: 2020
"""

from Graphics.MainWindow import *
import PyQt5

import sys
import os

import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.info('Graphic interface for robot control')

    dir_name = os.path.dirname(PyQt5.__file__)
    plugin_path = os.path.join(dir_name, 'plugins', 'platforms')
    QtWidgets.QApplication.addLibraryPath(plugin_path)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
