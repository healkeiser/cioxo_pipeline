import os

# Cioxo parameters
cioxoProject = hou.node(".").evalParm('cioxoProject')
cioxoDiscipline = hou.node(".").evalParm('cioxoDiscipline')
cioxoSequence = hou.node(".").evalParm('cioxoSequence')
cioxoShot = hou.node(".").evalParm('cioxoShot')
cioxoLayer = hou.node(".").evalParm('cioxoLayer')
cioxoVersion = hou.node(".").evalParm('cioxoVersion')

# Render path
hip = hou.expandString("$HIP")
sceneDirectory = os.path.join(hip, "render")
renderFile = str(cioxoProject + '_' + cioxoSequence + '_' + cioxoShot + '_v' + cioxoVersion +'.$F4.exr')
renderPath = os.path.join(sceneDirectory,cioxoDiscipline,cioxoLayer,cioxoVersion,renderFile)
renderPath = renderPath.replace("\\", "/")

return renderPath
