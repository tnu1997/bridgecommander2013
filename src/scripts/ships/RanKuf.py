import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = { 
		"FilenameHigh": "data/Models/Ships/Birdofprey/Birdofprey.nif",
		"FilenameMed": "data/Models/Ships/Birdofprey/Birdofprey.nif",
		"FilenameLow": "data/Models/Ships/Birdofprey/Birdofprey.nif",
		"Name": "RanKuf",
		"HardpointFile": "rankuf",
		"Species": Multiplayer.SpeciesToShip.BIRDOFPREY
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
    pStats = GetShipStats()
    if (not App.g_kLODModelManager.Contains(pStats['Name'])):
        pLODModel = App.g_kLODModelManager.Create(pStats['Name'])
        pLODModel.AddLOD(pStats['FilenameHigh'], 10, 40.0, 15.0, 15.0, 400, 900, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameMed'], 10, 100.0, 15.0, 15.0, 400, 900, '_glow', None, '_specular')
        pLODModel.AddLOD(pStats['FilenameLow'], 10, 500.0, 15.0, 30.0, 400, 900, '_glow', None, None)
        if (bPreLoad == 0):
            pLODModel.Load()
        else:
            pLODModel.LoadIncremental()

def PreLoadModel():
	LoadModel(1)
