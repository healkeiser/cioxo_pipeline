import os

nukeDirectory = nuke.script_directory()
cioxoDisk = nukeDirectory.split("/")[0]
cioxoRoot = nukeDirectory.split("/")[1]
cioxoClient = nukeDirectory.split("/")[2]
cioxoProject = nukeDirectory.split("/")[3]
cioxoSequence = nukeDirectory.split("/")[5]
cioxoShot = nukeDirectory.split("/")[6]
cioxoRenderPath = cioxoDisk + "/" + cioxoRoot + "/" + cioxoClient + "/" + cioxoProject + "/02_production/" + cioxoSequence + "/" +  cioxoShot + "/houdini/render"
cioxoComment = "metadata exr/cioxo/comment"

n = nuke.thisNode()
cioxoDiscipline = n['cioxoDiscipline'].value()
cioxoLayer = n['cioxoLayer'].value()
cioxoVersionPath = cioxoRenderPath + "/" + cioxoDiscipline + "/" + cioxoLayer
cioxoVersion = os.listdir(cioxoVersionPath)

n['cioxoVersion'].setValues(cioxoVersion)

cioxoVersion = n['cioxoVersion'].value()

n['cioxoFinalPath'].setValue("<i>" + cioxoVersionPath + "/" + cioxoVersion + "</i>")

if not cioxoComment:
    n['cioxoComment'].setValue("<i>No comment found</i>")
else:
    n['cioxoComment'].setValue("<i>" + nuke.tcl(cioxoComment) + "</i>")
