from

toolbar = nuke.menu('Nodes')
menu = nuke.menu('Nuke')
gizmoVersion = 'v1'

# Align script
menu.addCommand('Scripts/align', 'align.aligner()')

# Cioxo save
import cioxo_save
menu.addCommand('Cioxo' + '/Save Comp', cioxo_save.cioxoSave)

from all import cioxo_houdini_openWorkspace
menu.addCommand('Cioxo' + '/Open Workspace', cioxo_save.cioxoSave)

# Cioxo toolbar
cioxo = toolbar.addMenu('Cioxo', icon="./C:/Users/" + USERNAME + "/Documents/PROJECTS/.pipeline/all/ui/graphics/logos/cioxoLogoBorder_24_32.png")
cioxo.addCommand('Gather', "nuke.createNode('cioxoGather_v1')", icon='Read.png')
cioxo.addCommand('AOVs', "nuke.createNode('cioxoAovs_v1')", icon='Merge.png')
cioxo.addCommand('Write', "nuke.createNode('cioxoWrite_v1')", icon='Write.png')
