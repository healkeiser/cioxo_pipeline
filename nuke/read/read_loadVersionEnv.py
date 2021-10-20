import os

# Get env variables
cioxoClient = os.getenv('CLIENT')
cioxoProject = os.getenv('PROJECT')
cioxoSequence = os.getenv('SEQ')
cioxoSequenceShort = cioxoSequence.split("_")[1]
cioxoShot = os.getenv('SHOT')
cioxoShotShort = cioxoShot.split("_")[1]
cioxoComment = "metadata exr/cioxo/comment"

# Scan for Discipline
def rootDirectory():
    return 'X:/FREELANCE'

renderPath = os.path.join(rootDirectory(), cioxoClient, cioxoProject, '02_production', cioxoSequence, cioxoShot, 'houdini/render')
cioxoDiscipline = os.listdir(renderPath)

# Link values to node parameter
n = nuke.thisNode()
cioxoDiscipline = n['cioxoDiscipline'].value()
cioxoLayer = n['cioxoLayer'].value()
cioxoVersionPath = renderPath + "/" + cioxoDiscipline + "/" + cioxoLayer
cioxoVersion = os.listdir(cioxoVersionPath)
n['cioxoVersion'].setValues(cioxoVersion)

# Define path to show
cioxoVersion = n['cioxoVersion'].value()
cioxoPath = cioxoVersionPath + "/" + cioxoVersion
cioxoPath = cioxoPath.replace('\\', '/')
n['cioxoPath'].setValue(cioxoPath)

# Show comment from MetaDatas
n['cioxoComment'].setValue(str(nuke.tcl(cioxoComment)))
