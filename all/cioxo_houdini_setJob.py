import os
# import hou


# Define JOB variable using HIP

HIP = hou.getenv("HIP")
print(HIP)
hou.putenv("JOB", HIP)
