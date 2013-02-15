from bcdebug import debug
# Play the credits sequence

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

	pAction = LineAction("Project & Programming Lead:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 8)

	pAction = LineAction("USS Sovereign", pPane, 14, 4, 14)
	pSequence.AddAction(pAction, None, 9)

	pAction = LineAction("Project XO:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 15)

	pAction = LineAction("Psycho", pPane, 14, 4, 12)
	pSequence.AddAction(pAction, None, 16)

	pAction = LineAction("Additional Programming:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 22)

	pAction = LineAction("Wowbagger\n\nLost_Jedi\n\nMLeo\n\nCackad", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 23)
	
        pAction = LineAction("Ships/Models/Retextures:", pPane, 10, 29, 18)
	pSequence.AddAction(pAction, None, 29)

	pAction = LineAction("LC Amaral\nBlaxxer\nSteven Davis\nZambie Zan\n9 of 9", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 30)
	
        pAction = LineAction("Mark\nBlackrook32\nLaurelin\nSmiley\nAdonis", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 36)

        pAction = LineAction("C2X\nP81\nPsycho\nScotchy\nCaptainRussell", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 42)

        pAction = LineAction("Sean Kennedy\nDurandal\nJeff Wallace\nATRA-HASIS\nWickedZombie45\nRob Archer", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 48)

        pAction = LineAction("DamoclesX\nRedragon\nNeoXarchNova\nZorg / Morpheus\nCube\nCollective Alliance", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 54)

	pAction = LineAction("Hardpoints/Weapon Scripts:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 60)
	
	pAction = LineAction("Elminster\nPsycho\nUSS Sovereign\nDkealt\nDurandal", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 61)

	pAction = LineAction("Music/SFX/Dialogue:", pPane, 10, 11, 18)
	pSequence.AddAction(pAction, None, 67)

	pAction = LineAction("Marcus Kleine\nRussell Watson\nBary McCreary\nBlackRook32", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 68)

	pAction = LineAction("Creative Inc\nC2X\nZambie Zan\nCaptainKeyes\nUSS Sovereign", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 74)

	pAction = LineAction("Logo designs:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 80)

	pAction = LineAction("Psycho\nMark", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 81)

	pAction = LineAction("Videos:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 87)

	pAction = LineAction("Dante Leonhart\nCyberOps\nUSS Sovereign", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 88)

	pAction = LineAction("Mission storylines:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 94)

	pAction = LineAction("CaptainKeyes\nBlaxxer", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 95)

	pAction = LineAction("Misc Credits:", pPane, 10, 5, 18)
	pSequence.AddAction(pAction, None, 101)

	pAction = LineAction("MLeo\nNanobyte\nDefiant", pPane, 14, 4, 10)
	pSequence.AddAction(pAction, None, 102)

	pAction = LineAction("Special thanks to all Beta Testers, \n\n\nto everyone who supported this mod \n\n\nand everyone involved.", pPane, 10, 5, 14)
	pSequence.AddAction(pAction, None, 108)

	pAction = LineAction("We hope that you will enjoy this mod.\n\n\nDS9FX Team wishes you happy gaming!", pPane, 10, 5, 14)
	pSequence.AddAction(pAction, None, 115)

	pAction = LineAction("BCS : TNG Contact:\n\nhttp://bcscripters.us.to/\n\nhttp://forums.bcscripters.us.to/", pPane, 10, 5, 14)
	pSequence.AddAction(pAction, None, 122)
	
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
