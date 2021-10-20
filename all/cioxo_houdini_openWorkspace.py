from ui_cioxo_houdini_openWorkspace import Ui_Houdini_projectManager
import ui_cioxo_QtResources_rc

# ------ Import necessary libraries
from PySide2.QtWidgets import *
import hou
import os
import sys


# ------ Houdini Cioxo - Open Workspace window features


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

# ----- Cioxo variables
CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
CIOXO_SHOT = os.getenv("CIOXO_SHOT")
CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
CIOXO_FILE = os.getenv("CIOXO_FILE")
USERNAME = os.getenv("USERNAME")
rootDir = os.getenv("CIOXO_ROOT")
version = str("v0.0.1-alpha")

# ------ Houdini variables
HOU_PROJECT = hou.getenv("HIP")
HOU_JOB = hou.getenv("JOB")


class Houdini_projectManager(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Houdini_projectManager()
        self.ui.setupUi(self)

        def openDirectories_files():
            os.startfile(HOU_PROJECT)
        self.ui.buttonDirectoryFiles.clicked.connect(openDirectories_files)

        # ------ Set version
        self.ui.labelVersion.setText(version)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Houdini Files Manager")


window = Houdini_projectManager()
window.show()
