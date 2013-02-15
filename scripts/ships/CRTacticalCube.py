import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/BorgShips/BorgTacticalCube.nif",
		"FilenameMed": "data/Models/Ships/BorgShips/BorgTacticalCube.nif",
		"FilenameLow": "data/Models/Ships/BorgShips/BorgTacticalCube.nif",
		"Name": "BorgTacticalCube",
		"HardpointFile": "CRTacticalCube",
		"Species": Multiplayer.SpeciesToShip.WARBIRD,
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
		# ***FIXME: Not all 3 levels of detail need OBB trees.  PickLeafSize should be 0 for the unused ones.
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  500.0, 150.0, 150.0, 400, 900, "_glow", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameMed"],  10,  250.0, 300.0, 300.0, 400, 900, "_glow", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameLow"],  10,  125.0, 600.0, 600.0, 400, 900, "_glow", None, None)
		
#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
