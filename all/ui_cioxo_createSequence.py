# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Valen\Documents\PROJECTS\.pipeline\all\ui\cioxo_createSequence.ui'
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


class Ui_cioxo_createSequence(object):
    def setupUi(self, cioxo_createSequence):
        cioxo_createSequence.setObjectName("cioxo_createSequence")
        cioxo_createSequence.resize(500, 250)
        cioxo_createSequence.setMinimumSize(QtCore.QSize(500, 250))
        cioxo_createSequence.setMaximumSize(QtCore.QSize(800, 300))
        cioxo_createSequence.setStyleSheet("background-color: rgb(27, 27, 27);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(cioxo_createSequence)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_all = QtWidgets.QFrame(cioxo_createSequence)
        self.frame_all.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_all.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_all.setObjectName("frame_all")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_all)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(self.frame_all)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_title.setStyleSheet("")
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setLineWidth(0)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_createProject = QtWidgets.QLabel(self.frame_title)
        self.label_createProject.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_createProject.setFont(font)
        self.label_createProject.setStyleSheet("color:white;")
        self.label_createProject.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_createProject.setObjectName("label_createProject")
        self.horizontalLayout_6.addWidget(self.label_createProject)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_input = QtWidgets.QFrame(self.frame_all)
        self.frame_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_input.setObjectName("frame_input")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_input)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
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
        self.verticalLayout.addWidget(self.frame_input)
        self.frame_informations = QtWidgets.QFrame(self.frame_all)
        self.frame_informations.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_informations.setStyleSheet("")
        self.frame_informations.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_informations.setFrameShadow(QtWidgets.QFrame.Raised)
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
        self.frame_choice = QtWidgets.QFrame(self.frame_all)
        self.frame_choice.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_choice.setMaximumSize(QtCore.QSize(16777215, 33))
        self.frame_choice.setStyleSheet("    background-color: rgb(50, 50, 50);")
        self.frame_choice.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_choice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_choice.setLineWidth(0)
        self.frame_choice.setObjectName("frame_choice")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_choice)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 9)
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
        self.verticalLayout_3.addWidget(self.frame_all)

        self.retranslateUi(cioxo_createSequence)
        QtCore.QMetaObject.connectSlotsByName(cioxo_createSequence)

    def retranslateUi(self, cioxo_createSequence):
        _translate = QtCore.QCoreApplication.translate
        cioxo_createSequence.setWindowTitle(_translate("cioxo_createSequence", "Dialog"))
        self.label_createProject.setText(_translate("cioxo_createSequence", "Create Sequence"))
        self.lineEdit_input.setText(_translate("cioxo_createSequence", "seq"))
        self.label_informations.setText(_translate("cioxo_createSequence", ">>> Terminal - Add seq before number/name!\n"
">>> Example: seq001, seqKfc"))
        self.button_ok.setText(_translate("cioxo_createSequence", "OK"))
        self.button_cancel.setText(_translate("cioxo_createSequence", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cioxo_createSequence = QtWidgets.QDialog()
    ui = Ui_cioxo_createSequence()
    ui.setupUi(cioxo_createSequence)
    cioxo_createSequence.show()
    sys.exit(app.exec_())
