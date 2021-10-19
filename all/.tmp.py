# ----- Look for disciplines folders
foldersDisciplineList = []
for folderDisciplines in os.listdir(os.path.join(filesPath, "workspaces")):
    foldersDisciplineList.append(folderDisciplines)
    # ------ Look for houdini files
    for disciplines in foldersDisciplineList:
        filesHoudini = os.listdir(os.path.join(filesPath, "workspaces", disciplines))
    self.ui.listFilesSequences.addItems(filesHoudini)