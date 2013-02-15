import App
import Multiplayer.SpeciesToShip


def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Bioship/Bioship.nif",
		"FilenameLow": "data/Models/Ships/Bioship/Bioship.nif",
		"FilenameMed": "data/Models/Ships/Bioship/Bioship.nif",
		"Name": "Bioship",
		"HardpointFile": "Bioship",
		"Species": Multiplayer.SpeciesToShip.AMBASSADOR
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 200.0, 15.0, 15.0, 400, 900, "", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameHigh"],  10, 400.0, 15.0, 15.0, 400, 900, "", None, "_spec")
		pLODModel.AddLOD(pStats["FilenameHigh"],  10, 800.0, 15.0, 30.0, 400, 900, "", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
