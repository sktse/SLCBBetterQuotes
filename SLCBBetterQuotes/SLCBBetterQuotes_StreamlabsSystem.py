#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")


#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    pass

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    pass

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return
