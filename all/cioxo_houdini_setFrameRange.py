import os
import hou


# ------ Define Frame Range using .txt files created by Cioxo - Project Manager


# ------ Cioxo variables
rootDir = os.getenv("CIOXO_ROOT")
CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
CIOXO_SHOT = os.getenv("CIOXO_SHOT")

# ------ Get Frame Range from file
frameRangeFile = os.path.join(rootDir, CIOXO_PROJECT, CIOXO_SEQUENCE, CIOXO_SHOT, "." + CIOXO_PROJECT + "_" + CIOXO_SEQUENCE + "_" + CIOXO_SHOT + "_frameRange.txt")
if os.path.isfile(frameRangeFile):
    with open(frameRangeFile) as f:
        frameRange = f.readline()
    frameStart = frameRange.split("_")[0]
    frameEnd = frameRange.split("_")[1]
    hou.playbar.setFrameRange(int(frameStart), int(frameEnd))
    hou.playbar.setPlaybackRange(int(frameStart), int(frameEnd))
else:
    hou.ui.displayMessage("No Frame Range found in Cioxo - Project Manager", severity=hou.severityType.Warning)
