import os

# Cioxo parameters
cioxoDiscipline = hou.node(".").evalParm('cioxoDiscipline')
cioxoLayer = hou.node(".").evalParm('cioxoLayer')

# Render path
hip = hou.expandString("$HIP")
sceneDirectory = os.path.join(hip, "render")
renderPath = os.path.join(sceneDirectory,cioxoDiscipline,cioxoLayer)
renderPath = renderPath.replace("\\", "/")

# Maximum version in directory
scanRenderPath = os.listdir(renderPath)
maxVersion = [i for i in scanRenderPath if i==max(scanRenderPath)]
maxVersion = map(int, maxVersion)
maxVersion = str(maxVersion)

# Auto version
removeListCharacters = "[]"
for characters in removeListCharacters:
    maxVersion = maxVersion.replace(characters,"")
autoVersion = int(maxVersion)
autoVersion = str(autoVersion)
autoVersionCount = len(autoVersion)
if autoVersionCount < 2:
    return "00" + autoVersion
elif autoVersionCount < 3:
    return "0" + autoVersion
else:
    return autoVersion
