import os

# Get env variables
cioxoClient = os.getenv('CLIENT')
cioxoProject = os.getenv('PROJECT')
cioxoSequence = os.getenv('SEQ')
cioxoSequenceShort = cioxoSequence.split("_")[1]
cioxoShot = os.getenv('SHOT')
cioxoShotShort = cioxoShot.split("_")[1]

np = nuke.thisParent()
cioxoVersion = np['cioxoVersion'].value()

# Define paths
def rootDirectory():
    return 'X:/FREELANCE'

renderPath = os.path.join(rootDirectory(), cioxoClient, cioxoProject, '03_postproduction', cioxoSequence, cioxoShot, 'nuke/output')
dailiesTime = date.today().strftime("%d.%m.%Y")
dailiesPath = os.path.join(rootDirectory(), cioxoClient, cioxoProject, '04_other/dailies', dailiesTime)
