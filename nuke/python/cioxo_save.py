import nukescripts
import nuke
import re
import os
from glob import glob


# ----- Cioxo variables
CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
CIOXO_SHOT = os.getenv("CIOXO_SHOT")
CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
CIOXO_FILE = os.getenv("CIOXO_FILE")
cioxo_discipline = CIOXO_FILE.split(".")[0].split("_")[3]
USERNAME = os.getenv("USERNAME")
rootDir = os.getenv("CIOXO_ROOT")
version = str("v0.0.1-alpha")


# Nuke shot directory accorded to env variables
def nukeDirectory():
    nukeDirectory = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, CIOXO_SOFTWARE)
    if not os.path.isdir(nukeDirectory):
        print('Nuke directory does not exist')
    return nukeDirectory


def cioxoSave():
    nukeDirectorySave = nukeDirectory()
    nukeNonCommercial = '.nknc'
    nukeCommercial = '.nk'
    # Get description but remove all the white spaces
    description = nuke.getInput("script description", "compositing").replace(' ', '')

    fileSaved = False
    version = 1
    while not fileSaved:
        # File name
        nukeName = '%s_%s_%s_%s_v%03d.nknc' % (CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, description, version)
        # Join directory to form full path
        nukePath = os.path.join(nukeDirectorySave, nukeName)
        # Version up on existing file
        if os.path.isfile(nukePath):
            version += 1
            continue
        # Save script
        nuke.scriptSaveAs(nukePath)
        fileSaved = True
    return nukePath
