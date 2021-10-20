import os
from string import ascii_letters, digits

# Cioxo parameters
cioxoLayer = hou.node(".").evalParm('cioxoLayer')

# Check characters in string
if set(cioxoLayer).difference(ascii_letters):
    return ("Invalid characters detected")
else:
    return ("No invalid characters detected")
