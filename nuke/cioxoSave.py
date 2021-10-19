import nukescripts
import nuke
import re
import os
from glob import glob


# Temporary env variables
# os.environ['CLIENT'] = 'valentin'
# os.environ['PROJECT'] = 'nsl'
# os.environ['SEQ'] = 'seq_001'
# os.environ['SHOT'] = 'sh_lily'

# Root directory (basis for all projects)
def rootDirectory():
    return 'X:/FREELANCE'


# Nuke shot directory accorded to env variables
def nukeDirectory():
    nukeDirectory = os.path.join(rootDirectory(), os.getenv('CLIENT'), os.getenv('PROJECT'), '03_postproduction',
                                 os.getenv('SEQ'), os.getenv('SHOT'), 'nuke')
    if not os.path.isdir(nukeDirectory):
        print('Nuke directory does not exist')
    return nukeDirectory


def cioxoSave():
    nukeDirectorySave = nukeDirectory()
    nukeNonCommercial = '.nknc'
    nukeCommercial = '.nk'
    # Get description but remove all the white spaces
    description = nuke.getInput('script description', 'compositing').replace(' ', '')

    fileSaved = False
    version = 1
    while not fileSaved:
        # File name
        nukeName = '%s_%s_%s_%s_v%03d.nknc' % (
        os.getenv('PROJECT'), os.getenv('SEQ'), os.getenv('SHOT'), description, version)
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
