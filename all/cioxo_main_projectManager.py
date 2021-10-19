from ui_splashScreen_functions import *
from ui_cioxo_main_projectManager import Ui_ProjectManager
from ui_createProject import Ui_CreateProject
from ui_createSequence import Ui_CreateSequence
from ui_createShot import Ui_CreateShot
from ui_createAsset import Ui_CreateAsset
from ui_createFile import Ui_CreateFile
from ui_createThumbnail import Ui_CreateThumbnail
from ui_splashScreen import Ui_SplashScreen
import ui_cioxoQtResources_rc

# ------ Import necessary libraries
import os
import sys
from PIL import Image
from distutils.dir_util import copy_tree
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import *

# ------ DEFINE GLOBALS
counter = 0
version = str("v1.0.0")
labelInformationsRed = ("QLabel\n"
                        "{\n"
                        "    color: rgb(255, 0, 0);\n"
                        "    background-color: rgb(0, 0, 0);\n"
                        "    border-style: solid;\n"
                        "    border-width: 1px;\n"
                        "    border-radius: 5px;\n"
                        "    border-color: rgb(50, 50, 50);\n"
                        "}")
labelInformationsOrange = ("QLabel\n"
                        "{\n"
                        "    color: rgb(255, 165, 0);\n"
                        "    background-color: rgb(0, 0, 0);\n"
                        "    border-style: solid;\n"
                        "    border-width: 1px;\n"
                        "    border-radius: 5px;\n"
                        "    border-color: rgb(50, 50, 50);\n"
                        "}")
labelInformationsGreen = ("QLabel\n"
                          "{\n"
                          "    color: rgb(0, 255, 0);\n"
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
buttonGrey = ("QPushButton\n"
              "{\n"
              "    background-color: rgb(83, 83, 83);\n"
              "    color: rgb(255, 255, 255);\n"
              "    border-radius: 3px;\n"
              "}\n"
              "QPushButton:hover:!pressed\n"
              "{\n"
              "    background-color: rgb(100, 100, 100);\n"
              "}")
buttonRed = ("QPushButton\n"
             "{\n"
             "    background-color: rgb(83, 0, 0);\n"
             "    color: rgb(255, 255, 255);\n"
             "    border-radius: 3px;\n"
             "}\n"
             "QPushButton:hover:!pressed\n"
             "{\n"
             "    background-color: rgb(120, 0, 0);\n"
             "}")
buttonOrange = ("QPushButton\n"
             "{\n"
             "    background-color: rgb(130,75,0);\n"
             "    color: rgb(255, 255, 255);\n"
             "    border-radius: 3px;\n"
             "}\n"
             "QPushButton:hover:!pressed\n"
             "{\n"
             "    background-color: rgb(100, 100, 100);\n"
             "}")
buttonGreen = ("QPushButton\n"
               "{\n"
               "    background-color: rgb(0, 83, 0);\n"
               "    color: rgb(255, 255, 255);\n"
               "    border-radius: 3px;\n"
               "}\n"
               "QPushButton:hover:!pressed\n"
               "{\n"
               "    background-color: rgb(0, 120, 0);\n"
               "}")

# ----- Files extensions
houdiniExtension = ".hip", ".hiplc"
mayaExtension = ".ma", ".mb"
substanceExtension = ".spp"
nukeExtension = ".nk", ".nknc"
afterEffectsExtension = ".aep"
photoshopExtension = ".psd"

# ------ Define rootDir PROJECTS
USERNAME = os.getenv("USERNAME")
windowsBase = "C:/Users/" + USERNAME
cioxoBase = os.path.join(windowsBase, ".cioxo")
rootFile = os.path.join(windowsBase, ".cioxo", ".cioxoRoot.txt")
if os.path.isdir(cioxoBase):
    if os.path.isfile(rootFile):
        with open(rootFile) as f:
            rootDir = f.readline()
    else:
        print("No .cioxo file found, please run 'Define Root' first!")
        input("Press Enter to exit")
else:
    print("No .cioxo folder found, please run 'Define Root' first!")
    input("Press Enter to exit")
os.environ["CIOXO_ROOT"] = rootDir
CIOXO_ROOT = os.getenv("CIOXO_ROOT")

# ------ Define where to find templates
projectTemplate = os.path.join(cioxoBase, ".templates", ".templateProject")
sequenceTemplate = os.path.join(cioxoBase, ".templates", ".templateSequence")
assetTemplate = os.path.join(cioxoBase, ".templates", ".templateAsset")
shotTemplate = os.path.join(cioxoBase, ".templates", ".templateShot")


# ------ PROJECT MANAGER
class ProjectManager(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ProjectManager()
        self.ui.setupUi(self)

        # ------ Additional windows
        self.createProjectWindow = None  # ------ No "Create Project" window yet
        self.createAssetWindow = None  # ------ No "Create Asset" window yet
        self.createSequenceWindow = None  # ------ No "Create Sequence" window yet
        self.createShotWindow = None  # ------ No "Create Shot" window yet
        self.createFileAssetWindow = None  # ------ No "Create File Asset" window yet
        self.createFileShotWindow = None  # ------ No "Create File Shot" window yet
        self.createThumbnailWindowProject = None  # ------ No "Create Thumbnail Project" window yet
        self.createThumbnailWindowAsset = None  # ------ No "Create Thumbnail Asset" window yet
        self.createThumbnailWindowShot = None  # ------ No "Create Thumbnail Shot" window yet
        self.createThumbnailWindowFile = None  # ------ No "Create Thumbnail File Shot" window yet
        self.createThumbnailWindowFileAsset = None  # ------ No "Create Thumbnail File Asset" window yet

        # ------ Tabs state at opening
        tabProjects = 0
        tabAssets = 1
        tabFilesAssets = 2
        tabSequences = 3
        tabFilesSequences = 4
        self.ui.tabWidget.setTabsClosable(False)
        self.ui.tabWidget.setTabEnabled(tabProjects, True)
        self.ui.tabWidget.setTabEnabled(tabAssets, True)
        self.ui.tabWidget.setTabEnabled(tabFilesAssets, False)
        self.ui.tabWidget.setTabEnabled(tabSequences, True)
        self.ui.tabWidget.setTabEnabled(tabFilesSequences, False)

        # ------ Buttons state at opening
        self.ui.buttonHoudiniAssets.setEnabled(False)
        self.ui.buttonMayaAssets.setEnabled(False)
        self.ui.buttonSubstanceAssets.setEnabled(False)
        self.ui.buttonNukeAssets.setEnabled(False)
        self.ui.buttonHoudiniSequences.setEnabled(False)
        self.ui.buttonMayaSequences.setEnabled(False)
        self.ui.buttonSubstanceSequences.setEnabled(False)
        self.ui.buttonNukeSequences.setEnabled(False)
        self.ui.buttonAfterEffectsSequences.setEnabled(False)
        self.ui.buttonPhotoshopSequences.setEnabled(False)

        # ------ Start Cioxo on project tab
        self.ui.tabWidget.setCurrentIndex(tabProjects)

        # ------ Add items from rootDir in listWidget projects
        for file in os.listdir(rootDir):
            if len(file) <= 3:
                self.ui.listProjects.addItems(file.split())

# ---------------------------#
# ------ PROJECTS TAB ------ #
# ---------------------------#

        def defineCioxoVariable_PROJECT():
            activeListItem = [item.text() for item in self.ui.listProjects.selectedItems()]
            listToString = ''.join([str(elem) for elem in activeListItem])
            # ------ Define CIOXO_PROJECT environment variable on item selected
            os.environ["CIOXO_PROJECT"] = listToString
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Project variable defined on: " + CIOXO_PROJECT)
        self.ui.listProjects.itemSelectionChanged.connect(defineCioxoVariable_PROJECT)

        def reloadList_projects():
            self.ui.listProjects.clear()
            for fileProject in os.listdir(rootDir):
                if len(fileProject) <= 3:
                    self.ui.listProjects.addItems(fileProject.split())
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Reloaded")
        self.ui.buttonReloadProjects.clicked.connect(reloadList_projects)

        def loadThumbnail_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailProjects.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailProjects.setText("No Thumbnail found")
        self.ui.listProjects.itemSelectionChanged.connect(loadThumbnail_projects)
        self.ui.buttonRefreshThumbnailProjects.clicked.connect(loadThumbnail_projects)

        def deleteThumbnail_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                self.ui.labelInformations.setText(">>> Thumbnail deleted")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No thumbnail found!")
        self.ui.buttonDeleteThumbnailProjects.clicked.connect(deleteThumbnail_projects)

        def openCreateThumbnail_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            if CIOXO_PROJECT == "project" or os.path.isdir(os.path.join(rootDir, CIOXO_PROJECT)) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                if self.createThumbnailWindowProject is None:
                    self.createThumbnailWindowProject = CreateThumbnailProject()
                    self.createThumbnailWindowProject.show()
                    self.createThumbnailWindowProject = None  # ------ Discard reference
                else:
                    self.createThumbnailWindowProject.close()  # ------ Close window
                    self.createThumbnailWindowProject = None  # ------ Discard reference
        self.ui.buttonChargeThumbnailProjects.clicked.connect(openCreateThumbnail_projects)

        def openAssetsManager():  # ------ Show Assets Manager tab
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            projectPath = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(projectPath) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                self.ui.tabWidget.setCurrentIndex(tabAssets)
        self.ui.buttonAssets.clicked.connect(openAssetsManager)

        def openSequencesManager():  # ------ Show Sequences Manager tab
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            projectPath = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(projectPath) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                self.ui.tabWidget.setCurrentIndex(tabSequences)
        self.ui.buttonSequences.clicked.connect(openSequencesManager)

        def openCreate_projects():  # ------ Show Create Asset window
            if self.createProjectWindow is None:
                self.createProjectWindow = CreateProject()
                self.createProjectWindow.show()
                self.createProjectWindow = None  # ------ Discard reference
            else:
                self.createProjectWindow.close()  # ------ Close window
                self.createProjectWindow = None  # ------ Discard reference
        self.ui.buttonCreateProjects.clicked.connect(openCreate_projects)

        def setResolution_project():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.lineEditResolutionProjectX.setInputMask("99900")
            resolutionXInput = self.ui.lineEditResolutionProjectX.text()
            self.ui.lineEditResolutionProjectY.setInputMask("99900")
            resolutionYInput = self.ui.lineEditResolutionProjectY.text()
            with open(os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_resolution.txt"), 'w') as f:
                f.write(resolutionXInput + "_" + resolutionYInput)
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Project resolution changed")
        self.ui.buttonValidateResolution.clicked.connect(setResolution_project)

        def getResolution_project():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            resolutionFile = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_resolution.txt")
            if os.path.isfile(resolutionFile):
                with open(resolutionFile) as f:
                    resolution = f.readline()
                resolutionX = resolution.split("_")[0]
                resolutionY = resolution.split("_")[1]
                self.ui.lineEditResolutionProjectX.setText(resolutionX)
                self.ui.lineEditResolutionProjectY.setText(resolutionY)
            else:
                self.ui.lineEditResolutionProjectX.setText("None")
                self.ui.lineEditResolutionProjectY.setText("None")
        self.ui.listProjects.itemSelectionChanged.connect(getResolution_project)
        self.ui.buttonValidateResolution.clicked.connect(getResolution_project)

        def setFPS_project():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.lineEditFPS.setInputMask("00000")
            fpsInput = self.ui.lineEditFPS.text()
            with open(os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_fps.txt"), 'w') as f:
                f.write(fpsInput)
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Project FPS changed")
        self.ui.buttonValidateFPS.clicked.connect(setFPS_project)

        def getFPS_project():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            fpsFile = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_fps.txt")
            if os.path.isfile(fpsFile):
                with open(fpsFile) as f:
                    FPS = f.readline()
                self.ui.lineEditFPS.setText(FPS)
            else:
                self.ui.lineEditFPS.setText("None")
        self.ui.listProjects.itemSelectionChanged.connect(getFPS_project)
        self.ui.buttonValidateFPS.clicked.connect(getFPS_project)

        def openDirectories_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            projectPath = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(projectPath) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                os.startfile(projectPath)
                self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
                self.ui.labelInformations.setText(">>> Opening Directory")
        self.ui.buttonDirectoryProjects.clicked.connect(openDirectories_projects)

        def next_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            projectPath = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(projectPath) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                self.ui.tabWidget.setCurrentIndex(tabAssets)
        self.ui.pushButtonNextProjects.clicked.connect(next_projects)

# -------------------------#
# ------ ASSETS TAB ------ #
# -------------------------#

        self.ui.listAssets.addItems(["Select a project"])

        def changeTitle_projectAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.labelWelcomeAssets.setText(CIOXO_PROJECT)
        self.ui.listProjects.itemSelectionChanged.connect(changeTitle_projectAssets)

        def changeTitle_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.tabWidget.setTabText(tabAssets, "Assets | " + CIOXO_PROJECT)
        self.ui.listProjects.itemSelectionChanged.connect(changeTitle_assets)

        def fillList_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            assetsPath = os.path.join(rootDir, CIOXO_PROJECT, "assets")
            if CIOXO_PROJECT == "project" or os.path.isdir(assetsPath) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                self.ui.listAssets.clear()
                self.ui.listAssets.addItems(os.listdir(assetsPath))
        self.ui.listProjects.itemSelectionChanged.connect(fillList_assets)
        self.ui.buttonReloadAssets.clicked.connect(fillList_assets)

        def reloadList_assets():
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Reloaded")
        self.ui.buttonReloadAssets.clicked.connect(reloadList_assets)

        def openWindow_createAssets():  # ------ Show Create Asset window
            if self.createAssetWindow is None:
                self.createAssetWindow = CreateAsset()
                self.createAssetWindow.show()
                self.createAssetWindow = None  # ------ Discard reference
            else:
                self.createAssetWindow.close()  # ------ Close window
                self.createAssetWindow = None  # ------ Discard reference
        self.ui.buttonCreateAssets.clicked.connect(openWindow_createAssets)

        def defineCioxoVariable_ASSET():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            # ------ Get change in list assets
            activeListItem = [item.text() for item in self.ui.listAssets.selectedItems()]
            listToString = ''.join([str(elem) for elem in activeListItem])
            # ------ Define CIOXO SEQUENCE environment variable on item selected
            os.environ["CIOXO_ASSET"] = listToString
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Asset variable defined on: " + CIOXO_ASSET)
        self.ui.listAssets.itemSelectionChanged.connect(defineCioxoVariable_ASSET)

        def checkFilesExists_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            assetsPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET)

            # ------ Reset button colors
            self.ui.buttonHoudiniAssets.setStyleSheet(buttonGrey)
            self.ui.buttonMayaAssets.setStyleSheet(buttonGrey)
            self.ui.buttonSubstanceAssets.setStyleSheet(buttonGrey)
            self.ui.buttonNukeAssets.setStyleSheet(buttonGrey)

            # ------ Houdini
            filesPath = os.path.join(assetsPath, "houdini", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonHoudiniAssets.setEnabled(True)
                self.ui.buttonHoudiniAssets.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesHoudini = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesHoudini:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".hip" or extension == ".hiplc":
                                self.ui.buttonHoudiniAssets.setEnabled(True)
                                self.ui.buttonHoudiniAssets.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonHoudiniAssets.setEnabled(True)
                                self.ui.buttonHoudiniAssets.setStyleSheet(buttonRed)
            else:
                self.ui.buttonHoudiniAssets.setEnabled(True)
                self.ui.buttonHoudiniAssets.setStyleSheet(buttonRed)

            # ------ Maya
            filesPath = os.path.join(assetsPath, "maya", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonMayaAssets.setEnabled(True)
                self.ui.buttonMayaAssets.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesMaya = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesMaya:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".mb" or extension == ".ma":
                                self.ui.buttonMayaAssets.setEnabled(True)
                                self.ui.buttonMayaAssets.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonMayaAssets.setEnabled(True)
                                self.ui.buttonMayaAssets.setStyleSheet(buttonRed)
            else:
                self.ui.buttonMayaAssets.setEnabled(True)
                self.ui.buttonMayaAssets.setStyleSheet(buttonRed)

            # ------ Substance
            filesPath = os.path.join(assetsPath, "substance", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonSubstanceAssets.setEnabled(True)
                self.ui.buttonSubstanceAssets.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesSubstance = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesSubstance:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".spp":
                                self.ui.buttonSubstanceAssets.setEnabled(True)
                                self.ui.buttonSubstanceAssets.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonSubstanceAssets.setEnabled(True)
                                self.ui.buttonSubstanceAssets.setStyleSheet(buttonRed)
            else:
                self.ui.buttonSubstanceAssets.setEnabled(True)
                self.ui.buttonSubstanceAssets.setStyleSheet(buttonRed)

            # ------ Nuke
            filesPath = os.path.join(assetsPath, "nuke", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonNukeAssets.setEnabled(True)
                self.ui.buttonNukeAssets.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesNuke = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesNuke:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".nk" or extension == ".nknc":
                                self.ui.buttonNukeAssets.setEnabled(True)
                                self.ui.buttonNukeAssets.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonNukeAssets.setEnabled(True)
                                self.ui.buttonNukeAssets.setStyleSheet(buttonRed)
            else:
                self.ui.buttonNukeAssets.setEnabled(True)
                self.ui.buttonNukeAssets.setStyleSheet(buttonRed)
        self.ui.listAssets.itemSelectionChanged.connect(checkFilesExists_assets)

        def loadThumbnail_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, "." + CIOXO_PROJECT + "_" + CIOXO_ASSET + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailAssets.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailAssets.setText("No Thumbnail found")
        self.ui.listAssets.itemSelectionChanged.connect(loadThumbnail_assets)
        self.ui.buttonRefreshThumbnailAssets.clicked.connect(loadThumbnail_assets)

        def openWindow_createThumbnailAssets():
            if self.createThumbnailWindowAsset is None:
                self.createThumbnailWindowAsset = CreateThumbnailAsset()
                self.createThumbnailWindowAsset.show()
                self.createThumbnailWindowAsset = None  # ------ Discard reference
            else:
                self.createThumbnailWindowAsset.close()  # ------ Close window
                self.createThumbnailWindowAsset = None  # ------ Discard reference
        self.ui.buttonChargeThumbnailAssets.clicked.connect(openWindow_createThumbnailAssets)

        def deleteThumbnail_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, "." + CIOXO_PROJECT + "_" + CIOXO_ASSET + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                self.ui.labelInformations.setText(">>> Thumbnail deleted")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No thumbnail found!")
        self.ui.buttonDeleteThumbnailAssets.clicked.connect(deleteThumbnail_assets)

        def openDirectories_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            pathAsset = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET)
            if CIOXO_ASSET == "asset" or os.path.isdir(pathAsset) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No asset selected!")
            else:
                os.startfile(pathAsset)
                self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
                self.ui.labelInformations.setText(">>> Opening Directory")
        self.ui.buttonDirectoryAssets.clicked.connect(openDirectories_assets)

        def openWindow_createAssetFile():
            if self.createFileAssetWindow is None:
                self.createFileAssetWindow = CreateFileAsset()
                self.createFileAssetWindow.show()
                self.createFileAssetWindow = None  # ------ Discard reference
            else:
                self.createFileAssetWindow.close()  # ------ Close window
                self.createFileAssetWindow = None  # ------ Discard reference
        self.ui.buttonCreateFilesAssets.clicked.connect(openWindow_createAssetFile)

        def openTab_filesAssets():
            self.ui.tabWidget.setCurrentIndex(tabFilesAssets)
            self.ui.tabWidget.setTabEnabled(tabFilesAssets, True)
        self.ui.buttonHoudiniAssets.clicked.connect(openTab_filesAssets)
        self.ui.buttonMayaAssets.clicked.connect(openTab_filesAssets)
        self.ui.buttonSubstanceAssets.clicked.connect(openTab_filesAssets)
        self.ui.buttonNukeAssets.clicked.connect(openTab_filesAssets)

        def previous_assets():
            self.ui.tabWidget.setCurrentIndex(tabProjects)
        self.ui.pushButtonPreviousAssets.clicked.connect(previous_assets)

# -------------------------------#
# ------ FILES ASSETS TAB ------ #
# -------------------------------#

        self.ui.listFilesAssets.addItems(["Select an asset"])

        def defineCioxoVariable_HOUDINI():
            os.environ["CIOXO_SOFTWARE"] = "houdini"
        self.ui.buttonHoudiniAssets.clicked.connect(defineCioxoVariable_HOUDINI)

        def defineCioxoVariable_MAYA():
            os.environ["CIOXO_SOFTWARE"] = "maya"
        self.ui.buttonMayaAssets.clicked.connect(defineCioxoVariable_MAYA)

        def defineCioxoVariable_SUBSTANCE():
            os.environ["CIOXO_SOFTWARE"] = "substance"
        self.ui.buttonSubstanceAssets.clicked.connect(defineCioxoVariable_SUBSTANCE)

        def defineCioxoVariable_NUKE():
            os.environ["CIOXO_SOFTWARE"] = "nuke"
        self.ui.buttonNukeAssets.clicked.connect(defineCioxoVariable_NUKE)

        def changeTitle_sequenceShotSoftware():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            self.ui.labelWelcomeFilesAssets.setText(CIOXO_PROJECT + " - " + CIOXO_ASSET + " | " + CIOXO_SOFTWARE)
        self.ui.listAssets.itemSelectionChanged.connect(changeTitle_sequenceShotSoftware)
        self.ui.buttonHoudiniAssets.clicked.connect(changeTitle_sequenceShotSoftware)
        self.ui.buttonMayaAssets.clicked.connect(changeTitle_sequenceShotSoftware)
        self.ui.buttonSubstanceAssets.clicked.connect(changeTitle_sequenceShotSoftware)
        self.ui.buttonNukeAssets.clicked.connect(changeTitle_sequenceShotSoftware)

        def changeTabTitle_filesAssets():
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            self.ui.tabWidget.setTabText(tabFilesAssets, CIOXO_ASSET + " | " + CIOXO_SOFTWARE)
        self.ui.buttonHoudiniAssets.clicked.connect(changeTabTitle_filesAssets)
        self.ui.buttonMayaAssets.clicked.connect(changeTabTitle_filesAssets)
        self.ui.buttonSubstanceAssets.clicked.connect(changeTabTitle_filesAssets)
        self.ui.buttonNukeAssets.clicked.connect(changeTabTitle_filesAssets)

        def fillList_filesAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            filesPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE)
            self.ui.listFilesAssets.clear()

            # ------ Houdini
            if CIOXO_SOFTWARE == "houdini":
                # ----- Look for disciplines folders
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
                    self.ui.listFilesAssets.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(houdiniExtension):
                            filesList.append(files)
                            self.ui.listFilesAssets.addItem(files)
                        else:
                            pass

            # ------ Maya
            if CIOXO_SOFTWARE == "maya":
                # ----- Look for disciplines folders
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
                    self.ui.listFilesAssets.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(mayaExtension):
                            filesList.append(files)
                            self.ui.listFilesAssets.addItem(files)
                        else:
                            pass

            # ------ Substance
            if CIOXO_SOFTWARE == "substance":
                # ----- Look for disciplines folders
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(os.path.join(filesPath, "workspaces")):
                    foldersDisciplineList.append(folderDisciplines)
                    # ------ Add delimiter for categories to list
                    delimiter = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.listFilesAssets.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(substanceExtension):
                            filesList.append(files)
                            self.ui.listFilesAssets.addItem(files)

            # ------ Nuke
            if CIOXO_SOFTWARE == "nuke":
                # ----- Look for disciplines folders
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(os.path.join(filesPath, "workspaces")):
                    foldersDisciplineList.append(folderDisciplines)
                    # ------ Add delimiter for categories to list
                    delimiter = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.listFilesAssets.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(nukeExtension):
                            filesList.append(files)
                            self.ui.listFilesAssets.addItem(files)

            # ------ After Effects
            if CIOXO_SOFTWARE == "afterEffects":
                # ----- Look for disciplines folders
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(os.path.join(filesPath, "workspaces")):
                    foldersDisciplineList.append(folderDisciplines)
                    # ------ Add delimiter for categories to list
                    delimiter = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.listFilesAssets.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(afterEffectsExtension):
                            filesList.append(files)
                            self.ui.listFilesAssets.addItem(files)

            # ------ Photoshop
            if CIOXO_SOFTWARE == "photoshop":
                # ----- Look for disciplines folders
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(os.path.join(filesPath, "workspaces")):
                    foldersDisciplineList.append(folderDisciplines)
                    # ------ Add delimiter for categories to list
                    delimiter = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.listFilesAssets.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(photoshopExtension):
                            filesList.append(files)
                            self.ui.listFilesAssets.addItem(files)
        self.ui.buttonHoudiniAssets.clicked.connect(fillList_filesAssets)
        self.ui.buttonMayaAssets.clicked.connect(fillList_filesAssets)
        self.ui.buttonSubstanceAssets.clicked.connect(fillList_filesAssets)
        self.ui.buttonNukeAssets.clicked.connect(fillList_filesAssets)
        # TODO: create GUI buttons for Nuke and After Effects
        # self.ui.buttonNukeAssets.clicked.connect(fillList_filesAssets)
        # self.ui.buttonNukeAssets.clicked.connect(fillList_filesAssets)
        self.ui.buttonReloadFilesAssets.clicked.connect(fillList_filesAssets)

        def reloadList_filesAssets():
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Reloaded")
        self.ui.buttonReloadFilesAssets.clicked.connect(reloadList_filesAssets)

        def defineCioxoVariable_FILE():
            activeListItem = [item.text() for item in self.ui.listFilesAssets.selectedItems()]
            listToString = ''.join([str(elem) for elem in activeListItem])
            os.environ["CIOXO_FILE"] = listToString
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            os.environ["CIOXO_DISCIPLINE"] = CIOXO_FILE.lower().split("_")[2]
            CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> File variable defined on: " + CIOXO_FILE + "\n>>> Discipline variable defined on: " + CIOXO_DISCIPLINE)
        self.ui.listFilesAssets.itemSelectionChanged.connect(defineCioxoVariable_FILE)

        def loadThumbnail_filesAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[2]
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailFilesAssets.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailFilesAssets.setText("No Thumbnail found")
        self.ui.listFilesAssets.itemSelectionChanged.connect(loadThumbnail_filesAssets)
        self.ui.buttonRefreshThumbnailFilesAssets.clicked.connect(loadThumbnail_filesAssets)

        def openCreateThumbnail_filesAssets():
            if self.createThumbnailWindowFileAsset is None:
                self.createThumbnailWindowFileAsset = CreateThumbnailFileAsset()
                self.createThumbnailWindowFileAsset.show()
                self.createThumbnailWindowFileAsset = None  # ------ Discard reference
            else:
                self.createThumbnailWindowFileAsset.close()  # ------ Close window
                self.createThumbnailWindowFileAsset = None  # ------ Discard reference
        self.ui.buttonChargeThumbnailFilesAssets.clicked.connect(openCreateThumbnail_filesAssets)

        def deleteThumbnail_fileAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[2]
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                self.ui.labelInformations.setText(">>> Thumbnail deleted")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No thumbnail found!")
        self.ui.buttonDeleteThumbnailFilesAssets.clicked.connect(deleteThumbnail_fileAssets)

        def showComment_filesAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[2]
            fileCommentPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_comment.txt")
            if os.path.isfile(fileCommentPath):
                with open(fileCommentPath) as f:
                    comment = f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline()
                self.ui.labelCommentFilesAssets.setText(comment)
            else:
                self.ui.labelCommentFilesAssets.setText("No comment found")
        self.ui.listFilesAssets.itemSelectionChanged.connect(showComment_filesAssets)

        def openFile_fileAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            filesPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, CIOXO_FILE)
            if CIOXO_FILE == "file" or os.path.isfile(filesPath) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No file selected!")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
                os.startfile(filesPath)
                self.ui.labelInformations.setText(">>> Opening " + filesPath)
        self.ui.buttonOpenFilesAssets.clicked.connect(openFile_fileAssets)

        def clearList_filesAssets():
            # ------ Reset button colors
            self.ui.buttonHoudiniAssets.setStyleSheet(buttonGrey)
            self.ui.buttonMayaAssets.setStyleSheet(buttonGrey)
            self.ui.buttonSubstanceAssets.setStyleSheet(buttonGrey)
            self.ui.buttonNukeAssets.setStyleSheet(buttonGrey)
            # ------ Clear
            self.ui.tabWidget.setTabText(tabFilesAssets, "Asset Files")
            self.ui.tabWidget.setTabEnabled(tabFilesAssets, False)
            self.ui.listFilesAssets.clear()
        self.ui.listProjects.itemSelectionChanged.connect(clearList_filesAssets)

        def clearList_filesAssetsSecondary():
            # ------ Clear
            self.ui.tabWidget.setTabText(tabFilesAssets, "Asset Files")
            self.ui.tabWidget.setTabEnabled(tabFilesAssets, False)
            self.ui.listFilesAssets.clear()
        self.ui.listAssets.itemSelectionChanged.connect(clearList_filesAssetsSecondary)

        def openDirectories_filesAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            pathFile = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE)
            os.startfile(pathFile)
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Opening Directory")
        self.ui.buttonDirectoryFilesAssets.clicked.connect(openDirectories_filesAssets)

        def previous_fileAssets():
            self.ui.tabWidget.setCurrentIndex(tabAssets)
        self.ui.pushButtonPreviousFilesAssets.clicked.connect(previous_fileAssets)

# ---------------------------#
# ------ SEQUENCES TAB ------#
# ---------------------------#

        self.ui.listSequences.addItems(["Select a project"])
        self.ui.listShots.addItems(["Select a sequence"])

        def changeTitle_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.labelWelcomeSequences.setText(CIOXO_PROJECT)
        self.ui.listProjects.itemSelectionChanged.connect(changeTitle_sequences)

        def changeTabTitle_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.tabWidget.setTabText(tabSequences, "Sequences | " + CIOXO_PROJECT)
        self.ui.listProjects.itemSelectionChanged.connect(changeTabTitle_sequences)

        def fillList_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            pathSequences = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(pathSequences) is False:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                self.ui.listSequences.clear()
                for sequences in os.listdir(pathSequences):
                    if sequences.startswith("seq"):
                        self.ui.listSequences.addItems(sequences.split())
        self.ui.listProjects.itemSelectionChanged.connect(fillList_sequences)
        self.ui.buttonReloadSequence.clicked.connect(fillList_sequences)

        def loadThumbnail_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)
            pathThumbnail = os.path.join(shotPath, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailSequences.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailSequences.setText("No Thumbnail found")
        self.ui.listShots.itemSelectionChanged.connect(loadThumbnail_sequences)
        self.ui.buttonRefreshThumbnailSequences.clicked.connect(loadThumbnail_sequences)

        def deleteThumbnail_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)
            pathThumbnail = os.path.join(shotPath,
                                         "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                self.ui.labelInformations.setText(">>> Thumbnail deleted")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No thumbnail found!")
        self.ui.buttonDeleteThumbnailSequences.clicked.connect(deleteThumbnail_sequences)

        def openCreateThumbnail_sequences():
            if self.createThumbnailWindowProject is None:
                self.createThumbnailWindowShot = CreateThumbnailShot()
                self.createThumbnailWindowShot.show()
                self.createThumbnailWindowShot = None  # ------ Discard reference
            else:
                self.createThumbnailWindowShot.close()  # ------ Close window
                self.createThumbnailWindowShot = None  # ------ Discard reference
        self.ui.buttonChargeThumbnailSequences.clicked.connect(openCreateThumbnail_sequences)

        def defineCioxoVariable_SEQUENCE():
            # --- SEQUENCE
            # ------ Get change in list sequence
            activeListItemSequence = [item.text() for item in self.ui.listSequences.selectedItems()]
            listToStringSequence = ''.join([str(elem) for elem in activeListItemSequence])
            # ------ Define CIOXO SEQUENCE environment variable on item selected
            os.environ["CIOXO_SEQUENCE"] = listToStringSequence
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Sequence variable defined on: " + CIOXO_SEQUENCE)
        self.ui.listSequences.itemSelectionChanged.connect(defineCioxoVariable_SEQUENCE)

        def fillList_shots():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            shotsPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)
            self.ui.listShots.clear()
            for shots in os.listdir(shotsPath):
                if shots.startswith("sh"):
                    self.ui.listShots.addItems(shots.split())
        self.ui.listSequences.itemSelectionChanged.connect(fillList_shots)
        self.ui.buttonReloadShots.clicked.connect(fillList_shots)

        def defineCioxoVariable_SHOT():
            # ------ Get change in list shot
            activeListItemShots = [item.text() for item in self.ui.listShots.selectedItems()]
            listToStringShot = ''.join([str(elem) for elem in activeListItemShots])
            # ------ Define CIOXO SHOT environment variable on item selected
            os.environ["CIOXO_SHOT"] = listToStringShot
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Shot variable defined on: " + CIOXO_SHOT)
        self.ui.listShots.itemSelectionChanged.connect(defineCioxoVariable_SHOT)

        def loadThumbnail_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailSequences.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailSequences.setText("No Thumbnail found")
        self.ui.listShots.itemSelectionChanged.connect(loadThumbnail_sequences)
        self.ui.buttonRefreshThumbnailSequences.clicked.connect(loadThumbnail_sequences)

        def checkFilesExists_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)

            # ------ Reset button colors and state
            self.ui.buttonHoudiniSequences.setStyleSheet(buttonGrey)
            self.ui.buttonMayaSequences.setStyleSheet(buttonGrey)
            self.ui.buttonSubstanceSequences.setStyleSheet(buttonGrey)
            self.ui.buttonNukeSequences.setStyleSheet(buttonGrey)
            self.ui.buttonAfterEffectsSequences.setStyleSheet(buttonGrey)
            self.ui.buttonPhotoshopSequences.setStyleSheet(buttonGrey)

            # ------ Houdini
            filesPath = os.path.join(shotPath, "houdini", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonHoudiniSequences.setEnabled(True)
                self.ui.buttonHoudiniSequences.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesHoudini = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesHoudini:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".hip" or extension == ".hiplc":
                                self.ui.buttonHoudiniSequences.setEnabled(True)
                                self.ui.buttonHoudiniSequences.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonHoudiniSequences.setEnabled(True)
                                self.ui.buttonHoudiniSequences.setStyleSheet(buttonRed)
            else:
                self.ui.buttonHoudiniSequences.setEnabled(True)
                self.ui.buttonHoudiniSequences.setStyleSheet(buttonRed)

            # ------ Maya
            filesPath = os.path.join(shotPath, "maya", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonMayaSequences.setEnabled(True)
                self.ui.buttonMayaSequences.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesMaya = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesMaya:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".ma" or extension == ".mb":
                                self.ui.buttonMayaSequences.setEnabled(True)
                                self.ui.buttonMayaSequences.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonMayaSequences.setEnabled(True)
                                self.ui.buttonMayaSequences.setStyleSheet(buttonRed)
            else:
                self.ui.buttonMayaSequences.setEnabled(True)
                self.ui.buttonMayaSequences.setStyleSheet(buttonRed)

            # ------ Substance
            filesPath = os.path.join(shotPath, "substance", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonSubstanceSequences.setEnabled(True)
                self.ui.buttonSubstanceSequences.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesSubstance = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesSubstance:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".spp":
                                self.ui.buttonSubstanceSequences.setEnabled(True)
                                self.ui.buttonSubstanceSequences.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonSubstanceSequences.setEnabled(True)
                                self.ui.buttonSubstanceSequences.setStyleSheet(buttonRed)
            else:
                self.ui.buttonSubstanceSequences.setEnabled(True)
                self.ui.buttonSubstanceSequences.setStyleSheet(buttonRed)

            # ------ Nuke
            filesPath = os.path.join(shotPath, "nuke", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonNukeSequences.setEnabled(True)
                self.ui.buttonNukeSequences.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesNuke = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesNuke:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".nk" or extension == ".nknc":
                                self.ui.buttonNukeSequences.setEnabled(True)
                                self.ui.buttonNukeSequences.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonNukeSequences.setEnabled(True)
                                self.ui.buttonNukeSequences.setStyleSheet(buttonRed)
            else:
                self.ui.buttonNukeSequences.setEnabled(True)
                self.ui.buttonNukeSequences.setStyleSheet(buttonRed)

            # ------ After Effects
            filesPath = os.path.join(shotPath, "afterEffects", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonAfterEffectsSequences.setEnabled(True)
                self.ui.buttonAfterEffectsSequences.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesAfterEffects = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesAfterEffects:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".aep":
                                self.ui.buttonAfterEffectsSequences.setEnabled(True)
                                self.ui.buttonAfterEffectsSequences.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonAfterEffectsSequences.setEnabled(True)
                                self.ui.buttonAfterEffectsSequences.setStyleSheet(buttonRed)
            else:
                self.ui.buttonAfterEffectsSequences.setEnabled(True)
                self.ui.buttonAfterEffectsSequences.setStyleSheet(buttonRed)

            # ------ Photoshop
            filesPath = os.path.join(shotPath, "photoshop", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.buttonPhotoshopSequences.setEnabled(True)
                self.ui.buttonPhotoshopSequences.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesPhotoshop = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesPhotoshop:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".psd":
                                self.ui.buttonPhotoshopSequences.setEnabled(True)
                                self.ui.buttonPhotoshopSequences.setStyleSheet(buttonGreen)
                            else:
                                self.ui.buttonPhotoshopSequences.setEnabled(True)
                                self.ui.buttonPhotoshopSequences.setStyleSheet(buttonRed)
            else:
                self.ui.buttonPhotoshopSequences.setEnabled(True)
                self.ui.buttonPhotoshopSequences.setStyleSheet(buttonRed)
        self.ui.listShots.itemSelectionChanged.connect(checkFilesExists_sequences)

        def deleteThumbnail_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT,
                                         "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                self.ui.labelInformations.setText(">>> Thumbnail deleted")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No thumbnail found!")
        self.ui.buttonDeleteThumbnailSequences.clicked.connect(deleteThumbnail_sequences)

        def setFrameRange_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            frameRangeFile = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_frameRange.txt")
            self.ui.lineEditFrameStart.setInputMask("99900")
            frameStart = self.ui.lineEditFrameStart.text()
            self.ui.lineEditFrameEnd.setInputMask("99900")
            frameEnd = self.ui.lineEditFrameEnd.text()
            with open(os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_frameRange.txt"), "w") as f:
                f.write(frameStart + "_" + frameEnd)
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Shot frame range changed")
        self.ui.buttonValidateFrameRange.clicked.connect(setFrameRange_sequences)

        def getFrameRange_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            frameRangeFile = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_frameRange.txt")
            if os.path.isfile(frameRangeFile):
                with open(frameRangeFile) as f:
                    frameRange = f.readline()
                frameStart = frameRange.split("_")[0]
                frameEnd = frameRange.split("_")[1]
                self.ui.lineEditFrameStart.setText(frameStart)
                self.ui.lineEditFrameEnd.setText(frameEnd)
            else:
                self.ui.lineEditFrameStart.setText("None")
                self.ui.lineEditFrameEnd.setText("None")
        self.ui.listShots.itemSelectionChanged.connect(getFrameRange_sequences)
        self.ui.buttonValidateFrameRange.clicked.connect(getFrameRange_sequences)

        def openWindow_createShotFile():
            if self.createFileShotWindow is None:
                self.createFileShotWindow = CreateFileShot()
                self.createFileShotWindow.show()
                self.createFileShotWindow = None  # ------ Discard reference
            else:
                self.createFileShotWindow.close()  # ------ Close window
                self.createFileShotWindow = None  # ------ Discard reference
        self.ui.buttonCreateFilesSequences.clicked.connect(openWindow_createShotFile)

        def openWindow_createSequence():  # ------ Show Create Asset window
            if self.createSequenceWindow is None:
                self.createSequenceWindow = CreateSequence()
                self.createSequenceWindow.show()
                self.createSequenceWindow = None  # ------ Discard reference
            else:
                self.createSequenceWindow.close()  # ------ Close window
                self.createSequenceWindow = None  # ------ Discard reference
        self.ui.buttonCreateSequence.clicked.connect(openWindow_createSequence)

        def openWindow_createShot():  # ------ Show Create Asset window
            if self.createShotWindow is None:
                self.createShotWindow = CreateShot()
                self.createShotWindow.show()
                self.createShotWindow = None  # ------ Discard reference
            else:
                self.createShotWindow.close()  # ------ Close window
                self.createShotWindow = None  # ------ Discard reference
        self.ui.buttonCreateShots.clicked.connect(openWindow_createShot)

        def openDirectories_Sequence():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)
            if CIOXO_SHOT == "shot" or os.path.isdir(shotPath) is False:
                shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)
                os.startfile(shotPath)
                if CIOXO_SEQUENCE == "sequence" or os.path.isdir(shotPath) is False:
                    self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                    self.ui.labelInformations.setText(">>> No sequence selected!")
            else:
                os.startfile(shotPath)
                self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
                self.ui.labelInformations.setText(">>> Opening Directory")
        self.ui.buttonDirectorySequences.clicked.connect(openDirectories_Sequence)

        def openTab_filesSequences():
            self.ui.tabWidget.setCurrentIndex(tabFilesSequences)
            self.ui.tabWidget.setTabEnabled(tabFilesSequences, True)
        self.ui.buttonHoudiniSequences.clicked.connect(openTab_filesSequences)
        self.ui.buttonMayaSequences.clicked.connect(openTab_filesSequences)
        self.ui.buttonSubstanceSequences.clicked.connect(openTab_filesSequences)
        self.ui.buttonNukeSequences.clicked.connect(openTab_filesSequences)
        self.ui.buttonAfterEffectsSequences.clicked.connect(openTab_filesSequences)
        self.ui.buttonPhotoshopSequences.clicked.connect(openTab_filesSequences)

        def previous_sequences():
            self.ui.tabWidget.setCurrentIndex(tabProjects)
        self.ui.pushButtonPreviousSequences.clicked.connect(previous_sequences)

# ---------------------------------#
# ------ FILES SEQUENCES TAB ------#
# ---------------------------------#

        self.ui.listFilesSequences.addItems(["Select a shot"])

        def changeTitle_SequenceShot():
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            self.ui.labelWelcomeFilesSequences.setText(CIOXO_SEQUENCE + " - " + CIOXO_SHOT)
        self.ui.listSequences.itemSelectionChanged.connect(changeTitle_SequenceShot)
        self.ui.listShots.itemSelectionChanged.connect(changeTitle_SequenceShot)

        def defineCioxoVariable_HOUDINI():
            os.environ["CIOXO_SOFTWARE"] = "houdini"
        self.ui.buttonHoudiniSequences.clicked.connect(defineCioxoVariable_HOUDINI)

        def defineCioxoVariable_MAYA():
            os.environ["CIOXO_SOFTWARE"] = "maya"
        self.ui.buttonMayaSequences.clicked.connect(defineCioxoVariable_MAYA)

        def defineCioxoVariable_SUBSTANCE():
            os.environ["CIOXO_SOFTWARE"] = "substance"
        self.ui.buttonSubstanceSequences.clicked.connect(defineCioxoVariable_SUBSTANCE)

        def defineCioxoVariable_NUKE():
            os.environ["CIOXO_SOFTWARE"] = "nuke"
        self.ui.buttonNukeSequences.clicked.connect(defineCioxoVariable_NUKE)

        def defineCioxoVariable_AFTEREFFECTS():
            os.environ["CIOXO_SOFTWARE"] = "afterEffects"
        self.ui.buttonAfterEffectsSequences.clicked.connect(defineCioxoVariable_AFTEREFFECTS)

        def defineCioxoVariable_PHOTOSHOP():
            os.environ["CIOXO_SOFTWARE"] = "photoshop"
        self.ui.buttonPhotoshopSequences.clicked.connect(defineCioxoVariable_PHOTOSHOP)

        def changeTitle_SequenceShotSoftware():
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            self.ui.labelWelcomeFilesSequences.setText(CIOXO_SEQUENCE + " - " + CIOXO_SHOT + " | " + CIOXO_SOFTWARE)
        self.ui.listSequences.itemSelectionChanged.connect(changeTitle_SequenceShotSoftware)
        self.ui.listShots.itemSelectionChanged.connect(changeTitle_SequenceShotSoftware)
        self.ui.buttonHoudiniSequences.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.buttonMayaSequences.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.buttonSubstanceSequences.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.buttonNukeSequences.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.buttonAfterEffectsSequences.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.buttonPhotoshopSequences.clicked.connect(changeTitle_SequenceShotSoftware)

        def changeTabTitle_SequenceShotSoftware():
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            self.ui.tabWidget.setTabText(tabFilesSequences, CIOXO_SEQUENCE + " - " + CIOXO_SHOT + " | " + CIOXO_SOFTWARE)
        self.ui.buttonHoudiniSequences.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.buttonMayaSequences.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.buttonSubstanceSequences.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.buttonNukeSequences.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.buttonAfterEffectsSequences.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.buttonPhotoshopSequences.clicked.connect(changeTabTitle_SequenceShotSoftware)

        def fillList_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            filesPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE)
            self.ui.listFilesSequences.clear()

            # ------ Houdini
            if CIOXO_SOFTWARE == "houdini":
                # ----- Look for disciplines folders
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
                    self.ui.listFilesSequences.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(houdiniExtension):
                            filesList.append(files)
                            self.ui.listFilesSequences.addItem(files)
                        else:
                            pass

            # ------ Maya
            if CIOXO_SOFTWARE == "maya":
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
                    self.ui.listFilesSequences.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(mayaExtension):
                            filesList.append(files)
                            self.ui.listFilesSequences.addItem(files)
                        else:
                            pass

            # ------ Substance
            if CIOXO_SOFTWARE == "substance":
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(os.path.join(filesPath, "workspaces")):
                    foldersDisciplineList.append(folderDisciplines)
                    # ------ Add delimiter for categories to list
                    delimiter = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.listFilesSequences.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(substanceExtension):
                            filesList.append(files)
                            self.ui.listFilesSequences.addItem(files)
                        else:
                            pass

            # ------ Nuke
            if CIOXO_SOFTWARE == "nuke":
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
                    self.ui.listFilesSequences.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(nukeExtension):
                            filesList.append(files)
                            self.ui.listFilesSequences.addItem(files)
                        else:
                            pass

            # ------ After Effects
            if CIOXO_SOFTWARE == "afterEffects":
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(os.path.join(filesPath, "workspaces")):
                    foldersDisciplineList.append(folderDisciplines)
                    # ------ Add delimiter for categories to list
                    delimiter = QtWidgets.QListWidgetItem()
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.listFilesSequences.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(afterEffectsExtension):
                            filesList.append(files)
                            self.ui.listFilesSequences.addItem(files)
                        else:
                            pass

            # ------ Photoshop
            if CIOXO_SOFTWARE == "photoshop":
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
                    self.ui.listFilesSequences.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(photoshopExtension):
                            filesList.append(files)
                            self.ui.listFilesSequences.addItem(files)
                        else:
                            pass
        self.ui.buttonHoudiniSequences.clicked.connect(fillList_filesSequences)
        self.ui.buttonMayaSequences.clicked.connect(fillList_filesSequences)
        self.ui.buttonSubstanceSequences.clicked.connect(fillList_filesSequences)
        self.ui.buttonNukeSequences.clicked.connect(fillList_filesSequences)
        self.ui.buttonAfterEffectsSequences.clicked.connect(fillList_filesSequences)
        self.ui.buttonPhotoshopSequences.clicked.connect(fillList_filesSequences)
        self.ui.buttonReloadFilesSequences.clicked.connect(fillList_filesSequences)

        def reloadFiles_filesSequences():
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Reloaded")
        self.ui.buttonReloadFilesSequences.clicked.connect(reloadFiles_filesSequences)

        def defineCioxoVariable_FILE():
            activeListItem = [item.text() for item in self.ui.listFilesSequences.selectedItems()]
            listToString = ''.join([str(elem) for elem in activeListItem])
            os.environ["CIOXO_FILE"] = listToString
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            os.environ["CIOXO_DISCIPLINE"] = CIOXO_FILE.lower().split("_")[3]
            CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> File variable defined on: " + CIOXO_FILE + "\n>>> Discipline variable defined on: " + CIOXO_DISCIPLINE)
        self.ui.listFilesSequences.itemSelectionChanged.connect(defineCioxoVariable_FILE)

        def loadThumbnail_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailFilesSequences.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailFilesSequences.setText("No Thumbnail found")
        self.ui.listFilesSequences.itemSelectionChanged.connect(loadThumbnail_filesSequences)
        self.ui.buttonRefreshThumbnailFilesSequences.clicked.connect(loadThumbnail_filesSequences)

        def openWindow_createThumbnailFiles():
            if self.createThumbnailWindowFile is None:
                self.createThumbnailWindowFile = CreateThumbnailFile()
                self.createThumbnailWindowFile.show()
                self.createThumbnailWindowFile = None  # ------ Discard reference
            else:
                self.createThumbnailWindowFile.close()  # ------ Close window
                self.createThumbnailWindowFile = None  # ------ Discard reference
        self.ui.buttonChargeThumbnailFilesSequences.clicked.connect(openWindow_createThumbnailFiles)

        def deleteThumbnail_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                self.ui.labelInformations.setText(">>> Thumbnail deleted")
            else:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No thumbnail found!")
        self.ui.buttonDeleteThumbnailFilesSequences.clicked.connect(deleteThumbnail_filesSequences)

        def showComment_filesSequences():
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
                self.ui.labelCommentFilesSequences.setText(comment)
            else:
                self.ui.labelCommentFilesSequences.setText("No comment found")
        self.ui.listFilesSequences.itemSelectionChanged.connect(showComment_filesSequences)

        def openFile_filesSequences():
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
                os.startfile(filesPath)
                self.ui.labelInformations.setText(">>> Opening " + filesPath)
        self.ui.buttonOpenFilesSequences.clicked.connect(openFile_filesSequences)

        def clearList_filesSequences():

            # ------ Reset button colors
            self.ui.buttonHoudiniSequences.setStyleSheet(buttonGrey)
            self.ui.buttonMayaSequences.setStyleSheet(buttonGrey)
            self.ui.buttonSubstanceSequences.setStyleSheet(buttonGrey)
            self.ui.buttonNukeSequences.setStyleSheet(buttonGrey)
            self.ui.buttonAfterEffectsSequences.setStyleSheet(buttonGrey)
            self.ui.buttonPhotoshopSequences.setStyleSheet(buttonGrey)
            # ------ Clear
            self.ui.tabWidget.setTabText(tabFilesSequences, "Shot Files")
            self.ui.tabWidget.setTabEnabled(tabFilesSequences, False)
            self.ui.listFilesSequences.clear()
        self.ui.listProjects.itemSelectionChanged.connect(clearList_filesSequences)

        def clearList_filesSequencesSecondary():
            # ------ Clear
            self.ui.tabWidget.setTabText(tabFilesSequences, "Shot Files")
            self.ui.tabWidget.setTabEnabled(tabFilesSequences, False)
            self.ui.listFilesSequences.clear()
        self.ui.listSequences.itemSelectionChanged.connect(clearList_filesSequencesSecondary)
        self.ui.listShots.itemSelectionChanged.connect(clearList_filesSequencesSecondary)

        def openDirectories_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            pathFile = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces")
            os.startfile(pathFile)
            self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
            self.ui.labelInformations.setText(">>> Opening Directory")
        self.ui.buttonDirectoryFilesSequences.clicked.connect(openDirectories_filesSequences)

        def previous_filesSequences():
            self.ui.tabWidget.setCurrentIndex(tabSequences)
        self.ui.pushButtonPreviousFilesSequences.clicked.connect(previous_filesSequences)

# ---------------------#
# ------ GENERAL ------#
# ---------------------#

        def openDocumentation():
            pathDocumentation = "https://www.google.fr"
            os.startfile(pathDocumentation)
        self.ui.buttonHelp.clicked.connect(openDocumentation)

        def openPlanning():
            if os.getenv("CIOXO_PROJECT") == "project":
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
                planningPath = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_planning.url")
                if os.path.isfile(planningPath):
                    os.startfile(planningPath)
                    self.ui.labelInformations.setStyleSheet(labelInformationsWhite)
                    self.ui.labelInformations.setText(">>> Opening Planning")
                else:
                    self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                    self.ui.labelInformations.setText(">>> No planning for this project!")
        self.ui.buttonPlanningProjects.clicked.connect(openPlanning)

        # ------ Define username
        USERNAME = os.getenv("USERNAME")
        self.ui.labelUsername.setText(USERNAME)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Project Manager")


# ------ CREATE PROJECT
class CreateProject(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateProject()
        self.ui.setupUi(self)

        self.ui.lineEditInput.setInputMask("AAA")

        def createDirectory_project():
            projectInput = self.ui.lineEditInput.text()
            pathExists = True
            while pathExists:
                if os.path.isdir(os.path.join(rootDir, projectInput)):
                    self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                    self.ui.labelInformations.setText(">>> Project already exists!")
                    break
                else:
                    self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                    self.ui.labelInformations.setText(">>> Project " + projectInput + " created - You can now close the window")
                    self.ui.buttonCancel.setText("Close")
                    toDirectory = os.path.join(rootDir, projectInput)
                    copy_tree(projectTemplate, toDirectory)
                    pathExists = False
        self.ui.buttonOk.clicked.connect(createDirectory_project)

        def writeResolution_project():
            projectInput = self.ui.lineEditInput.text()
            self.ui.lineEditResolutionX.setInputMask("99900")
            resolutionXInput = self.ui.lineEditResolutionX.text()
            self.ui.lineEditResolutionY.setInputMask("99900")
            resolutionYInput = self.ui.lineEditResolutionY.text()
            with open(os.path.join(rootDir, projectInput, "." + projectInput + "_resolution.txt"), 'w') as resolution:
                resolution.write(resolutionXInput + "_" + resolutionYInput)
        self.ui.buttonOk.clicked.connect(writeResolution_project)

        def writeFPS_project():
            projectInput = self.ui.lineEditInput.text()
            self.ui.lineEditFPS.setInputMask("99000")
            fpsInput = self.ui.lineEditFPS.text()
            with open(os.path.join(rootDir, projectInput, "." + projectInput + "_fps.txt"), 'w') as fps:
                fps.write(fpsInput)
        self.ui.buttonOk.clicked.connect(writeFPS_project)

        def closeWindow_createProject():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createProject)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Project")

    # END


# ------ CREATE SEQUENCE
class CreateSequence(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateSequence()
        self.ui.setupUi(self)

        self.ui.lineEditInput.setInputMask("seqNNN")

        def createDirectory_sequence():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            sequencePath = os.path.join(rootDir, CIOXO_PROJECT)
            sequenceInput = self.ui.lineEditInput.text()
            if CIOXO_PROJECT == "project" or os.path.isdir(sequencePath) is None:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                pathExists = True
                while pathExists:
                    if os.path.isdir(os.path.join(sequencePath, sequenceInput)):
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> Sequence already exists!")
                        break
                    else:
                        self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                        self.ui.labelInformations.setText(
                            ">>> Sequence " + sequenceInput + " created - You can now close the window")
                        self.ui.buttonCancel.setText("Close")
                        toDirectory = os.path.join(sequencePath, sequenceInput)
                        copy_tree(sequenceTemplate, toDirectory)
                        pathExists = False
        self.ui.buttonOk.clicked.connect(createDirectory_sequence)

        def closeWindow_createSequence():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createSequence)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Sequence")


# ------ CREATE SHOT
class CreateShot(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateShot()
        self.ui.setupUi(self)

        self.ui.lineEditInput.setText("sh")

        def createDirectory_shot():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)
            shotInput = self.ui.lineEditInput.text()
            # ------ Check if directory already exists
            pathExists = True
            while pathExists:
                if os.path.isdir(os.path.join(shotPath, shotInput)):
                    self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                    self.ui.labelInformations.setText(">>> Shot already exists!")
                    break
                else:
                    if CIOXO_SEQUENCE == "sequence" or os.path.isdir(shotPath) is False:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> No sequence selected!")
                    else:
                        self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                        self.ui.labelInformations.setText(
                            ">>> Shot " + shotInput + " created - You can now close the window")
                        self.ui.buttonCancel.setText("Close")
                        # ------ Copy template to destination
                        toDirectory = os.path.join(shotPath, shotInput)
                        copy_tree(shotTemplate, toDirectory)
                        pathExists = False
                        # ------ Create base files file when creating shot
                        filesPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, shotInput)

                        # ------ Houdini
                        if self.ui.radioButtonHoudini.isChecked():
                            filesPathHoudini = os.path.join(filesPath, "houdini", "workspaces", "none")
                            os.makedirs(filesPathHoudini, exist_ok=True)
                            fileHoudini = CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + shotInput + "_none_v001" + ".hip"
                            with open(os.path.join(filesPathHoudini, fileHoudini), 'w'):
                                pass
                        else:
                            pass

                        # ------ Maya
                        if self.ui.radioButtonMaya.isChecked():
                            filesPathMaya = os.path.join(filesPath, "maya", "workspaces", "none")
                            os.makedirs(filesPathMaya, exist_ok=True)
                            fileMaya = CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + shotInput + "_none_v001" + ".mb"
                            with open(os.path.join(filesPathMaya, fileMaya), 'w'):
                                pass
                        else:
                            pass

                        # ------ Substance
                        if self.ui.radioButtonSubstance.isChecked():
                            filesPathSubstance = os.path.join(filesPath, "substance", "workspaces", "none")
                            os.makedirs(filesPathSubstance, exist_ok=True)
                            fileSubstance = CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + shotInput + "_none_v001" + ".spp"
                            with open(os.path.join(filesPathSubstance, fileSubstance), 'w'):
                                pass
                        else:
                            pass

                        # ------ Nuke
                        if self.ui.radioButtonNuke.isChecked():
                            filesPathNuke = os.path.join(filesPath, "nuke", "workspaces", "none")
                            os.makedirs(filesPathNuke, exist_ok=True)
                            fileNuke = CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + shotInput + "_none_v001" + ".nk"
                            with open(os.path.join(filesPathNuke, fileNuke), 'w'):
                                pass
                        else:
                            pass

                        # ------ After Effects
                        if self.ui.radioButtonAfterEffects.isChecked():
                            filesPathAfterEffects = os.path.join(filesPath, "afterEffects", "workspaces", "none")
                            os.makedirs(filesPathAfterEffects, exist_ok=True)
                            fileAfterEffects = CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + shotInput + "_none_v001" + ".aep"
                            with open(os.path.join(filesPathAfterEffects, fileAfterEffects), 'w'):
                                pass
                        else:
                            pass

                        # ------ Photoshop
                        if self.ui.radioButtonPhotoshop.isChecked():
                            filesPathPhotoshop = os.path.join(filesPath, "photoshop", "workspaces", "none")
                            os.makedirs(filesPathPhotoshop, exist_ok=True)
                            filePhotoshop = CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + shotInput + "_none_v001" + ".psd"
                            with open(os.path.join(filesPathPhotoshop, filePhotoshop), 'w'):
                                pass
                        else:
                            pass
        self.ui.buttonOk.clicked.connect(createDirectory_shot)

        def writeFrameRange_shot():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)
            shotInput = self.ui.lineEditInput.text()
            self.ui.lineEditFrameStart.setInputMask("99900")
            frameStartInput = self.ui.lineEditFrameStart.text()
            self.ui.lineEditFrameEnd.setInputMask("99900")
            frameEndInput = self.ui.lineEditFrameEnd.text()
            with open(os.path.join(shotPath, shotInput, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + shotInput + "_frameRange.txt"), 'w') as f:
                f.write(frameStartInput + "_" + frameEndInput)
        self.ui.buttonOk.clicked.connect(writeFrameRange_shot)

        def closeWindow_createShot():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createShot)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Shot")


# ------ CREATE ASSET
class CreateAsset(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateAsset()
        self.ui.setupUi(self)

        def createDirectory_asset():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            assetsPath = os.path.join(rootDir, CIOXO_PROJECT)
            assetInput = self.ui.lineEditInput.text()
            if CIOXO_PROJECT == "project" or os.path.isdir(assetsPath) is None:
                self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                self.ui.labelInformations.setText(">>> No project selected!")
            else:
                pathExists = True
                while pathExists:
                    if os.path.isdir(os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_PROJECT + "_" + assetInput)):
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> Asset already exists!")
                        break
                    else:
                        self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                        self.ui.labelInformations.setText(">>> Asset " + assetInput + " created - You can now close the window")
                        self.ui.buttonCancel.setText("Close")
                        # ------ Copy template to destination
                        toDirectory = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_PROJECT + "_" + assetInput)
                        copy_tree(assetTemplate, toDirectory)
                        pathExists = False
                        # ------ Create base files file when creating Asset
                        filesPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_PROJECT + "_" + assetInput)

                        # ------ Houdini
                        if self.ui.radioButtonHoudini.isChecked():
                            filesPathHoudini = os.path.join(filesPath, "houdini", "workspaces", "none")
                            os.makedirs(filesPathHoudini, exist_ok=True)
                            fileHoudini = CIOXO_PROJECT + "_" + assetInput + "_none_v001" + ".hip"
                            with open(os.path.join(filesPathHoudini, fileHoudini), 'w'):
                                pass
                        else:
                            pass

                        # ------ Maya
                        if self.ui.radioButtonMaya.isChecked():
                            filesPathMaya = os.path.join(filesPath, "maya", "workspaces", "none")
                            os.makedirs(filesPathMaya, exist_ok=True)
                            fileMaya = CIOXO_PROJECT + "_" + assetInput + "_none_v001" + ".mb"
                            with open(os.path.join(filesPathMaya, fileMaya), 'w'):
                                pass
                        else:
                            pass

                        # ------ Substance
                        if self.ui.radioButtonSubstance.isChecked():
                            filesPathSubstance = os.path.join(filesPath, "substance", "workspaces", "none")
                            os.makedirs(filesPathSubstance, exist_ok=True)
                            fileSubstance = CIOXO_PROJECT + "_" + assetInput + "_none_v001" + ".spp"
                            with open(os.path.join(filesPathSubstance, fileSubstance), 'w'):
                                pass
                        else:
                            pass

                        # ------ Nuke
                        if self.ui.radioButtonNuke.isChecked():
                            filesPathNuke = os.path.join(filesPath, "nuke", "workspaces", "none")
                            os.makedirs(filesPathNuke, exist_ok=True)
                            fileNuke = CIOXO_PROJECT + "_" + assetInput + "_none_v001" + ".nk"
                            with open(os.path.join(filesPathNuke, fileNuke), 'w'):
                                pass
                        else:
                            pass
        self.ui.buttonOk.clicked.connect(createDirectory_asset)

        def closeWindow_createAsset():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createAsset)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Asset")


# ------ CREATE FILE SHOT
class CreateFileShot(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateFile()
        self.ui.setupUi(self)

        # ------ Window variables
        self.ui.labelActualProject.setText("  " + os.getenv("CIOXO_PROJECT"))
        self.ui.labelActualSequence.setText("  " + os.getenv("CIOXO_SEQUENCE"))
        self.ui.labelActualShot.setText("  " + os.getenv("CIOXO_SHOT"))
        self.ui.plainTextEditComment.setPlaceholderText("Comment...")

        def createDirectory_fileShot():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            disciplineInput = self.ui.comboBoxDiscipline.currentText()
            os.environ["CIOXO_DISCIPLINE"] = disciplineInput
            CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")
            # ------ Window variable
            self.ui.labelCreateFile.setText("Create File | " + CIOXO_SOFTWARE)
            self.ui.lineEditVersion.setInputMask("999")
            versionInput = self.ui.lineEditVersion.text()
            # ------ Paths
            filePath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE)
            fileName = CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_" + CIOXO_DISCIPLINE + "_v" + versionInput
            fileCommentPath = os.path.join(filePath, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_" + CIOXO_DISCIPLINE + "_v" + versionInput + "_comment.txt")
            comment = self.ui.plainTextEditComment.toPlainText()
            # ------ Create file
            # ------ Houdini
            if CIOXO_SOFTWARE == "houdini":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".hip")) is True or os.path.isfile(os.path.join(filePath, fileName + ".hiplc")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".hip"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created\n>>> Comment created - You can now close the window")

            # ------ Maya
            elif CIOXO_SOFTWARE == "maya":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".mb")) is True or os.path.isfile(os.path.join(filePath, fileName + ".ma")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".mb"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created\n>>> Comment created - You can now close the window")

            # ------ Substance
            elif CIOXO_SOFTWARE == "substance":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".spp")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".spp"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created\n>>> Comment created - You can now close the window")

            # ------ Nuke
            elif CIOXO_SOFTWARE == "nuke":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".nk")) is True or os.path.isfile(os.path.join(filePath, fileName + ".nknc")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".nk"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created\n>>> Comment created - You can now close the window")

            # ------ After Effects
            elif CIOXO_SOFTWARE == "afterEffects":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".aep")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".aep"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created\n>>> Comment created - You can now close the window")
                            pass
                        pathExists = False

            # ------ Photoshop
            elif CIOXO_SOFTWARE == "photoshop":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".psd")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".psd"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(">>> file created\n>>> Comment created - You can now close the window")
        self.ui.buttonOk.clicked.connect(createDirectory_fileShot)

        def closeWindow_createFileShot():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createFileShot)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create File")


# ------ CREATE FILE ASSET
class CreateFileAsset(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateFile()
        self.ui.setupUi(self)

        # ------ Window variables
        self.ui.labelActualProject.setText("  " + os.getenv("CIOXO_PROJECT"))
        self.ui.labelActualSequence.setText("  assets")
        self.ui.labelActualSequence.setMaximumSize(2000, 21)
        self.ui.labelActualShot.close()
        self.ui.plainTextEditComment.setPlaceholderText("Comment...")

        def createDirectory_fileShot():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            disciplineInput = self.ui.comboBoxDiscipline.currentText()
            os.environ["CIOXO_DISCIPLINE"] = disciplineInput
            CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")
            # ------ Window variables
            self.ui.labelCreateFile.setText("Create File | " + CIOXO_SOFTWARE)
            self.ui.lineEditVersion.setInputMask("999")
            versionInput = self.ui.lineEditVersion.text()
            # ------ Paths
            filePath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE)
            fileName = CIOXO_ASSET + "_" + CIOXO_DISCIPLINE + "_v" + versionInput
            fileCommentPath = os.path.join(filePath, "." + CIOXO_ASSET + "_" + CIOXO_DISCIPLINE + "_v" + versionInput + "_comment.txt")
            comment = self.ui.plainTextEditComment.toPlainText()
            # ------ Create file
            # ------ Houdini
            if CIOXO_SOFTWARE == "houdini":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".hip")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".hiplc")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".hip"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Maya
            elif CIOXO_SOFTWARE == "maya":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".mb")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".ma")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".mb"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Substance
            elif CIOXO_SOFTWARE == "substance":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".spp")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".spp"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Nuke
            elif CIOXO_SOFTWARE == "nuke":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".nk")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".nknc")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".nk"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ After Effects
            elif CIOXO_SOFTWARE == "afterEffects":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".aep")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".aep"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Photoshop
            elif CIOXO_SOFTWARE == "photoshop":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".psd")) is True:
                        self.ui.labelInformations.setStyleSheet(labelInformationsRed)
                        self.ui.labelInformations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".psd"), 'w'):
                            pass
                        self.ui.buttonCancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
                            self.ui.labelInformations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")
        self.ui.buttonOk.clicked.connect(createDirectory_fileShot)

        def closeWindow_createFileShot():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createFileShot)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create File")


# ------ CREATE THUMBNAIL PROJECT
class CreateThumbnailProject(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateThumbnail()
        self.ui.setupUi(self)

        def browseThumbnail_project():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/", "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.labelFile.setText(fileName)
        self.ui.buttonBrowse.clicked.connect(browseThumbnail_project)

        def openWindow_createThumbnail_project():
            # ------ CIOXO VARIABLES
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            # ------ Thumbnail project paths
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_thumbnail.png")
            # ------ Save image as thumbnail
            imageFile = self.ui.labelFile.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.buttonCancel.setText("Close")
            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
            self.ui.labelInformations.setText(">>> Thumbnail created - You can now close the window")
        self.ui.buttonOk.clicked.connect(openWindow_createThumbnail_project)

        def closeWindow_createThumbnail_project():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createThumbnail_project)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Thumbnail")


# ------ CREATE THUMBNAIL ASSET
class CreateThumbnailAsset(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateThumbnail()
        self.ui.setupUi(self)

        def browseThumbnail_asset():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/", "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.labelFile.setText(fileName)
        self.ui.buttonBrowse.clicked.connect(browseThumbnail_asset)

        def openWindow_createThumbnail_asset():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            # ------ Thumbnail assets paths
            assetPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET)
            pathThumbnail = os.path.join(assetPath, "." + CIOXO_PROJECT + "_" + CIOXO_ASSET + "_thumbnail.png")
            # ------ Save image as thumbnail
            imageFile = self.ui.labelFile.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.buttonCancel.setText("Close")
            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
            self.ui.labelInformations.setText(">>> Thumbnail created - You can now close the window")
        self.ui.buttonOk.clicked.connect(openWindow_createThumbnail_asset)

        def closeWindow_createThumbnail_asset():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createThumbnail_asset)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Thumbnail")


# ------ CREATE THUMBNAIL FILE ASSET
class CreateThumbnailFileAsset(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateThumbnail()
        self.ui.setupUi(self)

        def browseThumbnail_fileAsset():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/", "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.labelFile.setText(fileName)
        self.ui.buttonBrowse.clicked.connect(browseThumbnail_fileAsset)

        def openWindow_createThumbnail_fileAsset():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[2]
            # ------ Thumbnail files assets paths
            filePath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE)
            pathThumbnail = os.path.join(filePath, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            # ------ Save image as thumbnail
            imageFile = self.ui.labelFile.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.buttonCancel.setText("Close")
            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
            self.ui.labelInformations.setText(">>> Thumbnail created - You can now close the window")
        self.ui.buttonOk.clicked.connect(openWindow_createThumbnail_fileAsset)

        def closeWindow_createThumbnail_fileAsset():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createThumbnail_fileAsset)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Thumbnail")


# ------ CREATE THUMBNAIL SHOT
class CreateThumbnailShot(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateThumbnail()
        self.ui.setupUi(self)

        def browseThumbnail_shot():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/", "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.labelFile.setText(fileName)
        self.ui.buttonBrowse.clicked.connect(browseThumbnail_shot)

        def openWindow_createThumbnail_shot():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            # ------ Thumbnail shots paths
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)
            pathThumbnail = os.path.join(shotPath, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            # ------ Save thumbnail
            imageFile = self.ui.labelFile.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.buttonCancel.setText("Close")
            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
            self.ui.labelInformations.setText(">>> Thumbnail created - You can now close the window")
        self.ui.buttonOk.clicked.connect(openWindow_createThumbnail_shot)

        def closeWindow_createThumbnail_shot():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createThumbnail_shot)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Thumbnail")


# ------ CREATE THUMBNAIL FILE
class CreateThumbnailFile(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_CreateThumbnail()
        self.ui.setupUi(self)

        def browseThumbnail_filesSequences():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/", "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.labelFile.setText(fileName)
        self.ui.buttonBrowse.clicked.connect(browseThumbnail_filesSequences)

        def openWindow_createThumbnail_filesSequences():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]
            # ------- Thumbnail files sequences paths
            filePath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE)
            pathThumbnail = os.path.join(filePath, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            # ------- Save thumbnail
            imageFile = self.ui.labelFile.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.buttonCancel.setText("Close")
            self.ui.labelInformations.setStyleSheet(labelInformationsGreen)
            self.ui.labelInformations.setText(">>> Thumbnail created - You can now close the window")
        self.ui.buttonOk.clicked.connect(openWindow_createThumbnail_filesSequences)

        def closeWindow_createThumbnail_filesSequences():
            self.close()
        self.ui.buttonCancel.clicked.connect(closeWindow_createThumbnail_filesSequences)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Thumbnail")


# ------ SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main = ProjectManager()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # ------ Set UI Definitions
        UIFunctionsSplashScreen.uiDefinitions(self)

        # ------ Start QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # ------ Timer in milliseconds (Increase to make Screen Splash last longer)
        self.timer.start(10)

        # ------ Change Loading Texts
        QtCore.QTimer.singleShot(0, lambda: self.ui.labelLoading.setText("Loading Preferences"))
        QtCore.QTimer.singleShot(1000, lambda: self.ui.labelLoading.setText("Communicating with CG gods"))
        QtCore.QTimer.singleShot(1800, lambda: self.ui.labelLoading.setText("Ray Tracing your mum's face"))
        QtCore.QTimer.singleShot(2250, lambda: self.ui.labelLoading.setText("Loading Database"))

        # ------ Change Version
        self.ui.labelVersion.setText(version)

        # ------ Show Screen Splash
        self.show()

    # ------ App functions
    def progress(self):
        global counter

        # ------ Set value to Progress Bar
        self.ui.progressBarLoading.setValue(counter)

        # Close Screen Splash and open Project Manager
        if counter > 100:
            # ------ Stop Timer
            self.timer.stop()

            # ------ Show Project Manager
            self.main.show()
            # self.main.showMaximized()

            # ------ Close Splash Screen
            self.close()

        # ------ Increase Counter
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
