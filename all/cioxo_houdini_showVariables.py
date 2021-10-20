import os
import hou


# ------ Show environment variables


# ------ Cioxo variables
CIOXO_PROJECT = os.getenv("CIOXO_PROJECT")
CIOXO_SEQUENCE = os.getenv("CIOXO_SEQUENCE")
CIOXO_SHOT = os.getenv("CIOXO_SHOT")
CIOXO_SOFTWARE = os.getenv("CIOXO_SOFTWARE")
CIOXO_DISCIPLINE = os.getenv("CIOXO_DISCIPLINE")

message = "Cioxo Project:   " + CIOXO_PROJECT + "\n" + "Cioxo Sequence:   " + CIOXO_SEQUENCE + "\n" + "Cioxo Shot:   " + CIOXO_SHOT + "\n" + "Cioxo Software:   " + CIOXO_SOFTWARE + "\n" + "Cioxo Discipline:   " + CIOXO_DISCIPLINE
hou.ui.displayMessage(message)
