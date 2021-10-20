from ui_cioxo_houdini_publishWorkspace import Ui_CreateFile
import ui_cioxo_QtResources_rc

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


# ------ Houdini Cioxo - Publish Workspace window features


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

USERNAME = os.getenv("USERNAME")
rootDir = os.getenv("CIOXO_ROOT")


class Houdini_publishWorkspace(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateFile()
        self.ui.setupUi(self)

        hip = hou.hipFile.basename()

        # ------ Cioxo variables
        CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
        cioxo_project = hip.split(".")[0].split("_")[0]
        CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
        cioxo_sequence = hip.split(".")[0].split("_")[1]
        CIOXO_SHOT = os.getenv("CIOXO_SHOT")
        cioxo_shot = hip.split(".")[0].split("_")[2]
        CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
        CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")
        cioxo_discipline = hip.split(".")[0].split("_")[3]
        cioxo_version = hip.split(".")[0].split("_")[-1]
        os.environ["CIOXO_VERSION"] = cioxo_version

        # ------ Window variables
        self.ui.labelActualProject.setText("  " + cioxo_project)
        self.ui.labelActualProject_2.setText("  " + cioxo_project)
        self.ui.labelActualSequence.setText("  " + cioxo_sequence)
        self.ui.labelActualShot.setText("  " + cioxo_shot)
        self.ui.labelActualDiscipline.setText("  " + cioxo_discipline)
        self.ui.labelActualVersion.setText("  " + cioxo_version)
        self.ui.plainTextEditComment.setPlaceholderText("Comment...")
        self.ui.labelCreateFile.setText("Publish Workspace")

        # ------ Fill combo boxes with current environment variables
        # ------ Sequences
        for sequences in os.listdir(os.path.join(rootDir, CIOXO_PROJECT)):
            if sequences.startswith("seq"):
                os.environ["CIOXO_SEQUENCE"] = self.ui.comboBoxSequence.currentText()
                self.ui.comboBoxSequence.addItem(sequences)
            else:
                pass
        sequencesList = [self.ui.comboBoxSequence.itemText(i) for i in range(self.ui.comboBoxSequence.count())]
        currentSequence = sequencesList.index(CIOXO_SEQUENCE)
        self.ui.comboBoxSequence.setCurrentIndex(currentSequence)

        # ------ Shots
        for shots in os.listdir(os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)):
            if shots.startswith("sh"):
                self.ui.comboBoxShot.addItem(shots)
                os.environ["CIOXO_SHOT"] = self.ui.comboBoxShot.currentText()
            else:
                pass
        shotsList = [self.ui.comboBoxShot.itemText(i) for i in range(self.ui.comboBoxShot.count())]
        currentShot = shotsList.index(CIOXO_SHOT)
        self.ui.comboBoxShot.setCurrentIndex(currentShot)

        # ------ Discipline
        disciplineList = [self.ui.comboBoxDiscipline.itemText(i) for i in range(self.ui.comboBoxDiscipline.count())]
        if cioxo_discipline not in disciplineList:
            self.ui.comboBoxDiscipline.addItem(cioxo_discipline)
            disciplineList.append(cioxo_discipline)
        else:
            pass
        currentDiscipline = disciplineList.index(cioxo_discipline)
        self.ui.comboBoxDiscipline.setCurrentIndex(currentDiscipline)

        # ------ Version
        filesPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "houdini", "workspaces", cioxo_discipline)
        versionsList = []
        for files in os.listdir(filesPath):
            extension = os.path.splitext(files)[-1]
            if extension == ".hip" or extension == ".hiplc":
                versions = files.split(".")[0].split("_")[-1]
                versionsList.append(versions)
                self.ui.comboBoxVersion.addItem(versions)
            else:
                pass
        # ------ Create last version
        maxVersion = max(versionsList)
        maxVersion = ''.join(char for char in maxVersion if char.isdigit())
        maxVersion = int(maxVersion)
        if len(str(maxVersion)) == 1:
            newVersion = "v00" + str(maxVersion + 1)
        elif len(str(maxVersion)) == 2:
            newVersion = "v0" + str(maxVersion + 1)
        elif len(str(maxVersion)) == 3:
            newVersion = "v" + str(maxVersion + 1)
        # ------ Add new version to list of choices and select it automatically
        self.ui.comboBoxVersion.addItem(newVersion)
        versionList = [self.ui.comboBoxVersion.itemText(i) for i in range(self.ui.comboBoxVersion.count())]
        versionUp = versionList.index(newVersion)
        self.ui.comboBoxVersion.setCurrentIndex(versionUp)
        versionInput = self.ui.comboBoxVersion.currentText()

        def refresh_CIOXO_SEQUENCE():
            # ------ Set CIOXO_SEQUENCE according to current selected item in list Sequences
            os.environ["CIOXO_SEQUENCE"] = self.ui.comboBoxSequence.currentText()
        self.ui.comboBoxSequence.currentIndexChanged.connect(refresh_CIOXO_SEQUENCE)

        def refresh_shots():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            # ------ Clear list on refresh
            self.ui.comboBoxShot.clear()
            # ------ Look for folders beginning by "sh" and add them in list Shots
            for shots in os.listdir(os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)):
                if shots.startswith("sh"):
                    self.ui.comboBoxShot.addItem(shots)
                else:
                    pass
        self.ui.comboBoxSequence.currentIndexChanged.connect(refresh_shots)

        def refresh_CIOXO_SHOT():
            # ------ Set CIOXO_SHOT according to current selected item in list Shots
            os.environ["CIOXO_SHOT"] = self.ui.comboBoxShot.currentText()
        self.ui.comboBoxShot.currentIndexChanged.connect(refresh_CIOXO_SHOT)

        def refresh_disciplines():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            # ------ Paths
            filesPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "houdini", "workspaces")
            # ------ Clear list on refresh
            self.ui.comboBoxDiscipline.clear()
            # ------ Reset disciplines list with default values
            disciplineList = ["none", "research", "modeling", "rigging", "lookdev", "lighting", "rendering"]
            # ------ Add basic disciplines plus the ones created by User
            if os.path.isdir(filesPath):
                seen = set(disciplineList)
                for disciplines in os.listdir(filesPath):
                    if disciplines not in seen:
                        seen.add(disciplines)
                    else:
                        pass
                disciplineList = sorted(list(seen))
                self.ui.comboBoxDiscipline.addItems(disciplineList)
                self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
                self.ui.labelInformations.setText(">>> Terminal")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> Can't find the path!")
        self.ui.comboBoxSequence.currentIndexChanged.connect(refresh_disciplines)
        self.ui.comboBoxShot.currentIndexChanged.connect(refresh_disciplines)

        def refresh_CIOXO_DISCIPLINE():
            os.environ["CIOXO_DISCIPLINE"] = self.ui.comboBoxDiscipline.currentText()
        self.ui.comboBoxDiscipline.currentIndexChanged.connect(refresh_CIOXO_DISCIPLINE)

        def publishWorkspace_houdini():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            disciplineInput = self.ui.comboBoxDiscipline.currentText()
            os.environ["CIOXO_DISCIPLINE"] = disciplineInput
            CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")

            # self.ui.lineEditVersion.setInputMask("999")
            versionInput = self.ui.comboBoxVersion.currentText()

            filePath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE)
            fileName = os.path.join(filePath, CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_" + CIOXO_DISCIPLINE + "_" + versionInput)
            fileCommentPath = os.path.join(filePath, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_" + CIOXO_DISCIPLINE + "_" + versionInput + "_comment.txt")
            comment = self.ui.plainTextEditComment.toPlainText()

            pathExists = True
            while pathExists:
                if os.path.isfile(fileName + ".hip") is True or os.path.isfile(fileName + ".hiplc") is True:
                    self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                    self.ui.labelInformations.setText(">>> File already exists! - Change discipline or version up")
                    break
                else:
                    if os.path.isdir(filePath):
                        pass
                    else:
                        os.makedirs(filePath)
                    # ------ Write file
                    hou.hipFile.save(fileName + ".hip")
                    self.ui.buttonCancel.setText("Close")
                    pathExists = False
                    # ------ Write comment
                    if comment == "":
                        self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                        self.ui.labelInformations.setText(
                            ">>> file created - You can now close the window")
                        pass
                    else:
                        with open(fileCommentPath, 'w') as f:
                            f.write(comment)
                        self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                        self.ui.labelInformations.setText(
                            ">>> file created\n>>> Comment created - You can now close the window")
        self.ui.buttonOk.clicked.connect(publishWorkspace_houdini)

        def closeWindow_publishWorkspace_houdini():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_publishWorkspace_houdini)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Publish Workspace")


window = Houdini_publishWorkspace()
window.show()
