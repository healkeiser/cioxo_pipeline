from ui_defineRoot import Ui_DefineRoot
import ui_cioxo_QtResources_rc

# ------ Import necessary libraries
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
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


# ------ DEFINE ROOT
class DefineRoot(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_DefineRoot()
        self.ui.setupUi(self)
        self.show()

        def browseRoot():
            USERNAME = os.getenv("USERNAME")
            rootDir = QFileDialog.getExistingDirectory(self, "Open directory", "C:/Users/" + USERNAME + "/Documents/")
            # rootDir = rootDir[0]
            rootDir = "".join(rootDir)
            self.ui.labelFile.setText(rootDir)
        self.ui.buttonBrowse.clicked.connect(browseRoot)

        def defineRoot():
            root = self.ui.labelFile.text()

            # ------ Create base .cioxo folder
            USERNAME = os.getenv("USERNAME")
            windowsBase = "C:/Users/" + USERNAME
            cioxoBase = os.path.join(windowsBase, ".cioxo")
            if os.path.isdir(cioxoBase):
                pass
            else:
                os.mkdir(cioxoBase)

            # ------ Write cioxoRoot.txt file
            with open(os.path.join(cioxoBase, ".cioxoRoot.txt"), 'w') as f:
                f.write(root)

            # ------ Write .templates folders
            templateBase = os.path.join(cioxoBase, ".templates")
            # ------ Project
            projectFolder = ".templateProject"
            projectFolders = ["assets", "misc"]
            projectMiscFolders = ["other", "fonts", "images", "music", "references", "assets", ""]
            projectAssetsFolders = ["downloads", ""]
            for projectFolders in projectFolders:
                os.makedirs(os.path.join(templateBase, projectFolder, projectFolders), exist_ok=True)
                for projectMiscFolders in projectMiscFolders:
                    os.makedirs(os.path.join(templateBase, projectFolder, "misc", projectMiscFolders), exist_ok=True)
                for projectAssetsFolders in projectAssetsFolders:
                    os.makedirs(os.path.join(templateBase, projectFolder, "assets", projectAssetsFolders), exist_ok=True)

            # ------ Asset
            assetFolder = ".templateAsset"
            assetFolders = ["houdini", "maya", "nuke", "output", "substance", ""]
            houdiniFolders = ["abc", "audio", "comp", "desk", "flip", "geo", "hda", "render", "scripts", "sim", "tex", "video", "workspaces", ""]
            mayaFolders = ["assets", "autosave", "cache", "clips", "data", "images", "movies", "renderData", "sceneAssembly", "workspaces", "scripts", "sound", "sourceimages", "Time Editor", ""]
            nukeFolders = ["output", "workspaces",""]
            substanceFolders = ["output", "workspaces", ""]
            for assetFolders in assetFolders:
                os.makedirs(os.path.join(templateBase, assetFolder, assetFolders), exist_ok=True)
                for houdiniFolders in houdiniFolders:
                    os.makedirs(os.path.join(templateBase, assetFolder, "houdini", houdiniFolders), exist_ok=True)
                for mayaFolders in mayaFolders:
                    os.makedirs(os.path.join(templateBase, assetFolder, "maya", mayaFolders), exist_ok=True)
                for nukeFolders in nukeFolders:
                    os.makedirs(os.path.join(templateBase, assetFolder, "nuke", nukeFolders), exist_ok=True)
                for substanceFolders in substanceFolders:
                    os.makedirs(os.path.join(templateBase, assetFolder, "substance", substanceFolders), exist_ok=True)

            # ------ Sequence
            sequenceFolder = ".templateSequence"
            os.makedirs(os.path.join(templateBase, sequenceFolder), exist_ok=True)

            # ------ Shot
            shotFolder = ".templateShot"
            shotFolders = ["houdini", "maya", "nuke", "output", "substance", "afterEffects", "photoshop", ""]
            houdiniFolders = ["abc", "audio", "comp", "desk", "flip", "geo", "hda", "render", "scripts", "sim", "tex",
                              "video", "workspaces", ""]
            mayaFolders = ["assets", "autosave", "cache", "clips", "data", "images", "movies", "renderData",
                           "sceneAssembly", "workspaces", "scripts", "sound", "sourceimages", "Time Editor", ""]
            nukeFolders = ["output", "workspaces", ""]
            substanceFolders = ["output", "workspaces", ""]
            afterEffectsFolders = ["output", "workspaces", ""]
            photoshopFolders = ["output", "workspaces", ""]
            for shotFolders in shotFolders:
                os.makedirs(os.path.join(templateBase, shotFolder, shotFolders), exist_ok=True)
                for houdiniFolders in houdiniFolders:
                    os.makedirs(os.path.join(templateBase, shotFolder, "houdini", houdiniFolders), exist_ok=True)
                for mayaFolders in mayaFolders:
                    os.makedirs(os.path.join(templateBase, shotFolder, "maya", mayaFolders), exist_ok=True)
                for nukeFolders in nukeFolders:
                    os.makedirs(os.path.join(templateBase, shotFolder, "nuke", nukeFolders), exist_ok=True)
                for substanceFolders in substanceFolders:
                    os.makedirs(os.path.join(templateBase, shotFolder, "substance", substanceFolders), exist_ok=True)
                for afterEffectsFolders in afterEffectsFolders:
                    os.makedirs(os.path.join(templateBase, shotFolder, "afterEffects", afterEffectsFolders), exist_ok=True)
                for photoshopFolders in photoshopFolders:
                    os.makedirs(os.path.join(templateBase, shotFolder, "photoshop", photoshopFolders), exist_ok=True)

            # ------ GUI feedback
            self.ui.buttonCancel.setText("Close")
            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
            self.ui.labelInformations.setText(">>> Root defined - You can now close the window")
        self.ui.buttonOk.clicked.connect(defineRoot)

        def closeWindow_defineRoot():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_defineRoot)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Define Root")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DefineRoot()
    sys.exit(app.exec_())
