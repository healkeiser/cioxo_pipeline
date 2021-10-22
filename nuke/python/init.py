import os

USERNAME = os.getenv("USERNAME")

nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath("./my_scripts")
nuke.pluginAddPath("./C:/Users/" + USERNAME + "/Documents/PROJECTS/.pipeline/all/ui")
nuke.pluginAddPath("./C:/Users/" + USERNAME + "/Documents/PROJECTS/.pipeline/all/ui/graphics/logos")

