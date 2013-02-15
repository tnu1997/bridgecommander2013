from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# by USS Sovereign, Mission 5 from the campaign

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pIntroVid = pModule.IntroVid
pCompletionVid = pModule.CompletionVid

# Imports
import App
import loadspacehelper
import MissionLib
import Custom.DS9FX.DS9FXmain
import nt
import string
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

# Events
ET_ACCEPT = App.Mission_GetNextEventType() + 1
ET_DECLINE = App.Mission_GetNextEventType() + 2

# Vars
pPane = None
pMainPane = None
ObjectiveShipList = []
pPaneID = App.NULL_ID

# Briefing function
def Briefing():
        debug(__name__ + ", Briefing")
        global pMainPane, pPane
        
        # Redesigned code to fix Cackad's issue with the GUI he attempted to make
        pPane = App.TGPane_Create(1.0, 1.0) 
	pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
	pTCW.AddChild(pPane, 0, 0) 
	pMainPane = App.TGPane_Create(0.60, 0.65) 
	pPane.AddChild(pMainPane, 0.22, 0.12)
                
        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        # Setup Events
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_DECLINE, pMission, __name__ + ".Decline")

        # Create Entries now
        CreateEntries(None, None)


# Create buttons & Mission Briefing
def CreateEntries(pObject, pEvent):
        debug(__name__ + ", CreateEntries")
        global pMainPane, pPane

        # Windows created first, just to be honest! I hate Microsoft's Windows :P
        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Once More Unto The Breach"), 0.0, 0.0, None, 1, 0.30, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Go to the Gamma Quadrant\n-Destroy all Dominion ships"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)
        
        pText = App.TGParagraph_CreateW(App.TGString("The Dominion just confirmed that their taskforce was destroyed on the far side of the wormhole by the rogues. So it is up to you once again to head to the Gamma Quadrant and put an end to the threat."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pBriefingWindow.AddChild(pText, 0, 0.01)

        # Create an icon... Cackad promised not to poke with my code anymore if I use his suggestions
        CreateRandomIcon(pIconWindow)

        x = 0
        y = 0.01
        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_ACCEPT)
        pEvent.SetString("Accepting")
        pButton = App.STRoundedButton_CreateW(App.TGString("Accept Mission"), pEvent, 0.13125, 0.034583)
        pButton.SetNormalColor(App.g_kMainMenuButtonColor)
        pButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
        pButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
        pButton.SetDisabledColor(App.g_kSTMenu1Disabled)
        pButton.SetColorBasedOnFlags()
        pButtonWindow.AddChild(pButton, x, y)


        x = 0 + 0.2
        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_DECLINE)
        pEvent.SetString("Declining")
        pButton = App.STRoundedButton_CreateW(App.TGString("Decline Mission"), pEvent, 0.13125, 0.034583)
        pButton.SetNormalColor(App.g_kMainMenuButtonColor)
        pButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
        pButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
        pButton.SetDisabledColor(App.g_kSTMenu1Disabled)
        pButton.SetColorBasedOnFlags()
        pButtonWindow.AddChild(pButton, x, y)

        # Glass background for pMainPane
	pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
	pLCARS = pGraphicsMode.GetLcarsString() 
	pGlass = App.TGIcon_Create(pLCARS, 120) 
	pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
	pMainPane.AddChild(pGlass, 0, 0) 

        # Change interior size and refresh windows
        pIconWindow.InteriorChangedSize()
        pIconWindow.Layout()
        pObjectivesWindow.InteriorChangedSize()
        pObjectivesWindow.Layout()
        pBriefingWindow.InteriorChangedSize()
        pBriefingWindow.Layout()
        pButtonWindow.InteriorChangedSize()
        pButtonWindow.Layout()
        pMainPane.Layout()
        pPane.Layout()

        # Switch to outside view
        pTop = App.TopWindow_GetTopWindow()
        pTop.ForceTacticalVisible()

        # Now show the pane
        pPane.SetVisible()

# Used partial Cackad's code
def CreateRandomIcon(pWindow):
    
        debug(__name__ + ", CreateRandomIcon")
        from Custom.DS9FX.DS9FXIconManager import IconManager

        IconManager.LoadDS9FX_Icons()
        
        pIcon = App.TGIcon_Create("DS9FX_Icons", App.SPECIES_UNKNOWN)
        pIcon.Resize(0.26, 0.25)
        pIcon.SetVisible()
        # Randomize icon selection
        pSelection = GetRandomRate(1)
        pIcon.SetIconNum(pSelection)
        
        pWindow.AddChild(pIcon,0.01,0.01)
    

# Returns a random number in between 1 and 17
def GetRandomRate(iNumber):

        debug(__name__ + ", GetRandomRate")
        return App.g_kSystemWrapper.GetRandomNumber(16) + iNumber


# Mission rejected!
def Decline(pObject, pEvent):
        debug(__name__ + ", Decline")
        global pMainPane, pPane

         # A bugfix
        try:
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()

            App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
            App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")

        except:
            pass

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        # New way of getting rid of a window, destroy it.
        App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

        pTCW.DeleteChild(pPane)

        pPane = None
        
        pMainPane = None

                    
# Mission Accepted, Initialize all handlers. Kill Mission Briefing Menu
def Accept(pObject, pEvent):
        debug(__name__ + ", Accept")
        global pMainPane, pPane

         # A bugfix
        try:
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()

            App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
            App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")

        except:
            pass

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        # New way of getting rid of a window, destroy it.
        App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

        pTCW.DeleteChild(pPane)

        pPane = None
        
        pMainPane = None

        MissionTittle(None, None)

        MissionInitiate(None, None)

# Tell the user that he is in a mission
def MissionTittle(pObject, pEvent):
            debug(__name__ + ", MissionTittle")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(TextSequence(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Print the text to the screen
def TextSequence(pPane):
            # Sequence which contains only 1 line of text
            debug(__name__ + ", TextSequence")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # prompt
            pAction = LineAction("Mission: Once More Unto The Breach", pPane, 3, 6, 16)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# Add a line action 
def LineAction(sLine, pPane, fPos, duration, fontSize):
	debug(__name__ + ", LineAction")
	fHeight = fPos * 0.0375
	App.TGCreditAction_SetDefaultColor(1.00, 1.00, 1.00, 1.00)
	pAction = App.TGCreditAction_CreateSTR(sLine, pPane, 0.0, fHeight, duration, 0.25, 0.5, fontSize)
	return pAction
    

# Start up needed handlers 
def MissionInitiate(pObject, pEvent):
        debug(__name__ + ", MissionInitiate")
        global pPlayerShipType
        
        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	# Player Setup
        SetupPlayer()
        
        SpawnSupportShips()

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

        # Start up all needed handlers
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
        
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

        global ObjectiveShipList
        ObjectiveShipList = ["Renegade 1", "Renegade 2", "Renegade 3", "Renegade 4", "Renegade 5", "Renegade 6", "Renegade 7", "Renegade 8"]

        if pIntroVid == 1:
                # Play the DS9FX Campaign Intro Movie
                from Custom.DS9FX.DS9FXVids import DS9FXIntroVideo

                DS9FXIntroVideo.PlayMovieSeq(None, None)

        else:
                pass
        

# Disable buttons that we have to!
def DisableDS9FXMenuButtons(pObject, pEvent):

    debug(__name__ + ", DisableDS9FXMenuButtons")
    try:
    
        bHail = DS9FXMenuLib.GetButton("Hail DS9", "Helm", "DS9FX")
        
        bHail.SetDisabled()

    except:
        
        pass

    try:
        
        Custom.DS9FX.DS9FXmain.DisableWarpButton()
        
        
    except:
        
        pass



# Let's restore the user to the ship he used in mission 4
def SetupPlayer():
            debug(__name__ + ", SetupPlayer")
            File = __import__("Save.mission5")
            pShip = File.Ship

            pPlayer = MissionLib.GetPlayer()
            pPlayerName = pPlayer.GetName()
            pSet = pPlayer.GetContainingSet()
            pSet.DeleteObjectFromSet(pPlayerName)
            
            loadspacehelper.CreateShip(pShip, pSet, pPlayerName, "Player Start")
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName(pPlayerName)
        
            GetPlayer = MissionLib.GetShip(pPlayerName, pSet)
            
            # Set the new player
            pGame = App.Game_GetCurrentGame()
            pGame.SetPlayer(GetPlayer)
            

# Is the player or another ship exploding
def PlayerExploding(pObject, pEvent):
                
        # Grab some values
        debug(__name__ + ", PlayerExploding")
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()
        pPlayeName = pPlayer.GetName()
        
        # Grab the ship that is exploding        
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
		return
	    
        ShipName = pShip.GetName()

        # Match the names 
        if (ShipName == pPlayeName):
            
            FailedTxt(None, None)
            
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
            except:
                pass
                
            
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")


# You've been destroyed            
def FailedTxt(pObject, pEvent):
            debug(__name__ + ", FailedTxt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(Failed(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry           
def Failed(pPane):
            debug(__name__ + ", Failed")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("Mission Failed!", pPane, 6, 6, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()
            

# Disable buttons to force the user to play the mission
def DisableButtons(pObject, pEvent):

    debug(__name__ + ", DisableButtons")
    pPlayer = App.Game_GetCurrentPlayer()    
    pSet = pPlayer.GetContainingSet()
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    if (pSet.GetName() == "BajoranWormhole1"):

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableExitToDS9Button", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)
            
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
        

    else:
        return

# Disable exit to ds9 button
def DisableExitToDS9Button(pObject, pEvent):
    
        debug(__name__ + ", DisableExitToDS9Button")
        try:
        
            bExitToDS9 = DS9FXMenuLib.GetButton("Exit To DS9", "Helm", "DS9FX")
            
            bExitToDS9.SetDisabled()

            
        except:
            
            pass


# Mission start
def MissionStart(pObject, pEvent):
        
        debug(__name__ + ", MissionStart")
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        if (pSet.GetName() == "GammaQuadrant1"):
            
            # Disable enter wormhole Button
            MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableEnterButton", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)
            
            
            Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
            GammaSet = Gamma.GetSet()

            # 1st ship      
            Bug1 = "Renegade 1"
            import Custom.DS9FX.DS9FXShips
            pBug1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, GammaSet, Bug1, "Location 1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug1)

            # Assign it's AI. 
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Bugship1 = MissionLib.GetShip(Bug1, GammaSet) 

            pBugship1 = App.ShipClass_Cast(Bugship1)

            pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pBugship1))

            # 2nd ship      
            Bug2 = "Renegade 2"
            pBug2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, GammaSet, Bug2, "Location 2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug2)

            Bugship2 = MissionLib.GetShip(Bug2, GammaSet) 

            pBugship2 = App.ShipClass_Cast(Bugship2)

            pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pBugship2))

                
            Bug3 = "Renegade 3"
            pBug3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, GammaSet, Bug3, "Bugship 4 Mission Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug3)

            Bugship3 = MissionLib.GetShip(Bug3, GammaSet) 

            pBugship3 = App.ShipClass_Cast(Bugship3)

            pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pBugship3))

            Bug4 = "Renegade 4"
            pBug4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, GammaSet, Bug4, "Location 3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug4)

            Bugship4 = MissionLib.GetShip(Bug4, GammaSet) 

            pBugship4 = App.ShipClass_Cast(Bugship4)

            pBugship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pBugship4))

            Bug5 = "Renegade 5"
            pBug5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, GammaSet, Bug5, "Location 4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug5)

            Bugship5 = MissionLib.GetShip(Bug5, GammaSet) 

            pBugship5 = App.ShipClass_Cast(Bugship5)

            pBugship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pBugship5))

            Bug6 = "Renegade 6"
            pBug6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, GammaSet, Bug6, "Location 5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug6)

            Bugship6 = MissionLib.GetShip(Bug6, GammaSet) 

            pBugship6 = App.ShipClass_Cast(Bugship6)

            pBugship6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pBugship6))


            Bug7 = "Renegade 7"
            pBug7 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, GammaSet, Bug7, "Location 6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug7)

            Bugship7 = MissionLib.GetShip(Bug7, GammaSet) 

            pBugship7 = App.ShipClass_Cast(Bugship7)

            pBugship7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pBugship7))

            Bug8 = "Renegade 8"
            pBug8 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, GammaSet, Bug8, "Location 7")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug8)

            Bugship8 = MissionLib.GetShip(Bug8, GammaSet) 

            pBugship8 = App.ShipClass_Cast(Bugship8)

            pBugship8.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pBugship8))
            

            # Kill the handler
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")

            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")

                        

        else:
            return


# Disable buttons
def DisableEnterButton(pObject, pEvent):
            debug(__name__ + ", DisableEnterButton")
            global bEnter
            
            try:
        
                bEnter = DS9FXMenuLib.GetButton("Enter Wormhole", "Helm", "DS9FX")
            
                bEnter.SetDisabled()

            
            except:
            
                pass

# Spawning Fed support ships
def SpawnSupportShips():
    
        debug(__name__ + ", SpawnSupportShips")
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        
        import Custom.DS9FX.DS9FXShips        
        loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXExcelsior, pSet, "USS Moscow", "WarpIn 1")
        
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName("USS Moscow")

        # Assign it's AI
        import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

        ship1 = MissionLib.GetShip("USS Moscow", pSet) 

        pship1 = App.ShipClass_Cast(ship1)

        pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))

        
        loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalaxy, pSet, "USS Budapest", "WarpIn 2")
        
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName("USS Budapest")

        ship2 = MissionLib.GetShip("USS Budapest", pSet) 

        pship2 = App.ShipClass_Cast(ship2)

        pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship2))

        
        loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXNebula, pSet, "USS Legacy", "WarpIn 3")
        
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName("USS Legacy")

        ship3 = MissionLib.GetShip("USS Legacy", pSet) 

        pship3 = App.ShipClass_Cast(ship3)

        pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship3))
        

        loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXCentaur, pSet, "USS Morning Star", "WarpIn 4")
        
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName("USS Morning Star")

        ship4 = MissionLib.GetShip("USS Morning Star", pSet) 

        pship4 = App.ShipClass_Cast(ship4)

        pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship4))
        
# Object is exploding, let's check it's name
def ObjectExploding(pObject, pEvent):
        debug(__name__ + ", ObjectExploding")
        global bEnter
        
        # Grab some values
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        # Grab the ship that is exploding        
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
		return
	    
        ShipName = pShip.GetName()

        # Match the names 
        if (ShipName in ObjectiveShipList):
            
            global ObjectiveShipList
            
            ObjectiveShipList.remove(ShipName)
            
            if (len(ObjectiveShipList) == 0):
                
                # RTB Prompt
                ReturnToBase(None, None)

                try:
                   bEnter.SetEnabled()
                   
                except:
                    pass

                AdditionalHandlersStarted(None, None)
                    
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")



# RTB Prompt
def ReturnToBase(pObject, pEvent):
            debug(__name__ + ", ReturnToBase")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(ReturnASAP(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry      
def ReturnASAP(pPane):
            debug(__name__ + ", ReturnASAP")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("Enemy Forces Destroyed!\n\nReturn to DS9 Captain!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# Start up additional handlers            
def AdditionalHandlersStarted(pObject, pEvent):
            
        # Grab some values
        debug(__name__ + ", AdditionalHandlersStarted")
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        # Start up a Mission Placement Handler
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")


# We have returned back to base
def BackToDS9(pObject, pEvent):
        debug(__name__ + ", BackToDS9")
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        if (pSet.GetName() == "DeepSpace91"):

            try:                
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            except:
                pass


            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
            
            MissionCompletedPrompt(None, None)

            RemoveSupportShips()

            if pCompletionVid == 1:
                # Start the timer which will play Victory Video, 15 secs delay
                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".PlayVictoryVid", App.g_kUtopiaModule.GetGameTime() + 15, 0, 0)

            else:
                pass
            
        else:
            return


# Campaign Done
def MissionCompletedPrompt(pObject, pEvent):
            debug(__name__ + ", MissionCompletedPrompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(Completed(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry      
def Completed(pPane):
            debug(__name__ + ", Completed")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("Renegade Dominion forces have been defeated!\n\nYou made the Federation proud today Captain!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 30)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()

# Cya out there captain
def RemoveSupportShips():
        debug(__name__ + ", RemoveSupportShips")
        pSet = MissionLib.GetPlayer().GetContainingSet()

        try:
            pSet.DeleteObjectFromSet("USS Moscow")
        except:
            pass
        try:
            pSet.DeleteObjectFromSet("USS Budapest")
        except:
            pass
        try:
            pSet.DeleteObjectFromSet("USS Legacy")
        except:
            pass
        try:
            pSet.DeleteObjectFromSet("USS Morning Star")
            
        except:
            pass    


# Let's play victory video
def PlayVictoryVid(pObject, pEvent):
        debug(__name__ + ", PlayVictoryVid")
        from Custom.DS9FX.DS9FXVids import DS9FXCompletionVideo
        
        DS9FXCompletionVideo.PlayMovieSeq(None, None)


# Kill the pane, fixes the crashing bug and several other bugs
def KillPane(pAction):
        debug(__name__ + ", KillPane")
        global pPaneID
        
        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
	App.g_kRootWindow.DeleteChild(pPane)
		
	pPaneID = App.NULL_ID
	
	return 0

        

# Exit function
def Quit():
        debug(__name__ + ", Quit")
        global pMainPane, pPane

        if not pPane == None:

             # A bugfix
            try:
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.RemoveBroadcastHandler(ET_ACCEPT, pMission, __name__ + ".Accept")
                App.g_kEventManager.RemoveBroadcastHandler(ET_DECLINE, pMission, __name__ + ".Decline")

            except:
                pass

            pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

            # Destroy the window
            App.g_kFocusManager.RemoveAllObjectsUnder(pPane)

            pTCW.DeleteChild(pPane)

            pPane = None
            
