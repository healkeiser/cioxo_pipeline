import os

# ------ CIOXO environment
nukeDirectory = nuke.script_directory()
CIOXO_ROOT = os.getenv("CIOXO_ROOT")
CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
CIOXO_SHOT = os.getenv("CIOXO_SHOT")
cioxoRenderPath = os.path.join(CIOXO_ROOT, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "houdini/render")
cioxoDiscipline = os.listdir(cioxoRenderPath)

n = nuke.thisNode()

n['cioxoProjectDisplay'].setValue("<b><font color='#ffbc04'>" + CIOXO_PROJECT + "<font></b>")
n['cioxoProject'].setValue(CIOXO_PROJECT)

n['cioxoSequenceDisplay'].setValue("<b><font color='#ffbc04'>" + CIOXO_SEQUENCE + "<font></b>")
n['cioxoSequence'].setValue(CIOXO_SEQUENCE)

n['cioxoShotDisplay'].setValue("<b><font color='#ffbc04'>" + CIOXO_SHOT + "<font></b>")
n['cioxoShot'].setValue(CIOXO_SHOT)

n['cioxoDiscipline'].setValues(cioxoDiscipline)
