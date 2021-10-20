import os
from string import ascii_letters, digits

nukeDirectory = nuke.script_directory()
cioxoDisk = nukeDirectory.split("/")[0]
cioxoRoot = nukeDirectory.split("/")[1]
cioxoClient = nukeDirectory.split("/")[2]
cioxoProject = nukeDirectory.split("/")[3]
cioxoSequence = nukeDirectory.split("/")[5]
cioxoSequenceShort = cioxoSequence.split("_")[1]
cioxoShot = nukeDirectory.split("/")[6]
cioxoShotShort = cioxoShot.split("_")[1]
n = nuke.thisNode()
cioxoVersion = n['cioxoVersion'].value()

if set(cioxoVersion).difference(digits):
   n['cioxoVersionChecker'].setValue("<font color='red'>Invalid characters detected<font>")
else:
    n['cioxoVersionChecker'].setValue("<font color='green'>No invalid characters detected<font>")

renderPath = cioxoDisk + "/" + cioxoRoot + "/" + cioxoClient + "/" + cioxoProject + "/03_postproduction/" + cioxoSequence + "/" +  cioxoShot + "/nuke/output/"

scanRenderPath = os.listdir(renderPath)
maxVersion = [i for i in scanRenderPath if i==max(scanRenderPath)]
maxVersion = str(maxVersion)
autoVersion = maxVersion

if (len(autoVersion) == 0):
    n['cioxoAutoVersion'].setValue("No file existing")
else:
    n['cioxoAutoVersion'].setValue(autoVersion.translate({ord(i): None for i in "'[]'"}))
