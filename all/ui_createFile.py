# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Valen\Documents\PROJECTS\.pipeline\all\ui\createFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import ui_cioxoQtResources_rc


class Ui_CreateFile(object):
    def setupUi(self, CreateFile):
        CreateFile.setObjectName("CreateFile")
        CreateFile.resize(473, 339)
        CreateFile.setStyleSheet("background-color: rgb(27, 27, 27);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(CreateFile)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameAll = QtWidgets.QFrame(CreateFile)
        self.frameAll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameAll.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameAll.setLineWidth(0)
        self.frameAll.setObjectName("frameAll")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameAll)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameTitle = QtWidgets.QFrame(self.frameAll)
        self.frameTitle.setMinimumSize(QtCore.QSize(0, 50))
        self.frameTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameTitle.setStyleSheet("")
        self.frameTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameTitle.setLineWidth(0)
        self.frameTitle.setObjectName("frameTitle")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frameTitle)
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelCreateFile = QtWidgets.QLabel(self.frameTitle)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCreateFile.setFont(font)
        self.labelCreateFile.setStyleSheet("color:white;")
        self.labelCreateFile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCreateFile.setObjectName("labelCreateFile")
        self.horizontalLayout_6.addWidget(self.labelCreateFile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frameTitle)
        self.frameInput = QtWidgets.QFrame(self.frameAll)
        self.frameInput.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameInput.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameInput.setLineWidth(0)
        self.frameInput.setObjectName("frameInput")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameInput)
        self.verticalLayout_2.setContentsMargins(9, -1, 9, 6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameActualFile = QtWidgets.QFrame(self.frameInput)
        self.frameActualFile.setStyleSheet("")
        self.frameActualFile.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameActualFile.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameActualFile.setObjectName("frameActualFile")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameActualFile)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addWidget(self.frameActualFile)
        self.frameFileInput = QtWidgets.QFrame(self.frameInput)
        self.frameFileInput.setMaximumSize(QtCore.QSize(16777215, 24))
        self.frameFileInput.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameFileInput.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameFileInput.setLineWidth(0)
        self.frameFileInput.setObjectName("frameFileInput")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameFileInput)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelActualProject = QtWidgets.QLabel(self.frameFileInput)
        self.labelActualProject.setMinimumSize(QtCore.QSize(30, 21))
        self.labelActualProject.setMaximumSize(QtCore.QSize(30, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelActualProject.setFont(font)
        self.labelActualProject.setStyleSheet("    background-color: rgb(50, 50, 50);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    border-color: rgb(50, 50, 50);")
        self.labelActualProject.setObjectName("labelActualProject")
        self.horizontalLayout.addWidget(self.labelActualProject)
        self.labelActualSequence = QtWidgets.QLabel(self.frameFileInput)
        self.labelActualSequence.setMinimumSize(QtCore.QSize(65, 21))
        self.labelActualSequence.setMaximumSize(QtCore.QSize(65, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelActualSequence.setFont(font)
        self.labelActualSequence.setStyleSheet("    background-color: rgb(50, 50, 50);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    border-color: rgb(50, 50, 50);")
        self.labelActualSequence.setObjectName("labelActualSequence")
        self.horizontalLayout.addWidget(self.labelActualSequence)
        self.labelActualShot = QtWidgets.QLabel(self.frameFileInput)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelActualShot.setFont(font)
        self.labelActualShot.setStyleSheet("    background-color: rgb(50, 50, 50);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    border-color: rgb(50, 50, 50);")
        self.labelActualShot.setObjectName("labelActualShot")
        self.horizontalLayout.addWidget(self.labelActualShot)
        self.comboBoxDiscipline = QtWidgets.QComboBox(self.frameFileInput)
        self.comboBoxDiscipline.setMinimumSize(QtCore.QSize(100, 21))
        self.comboBoxDiscipline.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.comboBoxDiscipline.setFont(font)
        self.comboBoxDiscipline.setStyleSheet("QComboBox {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(50, 50, 50);\n"
"}\n"
"QComboBox:item {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.comboBoxDiscipline.setEditable(True)
        self.comboBoxDiscipline.setObjectName("comboBoxDiscipline")
        self.comboBoxDiscipline.addItem("")
        self.comboBoxDiscipline.addItem("")
        self.comboBoxDiscipline.addItem("")
        self.comboBoxDiscipline.addItem("")
        self.comboBoxDiscipline.addItem("")
        self.comboBoxDiscipline.addItem("")
        self.comboBoxDiscipline.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxDiscipline)
        self.lineEditVersion = QtWidgets.QLineEdit(self.frameFileInput)
        self.lineEditVersion.setMinimumSize(QtCore.QSize(63, 21))
        self.lineEditVersion.setMaximumSize(QtCore.QSize(63, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEditVersion.setFont(font)
        self.lineEditVersion.setStyleSheet("\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(50, 50, 50);\n"
"")
        self.lineEditVersion.setObjectName("lineEditVersion")
        self.horizontalLayout.addWidget(self.lineEditVersion)
        self.verticalLayout_2.addWidget(self.frameFileInput)
        self.frameComment = QtWidgets.QFrame(self.frameInput)
        self.frameComment.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameComment.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameComment.setLineWidth(0)
        self.frameComment.setObjectName("frameComment")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameComment)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEditComment = QtWidgets.QPlainTextEdit(self.frameComment)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.plainTextEditComment.setFont(font)
        self.plainTextEditComment.setStyleSheet("    background-color: rgb(50, 50, 50);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    border-color: rgb(50, 50, 50);")
        self.plainTextEditComment.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEditComment.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEditComment.setObjectName("plainTextEditComment")
        self.horizontalLayout_2.addWidget(self.plainTextEditComment)
        self.verticalLayout_2.addWidget(self.frameComment)
        self.verticalLayout.addWidget(self.frameInput)
        self.frameInformations = QtWidgets.QFrame(self.frameAll)
        self.frameInformations.setStyleSheet("")
        self.frameInformations.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameInformations.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameInformations.setLineWidth(0)
        self.frameInformations.setObjectName("frameInformations")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameInformations)
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 18)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelInformations = QtWidgets.QLabel(self.frameInformations)
        self.labelInformations.setMinimumSize(QtCore.QSize(0, 50))
        self.labelInformations.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.labelInformations.setFont(font)
        self.labelInformations.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelInformations.setStyleSheet("QLabel\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(50, 50, 50);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255, 255, 255);\n"
"    selection-background-color: lightgray;\n"
"}")
        self.labelInformations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelInformations.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelInformations.setWordWrap(True)
        self.labelInformations.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelInformations.setObjectName("labelInformations")
        self.verticalLayout_4.addWidget(self.labelInformations)
        self.verticalLayout.addWidget(self.frameInformations)
        self.frameChoice = QtWidgets.QFrame(self.frameAll)
        self.frameChoice.setMinimumSize(QtCore.QSize(0, 50))
        self.frameChoice.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameChoice.setStyleSheet("    background-color: rgb(50, 50, 50);")
        self.frameChoice.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameChoice.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameChoice.setLineWidth(0)
        self.frameChoice.setObjectName("frameChoice")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frameChoice)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.labelSeparator = QtWidgets.QLabel(self.frameChoice)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelSeparator.setFont(font)
        self.labelSeparator.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelSeparator.setText("")
        self.labelSeparator.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelSeparator.setObjectName("labelSeparator")
        self.horizontalLayout_9.addWidget(self.labelSeparator)
        self.buttonOk = QtWidgets.QPushButton(self.frameChoice)
        self.buttonOk.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.buttonOk.setFont(font)
        self.buttonOk.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(83, 83, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(100, 100, 100);\n"
"}")
        self.buttonOk.setObjectName("buttonOk")
        self.horizontalLayout_9.addWidget(self.buttonOk)
        spacerItem2 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.buttonCancel = QtWidgets.QPushButton(self.frameChoice)
        self.buttonCancel.setMinimumSize(QtCore.QSize(0, 20))
        self.buttonCancel.setMaximumSize(QtCore.QSize(95, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.buttonCancel.setFont(font)
        self.buttonCancel.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(83, 83, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(100, 100, 100);\n"
"}")
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout_9.addWidget(self.buttonCancel)
        self.verticalLayout.addWidget(self.frameChoice)
        self.verticalLayout_3.addWidget(self.frameAll)

        self.retranslateUi(CreateFile)
        QtCore.QMetaObject.connectSlotsByName(CreateFile)

    def retranslateUi(self, CreateFile):
        _translate = QtCore.QCoreApplication.translate
        CreateFile.setWindowTitle(_translate("CreateFile", "Dialog"))
        self.labelCreateFile.setText(_translate("CreateFile", "Create File"))
        self.labelActualProject.setText(_translate("CreateFile", "  pro"))
        self.labelActualSequence.setText(_translate("CreateFile", "  seq001"))
        self.labelActualShot.setText(_translate("CreateFile", "  sh0000"))
        self.comboBoxDiscipline.setItemText(0, _translate("CreateFile", "none"))
        self.comboBoxDiscipline.setItemText(1, _translate("CreateFile", "research"))
        self.comboBoxDiscipline.setItemText(2, _translate("CreateFile", "modeling"))
        self.comboBoxDiscipline.setItemText(3, _translate("CreateFile", "rigging"))
        self.comboBoxDiscipline.setItemText(4, _translate("CreateFile", "lookdev"))
        self.comboBoxDiscipline.setItemText(5, _translate("CreateFile", "lighting"))
        self.comboBoxDiscipline.setItemText(6, _translate("CreateFile", "rendering"))
        self.lineEditVersion.setText(_translate("CreateFile", "001"))
        self.labelInformations.setText(_translate("CreateFile", ">>> Terminal - Choose a discipline and version for the new file"))
        self.buttonOk.setText(_translate("CreateFile", "OK"))
        self.buttonCancel.setText(_translate("CreateFile", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateFile = QtWidgets.QDialog()
    ui = Ui_CreateFile()
    ui.setupUi(CreateFile)
    CreateFile.show()
    sys.exit(app.exec_())