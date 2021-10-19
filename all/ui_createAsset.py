# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Valen\Documents\PROJECTS\.pipeline\all\ui\createAsset.ui'
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


class Ui_CreateAsset(object):
    def setupUi(self, CreateAsset):
        CreateAsset.setObjectName("CreateAsset")
        CreateAsset.resize(500, 250)
        CreateAsset.setMinimumSize(QtCore.QSize(500, 250))
        CreateAsset.setMaximumSize(QtCore.QSize(800, 300))
        CreateAsset.setStyleSheet("background-color: rgb(27, 27, 27);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(CreateAsset)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameAll = QtWidgets.QFrame(CreateAsset)
        self.frameAll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAll.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAll.setObjectName("frameAll")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameAll)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameTitle = QtWidgets.QFrame(self.frameAll)
        self.frameTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameTitle.setStyleSheet("")
        self.frameTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTitle.setLineWidth(0)
        self.frameTitle.setObjectName("frameTitle")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frameTitle)
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelCreateProject = QtWidgets.QLabel(self.frameTitle)
        self.labelCreateProject.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCreateProject.setFont(font)
        self.labelCreateProject.setStyleSheet("color:white;")
        self.labelCreateProject.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelCreateProject.setObjectName("labelCreateProject")
        self.horizontalLayout_6.addWidget(self.labelCreateProject)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frameTitle)
        self.frameInput = QtWidgets.QFrame(self.frameAll)
        self.frameInput.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInput.setObjectName("frameInput")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameInput)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditInput = QtWidgets.QLineEdit(self.frameInput)
        self.lineEditInput.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEditInput.setFont(font)
        self.lineEditInput.setStyleSheet("QLineEdit\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(50, 50, 50);\n"
"}")
        self.lineEditInput.setObjectName("lineEditInput")
        self.verticalLayout_2.addWidget(self.lineEditInput)
        self.frameSoftwares = QtWidgets.QFrame(self.frameInput)
        self.frameSoftwares.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSoftwares.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSoftwares.setObjectName("frameSoftwares")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameSoftwares)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(65)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonHoudini = QtWidgets.QRadioButton(self.frameSoftwares)
        self.radioButtonHoudini.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButtonHoudini.setFont(font)
        self.radioButtonHoudini.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonHoudini.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/houdini.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButtonHoudini.setIcon(icon)
        self.radioButtonHoudini.setChecked(True)
        self.radioButtonHoudini.setAutoExclusive(False)
        self.radioButtonHoudini.setObjectName("radioButtonHoudini")
        self.horizontalLayout.addWidget(self.radioButtonHoudini)
        self.radioButtonMaya = QtWidgets.QRadioButton(self.frameSoftwares)
        self.radioButtonMaya.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButtonMaya.setFont(font)
        self.radioButtonMaya.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonMaya.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/maya.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButtonMaya.setIcon(icon1)
        self.radioButtonMaya.setAutoExclusive(False)
        self.radioButtonMaya.setObjectName("radioButtonMaya")
        self.horizontalLayout.addWidget(self.radioButtonMaya)
        self.radioButtonSubstance = QtWidgets.QRadioButton(self.frameSoftwares)
        self.radioButtonSubstance.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButtonSubstance.setFont(font)
        self.radioButtonSubstance.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonSubstance.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/adobeSubstancePainter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButtonSubstance.setIcon(icon2)
        self.radioButtonSubstance.setAutoExclusive(False)
        self.radioButtonSubstance.setObjectName("radioButtonSubstance")
        self.horizontalLayout.addWidget(self.radioButtonSubstance)
        self.radioButtonNuke = QtWidgets.QRadioButton(self.frameSoftwares)
        self.radioButtonNuke.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButtonNuke.setFont(font)
        self.radioButtonNuke.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonNuke.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/nuke.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButtonNuke.setIcon(icon3)
        self.radioButtonNuke.setChecked(True)
        self.radioButtonNuke.setAutoExclusive(False)
        self.radioButtonNuke.setObjectName("radioButtonNuke")
        self.horizontalLayout.addWidget(self.radioButtonNuke)
        self.verticalLayout_2.addWidget(self.frameSoftwares)
        self.verticalLayout.addWidget(self.frameInput)
        self.frameInformations = QtWidgets.QFrame(self.frameAll)
        self.frameInformations.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frameInformations.setStyleSheet("")
        self.frameInformations.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameInformations.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInformations.setObjectName("frameInformations")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameInformations)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 18)
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
        self.frameChoice.setMaximumSize(QtCore.QSize(16777215, 33))
        self.frameChoice.setStyleSheet("    background-color: rgb(50, 50, 50);")
        self.frameChoice.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameChoice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameChoice.setLineWidth(0)
        self.frameChoice.setObjectName("frameChoice")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frameChoice)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 9)
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

        self.retranslateUi(CreateAsset)
        QtCore.QMetaObject.connectSlotsByName(CreateAsset)

    def retranslateUi(self, CreateAsset):
        _translate = QtCore.QCoreApplication.translate
        CreateAsset.setWindowTitle(_translate("CreateAsset", "Dialog"))
        self.labelCreateProject.setText(_translate("CreateAsset", "Create Asset"))
        self.lineEditInput.setText(_translate("CreateAsset", "assetExample01"))
        self.labelInformations.setText(_translate("CreateAsset", ">>> Terminal - Use camelCase writing!\n"
">>> Example: carTaxi01, bigHouse01"))
        self.buttonOk.setText(_translate("CreateAsset", "OK"))
        self.buttonCancel.setText(_translate("CreateAsset", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateAsset = QtWidgets.QDialog()
    ui = Ui_CreateAsset()
    ui.setupUi(CreateAsset)
    CreateAsset.show()
    sys.exit(app.exec_())
