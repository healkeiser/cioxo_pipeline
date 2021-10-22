from ui_cioxo_houdini_openWorkspace import Ui_cioxo_houdini_openWorkspace
import ui_cioxo_QtResources_rc

# ------ Import necessary libraries
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import hou
import os


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
labelInformationsWhite = ("QLabel\n"
                        "{\n"
                        "    color: rgb(255, 255, 255);\n"
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
houdiniExtension = ".hip", ".hiplc"


class Houdini_projectManager(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Houdini_projectManager()
        self.ui.setupUi(self)

        # ----- Change window label title
        self.ui.labelWelcomeFiles.setText(CIOXO_PROJECT + " | " + CIOXO_SEQUENCE + " - " + CIOXO_SHOT)

        # ----- Look for disciplines folders
        filesPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE)
        foldersDisciplineList = []
        for folderDisciplines in os.listdir(os.path.join(filesPath, "workspaces")):
            foldersDisciplineList.append(folderDisciplines)
            # ------ Add delimiter for categories to list
            delimiter = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            font = QtGui.QFont()
            font.setBold(True)
            delimiter.setIcon(icon)
            delimiter.setFont(font)
            delimiter.setFlags(QtCore.Qt.NoItemFlags)
            delimiter.setText(folderDisciplines.upper())
            self.ui.listFiles.addItem(delimiter)
            # ------ Look for houdini files
            filesList = []
            for disciplines in foldersDisciplineList:
                files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
            for files in files:
                if files.endswith(houdiniExtension):
                    filesList.append(files)
                    self.ui.listFiles.addItem(files)
                else:
                    pass

        def openFile_files():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]

            filesPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE, CIOXO_FILE)

            if CIOXO_FILE == "file" or os.path.isfile(filesPath) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No file selected!")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
                hou.hipFile.load(filesPath)
                self.ui.labelInformations.setText(">>> Opening " + filesPath)
        self.ui.buttonOpenFiles.clicked.connect(openFile_files)
        self.ui.listFiles.doubleClicked.connect(openFile_files)

        def showComment_files():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]
            fileCommentPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_comment.txt")
            if os.path.isfile(fileCommentPath):
                with open(fileCommentPath) as f:
                    comment = f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline()
                self.ui.labelCommentFiles.setText(comment)
            else:
                self.ui.labelCommentFiles.setText("No comment found")
        self.ui.listFiles.itemSelectionChanged.connect(showComment_files)

        def openDirectories_files():
            os.startfile(HOU_PROJECT)
        self.ui.buttonDirectoryFiles.clicked.connect(openDirectories_files)



        # ------ Set version
        self.ui.labelVersion.setText(version)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Houdini Files Manager")


window = Houdini_projectManager()
window.show()
