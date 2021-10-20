import os
import hou


# Define JOB variable using HIP

HIP = hou.getenv("HIP")
hou.putenv("JOB", HIP)
hou.ui.displayMessage("JOB defined on: " + HIP)
