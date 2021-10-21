from ui_cioxo_splashScreen_functions import *
from ui_cioxo_main_projectManager import Ui_cioxo_projectManager
from ui_cioxo_createProject import Ui_cioxo_createProject
from ui_cioxo_createSequence import Ui_cioxo_createSequence
from ui_cioxo_createShot import Ui_cioxo_createShot
from ui_cioxo_createAsset import Ui_cioxo_createAsset
from ui_cioxo_createFile import Ui_cioxo_createFile
from ui_cioxo_createThumbnail import Ui_cioxo_createTumbnail
from ui_cioxo_splashScreen import Ui_cioxo_splashScreen
import ui_cioxo_QtResources_rc

# ------ Import necessary libraries
import os
import sys
from PIL import Image
from distutils.dir_util import copy_tree
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import *

# ------ Cioxo - Project Manager window features


# ------ Globals
counter = 0
version = str("v0.0.1-alpha")
label_informationsRed = ("QLabel\n"
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
# ------ Check if Cioxo - Define Root has created the .cioxo folder
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
        self.ui = Ui_cioxo_projectManager()
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
        self.ui.tab_widget.setTabsClosable(False)
        self.ui.tab_widget.setTabEnabled(tabProjects, True)
        self.ui.tab_widget.setTabEnabled(tabAssets, True)
        self.ui.tab_widget.setTabEnabled(tabFilesAssets, False)
        self.ui.tab_widget.setTabEnabled(tabSequences, True)
        self.ui.tab_widget.setTabEnabled(tabFilesSequences, False)

        # ------ Buttons state at opening
        self.ui.button_houdiniAsset.setEnabled(False)
        self.ui.button_mayaAsset.setEnabled(False)
        self.ui.button_substanceAsset.setEnabled(False)
        self.ui.button_nukeAsset.setEnabled(False)
        self.ui.button_houdiniSequence.setEnabled(False)
        self.ui.button_mayaSequence.setEnabled(False)
        self.ui.buttonSubstanceSequences.setEnabled(False)
        self.ui.button_nukeSequences.setEnabled(False)
        self.ui.button_afterEffectsSequence.setEnabled(False)
        self.ui.button_photoshopSequence.setEnabled(False)

        # ------ Start Cioxo on project tab
        self.ui.tab_widget.setCurrentIndex(tabProjects)

        # ------ Add items from rootDir in listWidget projects
        for file in os.listdir(rootDir):
            if len(file) <= 3:
                self.ui.list_project.addItems(file.split())

        # ---------------------------#
        # ------ PROJECTS TAB ------ #
        # ---------------------------#

        def defineCioxoVariable_PROJECT():
            activeListItem = [item.text() for item in self.ui.list_project.selectedItems()]
            listToString = ''.join([str(elem) for elem in activeListItem])
            # ------ Define CIOXO_PROJECT environment variable on item selected
            os.environ["CIOXO_PROJECT"] = listToString
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Project variable defined on: " + CIOXO_PROJECT)

        self.ui.list_project.itemSelectionChanged.connect(defineCioxoVariable_PROJECT)

        def reloadList_projects():
            self.ui.list_project.clear()
            for fileProject in os.listdir(rootDir):
                if len(fileProject) <= 3:
                    self.ui.list_project.addItems(fileProject.split())
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Reloaded")

        self.ui.button_reloadProject.clicked.connect(reloadList_projects)

        def loadThumbnail_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.label_thumbnailProject.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.label_thumbnailProject.setText("No Thumbnail found")

        self.ui.list_project.itemSelectionChanged.connect(loadThumbnail_projects)
        self.ui.button_refreshThumbnailProjects.clicked.connect(loadThumbnail_projects)

        def deleteThumbnail_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                self.ui.label_informations.setText(">>> Thumbnail deleted")
            else:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No thumbnail found!")

        self.ui.button_deleteThumbnailProjects.clicked.connect(deleteThumbnail_projects)

        def openCreateThumbnail_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            if CIOXO_PROJECT == "project" or os.path.isdir(os.path.join(rootDir, CIOXO_PROJECT)) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                if self.createThumbnailWindowProject is None:
                    self.createThumbnailWindowProject = CreateThumbnailProject()
                    self.createThumbnailWindowProject.show()
                    self.createThumbnailWindowProject = None  # ------ Discard reference
                else:
                    self.createThumbnailWindowProject.close()  # ------ Close window
                    self.createThumbnailWindowProject = None  # ------ Discard reference

        self.ui.button_chargeThumbnailProjects.clicked.connect(openCreateThumbnail_projects)

        def openAssetsManager():  # ------ Show Assets Manager tab
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            projectPath = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(projectPath) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                self.ui.tab_widget.setCurrentIndex(tabAssets)

        self.ui.button_asset.clicked.connect(openAssetsManager)

        def openSequencesManager():  # ------ Show Sequences Manager tab
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            projectPath = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(projectPath) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                self.ui.tab_widget.setCurrentIndex(tabSequences)

        self.ui.button_sequence.clicked.connect(openSequencesManager)

        def openCreate_projects():  # ------ Show Create Asset window
            if self.createProjectWindow is None:
                self.createProjectWindow = CreateProject()
                self.createProjectWindow.show()
                self.createProjectWindow = None  # ------ Discard reference
            else:
                self.createProjectWindow.close()  # ------ Close window
                self.createProjectWindow = None  # ------ Discard reference

        self.ui.button_createProject.clicked.connect(openCreate_projects)

        def setResolution_project():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.lineEdit_resolutionX.setInputMask("99900")
            resolutionXInput = self.ui.lineEdit_resolutionX.text()
            self.ui.lineEdit_resolutionY.setInputMask("99900")
            resolutionYInput = self.ui.lineEdit_resolutionY.text()
            with open(os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_resolution.txt"), 'w') as f:
                f.write(resolutionXInput + "_" + resolutionYInput)
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Project resolution changed")

        self.ui.button_validateResolution.clicked.connect(setResolution_project)

        def getResolution_project():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            resolutionFile = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_resolution.txt")
            if os.path.isfile(resolutionFile):
                with open(resolutionFile) as f:
                    resolution = f.readline()
                resolutionX = resolution.split("_")[0]
                resolutionY = resolution.split("_")[1]
                self.ui.lineEdit_resolutionX.setText(resolutionX)
                self.ui.lineEdit_resolutionY.setText(resolutionY)
            else:
                self.ui.lineEdit_resolutionX.setText("None")
                self.ui.lineEdit_resolutionY.setText("None")

        self.ui.list_project.itemSelectionChanged.connect(getResolution_project)
        self.ui.button_validateResolution.clicked.connect(getResolution_project)

        def setFPS_project():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.lineEdit_FPS.setInputMask("00000")
            fpsInput = self.ui.lineEdit_FPS.text()
            with open(os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_fps.txt"), 'w') as f:
                f.write(fpsInput)
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Project FPS changed")

        self.ui.button_validateFPS.clicked.connect(setFPS_project)

        def getFPS_project():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            fpsFile = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_fps.txt")
            if os.path.isfile(fpsFile):
                with open(fpsFile) as f:
                    FPS = f.readline()
                self.ui.lineEdit_FPS.setText(FPS)
            else:
                self.ui.lineEdit_FPS.setText("None")

        self.ui.list_project.itemSelectionChanged.connect(getFPS_project)
        self.ui.button_validateFPS.clicked.connect(getFPS_project)

        def openDirectories_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            projectPath = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(projectPath) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                os.startfile(projectPath)
                self.ui.label_informations.setStyleSheet(labelInformationsWhite)
                self.ui.label_informations.setText(">>> Opening Directory")

        self.ui.button_directoryProject.clicked.connect(openDirectories_projects)

        def next_projects():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            projectPath = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(projectPath) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                self.ui.tab_widget.setCurrentIndex(tabAssets)

        self.ui.button_nextProject.clicked.connect(next_projects)

        # -------------------------#
        # ------ ASSETS TAB ------ #
        # -------------------------#

        self.ui.list_asset.addItems(["Select a project"])

        def changeTitle_projectAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.labelWelcomeAssets.setText(CIOXO_PROJECT)

        self.ui.list_project.itemSelectionChanged.connect(changeTitle_projectAssets)

        def changeTitle_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.tab_widget.setTabText(tabAssets, "Assets | " + CIOXO_PROJECT)

        self.ui.list_project.itemSelectionChanged.connect(changeTitle_assets)

        def fillList_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            assetsPath = os.path.join(rootDir, CIOXO_PROJECT, "assets")
            if CIOXO_PROJECT == "project" or os.path.isdir(assetsPath) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                self.ui.list_asset.clear()
                self.ui.list_asset.addItems(os.listdir(assetsPath))

        self.ui.list_project.itemSelectionChanged.connect(fillList_assets)
        self.ui.buttonReloadAssets.clicked.connect(fillList_assets)

        def reloadList_assets():
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Reloaded")

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
            activeListItem = [item.text() for item in self.ui.list_asset.selectedItems()]
            listToString = ''.join([str(elem) for elem in activeListItem])
            # ------ Define CIOXO SEQUENCE environment variable on item selected
            os.environ["CIOXO_ASSET"] = listToString
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Asset variable defined on: " + CIOXO_ASSET)

        self.ui.list_asset.itemSelectionChanged.connect(defineCioxoVariable_ASSET)

        def checkFilesExists_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            assetsPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET)

            # ------ Reset button colors
            self.ui.button_houdiniAsset.setStyleSheet(buttonGrey)
            self.ui.button_mayaAsset.setStyleSheet(buttonGrey)
            self.ui.button_substanceAsset.setStyleSheet(buttonGrey)
            self.ui.button_nukeAsset.setStyleSheet(buttonGrey)

            # ------ Houdini
            filesPath = os.path.join(assetsPath, "houdini", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.button_houdiniAsset.setEnabled(True)
                self.ui.button_houdiniAsset.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesHoudini = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesHoudini:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".hip" or extension == ".hiplc":
                                self.ui.button_houdiniAsset.setEnabled(True)
                                self.ui.button_houdiniAsset.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_houdiniAsset.setEnabled(True)
                                self.ui.button_houdiniAsset.setStyleSheet(buttonRed)
            else:
                self.ui.button_houdiniAsset.setEnabled(True)
                self.ui.button_houdiniAsset.setStyleSheet(buttonRed)

            # ------ Maya
            filesPath = os.path.join(assetsPath, "maya", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.button_mayaAsset.setEnabled(True)
                self.ui.button_mayaAsset.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesMaya = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesMaya:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".mb" or extension == ".ma":
                                self.ui.button_mayaAsset.setEnabled(True)
                                self.ui.button_mayaAsset.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_mayaAsset.setEnabled(True)
                                self.ui.button_mayaAsset.setStyleSheet(buttonRed)
            else:
                self.ui.button_mayaAsset.setEnabled(True)
                self.ui.button_mayaAsset.setStyleSheet(buttonRed)

            # ------ Substance
            filesPath = os.path.join(assetsPath, "substance", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.button_substanceAsset.setEnabled(True)
                self.ui.button_substanceAsset.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesSubstance = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesSubstance:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".spp":
                                self.ui.button_substanceAsset.setEnabled(True)
                                self.ui.button_substanceAsset.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_substanceAsset.setEnabled(True)
                                self.ui.button_substanceAsset.setStyleSheet(buttonRed)
            else:
                self.ui.button_substanceAsset.setEnabled(True)
                self.ui.button_substanceAsset.setStyleSheet(buttonRed)

            # ------ Nuke
            filesPath = os.path.join(assetsPath, "nuke", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.button_nukeAsset.setEnabled(True)
                self.ui.button_nukeAsset.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesNuke = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesNuke:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".nk" or extension == ".nknc":
                                self.ui.button_nukeAsset.setEnabled(True)
                                self.ui.button_nukeAsset.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_nukeAsset.setEnabled(True)
                                self.ui.button_nukeAsset.setStyleSheet(buttonRed)
            else:
                self.ui.button_nukeAsset.setEnabled(True)
                self.ui.button_nukeAsset.setStyleSheet(buttonRed)

        self.ui.list_asset.itemSelectionChanged.connect(checkFilesExists_assets)

        def loadThumbnail_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET,
                                         "." + CIOXO_PROJECT + "_" + CIOXO_ASSET + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailAssets.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailAssets.setText("No Thumbnail found")

        self.ui.list_asset.itemSelectionChanged.connect(loadThumbnail_assets)
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
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET,
                                         "." + CIOXO_PROJECT + "_" + CIOXO_ASSET + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                self.ui.label_informations.setText(">>> Thumbnail deleted")
            else:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No thumbnail found!")

        self.ui.buttonDeleteThumbnailAssets.clicked.connect(deleteThumbnail_assets)

        def openDirectories_assets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            pathAsset = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET)
            if CIOXO_ASSET == "asset" or os.path.isdir(pathAsset) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No asset selected!")
            else:
                os.startfile(pathAsset)
                self.ui.label_informations.setStyleSheet(labelInformationsWhite)
                self.ui.label_informations.setText(">>> Opening Directory")

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
            self.ui.tab_widget.setCurrentIndex(tabFilesAssets)
            self.ui.tab_widget.setTabEnabled(tabFilesAssets, True)

        self.ui.button_houdiniAsset.clicked.connect(openTab_filesAssets)
        self.ui.button_mayaAsset.clicked.connect(openTab_filesAssets)
        self.ui.button_substanceAsset.clicked.connect(openTab_filesAssets)
        self.ui.button_nukeAsset.clicked.connect(openTab_filesAssets)

        def previous_assets():
            self.ui.tab_widget.setCurrentIndex(tabProjects)

        self.ui.pushButtonPreviousAssets.clicked.connect(previous_assets)

        # -------------------------------#
        # ------ FILES ASSETS TAB ------ #
        # -------------------------------#

        self.ui.list_fileAsset.addItems(["Select an asset"])

        def defineCioxoVariable_HOUDINI():
            os.environ["CIOXO_SOFTWARE"] = "houdini"

        self.ui.button_houdiniAsset.clicked.connect(defineCioxoVariable_HOUDINI)

        def defineCioxoVariable_MAYA():
            os.environ["CIOXO_SOFTWARE"] = "maya"

        self.ui.button_mayaAsset.clicked.connect(defineCioxoVariable_MAYA)

        def defineCioxoVariable_SUBSTANCE():
            os.environ["CIOXO_SOFTWARE"] = "substance"

        self.ui.button_substanceAsset.clicked.connect(defineCioxoVariable_SUBSTANCE)

        def defineCioxoVariable_NUKE():
            os.environ["CIOXO_SOFTWARE"] = "nuke"

        self.ui.button_nukeAsset.clicked.connect(defineCioxoVariable_NUKE)

        def changeTitle_sequenceShotSoftware():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            self.ui.labelWelcomeFilesAssets.setText(CIOXO_PROJECT + " - " + CIOXO_ASSET + " | " + CIOXO_SOFTWARE)

        self.ui.list_asset.itemSelectionChanged.connect(changeTitle_sequenceShotSoftware)
        self.ui.button_houdiniAsset.clicked.connect(changeTitle_sequenceShotSoftware)
        self.ui.button_mayaAsset.clicked.connect(changeTitle_sequenceShotSoftware)
        self.ui.button_substanceAsset.clicked.connect(changeTitle_sequenceShotSoftware)
        self.ui.button_nukeAsset.clicked.connect(changeTitle_sequenceShotSoftware)

        def changeTabTitle_filesAssets():
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            self.ui.tab_widget.setTabText(tabFilesAssets, CIOXO_ASSET + " | " + CIOXO_SOFTWARE)

        self.ui.button_houdiniAsset.clicked.connect(changeTabTitle_filesAssets)
        self.ui.button_mayaAsset.clicked.connect(changeTabTitle_filesAssets)
        self.ui.button_substanceAsset.clicked.connect(changeTabTitle_filesAssets)
        self.ui.button_nukeAsset.clicked.connect(changeTabTitle_filesAssets)

        def fillList_filesAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            filesPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE)
            self.ui.list_fileAsset.clear()

            # ------ Houdini
            if CIOXO_SOFTWARE == "houdini":
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
                    self.ui.list_fileAsset.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(houdiniExtension):
                            filesList.append(files)
                            self.ui.list_fileAsset.addItem(files)
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
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.list_fileAsset.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(mayaExtension):
                            filesList.append(files)
                            self.ui.list_fileAsset.addItem(files)
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
                    self.ui.list_fileAsset.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(substanceExtension):
                            filesList.append(files)
                            self.ui.list_fileAsset.addItem(files)

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
                    self.ui.list_fileAsset.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(nukeExtension):
                            filesList.append(files)
                            self.ui.list_fileAsset.addItem(files)

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
                    self.ui.list_fileAsset.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(afterEffectsExtension):
                            filesList.append(files)
                            self.ui.list_fileAsset.addItem(files)

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
                    self.ui.list_fileAsset.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(photoshopExtension):
                            filesList.append(files)
                            self.ui.list_fileAsset.addItem(files)

        self.ui.button_houdiniAsset.clicked.connect(fillList_filesAssets)
        self.ui.button_mayaAsset.clicked.connect(fillList_filesAssets)
        self.ui.button_substanceAsset.clicked.connect(fillList_filesAssets)
        self.ui.button_nukeAsset.clicked.connect(fillList_filesAssets)
        # TODO: create GUI buttons for Nuke and After Effects
        # self.ui.button_nukeAsset.clicked.connect(fillList_filesAssets)
        # self.ui.button_nukeAsset.clicked.connect(fillList_filesAssets)
        self.ui.buttonReloadFilesAssets.clicked.connect(fillList_filesAssets)

        def reloadList_filesAssets():
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Reloaded")

        self.ui.buttonReloadFilesAssets.clicked.connect(reloadList_filesAssets)

        def defineCioxoVariable_FILE():
            activeListItem = [item.text() for item in self.ui.list_fileAsset.selectedItems()]
            listToString = ''.join([str(elem) for elem in activeListItem])
            os.environ["CIOXO_FILE"] = listToString
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            os.environ["CIOXO_DISCIPLINE"] = CIOXO_FILE.lower().split("_")[2]
            CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(
                ">>> File variable defined on: " + CIOXO_FILE + "\n>>> Discipline variable defined on: " + CIOXO_DISCIPLINE)

        self.ui.list_fileAsset.itemSelectionChanged.connect(defineCioxoVariable_FILE)

        def loadThumbnail_filesAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[2]
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces",
                                         CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailFilesAssets.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailFilesAssets.setText("No Thumbnail found")

        self.ui.list_fileAsset.itemSelectionChanged.connect(loadThumbnail_filesAssets)
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
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces",
                                         CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                self.ui.label_informations.setText(">>> Thumbnail deleted")
            else:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No thumbnail found!")

        self.ui.buttonDeleteThumbnailFilesAssets.clicked.connect(deleteThumbnail_fileAssets)

        def showComment_filesAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[2]
            fileCommentPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces",
                                           CIOXO_DISCIPLINE, "." + CIOXO_FILE.split(".")[0] + "_comment.txt")
            if os.path.isfile(fileCommentPath):
                with open(fileCommentPath) as f:
                    comment = f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline()
                self.ui.labelCommentFilesAssets.setText(comment)
            else:
                self.ui.labelCommentFilesAssets.setText("No comment found")

        self.ui.list_fileAsset.itemSelectionChanged.connect(showComment_filesAssets)

        def openFile_fileAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            filesPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, CIOXO_FILE)
            if CIOXO_FILE == "file" or os.path.isfile(filesPath) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No file selected!")
            else:
                self.ui.label_informations.setStyleSheet(labelInformationsWhite)
                os.startfile(filesPath)
                self.ui.label_informations.setText(">>> Opening " + filesPath)

        self.ui.button_openFileAsset.clicked.connect(openFile_fileAssets)
        self.ui.list_fileAsset.doubleClicked.connect(openFile_fileAssets)

        def clearList_filesAssets():
            # ------ Reset button colors
            self.ui.button_houdiniAsset.setStyleSheet(buttonGrey)
            self.ui.button_mayaAsset.setStyleSheet(buttonGrey)
            self.ui.button_substanceAsset.setStyleSheet(buttonGrey)
            self.ui.button_nukeAsset.setStyleSheet(buttonGrey)
            # ------ Clear
            self.ui.tab_widget.setTabText(tabFilesAssets, "Asset Files")
            self.ui.tab_widget.setTabEnabled(tabFilesAssets, False)
            self.ui.list_fileAsset.clear()

        self.ui.list_project.itemSelectionChanged.connect(clearList_filesAssets)

        def clearList_filesAssetsSecondary():
            # ------ Clear
            self.ui.tab_widget.setTabText(tabFilesAssets, "Asset Files")
            self.ui.tab_widget.setTabEnabled(tabFilesAssets, False)
            self.ui.list_fileAsset.clear()

        self.ui.list_asset.itemSelectionChanged.connect(clearList_filesAssetsSecondary)

        def openDirectories_filesAssets():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            pathFile = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE)
            os.startfile(pathFile)
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Opening Directory")

        self.ui.button_directoryFileAsset.clicked.connect(openDirectories_filesAssets)

        def previous_fileAssets():
            self.ui.tab_widget.setCurrentIndex(tabAssets)

        self.ui.button_previousFileAsset.clicked.connect(previous_fileAssets)

        # ---------------------------#
        # ------ SEQUENCES TAB ------#
        # ---------------------------#

        self.ui.list_sequence.addItems(["Select a project"])
        self.ui.list_shot.addItems(["Select a sequence"])

        def changeTitle_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.label_welcomeSequence.setText(CIOXO_PROJECT)

        self.ui.list_project.itemSelectionChanged.connect(changeTitle_sequences)

        def changeTabTitle_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            self.ui.tab_widget.setTabText(tabSequences, "Sequences | " + CIOXO_PROJECT)

        self.ui.list_project.itemSelectionChanged.connect(changeTabTitle_sequences)

        def fillList_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            pathSequences = os.path.join(rootDir, CIOXO_PROJECT)
            if CIOXO_PROJECT == "project" or os.path.isdir(pathSequences) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                self.ui.list_sequence.clear()
                for sequences in os.listdir(pathSequences):
                    if sequences.startswith("seq"):
                        self.ui.list_sequence.addItems(sequences.split())

        self.ui.list_project.itemSelectionChanged.connect(fillList_sequences)
        self.ui.button_reloadSequence.clicked.connect(fillList_sequences)

        def loadThumbnail_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)
            pathThumbnail = os.path.join(shotPath,
                                         "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.label_thumbnailSequence.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.label_thumbnailSequence.setText("No Thumbnail found")

        self.ui.list_shot.itemSelectionChanged.connect(loadThumbnail_sequences)
        self.ui.button_refreshThumbnailSequence.clicked.connect(loadThumbnail_sequences)

        def deleteThumbnail_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)
            pathThumbnail = os.path.join(shotPath,
                                         "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                self.ui.label_informations.setText(">>> Thumbnail deleted")
            else:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No thumbnail found!")

        self.ui.button_deleteThumbnailSequence.clicked.connect(deleteThumbnail_sequences)

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
            activeListItemSequence = [item.text() for item in self.ui.list_sequence.selectedItems()]
            listToStringSequence = ''.join([str(elem) for elem in activeListItemSequence])
            # ------ Define CIOXO SEQUENCE environment variable on item selected
            os.environ["CIOXO_SEQUENCE"] = listToStringSequence
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Sequence variable defined on: " + CIOXO_SEQUENCE)

        self.ui.list_sequence.itemSelectionChanged.connect(defineCioxoVariable_SEQUENCE)

        def fillList_shots():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            shotsPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)
            self.ui.list_shot.clear()
            for shots in os.listdir(shotsPath):
                if shots.startswith("sh"):
                    self.ui.list_shot.addItems(shots.split())

        self.ui.list_sequence.itemSelectionChanged.connect(fillList_shots)
        self.ui.buttonReloadShots.clicked.connect(fillList_shots)

        def defineCioxoVariable_SHOT():
            # ------ Get change in list shot
            activeListItemShots = [item.text() for item in self.ui.list_shot.selectedItems()]
            listToStringShot = ''.join([str(elem) for elem in activeListItemShots])
            # ------ Define CIOXO SHOT environment variable on item selected
            os.environ["CIOXO_SHOT"] = listToStringShot
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Shot variable defined on: " + CIOXO_SHOT)

        self.ui.list_shot.itemSelectionChanged.connect(defineCioxoVariable_SHOT)

        def loadThumbnail_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT,
                                         "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.label_thumbnailSequence.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.label_thumbnailSequence.setText("No Thumbnail found")

        self.ui.list_shot.itemSelectionChanged.connect(loadThumbnail_sequences)
        self.ui.button_refreshThumbnailSequence.clicked.connect(loadThumbnail_sequences)

        def checkFilesExists_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)

            # ------ Reset button colors and state
            self.ui.button_houdiniSequence.setStyleSheet(buttonGrey)
            self.ui.button_mayaSequence.setStyleSheet(buttonGrey)
            self.ui.buttonSubstanceSequences.setStyleSheet(buttonGrey)
            self.ui.button_nukeSequences.setStyleSheet(buttonGrey)
            self.ui.button_afterEffectsSequence.setStyleSheet(buttonGrey)
            self.ui.button_photoshopSequence.setStyleSheet(buttonGrey)

            # ------ Houdini
            filesPath = os.path.join(shotPath, "houdini", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.button_houdiniSequence.setEnabled(True)
                self.ui.button_houdiniSequence.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesHoudini = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesHoudini:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".hip" or extension == ".hiplc":
                                self.ui.button_houdiniSequence.setEnabled(True)
                                self.ui.button_houdiniSequence.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_houdiniSequence.setEnabled(True)
                                self.ui.button_houdiniSequence.setStyleSheet(buttonRed)
            else:
                self.ui.button_houdiniSequence.setEnabled(True)
                self.ui.button_houdiniSequence.setStyleSheet(buttonRed)

            # ------ Maya
            filesPath = os.path.join(shotPath, "maya", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.button_mayaSequence.setEnabled(True)
                self.ui.button_mayaSequence.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesMaya = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesMaya:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".ma" or extension == ".mb":
                                self.ui.button_mayaSequence.setEnabled(True)
                                self.ui.button_mayaSequence.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_mayaSequence.setEnabled(True)
                                self.ui.button_mayaSequence.setStyleSheet(buttonRed)
            else:
                self.ui.button_mayaSequence.setEnabled(True)
                self.ui.button_mayaSequence.setStyleSheet(buttonRed)

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
                self.ui.button_nukeSequences.setEnabled(True)
                self.ui.button_nukeSequences.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesNuke = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesNuke:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".nk" or extension == ".nknc":
                                self.ui.button_nukeSequences.setEnabled(True)
                                self.ui.button_nukeSequences.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_nukeSequences.setEnabled(True)
                                self.ui.button_nukeSequences.setStyleSheet(buttonRed)
            else:
                self.ui.button_nukeSequences.setEnabled(True)
                self.ui.button_nukeSequences.setStyleSheet(buttonRed)

            # ------ After Effects
            filesPath = os.path.join(shotPath, "afterEffects", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.button_afterEffectsSequence.setEnabled(True)
                self.ui.button_afterEffectsSequence.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesAfterEffects = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesAfterEffects:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".aep":
                                self.ui.button_afterEffectsSequence.setEnabled(True)
                                self.ui.button_afterEffectsSequence.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_afterEffectsSequence.setEnabled(True)
                                self.ui.button_afterEffectsSequence.setStyleSheet(buttonRed)
            else:
                self.ui.button_afterEffectsSequence.setEnabled(True)
                self.ui.button_afterEffectsSequence.setStyleSheet(buttonRed)

            # ------ Photoshop
            filesPath = os.path.join(shotPath, "photoshop", "workspaces")
            if os.path.isdir(filesPath) is True:
                self.ui.button_photoshopSequence.setEnabled(True)
                self.ui.button_photoshopSequence.setStyleSheet(buttonRed)
                foldersDisciplineList = []
                for folderDisciplines in os.listdir(filesPath):
                    foldersDisciplineList.append(folderDisciplines)
                    for disciplines in foldersDisciplineList:
                        filesPhotoshop = os.listdir(os.path.join(filesPath, disciplines))
                        for files in filesPhotoshop:
                            extension = os.path.splitext(files)[-1]
                            if extension == ".psd":
                                self.ui.button_photoshopSequence.setEnabled(True)
                                self.ui.button_photoshopSequence.setStyleSheet(buttonGreen)
                            else:
                                self.ui.button_photoshopSequence.setEnabled(True)
                                self.ui.button_photoshopSequence.setStyleSheet(buttonRed)
            else:
                self.ui.button_photoshopSequence.setEnabled(True)
                self.ui.button_photoshopSequence.setStyleSheet(buttonRed)

        self.ui.list_shot.itemSelectionChanged.connect(checkFilesExists_sequences)

        def deleteThumbnail_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT,
                                         "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                self.ui.label_informations.setText(">>> Thumbnail deleted")
            else:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No thumbnail found!")

        self.ui.button_deleteThumbnailSequence.clicked.connect(deleteThumbnail_sequences)

        def setFrameRange_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            frameRangeFile = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT,
                                          "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_frameRange.txt")
            self.ui.lineEdit_frameStart.setInputMask("99900")
            frameStart = self.ui.lineEdit_frameStart.text()
            self.ui.lineEdit_frameEnd.setInputMask("99900")
            frameEnd = self.ui.lineEdit_frameEnd.text()
            with open(os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT,
                                   "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_frameRange.txt"),
                      "w") as f:
                f.write(frameStart + "_" + frameEnd)
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Shot frame range changed")

        self.ui.button_validateFrameRange.clicked.connect(setFrameRange_sequences)

        def getFrameRange_sequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            frameRangeFile = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT,
                                          "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_frameRange.txt")
            if os.path.isfile(frameRangeFile):
                with open(frameRangeFile) as f:
                    frameRange = f.readline()
                frameStart = frameRange.split("_")[0]
                frameEnd = frameRange.split("_")[1]
                self.ui.lineEdit_frameStart.setText(frameStart)
                self.ui.lineEdit_frameEnd.setText(frameEnd)
            else:
                self.ui.lineEdit_frameStart.setText("None")
                self.ui.lineEdit_frameEnd.setText("None")

        self.ui.list_shot.itemSelectionChanged.connect(getFrameRange_sequences)
        self.ui.button_validateFrameRange.clicked.connect(getFrameRange_sequences)

        def openWindow_createShotFile():
            if self.createFileShotWindow is None:
                self.createFileShotWindow = CreateFileShot()
                self.createFileShotWindow.show()
                self.createFileShotWindow = None  # ------ Discard reference
            else:
                self.createFileShotWindow.close()  # ------ Close window
                self.createFileShotWindow = None  # ------ Discard reference

        self.ui.button_createFileShot.clicked.connect(openWindow_createShotFile)

        def openWindow_createSequence():  # ------ Show Create Asset window
            if self.createSequenceWindow is None:
                self.createSequenceWindow = CreateSequence()
                self.createSequenceWindow.show()
                self.createSequenceWindow = None  # ------ Discard reference
            else:
                self.createSequenceWindow.close()  # ------ Close window
                self.createSequenceWindow = None  # ------ Discard reference

        self.ui.button_createSequence.clicked.connect(openWindow_createSequence)

        def openWindow_createShot():  # ------ Show Create Asset window
            if self.createShotWindow is None:
                self.createShotWindow = CreateShot()
                self.createShotWindow.show()
                self.createShotWindow = None  # ------ Discard reference
            else:
                self.createShotWindow.close()  # ------ Close window
                self.createShotWindow = None  # ------ Discard reference

        self.ui.button_createShot.clicked.connect(openWindow_createShot)

        def openDirectories_Sequence():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)
            if CIOXO_SHOT == "shot" or os.path.isdir(shotPath) is False:
                shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)
                os.startfile(shotPath)
                if CIOXO_SEQUENCE == "sequence" or os.path.isdir(shotPath) is False:
                    self.ui.label_informations.setStyleSheet(label_informationsRed)
                    self.ui.label_informations.setText(">>> No sequence selected!")
            else:
                os.startfile(shotPath)
                self.ui.label_informations.setStyleSheet(labelInformationsWhite)
                self.ui.label_informations.setText(">>> Opening Directory")

        self.ui.buttonDirectorySequences.clicked.connect(openDirectories_Sequence)

        def openTab_filesSequences():
            self.ui.tab_widget.setCurrentIndex(tabFilesSequences)
            self.ui.tab_widget.setTabEnabled(tabFilesSequences, True)

        self.ui.button_houdiniSequence.clicked.connect(openTab_filesSequences)
        self.ui.button_mayaSequence.clicked.connect(openTab_filesSequences)
        self.ui.buttonSubstanceSequences.clicked.connect(openTab_filesSequences)
        self.ui.button_nukeSequences.clicked.connect(openTab_filesSequences)
        self.ui.button_afterEffectsSequence.clicked.connect(openTab_filesSequences)
        self.ui.button_photoshopSequence.clicked.connect(openTab_filesSequences)

        def previous_sequences():
            self.ui.tab_widget.setCurrentIndex(tabProjects)

        self.ui.button_previousSequence.clicked.connect(previous_sequences)

        # ---------------------------------#
        # ------ FILES SEQUENCES TAB ------#
        # ---------------------------------#

        self.ui.list_fileShot.addItems(["Select a shot"])

        def changeTitle_SequenceShot():
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            self.ui.label_welcomeFileShots.setText(CIOXO_SEQUENCE + " - " + CIOXO_SHOT)

        self.ui.list_sequence.itemSelectionChanged.connect(changeTitle_SequenceShot)
        self.ui.list_shot.itemSelectionChanged.connect(changeTitle_SequenceShot)

        def defineCioxoVariable_HOUDINI():
            os.environ["CIOXO_SOFTWARE"] = "houdini"

        self.ui.button_houdiniSequence.clicked.connect(defineCioxoVariable_HOUDINI)

        def defineCioxoVariable_MAYA():
            os.environ["CIOXO_SOFTWARE"] = "maya"

        self.ui.button_mayaSequence.clicked.connect(defineCioxoVariable_MAYA)

        def defineCioxoVariable_SUBSTANCE():
            os.environ["CIOXO_SOFTWARE"] = "substance"

        self.ui.buttonSubstanceSequences.clicked.connect(defineCioxoVariable_SUBSTANCE)

        def defineCioxoVariable_NUKE():
            os.environ["CIOXO_SOFTWARE"] = "nuke"

        self.ui.button_nukeSequences.clicked.connect(defineCioxoVariable_NUKE)

        def defineCioxoVariable_AFTEREFFECTS():
            os.environ["CIOXO_SOFTWARE"] = "afterEffects"

        self.ui.button_afterEffectsSequence.clicked.connect(defineCioxoVariable_AFTEREFFECTS)

        def defineCioxoVariable_PHOTOSHOP():
            os.environ["CIOXO_SOFTWARE"] = "photoshop"

        self.ui.button_photoshopSequence.clicked.connect(defineCioxoVariable_PHOTOSHOP)

        def changeTitle_SequenceShotSoftware():
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            self.ui.label_welcomeFileShots.setText(CIOXO_SEQUENCE + " - " + CIOXO_SHOT + " | " + CIOXO_SOFTWARE)

        self.ui.list_sequence.itemSelectionChanged.connect(changeTitle_SequenceShotSoftware)
        self.ui.list_shot.itemSelectionChanged.connect(changeTitle_SequenceShotSoftware)
        self.ui.button_houdiniSequence.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.button_mayaSequence.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.buttonSubstanceSequences.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.button_nukeSequences.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.button_afterEffectsSequence.clicked.connect(changeTitle_SequenceShotSoftware)
        self.ui.button_photoshopSequence.clicked.connect(changeTitle_SequenceShotSoftware)

        def changeTabTitle_SequenceShotSoftware():
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            self.ui.tab_widget.setTabText(tabFilesSequences,
                                         CIOXO_SEQUENCE + " - " + CIOXO_SHOT + " | " + CIOXO_SOFTWARE)

        self.ui.button_houdiniSequence.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.button_mayaSequence.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.buttonSubstanceSequences.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.button_nukeSequences.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.button_afterEffectsSequence.clicked.connect(changeTabTitle_SequenceShotSoftware)
        self.ui.button_photoshopSequence.clicked.connect(changeTabTitle_SequenceShotSoftware)

        def fillList_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            filesPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE)
            self.ui.list_fileShot.clear()

            # ------ Houdini
            if CIOXO_SOFTWARE == "houdini":
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
                    self.ui.list_fileShot.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(houdiniExtension):
                            filesList.append(files)
                            self.ui.list_fileShot.addItem(files)
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
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.list_fileShot.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(mayaExtension):
                            filesList.append(files)
                            self.ui.list_fileShot.addItem(files)
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
                    self.ui.list_fileShot.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(substanceExtension):
                            filesList.append(files)
                            self.ui.list_fileShot.addItem(files)
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
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.list_fileShot.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(nukeExtension):
                            filesList.append(files)
                            self.ui.list_fileShot.addItem(files)
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
                    self.ui.list_fileShot.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(afterEffectsExtension):
                            filesList.append(files)
                            self.ui.list_fileShot.addItem(files)
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
                    icon.addPixmap(QtGui.QPixmap(":/icons/graphics/icons/chevronDown.svg"), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
                    font = QtGui.QFont()
                    font.setBold(True)
                    delimiter.setIcon(icon)
                    delimiter.setFont(font)
                    delimiter.setFlags(QtCore.Qt.NoItemFlags)
                    delimiter.setText(folderDisciplines.upper())
                    self.ui.list_fileShot.addItem(delimiter)
                    # ------ Look for houdini files
                    filesList = []
                    for disciplines in foldersDisciplineList:
                        files = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
                    for files in files:
                        if files.endswith(photoshopExtension):
                            filesList.append(files)
                            self.ui.list_fileShot.addItem(files)
                        else:
                            pass

        self.ui.button_houdiniSequence.clicked.connect(fillList_filesSequences)
        self.ui.button_mayaSequence.clicked.connect(fillList_filesSequences)
        self.ui.buttonSubstanceSequences.clicked.connect(fillList_filesSequences)
        self.ui.button_nukeSequences.clicked.connect(fillList_filesSequences)
        self.ui.button_afterEffectsSequence.clicked.connect(fillList_filesSequences)
        self.ui.button_photoshopSequence.clicked.connect(fillList_filesSequences)
        self.ui.buttonReloadFilesSequences.clicked.connect(fillList_filesSequences)

        def reloadFiles_filesSequences():
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Reloaded")

        self.ui.buttonReloadFilesSequences.clicked.connect(reloadFiles_filesSequences)

        def defineCioxoVariable_FILE():
            activeListItem = [item.text() for item in self.ui.list_fileShot.selectedItems()]
            listToString = ''.join([str(elem) for elem in activeListItem])
            os.environ["CIOXO_FILE"] = listToString
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            os.environ["CIOXO_DISCIPLINE"] = CIOXO_FILE.lower().split("_")[3]
            CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(
                ">>> File variable defined on: " + CIOXO_FILE + "\n>>> Discipline variable defined on: " + CIOXO_DISCIPLINE)

        self.ui.list_fileShot.itemSelectionChanged.connect(defineCioxoVariable_FILE)

        def loadThumbnail_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE,
                                         "workspaces", CIOXO_DISCIPLINE,
                                         "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                self.ui.labelThumbnailFilesSequences.setPixmap(QtGui.QPixmap(pathThumbnail))
            else:
                self.ui.labelThumbnailFilesSequences.setText("No Thumbnail found")

        self.ui.list_fileShot.itemSelectionChanged.connect(loadThumbnail_filesSequences)
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
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE,
                                         "workspaces", CIOXO_DISCIPLINE,
                                         "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            if os.path.isfile(pathThumbnail):
                os.remove(pathThumbnail)
                self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                self.ui.label_informations.setText(">>> Thumbnail deleted")
            else:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No thumbnail found!")

        self.ui.buttonDeleteThumbnailFilesSequences.clicked.connect(deleteThumbnail_filesSequences)

        def showComment_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]
            fileCommentPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE,
                                           "workspaces", CIOXO_DISCIPLINE,
                                           "." + CIOXO_FILE.split(".")[0] + "_comment.txt")
            if os.path.isfile(fileCommentPath):
                with open(fileCommentPath) as f:
                    comment = f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline() + f.readline()
                self.ui.labelCommentFilesSequences.setText(comment)
            else:
                self.ui.labelCommentFilesSequences.setText("No comment found")

        self.ui.list_fileShot.itemSelectionChanged.connect(showComment_filesSequences)

        def openFile_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]

            filesPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces",
                                     CIOXO_DISCIPLINE, CIOXO_FILE)

            if CIOXO_FILE == "file" or os.path.isfile(filesPath) is False:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No file selected!")
            else:
                self.ui.label_informations.setStyleSheet(labelInformationsWhite)
                os.startfile(filesPath)
                self.ui.label_informations.setText(">>> Opening " + filesPath)

        self.ui.button_openFileShot.clicked.connect(openFile_filesSequences)
        self.ui.list_fileShot.doubleClicked.connect(openFile_filesSequences)

        def clearList_filesSequences():

            # ------ Reset button colors
            self.ui.button_houdiniSequence.setStyleSheet(buttonGrey)
            self.ui.button_mayaSequence.setStyleSheet(buttonGrey)
            self.ui.buttonSubstanceSequences.setStyleSheet(buttonGrey)
            self.ui.button_nukeSequences.setStyleSheet(buttonGrey)
            self.ui.button_afterEffectsSequence.setStyleSheet(buttonGrey)
            self.ui.button_photoshopSequence.setStyleSheet(buttonGrey)
            # ------ Clear
            self.ui.tab_widget.setTabText(tabFilesSequences, "Shot Files")
            self.ui.tab_widget.setTabEnabled(tabFilesSequences, False)
            self.ui.list_fileShot.clear()

        self.ui.list_project.itemSelectionChanged.connect(clearList_filesSequences)

        def clearList_filesSequencesSecondary():
            # ------ Clear
            self.ui.tab_widget.setTabText(tabFilesSequences, "Shot Files")
            self.ui.tab_widget.setTabEnabled(tabFilesSequences, False)
            self.ui.list_fileShot.clear()

        self.ui.list_sequence.itemSelectionChanged.connect(clearList_filesSequencesSecondary)
        self.ui.list_shot.itemSelectionChanged.connect(clearList_filesSequencesSecondary)

        def openDirectories_filesSequences():
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            pathFile = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces")
            os.startfile(pathFile)
            self.ui.label_informations.setStyleSheet(labelInformationsWhite)
            self.ui.label_informations.setText(">>> Opening Directory")

        self.ui.button_directoryFileShot.clicked.connect(openDirectories_filesSequences)

        def previous_filesSequences():
            self.ui.tab_widget.setCurrentIndex(tabSequences)

        self.ui.button_previousFileShot.clicked.connect(previous_filesSequences)

        # ---------------------#
        # ------ GENERAL ------#
        # ---------------------#

        def openDocumentation():
            pathDocumentation = "https://www.google.fr"
            os.startfile(pathDocumentation)

        self.ui.buttonHelp.clicked.connect(openDocumentation)

        def openPlanning():
            if os.getenv("CIOXO_PROJECT") == "project":
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
                planningPath = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_planning.url")
                if os.path.isfile(planningPath):
                    os.startfile(planningPath)
                    self.ui.label_informations.setStyleSheet(labelInformationsWhite)
                    self.ui.label_informations.setText(">>> Opening Planning")
                else:
                    self.ui.label_informations.setStyleSheet(label_informationsRed)
                    self.ui.label_informations.setText(">>> No planning for this project!")

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
        self.ui = Ui_cioxo_createProject()
        self.ui.setupUi(self)

        self.ui.lineEdit_input.setInputMask("AAA")

        def createDirectory_project():
            projectInput = self.ui.lineEdit_input.text()
            pathExists = True
            while pathExists:
                if os.path.isdir(os.path.join(rootDir, projectInput)):
                    self.ui.label_informations.setStyleSheet(label_informationsRed)
                    self.ui.label_informations.setText(">>> Project already exists!")
                    break
                else:
                    self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                    self.ui.label_informations.setText(
                        ">>> Project " + projectInput + " created - You can now close the window")
                    self.ui.button_cancel.setText("Close")
                    toDirectory = os.path.join(rootDir, projectInput)
                    copy_tree(projectTemplate, toDirectory)
                    pathExists = False

        self.ui.button_ok.clicked.connect(createDirectory_project)

        def writeResolution_project():
            projectInput = self.ui.lineEdit_input.text()
            self.ui.lineEditResolutionX.setInputMask("99900")
            resolutionXInput = self.ui.lineEditResolutionX.text()
            self.ui.lineEditResolutionY.setInputMask("99900")
            resolutionYInput = self.ui.lineEditResolutionY.text()
            with open(os.path.join(rootDir, projectInput, "." + projectInput + "_resolution.txt"), 'w') as resolution:
                resolution.write(resolutionXInput + "_" + resolutionYInput)

        self.ui.button_ok.clicked.connect(writeResolution_project)

        def writeFPS_project():
            projectInput = self.ui.lineEdit_input.text()
            self.ui.lineEdit_FPS.setInputMask("99000")
            fpsInput = self.ui.lineEdit_FPS.text()
            with open(os.path.join(rootDir, projectInput, "." + projectInput + "_fps.txt"), 'w') as fps:
                fps.write(fpsInput)

        self.ui.button_ok.clicked.connect(writeFPS_project)

        def closeWindow_createProject():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createProject)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Project")

    # END


# ------ CREATE SEQUENCE
class CreateSequence(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createSequence()
        self.ui.setupUi(self)

        # ------ Window variables
        self.setWindowTitle("Cioxo - Create Sequence")
        self.ui.lineEdit_input.setInputMask("seqNNN")

        def createDirectory_sequence():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            # ------ Paths
            sequencePath = os.path.join(rootDir, CIOXO_PROJECT)
            sequenceInput = self.ui.lineEdit_input.text()
            # ------ Check if project is selected
            if CIOXO_PROJECT == "project" or os.path.isdir(sequencePath) is None:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                pathExists = True
                while pathExists:
                    # ------ Check if sequence already exists
                    if os.path.isdir(os.path.join(sequencePath, sequenceInput)):
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> Sequence already exists!")
                        break
                    else:
                        # ------ Write sequence folder if it doesn't exist
                        self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                        self.ui.label_informations.setText(
                            ">>> Sequence " + sequenceInput + " created - You can now close the window")
                        self.ui.button_cancel.setText("Close")
                        toDirectory = os.path.join(sequencePath, sequenceInput)
                        copy_tree(sequenceTemplate, toDirectory)
                        pathExists = False

        self.ui.button_ok.clicked.connect(createDirectory_sequence)

        def closeWindow_createSequence():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createSequence)


# ------ CREATE SHOT
class CreateShot(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createShot()
        self.ui.setupUi(self)

        # ------ Window variables
        self.setWindowTitle("Cioxo - Create Shot")
        self.ui.lineEdit_input.setText("sh")
        self.ui.lineEdit_frameStart.setInputMask("99900")
        self.ui.lineEdit_frameEnd.setInputMask("99900")

        def createDirectory_shot():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            # ------ Paths
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)
            shotInput = self.ui.lineEdit_input.text()
            # ------ Check if directory already exists
            pathExists = True
            while pathExists:
                if os.path.isdir(os.path.join(shotPath, shotInput)):
                    self.ui.label_informations.setStyleSheet(label_informationsRed)
                    self.ui.label_informations.setText(">>> Shot already exists!")
                    break
                else:
                    if CIOXO_SEQUENCE == "sequence" or os.path.isdir(shotPath) is False:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> No sequence selected!")
                    else:
                        self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                        self.ui.label_informations.setText(
                            ">>> Shot " + shotInput + " created - You can now close the window")
                        self.ui.button_cancel.setText("Close")
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

        self.ui.button_ok.clicked.connect(createDirectory_shot)

        def writeFrameRange_shot():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            # ------ Paths
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE)
            shotInput = self.ui.lineEdit_input.text()
            # ------ Write Frame Range value
            frameStartInput = self.ui.lineEdit_frameStart.text()
            frameEndInput = self.ui.lineEdit_frameEnd.text()
            with open(os.path.join(shotPath, shotInput,
                                   "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + shotInput + "_frameRange.txt"),
                      'w') as f:
                f.write(frameStartInput + "_" + frameEndInput)

        self.ui.button_ok.clicked.connect(writeFrameRange_shot)

        def closeWindow_createShot():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createShot)


# ------ CREATE ASSET
class CreateAsset(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createAsset()
        self.ui.setupUi(self)

        # ------ Window variable
        self.setWindowTitle("Cioxo - Create Asset")

        def createDirectory_asset():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            # ------ Paths
            assetsPath = os.path.join(rootDir, CIOXO_PROJECT)
            assetInput = self.ui.lineEdit_input.text()
            # ------ Check if PROJECT is selected
            if CIOXO_PROJECT == "project" or os.path.isdir(assetsPath) is None:
                self.ui.label_informations.setStyleSheet(label_informationsRed)
                self.ui.label_informations.setText(">>> No project selected!")
            else:
                pathExists = True
                while pathExists:
                    # ------ Check if asset already exists
                    if os.path.isdir(os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_PROJECT + "_" + assetInput)):
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> Asset already exists!")
                        break
                    else:
                        # ------ Create if asset doesn't exist
                        self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                        self.ui.label_informations.setText(
                            ">>> Asset " + assetInput + " created - You can now close the window")
                        self.ui.button_cancel.setText("Close")
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

        self.ui.button_ok.clicked.connect(createDirectory_asset)

        def closeWindow_createAsset():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createAsset)


# ------ CREATE FILE SHOT
class CreateFileShot(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createFile()
        self.ui.setupUi(self)

        # ------ Window variables
        self.setWindowTitle("Cioxo - Create File")
        self.ui.labelActualProject.setText("  " + os.getenv("CIOXO_PROJECT"))
        self.ui.labelActualSequence.setText("  " + os.getenv("CIOXO_SEQUENCE"))
        self.ui.labelActualShot.setText("  " + os.getenv("CIOXO_SHOT"))
        self.ui.plainTextEditComment.setPlaceholderText("Comment...")
        self.ui.lineEditVersion.setInputMask("v999")
        self.ui.lineEditVersion.setText("v001")

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
            versionInput = self.ui.lineEditVersion.text()
            # ------ Paths
            filePath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces",
                                    CIOXO_DISCIPLINE)
            fileName = CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_" + CIOXO_DISCIPLINE + versionInput
            fileCommentPath = os.path.join(filePath,
                                           "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_" + CIOXO_DISCIPLINE + versionInput + "_comment.txt")
            comment = self.ui.plainTextEditComment.toPlainText()
            # ------ Create file
            # ------ Houdini
            if CIOXO_SOFTWARE == "houdini":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".hip")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".hiplc")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".hip"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Maya
            elif CIOXO_SOFTWARE == "maya":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".mb")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".ma")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".mb"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Substance
            elif CIOXO_SOFTWARE == "substance":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".spp")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".spp"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Nuke
            elif CIOXO_SOFTWARE == "nuke":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".nk")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".nknc")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".nk"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ After Effects
            elif CIOXO_SOFTWARE == "afterEffects":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".aep")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".aep"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")
                            pass
                        pathExists = False

            # ------ Photoshop
            elif CIOXO_SOFTWARE == "photoshop":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".psd")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".psd"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

        self.ui.button_ok.clicked.connect(createDirectory_fileShot)

        def closeWindow_createFileShot():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createFileShot)


# ------ CREATE FILE ASSET
class CreateFileAsset(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createFile()
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
            filePath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces",
                                    CIOXO_DISCIPLINE)
            fileName = CIOXO_ASSET + "_" + CIOXO_DISCIPLINE + "_v" + versionInput
            fileCommentPath = os.path.join(filePath,
                                           "." + CIOXO_ASSET + "_" + CIOXO_DISCIPLINE + "_v" + versionInput + "_comment.txt")
            comment = self.ui.plainTextEditComment.toPlainText()
            # ------ Create file
            # ------ Houdini
            if CIOXO_SOFTWARE == "houdini":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".hip")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".hiplc")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".hip"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Maya
            elif CIOXO_SOFTWARE == "maya":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".mb")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".ma")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".mb"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Substance
            elif CIOXO_SOFTWARE == "substance":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".spp")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".spp"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Nuke
            elif CIOXO_SOFTWARE == "nuke":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".nk")) is True or os.path.isfile(
                            os.path.join(filePath, fileName + ".nknc")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".nk"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ After Effects
            elif CIOXO_SOFTWARE == "afterEffects":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".aep")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".aep"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

            # ------ Photoshop
            elif CIOXO_SOFTWARE == "photoshop":
                pathExists = True
                while pathExists:
                    if os.path.isfile(os.path.join(filePath, fileName + ".psd")) is True:
                        self.ui.label_informations.setStyleSheet(label_informationsRed)
                        self.ui.label_informations.setText(
                            ">>> File already exists! - Change discipline or version up")
                        break
                    else:
                        # ------ Write file
                        os.makedirs(filePath, exist_ok=True)
                        with open(os.path.join(filePath, fileName + ".psd"), 'w'):
                            pass
                        self.ui.button_cancel.setText("Close")
                        pathExists = False
                        # ------ Comment condition
                        if comment == "":
                            # ------ Don't write comment if empty
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created - You can now close the window")
                            pass
                        else:
                            # ------ Write comment if not empty
                            with open(fileCommentPath, 'w') as f:
                                f.write(comment)
                            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
                            self.ui.label_informations.setText(
                                ">>> file created\n>>> Comment created - You can now close the window")

        self.ui.button_ok.clicked.connect(createDirectory_fileShot)

        def closeWindow_createFileShot():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createFileShot)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create File")


# ------ CREATE THUMBNAIL PROJECT
class CreateThumbnailProject(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createTumbnail()
        self.ui.setupUi(self)

        def browseThumbnail_project():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/",
                                                    "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.label_file.setText(fileName)

        self.ui.button_browse.clicked.connect(browseThumbnail_project)

        def openWindow_createThumbnail_project():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            # ------ Thumbnail project paths
            pathThumbnail = os.path.join(rootDir, CIOXO_PROJECT, "." + CIOXO_PROJECT + "_thumbnail.png")
            # ------ Save image as thumbnail
            imageFile = self.ui.label_file.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.button_cancel.setText("Close")
            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
            self.ui.label_informations.setText(">>> Thumbnail created - You can now close the window")

        self.ui.button_ok.clicked.connect(openWindow_createThumbnail_project)

        def closeWindow_createThumbnail_project():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createThumbnail_project)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Thumbnail")


# ------ CREATE THUMBNAIL ASSET
class CreateThumbnailAsset(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createTumbnail()
        self.ui.setupUi(self)

        def browseThumbnail_asset():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/",
                                                    "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.label_file.setText(fileName)

        self.ui.button_browse.clicked.connect(browseThumbnail_asset)

        def openWindow_createThumbnail_asset():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            # ------ Thumbnail assets paths
            assetPath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET)
            pathThumbnail = os.path.join(assetPath, "." + CIOXO_PROJECT + "_" + CIOXO_ASSET + "_thumbnail.png")
            # ------ Save image as thumbnail
            imageFile = self.ui.label_file.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.button_cancel.setText("Close")
            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
            self.ui.label_informations.setText(">>> Thumbnail created - You can now close the window")

        self.ui.button_ok.clicked.connect(openWindow_createThumbnail_asset)

        def closeWindow_createThumbnail_asset():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createThumbnail_asset)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Thumbnail")


# ------ CREATE THUMBNAIL FILE ASSET
class CreateThumbnailFileAsset(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createTumbnail()
        self.ui.setupUi(self)

        def browseThumbnail_fileAsset():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/",
                                                    "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.label_file.setText(fileName)

        self.ui.button_browse.clicked.connect(browseThumbnail_fileAsset)

        def openWindow_createThumbnail_fileAsset():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_ASSET = os.getenv("CIOXO_ASSET")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[2]
            # ------ Thumbnail files assets paths
            filePath = os.path.join(rootDir, CIOXO_PROJECT, "assets", CIOXO_ASSET, CIOXO_SOFTWARE, "workspaces",
                                    CIOXO_DISCIPLINE)
            pathThumbnail = os.path.join(filePath, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            # ------ Save image as thumbnail
            imageFile = self.ui.label_file.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.button_cancel.setText("Close")
            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
            self.ui.label_informations.setText(">>> Thumbnail created - You can now close the window")

        self.ui.button_ok.clicked.connect(openWindow_createThumbnail_fileAsset)

        def closeWindow_createThumbnail_fileAsset():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createThumbnail_fileAsset)

        # ------ Define window title
        self.setWindowTitle("Cioxo - Create Thumbnail")


# ------ CREATE THUMBNAIL SHOT
class CreateThumbnailShot(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createTumbnail()
        self.ui.setupUi(self)

        # ------ Window variable
        self.setWindowTitle("Cioxo - Create Thumbnail")

        def browseThumbnail_shot():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/",
                                                    "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.label_file.setText(fileName)

        self.ui.button_browse.clicked.connect(browseThumbnail_shot)

        def openWindow_createThumbnail_shot():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            # ------ Thumbnail shots paths
            shotPath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT)
            pathThumbnail = os.path.join(shotPath, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_thumbnail.png")
            # ------ Save thumbnail
            imageFile = self.ui.label_file.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.button_cancel.setText("Close")
            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
            self.ui.label_informations.setText(">>> Thumbnail created - You can now close the window")

        self.ui.button_ok.clicked.connect(openWindow_createThumbnail_shot)

        def closeWindow_createThumbnail_shot():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createThumbnail_shot)


# ------ CREATE THUMBNAIL FILE
class CreateThumbnailFile(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_cioxo_createTumbnail()
        self.ui.setupUi(self)

        # ------ Window variables
        self.setWindowTitle("Cioxo - Create Thumbnail")

        def browseThumbnail_filesSequences():
            # ------ Open explorer to choose picture
            USERNAME = os.getenv("USERNAME")
            fileName = QFileDialog.getOpenFileNames(self, "Open file", "C:/Users/" + USERNAME + "/Pictures/", "Images (*.png *.jpg *.bmp)")
            fileName = fileName[0]
            fileName = "".join(fileName)
            self.ui.label_file.setText(fileName)

        self.ui.button_browse.clicked.connect(browseThumbnail_filesSequences)

        def openWindow_createThumbnail_filesSequences():
            # ------ Cioxo variables
            CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
            CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
            CIOXO_SHOT = os.getenv("CIOXO_SHOT")
            CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
            CIOXO_FILE = os.getenv("CIOXO_FILE")
            CIOXO_DISCIPLINE = CIOXO_FILE.split(".")[0].split("_")[3]
            # ------- Paths
            filePath = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE, "workspaces", CIOXO_DISCIPLINE)
            pathThumbnail = os.path.join(filePath, "." + CIOXO_FILE.split(".")[0] + "_thumbnail.png")
            # ------- Save thumbnail
            imageFile = self.ui.label_file.text()
            image = Image.open(imageFile)
            image.thumbnail((256, 144), Image.ANTIALIAS)
            image.save(pathThumbnail)
            self.ui.button_cancel.setText("Close")
            self.ui.label_informations.setStyleSheet(labelInformationsGreen)
            self.ui.label_informations.setText(">>> Thumbnail created - You can now close the window")

        self.ui.button_ok.clicked.connect(openWindow_createThumbnail_filesSequences)

        def closeWindow_createThumbnail_filesSequences():
            self.close()

        self.ui.button_cancel.clicked.connect(closeWindow_createThumbnail_filesSequences)


# ------ SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main = ProjectManager()
        self.ui = Ui_cioxo_splashScreen()
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
