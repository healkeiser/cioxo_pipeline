import os
from string import ascii_letters, digits
from datetime import date

# Get env variables
cioxoClient = os.getenv('CLIENT')
cioxoProject = os.getenv('PROJECT')
cioxoSequence = os.getenv('SEQ')
cioxoSequenceShort = cioxoSequence.split("_")[1]
cioxoShot = os.getenv('SHOT')
cioxoShotShort = cioxoShot.split("_")[1]

# Define root
def rootDirectory():
    return 'X:/FREELANCE'

renderPath = os.path.join(rootDirectory(), cioxoClient, cioxoProject, '03_postproduction', cioxoSequence, cioxoShot, 'nuke/output')

# Link values to node parameter
n = nuke.thisNode()

# Check characters in Version string
cioxoVersion = n['cioxoVersion'].value()
if set(cioxoVersion).difference(digits):
   n['cioxoVersionChecker'].setValue("<font color='red'>Invalid characters detected<font>")
else:
    n['cioxoVersionChecker'].setValue("<font color='green'>No invalid characters detected<font>")

# Scan Last version existing
scanRenderPath = os.listdir(renderPath)
maxVersion = [i for i in scanRenderPath if i==max(scanRenderPath)]
maxVersion = str(maxVersion)
autoVersion = maxVersion

if (len(autoVersion) == 0):
    n['cioxoAutoVersion'].setValue("No file existing")
else:
    n['cioxoAutoVersion'].setValue(autoVersion.translate({ord(i): None for i in "'[]'"}))

# Show render path
cioxoPath = renderPath + "/" + cioxoVersion
cioxoPath = cioxoPath.replace('\\', '/')
n['cioxoPath'].setValue(cioxoPath)

# Show dailies path
dailiesTime = date.today().strftime("%d.%m.%Y")
dailiesPath = os.path.join(rootDirectory(), cioxoClient, cioxoProject, '04_other/dailies', dailiesTime)
cioxoDailiesPath = dailiesPath.replace('\\', '/')
n['cioxoDailiesPath'].setValue(cioxoDailiesPath)
