from bcdebug import debug
# Play the movie sequence based on Defiants fixmem.py and Maelstorm Campaign E8M2 Mission I think...
# Anyway the last mission where the game plays these movies

# by USS Sovereign

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pVideoSelection = pModule.VideoSelection


# Imports
import App
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

# Vars
iAllowExitFromVideoView = 0

# Movie sequence
def PlayMovieSeq(pAction, pEvent):
        debug(__name__ + ", PlayMovieSeq")
        global iAllowExitFromVideoView 

        if pVideoSelection == 1:
                # Append actions
                pSequence = App.TGSequence_Create()        
                pAction = App.TGScriptAction_Create(__name__, "EnterMovie")
                pSequence.AppendAction(pAction)
                pMovie = App.TGMovieAction_Create("data/Movies/DS9FXWormholeSeq.bik", 1, 1)
                pSequence.AppendAction(pMovie)
                pAction = App.TGScriptAction_Create(__name__, "ExitMovie")
                pSequence.AppendAction(pAction)

                # Play the sequence when called
                pSequence.Play()

                iAllowExitFromVideoView = None
                iAllowExitFromVideoView = 0

        else:
                # Because the sound is played, we need to compensate
                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AllowExit", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)
                return


# You cannot quit the movie it has to be played
def EnterMovie(pAction):
        debug(__name__ + ", EnterMovie")
        global iAllowExitFromVideoView
        
        # Grab some values
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return None

	pTopWindow.SetNotVisible()

        # Do not allow user tampering
	pTopWindow.DisableOptionsMenu(1)
	pTopWindow.AllowKeyboardInput(0)
	pTopWindow.AllowMouseInput(0)

        iAllowExitFromVideoView = None
        iAllowExitFromVideoView = 0

	return 0

# Restore all options
def ExitMovie(pAction):
        debug(__name__ + ", ExitMovie")
        global iAllowExitFromVideoView
        
        # Grab some values again and switch out of movie mode
        App.g_kMovieManager.SwitchOutOfMovieMode()
        
        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

	pTopWindow.SetVisible()

        # Restore all options back to default
	pTopWindow.DisableOptionsMenu(0)
	pTopWindow.AllowKeyboardInput(1)
	pTopWindow.AllowMouseInput(1)

        iAllowExitFromVideoView = None
	iAllowExitFromVideoView = 1

	return 0


def CheckExitFromVideo():
        debug(__name__ + ", CheckExitFromVideo")
        global iAllowExitFromVideoView
        
        return iAllowExitFromVideoView


def AllowExit(pObject, pEvent):
        debug(__name__ + ", AllowExit")
        global iAllowExitFromVideoView

        iAllowExitFromVideoView = None
        iAllowExitFromVideoView = 1
