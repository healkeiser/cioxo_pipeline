import os
import hou
from string import ascii_letters, digits

# Cioxo parameters
cioxoVersion = hou.node(".").evalParm('cioxoVersion')

# Check characters in string
if set(cioxoVersion).difference(digits):
    return ("Invalid characters detected")
else:
    return ("No invalid characters detected")
