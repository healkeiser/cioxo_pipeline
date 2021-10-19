import os

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

n['cioxoClientDisplay'].setValue("<b><font color='#ffbc04'>"+cioxoClient+"<font></b>")
n['cioxoClient'].setValue(cioxoClient)

n['cioxoProjectDisplay'].setValue("<b><font color='#ffbc04'>"+cioxoProject+"<font></b>")
n['cioxoProject'].setValue(cioxoProject)

n['cioxoSequenceDisplay'].setValue("<b><font color='#ffbc04'>"+cioxoSequence+"<font></b>")
n['cioxoSequence'].setValue(cioxoSequence)
n['cioxoSequenceShort'].setValue(cioxoSequenceShort)

n['cioxoShotDisplay'].setValue("<b><font color='#ffbc04'>"+cioxoShot+"<font></b>")
n['cioxoShot'].setValue(cioxoShot)
n['cioxoShotShort'].setValue(cioxoShotShort)
