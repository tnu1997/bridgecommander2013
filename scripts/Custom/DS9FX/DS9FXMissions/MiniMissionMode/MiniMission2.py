from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# by USS Sovereign, Mission: Anomalous Readings

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pIntroVid = pModule.IntroVid

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
sShips = []
pScanPTS = 0
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
        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Anomalous Readings"), 0.0, 0.0, None, 1, 0.30, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Get in close range to scan the comet\n-Scan the comet for 1 minute\n-See what happens next"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("We are getting some strange readings from the Comet Alpha. You are required to scan the comet and check out the readings. Who knows, you might even discover something new Captain..."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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


# Returns a random number in between 1 and 100
def GetRandomCoord(iNumber):

        debug(__name__ + ", GetRandomCoord")
        return App.g_kSystemWrapper.GetRandomNumber(99) + iNumber
    

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
            pAction = LineAction("Mission: Anomalous Readings", pPane, 3, 6, 16)
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

	pPlayer = MissionLib.GetPlayer()

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

        pComet = 'Comet Alpha'
        
        # Setup a condition in range
        DistanceCheckCondition = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 40, pPlayer.GetName(), pComet)
        MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "Redirect", DistanceCheckCondition)

        if pIntroVid == 1:
                # Play the DS9FX Intro Movie
                from Custom.DS9FX.DS9FXVids import DS9FXIntroVideo

                DS9FXIntroVideo.PlayMovieSeq(None, None)

        else:
                pass

# Redirect
def Redirect(bInRange):
        # Deactivate the condition script
        debug(__name__ + ", Redirect")
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "Redirect")

        ScanPrompt()

        ScanTimer()
        

# Disable buttons that we have to!
def DisableDS9FXMenuButtons(pObject, pEvent):

            debug(__name__ + ", DisableDS9FXMenuButtons")
            try:
            
                bHail = DS9FXMenuLib.GetButton("Hail DS9", "Helm", "DS9FX")
                
                bHail.SetDisabled()

            except:
                
                pass

            try:
                bEnter = DS9FXMenuLib.GetButton("Enter Wormhole", "Helm", "DS9FX")
                    
                bEnter.SetDisabled()

            except:
                
                pass

            try:

                Custom.DS9FX.DS9FXmain.DisableWarpButton()

            except:
                pass


# Player is exploding. 
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
                # Deactivate the condition script
                MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "Redirect")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
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

# Scan prompt          
def ScanPrompt():
            debug(__name__ + ", ScanPrompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(Scanners(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry           
def Scanners(pPane):
            debug(__name__ + ", Scanners")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("Sir, we will need at least \na minute to scan the comet!", pPane, 6, 6, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# scanning  
def Firstprompt():
            debug(__name__ + ", Firstprompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(Firstprompttxt(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry           
def Firstprompttxt(pPane):
            debug(__name__ + ", Firstprompttxt")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("45 seconds", pPane, 6, 6, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()

# scanning  
def Secondprompt():
            debug(__name__ + ", Secondprompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(Secondprompttxt(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry           
def Secondprompttxt(pPane):
            debug(__name__ + ", Secondprompttxt")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("30 seconds", pPane, 6, 6, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# scanning  
def Thirdprompt():
            debug(__name__ + ", Thirdprompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(Thirdprompttxt(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry           
def Thirdprompttxt(pPane):
            debug(__name__ + ", Thirdprompttxt")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("15 seconds", pPane, 6, 6, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()



# Scanning timer
def ScanTimer():
            debug(__name__ + ", ScanTimer")
            global pScanPTS

            # Already gained a point for entering the range
            pScanPTS = pScanPTS + 1
            
            MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ScanConfirm", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)


# Scan prompt          
def ScanComplete():
            debug(__name__ + ", ScanComplete")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(ScanSuccess(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry           
def ScanSuccess(pPane):
            debug(__name__ + ", ScanSuccess")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("Sir, nothing to report... \nFive Cardassian ships have jumped out of \nwarp near our location.", pPane, 6, 6, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()
            

# Every one second add a point to the player, do a distance check. 60 pts the scan is completed
def ScanConfirm(pObject, pEvent):
            debug(__name__ + ", ScanConfirm")
            global pScanPTS

            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Grab the Comet
            pComet = MissionLib.GetShip("Comet Alpha", pSet)

            if DistanceCheck(pComet) <= 40:
                if pScanPTS >= 60:
                    ScanComplete()
                    SetupExtraMissionHandlers()
                    
                else:
                    pScanPTS = pScanPTS + 1
                    if pScanPTS == 15:
                        Firstprompt()
                    elif pScanPTS == 30:
                        Secondprompt()
                    elif pScanPTS == 45:
                        Thirdprompt()
                        
                    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ScanConfirm", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
                
            else:
                    MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".ScanConfirm", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
            

# A distance check                                
def DistanceCheck(pObject):
	debug(__name__ + ", DistanceCheck")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()           


# Combat handlers
def SetupExtraMissionHandlers():
            debug(__name__ + ", SetupExtraMissionHandlers")
            global sShips

            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()

            sShips = ['Galor 1', 'Galor 2', 'Galor 3', 'Galor 4', 'Galor 5']
            
            SpawnCardies()

            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            

# Cardies are coming!!!
def SpawnCardies():
            debug(__name__ + ", SpawnCardies")
            global sShips
            
            # Get some values
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()

            # Get location of the player
            pLocation = pPlayer.GetWorldLocation() 
            import Custom.DS9FX.DS9FXShips

            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, "Galor 1", "FriendlyPos1")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("Galor 1")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            ship1 = MissionLib.GetShip("Galor 1", pSet)

            pship1 = App.ShipClass_Cast(ship1)

            pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship1))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, "Galor 2", "FriendlyPos2")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("Galor 2")

            ship2 = MissionLib.GetShip("Galor 2", pSet)

            pship2 = App.ShipClass_Cast(ship2)

            pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship2))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, "Galor 3", "FriendlyPos3")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("Galor 3")

            ship3 = MissionLib.GetShip("Galor 3", pSet)

            pship3 = App.ShipClass_Cast(ship3)

            pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship3))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, "Galor 4", "FriendlyPos4")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("Galor 4")

            ship4 = MissionLib.GetShip("Galor 4", pSet)

            pship4 = App.ShipClass_Cast(ship4)

            pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship4))

            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, "Galor 5", "FriendlyPos5")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("Galor 5")

            ship5 = MissionLib.GetShip("Galor 5", pSet)

            pship5 = App.ShipClass_Cast(ship5)

            pship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship5))

            for fship in sShips:
                # Translate all ships near the player
                kShipX = pLocation.GetX()
                    
                kShipY = pLocation.GetY()
                    
                kShipZ = pLocation.GetZ()

                RateX = GetRandomCoord(1)

                RateY = GetRandomCoord(1)

                RateZ = GetRandomCoord(1)

                pXCoord = kShipX + RateX

                pYCoord = kShipY + RateY

                pZCoord = kShipZ + RateZ

                # markings are 1, 2, 3, 4, 5
                iNum = 1

                kShip = MissionLib.GetShip("Galor " + str(iNum), pSet)

                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                kShip.UpdateNodeOnly()

                iNum = iNum + 1

                
# Check the exploding object
def ObjectExploding(pObject, pEvent):
        
        # Grab some values
        debug(__name__ + ", ObjectExploding")
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        # Grab the ship that is exploding        
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
		return
	    
        ShipName = pShip.GetName()

        # Match the names 
        if (ShipName in sShips):
            
            global sShips
            
            sShips.remove(ShipName)

            if (len(sShips) == 0):

                ReenableAllButtons()

                MissionWin(None, None)

                # Who knows, this could be active for some strange reason lol
                try:
                    # Deactivate the condition script
                    MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "Redirect")
                except:
                    pass

                try:                
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                except:
                    pass
                
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")

            else:
                pObject.CallNextHandler(pEvent)


# Enable buttons that we have to!
def ReenableAllButtons():

            debug(__name__ + ", ReenableAllButtons")
            try:
            
                bHail = DS9FXMenuLib.GetButton("Hail DS9", "Helm", "DS9FX")
                
                bHail.SetEnabled()

            except:
                pass

            try:
                bEnter = DS9FXMenuLib.GetButton("Enter Wormhole", "Helm", "DS9FX")
                    
                bEnter.SetEnabled()
                
            except:
                pass

            try:
                bDock = DS9FXMenuLib.GetButton("Dock To DS9", "Helm", "DS9FX")
                    
                bDock.SetEnabled()

            except:
                
                pass

            try:
                Custom.DS9FX.DS9FXmain.RestoreWarpButton()

            except:
                pass           


# Victory
def MissionWin(pObject, pEvent):
            debug(__name__ + ", MissionWin")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(WinSequence(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()
            

# Print the text to the screen
def WinSequence(pPane):
            # Sequence which contains only 1 line of text
            debug(__name__ + ", WinSequence")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # prompt
            pAction = LineAction("It would appear that the Cardassians had some sort of \nlistening device on the Comet! We have neutralized it. \nMission Completed!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


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
