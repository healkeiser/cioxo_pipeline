import os

nukeDirectory = nuke.script_directory()
cioxoDisk = nukeDirectory.split("/")[0]
cioxoRoot = nukeDirectory.split("/")[1]
cioxoClient = nukeDirectory.split("/")[2]
cioxoProject = nukeDirectory.split("/")[3]
cioxoSequence = nukeDirectory.split("/")[5]
cioxoSequenceShort = cioxoSequence.split("_")[1]
cioxoShot = nukeDirectory.split("/")[6]
cioxoShotShort = cioxoShot.split("_")[1]
cioxoRenderPath = cioxoDisk + "/" + cioxoRoot + "/" + cioxoClient + "/" + cioxoProject + "/03_postproduction/" + cioxoSequence + "/" +  cioxoShot + "/nuke/output"


n = nuke.thisNode()

n['cioxoClient'].setValue("<b><font color='#ffbc04'>" + cioxoClient + "<font></b>")
n['cioxoClientControl'].setValue(cioxoClient)

n['cioxoProject'].setValue("<b><font color='#ffbc04'>" + cioxoProject + "<font></b>")
n['cioxoProjectControl'].setValue(cioxoProject)

n['cioxoSequence'].setValue("<b><font color='#ffbc04'>" + cioxoSequence.split("_")[1] + "<font></b>")
n['cioxoSequenceControl'].setValue(cioxoSequence)
n['cioxoSequenceShort'].setValue(cioxoSequenceShort)

n['cioxoShot'].setValue("<b><font color='#ffbc04'>" + cioxoShot.split("_")[1] + "<font></b>")
n['cioxoShotControl'].setValue(cioxoShot)
n['cioxoShotShort'].setValue(cioxoShotShort)
