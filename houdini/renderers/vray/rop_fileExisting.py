import os

# Cioxo parameters
cioxoDiscipline = hou.node(".").evalParm('cioxoDiscipline')
cioxoLayer = hou.node(".").evalParm('cioxoLayer')
cioxoVersion = hou.node(".").evalParm('cioxoVersion')

# Render path
hip = hou.expandString("$HIP")
sceneDirectory = os.path.join(hip, "render")
renderPath = os.path.join(sceneDirectory,cioxoDiscipline,cioxoLayer,cioxoVersion)
#renderPath = renderPath.replace("\\", "/")

#return renderPath

if os.path.exists(renderPath):
    return ("File already existing")
else:
    return ("File does not exist")
