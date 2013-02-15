from bcdebug import debug
# Play the Campaign Victory Video, I think the video is a cool touch to the mod :)

# by USS Sovereign

# Imports
import App
import MissionLib

# Vars
SeqID = App.NULL_ID
pMoviePaneID = App.NULL_ID

# Play the movie
def PlayMovieSeq(pAction, pEvent):
                debug(__name__ + ", PlayMovieSeq")
                global SeqID, pMoviePaneID
    
                # Append actions & do the right thing (allow the user to skip the video of course)
                pMoviePane = App.TGPane_Create(1.0, 1.0)
                App.g_kRootWindow.PrependChild(pMoviePane)
                pMoviePane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__ + ".HandleKeyboard")
                pSequence = App.TGSequence_Create()        
                pAction = App.TGScriptAction_Create(__name__, "EnterMovie")
                pSequence.AppendAction(pAction)
                pMovie = App.TGMovieAction_Create("data/Movies/DS9FXCompletionVid.bik", 1, 1)
                pMovie.SetSkippable(1)
                pSequence.AppendAction(pMovie)
                pAction = App.TGScriptAction_Create(__name__, "ExitMovie")
                pSequence.AppendAction(pAction)
                pAction = App.TGScriptAction_Create(__name__, "KillPane")
                pSequence.AppendAction(pAction, 0.1)

                SeqID = pSequence.GetObjID()
                pMoviePaneID = pMoviePane.GetObjID()

                # Play the sequence when called
                pSequence.Play()


# Movie should be skippable so allow keyboard input
def EnterMovie(pAction):
        
                # Grab some values
                debug(__name__ + ", EnterMovie")
                pTopWindow = App.TopWindow_GetTopWindow()
                if (pTopWindow == None):
                        return None

                pTopWindow.SetNotVisible()

                # Disable options menu
                pTopWindow.DisableOptionsMenu(1)
                pTopWindow.AllowMouseInput(0)

                # Game paused
		App.g_kUtopiaModule.Pause(1)
		
		# Music Stopped
		App.g_kMusicManager.SetEnabled(0)

		App.InterfaceModule_DoTheRightThing()

                return 0


# Restore all options back to normal
def ExitMovie(pAction):
        
                # Grab some values again and switch out of movie mode
                debug(__name__ + ", ExitMovie")
                App.g_kMovieManager.SwitchOutOfMovieMode()
                
                pTopWindow = App.TopWindow_GetTopWindow()
                if (pTopWindow == None):
                        return None

                pTopWindow.SetVisible()

                # Restore all options back to default
                pTopWindow.DisableOptionsMenu(0)
                pTopWindow.AllowMouseInput(1)

                # Game unpaused
		App.g_kUtopiaModule.Pause(0)
		
		# Music Enabled
		App.g_kMusicManager.SetEnabled(1)

		try:
                    # A hack bugfix
                    pTop = App.TopWindow_GetTopWindow()
                    pTop.ForceBridgeVisible()
                    pTop.ForceTacticalVisible()
                    
                except:
                    pass

                return 0


# Check keys pressed and kill the sequence if needed
def HandleKeyboard(pPane, pEvent):
        debug(__name__ + ", HandleKeyboard")
        global SeqID

        # Basically this is from main menu
        KeyType = pEvent.GetKeyState()
	CharCode = pEvent.GetUnicode()

        # Check if esc key was pressed
        if KeyType == App.TGKeyboardEvent.KS_KEYUP:
            if (CharCode == App.WC_ESCAPE):
                pSequence = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(SeqID))
                try:
                    pSequence.Skip()
                except:
                    pass
                
                SeqID = App.NULL_ID

                BackToNormal(None)
                
                pEvent.SetHandled()

        if (pEvent.EventHandled() == 0):
		pPane.CallNextHandler(pEvent)


# Switch back to normal
def BackToNormal(pAction):
	debug(__name__ + ", BackToNormal")
	global SeqID
	SeqID = App.NULL_ID
        
	App.g_kMovieManager.SwitchOutOfMovieMode()

	# Game unpaused
	App.g_kUtopiaModule.Pause(0)
		
	# Music Enabled
	App.g_kMusicManager.SetEnabled(1)

	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return

	pTopWindow.SetVisible()

	pTopWindow.DisableOptionsMenu(0)
	pTopWindow.AllowMouseInput(1)

	try:
            # A hack bugfix
            pTop = App.TopWindow_GetTopWindow()
            pTop.ForceBridgeVisible()
            pTop.ForceTacticalVisible()
                    
        except:
            pass

        pSequence = App.TGSequence_Create()        
        pAct = App.TGScriptAction_Create(__name__, "KillPane")
        pSequence.AppendAction(pAct, 0.1)
        pSequence.Play()

	return 0


# Kill the pane, fixes the crashing bug and several other bugs
def KillPane(pAction):
        debug(__name__ + ", KillPane")
        global pMoviePaneID
        
        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pMoviePaneID))
	App.g_kRootWindow.DeleteChild(pPane)
	
	App.InterfaceModule_DoTheRightThing()
	
	pMoviePaneID = App.NULL_ID
	
	return 0
