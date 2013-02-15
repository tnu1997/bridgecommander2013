from bcdebug import debug
import App

INTRO_KMOLD="KobMaruIntro.bik"
INTO_DIR="data/Movies/"

pLoadDialog = App.STFileDialog_Create(0,0)
pFileMenu = pLoadDialog.GetFileMenu()
pFileMenu.SetDir(INTO_DIR)
pFileMenu.SetFilter(INTRO_KMOLD)
pLoadDialog.RefreshFileList()

if pFileMenu.GetNumChildren():
	pMod = __import__("MainMenu.mainmenu")
	if hasattr(pMod, "lIntroVideos"):
		lIntroVideos = pMod.lIntroVideos
		lIntroVideos.append(INTO_DIR + INTRO_KMOLD)
	else:
		print "Error: This is not a KM mainmenu"

def GetName():
    debug(__name__ + ", GetName")
    return "Play KM 0.9 Video"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
    debug(__name__ + ", CreateMenu")
    return None

def StartUp():
	debug(__name__ + ", StartUp")
	return
