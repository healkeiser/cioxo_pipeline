from ui_cioxo_houdini_projectManager import Ui_Houdini_projectManager
import ui_cioxoQtResources_rc

# ------ Import necessary libraries
from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import hou
import os
import sys

# ------ DEFINE GLOBALS
labelInformationsGreen = ("QLabel\n"
                          "{\n"
                          "    color: rgb(0, 255, 0);\n"
                          "    background-color: rgb(0, 0, 0);\n"
                          "    border-style: solid;\n"
                          "    border-width: 1px;\n"
                          "    border-radius: 5px;\n"
                          "    border-color: rgb(50, 50, 50);\n"
                          "}")
labelInformationsRed = ("QLabel\n"
                        "{\n"
                        "    color: rgb(255, 0, 0);\n"
                        "    background-color: rgb(0, 0, 0);\n"
                        "    border-style: solid;\n"
                        "    border-width: 1px;\n"
                        "    border-radius: 5px;\n"
                        "    border-color: rgb(50, 50, 50);\n"
                        "}")

project = hou.getenv("HIP")
job = hou.getenv("JOB")
USERNAME = os.getenv("USERNAME")
rootDir = os.getenv("CIOXO_ROOT")

print("project: " + project)
print("job: " + job)
print("rootDir: " + rootDir)


class Houdini_projectManager(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Houdini_projectManager()
        self.ui.setupUi(self)

        def openDirectories_files():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            pathFile = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE)
            os.startfile(pathFile)
            print(">>> Opening Directory")
        self.ui.buttonDirectoryFiles.clicked.connect(openDirectories_files)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Houdini Files Manager")


window = Houdini_projectManager()
window.show()
