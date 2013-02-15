from bcdebug import debug
# Play the beta credits sequence

# by USS Sovereign


# Imports
import App

# Vars
pSeq = App.NULL_ID
pSeq2 = App.NULL_ID

# DS9FX Version
pDS9FXVer = __import__("Custom.DS9FX.DS9FXVersionSignature")
pVer = pDS9FXVer.DS9FXVersion

# Call DS9FX Credits sequence sequence
def PlaySeq(pAction, pEvent):

        debug(__name__ + ", PlaySeq")
        DS9FXCredits(None, None)

# Start DS9FX Credits sequence
def DS9FXCredits(pObject, pEvent):
        # Grab some values
        debug(__name__ + ", DS9FXCredits")
        pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return

        # Disable top window and options menu
	pTopWindow.SetNotVisible()

	pTopWindow.DisableOptionsMenu(1)


        # Attach a pane
	pPane = App.TGPane_Create(1.0, 1.0)
	App.g_kRootWindow.PrependChild(pPane)



        # Add the keyboard listener function
	pPane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD,	__name__ + ".HandleKeyboard")

        # Stop all background movies
	import MainMenu.mainmenu

	MainMenu.mainmenu.StopBackgroundMovies()
	
        # Create a credits sequence and switch to warp set which is caled from the mainmenu.py
	pSequence = App.TGSequence_Create()
	pSequence.SetUseRealTime (1)
	pSequence.AddAction(App.TGScriptAction_Create("MainMenu.mainmenu", "ShowWarpBackground", 1))
	pSequence.AppendAction(CreditsSeq(pPane))
	pAction = App.TGScriptAction_Create(__name__, "BackToOptions")
	pAction.SetUseRealTime (1)
	pSequence.AppendAction(pAction, 1.0)
	pSequence.Play()

        # Get the ObjID of the sequence
	global pSeq2
        pSeq2 = pSequence.GetObjID()


# Credits sequence
def CreditsSeq(pPane):
        # Setting up grounds for the sequence
        debug(__name__ + ", CreditsSeq")
        App.InterfaceModule_DoTheRightThing()
        
	pSequence = App.TGSequence_Create()
	pSequence.SetUseRealTime (1)
	pSequence.SetSkippable(1)

        # Credit lines
	pAction = LineAction("DS9FX " + pVer, pPane, 8, 6, 20)
	pSequence.AddAction(pAction, None, 0)

	pAction = LineAction("by", pPane, 13, 5, 15)
	pSequence.AddAction(pAction, None, 1)

        pAction = LineAction("BCS : TNG", pPane, 18, 4, 18)
	pSequence.AddAction(pAction, None, 2)

	pAction = LineAction("Beta Squad:", pPane, 10, 35, 18)
	pSequence.AddAction(pAction, None, 8)

	pAction = LineAction("1DeadlySAMURAI\nAdonis\nAndrewJ\nAragorn\nBens\nBlackrook32\nblaXXer\nBren", pPane, 14, 4, 9)
	pSequence.AddAction(pAction, None, 9)

	pAction = LineAction("Cackad\nCapitan_Picard\nCaptGraham\ncobie2\nCpt.Eagleeye\nctman\nCube\nDante Leonhart", pPane, 14, 4, 9)
	pSequence.AddAction(pAction, None, 15)

	pAction = LineAction("DarkDragon\nDarkwaddi\ndazzharvey\nDarkthorne\nDragoon123\ndshash\nFekLeyr Targ\nGanstaUK", pPane, 14, 4, 9)
	pSequence.AddAction(pAction, None, 21)

	pAction = LineAction("Gamesfunk\nhellewellth\nInuyasha \njb06\nJimmyB76\nkai\nLegacy\nlapvlb", pPane, 14, 4,9)
	pSequence.AddAction(pAction, None, 27)

	pAction = LineAction("Mateo\nMichael Mendez\nMustang\nnaf9sd\nNebula\nNighthawk\nPsycho\nRob Archer\nredmanmark86", pPane, 14, 4, 9)
	pSequence.AddAction(pAction, None, 33)

	pAction = LineAction("Shinzon\nSuperSmeg\nspanner\nSwift\nThe Stig\ntrekie80\ntreleth\nWeaseal", pPane, 14, 4, 9)
	pSequence.AddAction(pAction, None, 39)

	pAction = LineAction("Thanks to all past, present and\n\nmaybe future Beta Testers!", pPane, 10, 5, 14)
	pSequence.AddAction(pAction, None, 45)

	pSequence.Play()

        # Grab the ObjID of the seq
        global pSeq
        pSeq = pSequence.GetObjID()
	
	return pSequence

# Add a line action 
def LineAction(sLine, pPane, fPos, duration, fontSize):
	debug(__name__ + ", LineAction")
	fHeight = fPos * 0.0375
	App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
	pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
	return pAction


# Check keys pressed and kill the credits sequence if needed
def HandleKeyboard(pPane, pEvent):
        debug(__name__ + ", HandleKeyboard")
        global pSeq, pSeq2

        # Basically this is from main menu
        KeyType = pEvent.GetKeyState()
	CharCode = pEvent.GetUnicode()

        # Check if esc key was pressed
        if KeyType == App.TGKeyboardEvent.KS_KEYUP:
            if (CharCode == App.WC_ESCAPE):
                pSequence = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(pSeq))
                pSequence2 = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(pSeq2))
                pSequence.Skip()
                pSequence2.Skip()
                pSeq = App.NULL_ID
                pSeq2 = App.NULL_ID

                BackToOptions (None)
                
                pEvent.SetHandled()

        if (pEvent.EventHandled() == 0):
		pPane.CallNextHandler(pEvent)

# Switch back to options
def BackToOptions(pAction):
	debug(__name__ + ", BackToOptions")
	global pSeq2, pSeq
	pSeq = App.NULL_ID
        pSeq2 = App.NULL_ID

	App.g_kMovieManager.SwitchOutOfMovieMode()

        import MainMenu.mainmenu
        
	MainMenu.mainmenu.ShowWarpBackground (None, 0)

	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return

	pPane = App.g_kRootWindow.GetNthChild (0)
	App.g_kRootWindow.DeleteChild (pPane)

	pTopWindow.SetVisible ()

	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
	MainMenu.mainmenu.SetVisible (pOptionsWindow, 1)
	pTopWindow.DisableOptionsMenu (0)

	App.InterfaceModule_DoTheRightThing()

	return 0
