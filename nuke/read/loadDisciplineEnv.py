import os

# Get env variables
cioxoClient = os.getenv('CLIENT')
cioxoProject = os.getenv('PROJECT')
cioxoSequence = os.getenv('SEQ')
cioxoSequenceShort = cioxoSequence.split("_")[1]
cioxoShot = os.getenv('SHOT')
cioxoShotShort = cioxoShot.split("_")[1]

# Scan for Discipline
def rootDirectory():
    return 'X:/FREELANCE'

renderPath = os.path.join(rootDirectory(), cioxoClient, cioxoProject, '02_production', cioxoSequence, cioxoShot, 'houdini/render')
cioxoDiscipline = os.listdir(renderPath)

# Link values to node parameter
n = nuke.thisNode()

cioxoDiscipline = n['cioxoDiscipline'].value()
cioxoLayerPath = renderPath + "/" + cioxoDiscipline
cioxoLayer = os.listdir(cioxoLayerPath)

n['cioxoLayer'].setValues(cioxoLayer)
