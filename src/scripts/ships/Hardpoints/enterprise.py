# C:\Utopia\Current\Build\scripts\ships\Hardpoints\enterprise.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.sovereign"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.sovereign", globals(), locals(), ['*'])
	reload(ParentModule)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
