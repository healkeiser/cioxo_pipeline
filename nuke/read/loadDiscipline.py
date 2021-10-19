import os

# ------ CIOXO environment
nukeDirectory = nuke.script_directory()
CIOXO_ROOT = os.getenv("CIOXO_ROOT")
CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
CIOXO_SHOT = os.getenv("CIOXO_SHOT")
cioxoRenderPath = os.path.join(CIOXO_ROOT, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "/houdini/render")

n = nuke.thisNode()
cioxoDiscipline = n['cioxoDiscipline'].value()
cioxoLayerPath = cioxoRenderPath + "/" + cioxoDiscipline
cioxoLayer = os.listdir(cioxoLayerPath)

n['cioxoLayer'].setValues(cioxoLayer)
