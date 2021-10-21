# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Valen\Documents\PROJECTS\.pipeline\all\ui\cioxo_createShot.ui'
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

import ui_cioxo_QtResources_rc


class Ui_cioxo_createShot(object):
    def setupUi(self, cioxo_createShot):
        cioxo_createShot.setObjectName("cioxo_createShot")
        cioxo_createShot.resize(583, 244)
        cioxo_createShot.setMinimumSize(QtCore.QSize(0, 0))
        cioxo_createShot.setStyleSheet("background-color: rgb(27, 27, 27);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(cioxo_createShot)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fram_all = QtWidgets.QFrame(cioxo_createShot)
        self.fram_all.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fram_all.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fram_all.setLineWidth(0)
        self.fram_all.setObjectName("fram_all")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fram_all)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(self.fram_all)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_title.setStyleSheet("")
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_title.setLineWidth(0)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_createShot = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_createShot.setFont(font)
        self.label_createShot.setStyleSheet("color:white;")
        self.label_createShot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_createShot.setObjectName("label_createShot")
        self.horizontalLayout_6.addWidget(self.label_createShot)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_input = QtWidgets.QFrame(self.fram_all)
        self.frame_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_input.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_input.setLineWidth(0)
        self.frame_input.setObjectName("frame_input")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_input)
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_input = QtWidgets.QLineEdit(self.frame_input)
        self.lineEdit_input.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setStyleSheet("QLineEdit\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(50, 50, 50);\n"
"}")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.verticalLayout_2.addWidget(self.lineEdit_input)
        self.frame = QtWidgets.QFrame(self.frame_input)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_frameStart = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_frameStart.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit_frameStart.setFont(font)
        self.lineEdit_frameStart.setStyleSheet("QLineEdit\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(50, 50, 50);\n"
"}")
        self.lineEdit_frameStart.setObjectName("lineEdit_frameStart")
        self.horizontalLayout_2.addWidget(self.lineEdit_frameStart)
        self.labe_frameRangeSeparator = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labe_frameRangeSeparator.setFont(font)
        self.labe_frameRangeSeparator.setStyleSheet("color: rgb(255, 255, 255);")
        self.labe_frameRangeSeparator.setObjectName("labe_frameRangeSeparator")
        self.horizontalLayout_2.addWidget(self.labe_frameRangeSeparator)
        self.lineEdit_frameEnd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_frameEnd.setMinimumSize(QtCore.QSize(0, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.lineEdit_frameEnd.setFont(font)
        self.lineEdit_frameEnd.setStyleSheet("QLineEdit\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(50, 50, 50);\n"
"}")
        self.lineEdit_frameEnd.setObjectName("lineEdit_frameEnd")
        self.horizontalLayout_2.addWidget(self.lineEdit_frameEnd)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_softwares = QtWidgets.QFrame(self.frame_input)
        self.frame_softwares.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_softwares.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_softwares.setLineWidth(0)
        self.frame_softwares.setObjectName("frame_softwares")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_softwares)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(65)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_houdini = QtWidgets.QRadioButton(self.frame_softwares)
        self.radioButton_houdini.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButton_houdini.setFont(font)
        self.radioButton_houdini.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_houdini.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/houdini.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_houdini.setIcon(icon)
        self.radioButton_houdini.setChecked(True)
        self.radioButton_houdini.setAutoExclusive(False)
        self.radioButton_houdini.setObjectName("radioButton_houdini")
        self.horizontalLayout.addWidget(self.radioButton_houdini)
        self.radioButton_maya = QtWidgets.QRadioButton(self.frame_softwares)
        self.radioButton_maya.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButton_maya.setFont(font)
        self.radioButton_maya.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_maya.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/maya.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_maya.setIcon(icon1)
        self.radioButton_maya.setAutoExclusive(False)
        self.radioButton_maya.setObjectName("radioButton_maya")
        self.horizontalLayout.addWidget(self.radioButton_maya)
        self.radioButton_substance = QtWidgets.QRadioButton(self.frame_softwares)
        self.radioButton_substance.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButton_substance.setFont(font)
        self.radioButton_substance.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_substance.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/adobeSubstancePainter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_substance.setIcon(icon2)
        self.radioButton_substance.setAutoExclusive(False)
        self.radioButton_substance.setObjectName("radioButton_substance")
        self.horizontalLayout.addWidget(self.radioButton_substance)
        self.radioButton_nuke = QtWidgets.QRadioButton(self.frame_softwares)
        self.radioButton_nuke.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButton_nuke.setFont(font)
        self.radioButton_nuke.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_nuke.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/nuke.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_nuke.setIcon(icon3)
        self.radioButton_nuke.setChecked(True)
        self.radioButton_nuke.setAutoExclusive(False)
        self.radioButton_nuke.setObjectName("radioButton_nuke")
        self.horizontalLayout.addWidget(self.radioButton_nuke)
        self.radioButton_afterEffects = QtWidgets.QRadioButton(self.frame_softwares)
        self.radioButton_afterEffects.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButton_afterEffects.setFont(font)
        self.radioButton_afterEffects.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_afterEffects.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/afterEffects.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_afterEffects.setIcon(icon4)
        self.radioButton_afterEffects.setAutoExclusive(False)
        self.radioButton_afterEffects.setObjectName("radioButton_afterEffects")
        self.horizontalLayout.addWidget(self.radioButton_afterEffects)
        self.radioButton_photoshop = QtWidgets.QRadioButton(self.frame_softwares)
        self.radioButton_photoshop.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.radioButton_photoshop.setFont(font)
        self.radioButton_photoshop.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_photoshop.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/photoshop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_photoshop.setIcon(icon5)
        self.radioButton_photoshop.setAutoExclusive(False)
        self.radioButton_photoshop.setObjectName("radioButton_photoshop")
        self.horizontalLayout.addWidget(self.radioButton_photoshop)
        self.verticalLayout_2.addWidget(self.frame_softwares)
        self.verticalLayout.addWidget(self.frame_input)
        self.frame_informations = QtWidgets.QFrame(self.fram_all)
        self.frame_informations.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_informations.setStyleSheet("")
        self.frame_informations.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_informations.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_informations.setLineWidth(0)
        self.frame_informations.setObjectName("frame_informations")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_informations)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 18)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_informations = QtWidgets.QLabel(self.frame_informations)
        self.label_informations.setMinimumSize(QtCore.QSize(0, 50))
        self.label_informations.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_informations.setFont(font)
        self.label_informations.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_informations.setStyleSheet("QLabel\n"
"{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(50, 50, 50);\n"
"}")
        self.label_informations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_informations.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_informations.setWordWrap(True)
        self.label_informations.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_informations.setObjectName("label_informations")
        self.verticalLayout_4.addWidget(self.label_informations)
        self.verticalLayout.addWidget(self.frame_informations)
        self.frame_choice = QtWidgets.QFrame(self.fram_all)
        self.frame_choice.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_choice.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_choice.setStyleSheet("    background-color: rgb(50, 50, 50);")
        self.frame_choice.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_choice.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_choice.setLineWidth(0)
        self.frame_choice.setObjectName("frame_choice")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_choice)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.label_separator = QtWidgets.QLabel(self.frame_choice)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_separator.setFont(font)
        self.label_separator.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_separator.setText("")
        self.label_separator.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_separator.setObjectName("label_separator")
        self.horizontalLayout_9.addWidget(self.label_separator)
        self.button_ok = QtWidgets.QPushButton(self.frame_choice)
        self.button_ok.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_ok.setFont(font)
        self.button_ok.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(83, 83, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(100, 100, 100);\n"
"}")
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_9.addWidget(self.button_ok)
        spacerItem2 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.button_cancel = QtWidgets.QPushButton(self.frame_choice)
        self.button_cancel.setMinimumSize(QtCore.QSize(0, 20))
        self.button_cancel.setMaximumSize(QtCore.QSize(95, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_cancel.setFont(font)
        self.button_cancel.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(83, 83, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background-color: rgb(100, 100, 100);\n"
"}")
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_9.addWidget(self.button_cancel)
        self.verticalLayout.addWidget(self.frame_choice)
        self.verticalLayout_3.addWidget(self.fram_all)

        self.retranslateUi(cioxo_createShot)
        QtCore.QMetaObject.connectSlotsByName(cioxo_createShot)

    def retranslateUi(self, cioxo_createShot):
        _translate = QtCore.QCoreApplication.translate
        cioxo_createShot.setWindowTitle(_translate("cioxo_createShot", "Dialog"))
        self.label_createShot.setText(_translate("cioxo_createShot", "Create shot"))
        self.lineEdit_input.setText(_translate("cioxo_createShot", "sh"))
        self.lineEdit_frameStart.setText(_translate("cioxo_createShot", "1001"))
        self.labe_frameRangeSeparator.setText(_translate("cioxo_createShot", "-"))
        self.lineEdit_frameEnd.setText(_translate("cioxo_createShot", "1240"))
        self.label_informations.setText(_translate("cioxo_createShot", ">>> Terminal - Add sh before number/name! - Example: sh0010, shLilith\n"
">>> Second Line is the shot frame range (Can be modified later on)"))
        self.button_ok.setText(_translate("cioxo_createShot", "OK"))
        self.button_cancel.setText(_translate("cioxo_createShot", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cioxo_createShot = QtWidgets.QDialog()
    ui = Ui_cioxo_createShot()
    ui.setupUi(cioxo_createShot)
    cioxo_createShot.show()
    sys.exit(app.exec_())
