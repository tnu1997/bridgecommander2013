from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# by USS Sovereign, Mission: Plant the minefield

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
pTimer = None
iMinesLayed = 0
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
        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Plant the minefield"), 0.0, 0.0, None, 1, 0.30, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Be sure to be in 10 km range before you plant mines\n-Plant 26 mines\n-Survive attack\n-In the end warp out in any direction"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("Captain, we are loosing at peace time. We have to stop the Dominion convoys which are coming through the wormhole constantly. It's up to you to place a cloaked minefield, you don't have a lot of time before the Dominion and Cardassian fleets arrive from Cardassia. Good luck, Captain. We are all counting on you! This is most likely the first battle of what will people one day call the Dominion Wars, let us pray that we can win."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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
            pAction = LineAction("Mission: Plant the minefield", pPane, 3, 6, 16)
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


# Start timers & Handlers
def MissionInitiate(pObject, pEvent):        
            # Grab some values
            debug(__name__ + ", MissionInitiate")
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()

            # Remove specific ships from the map
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            try:
                    pSet.DeleteObjectFromSet("USS Excalibur")
            except:
                pass
            try:
                    pSet.DeleteObjectFromSet("USS Defiant")
            except:
                pass
            try:
                    pSet.DeleteObjectFromSet("USS Oregon")
            except:
                pass
            try:
                    pSet.DeleteObjectFromSet("USS_Lakota")
            except:
                pass

            # Player Setup
            SetupPlayer()

            MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

            # Starting handlers
            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")

            ObjectivesPrompt(None, None)

            LayMines()

            if pIntroVid == 1:
                    # Play the DS9FX Intro Movie
                    from Custom.DS9FX.DS9FXVids import DS9FXIntroVideo

                    DS9FXIntroVideo.PlayMovieSeq(None, None)

            else:
                    pass


# Set the new player ship
def SetupPlayer():
            debug(__name__ + ", SetupPlayer")
            import Custom.DS9FX.DS9FXShips
            pShip = Custom.DS9FX.DS9FXShips.HistoricMission1Player

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

            DeletepTimer(None, None)
 
            # Remove all active handlers
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
                
            except:
                pass
            
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")


# DS9 is exploding. 
def DS9Exploding(pObject, pEvent):
        # Grab some values
        debug(__name__ + ", DS9Exploding")
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
        if (ShipName == "Deep_Space_9"):
            
            DS9FailedTxt(None, None)

            ReenableAllButtons()

            DeletepTimer(None, None)

            RemoveShips()

            RemoveMines()

            # Remove all active handlers
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                
            except:
                pass
            
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
                
            except:
                pass
            
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
            
            

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


# DS9 Has been destroyed          
def DS9FailedTxt(pObject, pEvent):
            debug(__name__ + ", DS9FailedTxt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(DS9Failed(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Txt entry           
def DS9Failed(pPane):
            debug(__name__ + ", DS9Failed")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("Mission Failed!\nPlease restart Quick Battle!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# Disable buttons that we have to!
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
                Custom.DS9FX.DS9FXmain.RestoreWarpButton()

            except:
                pass


# Objectives
def ObjectivesPrompt(pObject, pEvent):
            debug(__name__ + ", ObjectivesPrompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(ObjectivesSequence(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()
            

# Print the text to the screen
def ObjectivesSequence(pPane):
            # Sequence which contains only 1 line of text
            debug(__name__ + ", ObjectivesSequence")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # prompt
            pAction = LineAction("Captain, we should go over to the \nwormhole and place the minefield!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


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
                

# Over here we will control when a mine should be layed. It's fully automated the player only needs to be in the position!
def LayMines():
        debug(__name__ + ", LayMines")
        global pTimer
        
        pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MineLayingCheck", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)


# Should we lay in the mines or not?!
def MineLayingCheck(pObject, pEvent):
        debug(__name__ + ", MineLayingCheck")
        global iMinesLayed, pTimer

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        
        # Grab the wormhole model
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
        pDS9FXWormholeID = pDS9FXWormhole.GetObjID()

        # Check if we are in range 
        if DistanceCheck(pDS9FXWormhole) < 50:
            if iMinesLayed == 12:
                SpeedupPrompt()
                SpawnShips()
                pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MineLayingCheck", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)
                CreateMine()

            elif iMinesLayed > 25:
                RunPrompt()
                ReenableAllButtons()
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
                return

            else:
                pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MineLayingCheck", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)
                CreateMine()


        elif iMinesLayed > 25:
                RunPrompt()
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()

                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
                return
            

        else:
                pTimer = MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".MineLayingCheck", App.g_kUtopiaModule.GetGameTime() + 20, 0, 0)

 
# A distance check                                
def DistanceCheck(pObject):
	debug(__name__ + ", DistanceCheck")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()
    

# Mine creation, no AI's. Code taken in from the old Self-Manhiem Script of mine
def CreateMine():
        debug(__name__ + ", CreateMine")
        global iMinesLayed

        RemoveMines()

        iMinesLayed = iMinesLayed + 1
        
        # Get some values
        pPlayer	= MissionLib.GetPlayer()
	pSet = pPlayer.GetContainingSet()

        # Create the ship 
        pName = "Mine" + str(iMinesLayed)
        import Custom.DS9FX.DS9FXShips
        pMine = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXMine, pSet, pName, None)

        # Add it to a friendly group
	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName(pName)

        # Position it so to that it appears it's emerging from your hull
        pPosition = pPlayer.GetWorldLocation()
        pMine.SetTranslate(pPosition)
        pMine.UpdateNodeOnly()

        # Disable collisions with the player and created ship
        pMine.EnableCollisionsWith(pPlayer, 0)

        MinesPlaced()
        

# Ships coming in
def SpawnShips():
            # Get some values
            debug(__name__ + ", SpawnShips")
            pPlayer	= MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()

            import Custom.DS9FX.DS9FXShips
            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, "IKS Rotarran", "Excal Location")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("IKS Rotarran")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship1 = MissionLib.GetShip("IKS Rotarran", pSet)

            # Rotarran is invincible
            ship1.SetInvincible(1)
            ship1.SetHurtable(0)

            pship1 = App.ShipClass_Cast(ship1)

            pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))


            # Create the Attacking ship
            Att1 = "Enemy 1"
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXKeldon, pSet, Att1, "Help1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Enemy 1", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Enemy 2"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att2, "Help2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Enemy 2", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


            # Create the Attacking ship
            Att3 = "Enemy 3"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att3, "Help3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Enemy 3", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Enemy 4"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "WarpIn 4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Enemy 4", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

            # Create the Attacking ship
            Att5 = "Enemy 5"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att5, "WarpIn 3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Enemy 5", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

            # Create the Attacking ship
            Att6 = "Enemy 6"
            pAtt6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att6, "WarpIn 2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att6)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker6 = MissionLib.GetShip("Enemy 6", pSet) 

            pAttacker6 = App.ShipClass_Cast(Attacker6)

            pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))


            # Create the Attacking ship
            Att7 = "Enemy 7"
            pAtt7 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att7, "WarpIn 1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att7)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker7 = MissionLib.GetShip("Enemy 7", pSet) 

            pAttacker7 = App.ShipClass_Cast(Attacker7)

            pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))

# Del timer
def DeletepTimer(pObject, pEvent):
        debug(__name__ + ", DeletepTimer")
        global pTimer

        try:
                    App.g_kTimerManager.DeleteTimer(pTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(pTimer.GetObjID())
                    pTimer = None
        except:
                    pass


# Enemy fleet has arrived
def SpeedupPrompt():
            debug(__name__ + ", SpeedupPrompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(SpeedupSequence(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()
            

# Print the text to the screen
def SpeedupSequence(pPane):
            # Sequence which contains only 1 line of text
            debug(__name__ + ", SpeedupSequence")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # prompt
            pAction = LineAction("Sir, Dominion ships have arrived. \n\nWe have to hurry!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# Ruuuuuuuuuuuuuuuuun!
def RunPrompt():
            debug(__name__ + ", RunPrompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(RunSequence(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()
            

# Print the text to the screen
def RunSequence(pPane):
            # Sequence which contains only 1 line of text
            debug(__name__ + ", RunSequence")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # prompt
            pAction = LineAction("Sir, minefield is in place. \n\nWe have to warp out, \nin any direction", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# Mine no. placed
def MinesPlaced():
            debug(__name__ + ", MinesPlaced")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(MinesSequence(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()
            

# Print the text to the screen
def MinesSequence(pPane):
            debug(__name__ + ", MinesSequence")
            global iMinesLayed
            
            # Sequence which contains only 1 line of text
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # prompt
            pAction = LineAction("Mines Placed: " + str(iMinesLayed), pPane, 12, 3, 12)
            pSequence.AddAction(pAction, None, 0.1)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# Runing away from DS9
def EvacDS9(pObject, pEvent):
            debug(__name__ + ", EvacDS9")
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()

            RemoveShips()

            RemoveMines()

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                
            except:
                pass

            App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".EvacDS9")
            
            
# Remove ships
def RemoveShips():
            debug(__name__ + ", RemoveShips")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            try:
                    pSet.DeleteObjectFromSet("IKS Rotarran")
            except:
                pass
            try:
                    pSet.DeleteObjectFromSet("Enemy 1")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("Enemy 2")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("Enemy 3")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("Enemy 4")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("Enemy 5")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("Enemy 6")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("Enemy 7")
            except:
                pass


# Kill the pane, fixes the crashing bug and several other bugs
def KillPane(pAction):
        debug(__name__ + ", KillPane")
        global pPaneID
        
        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
	App.g_kRootWindow.DeleteChild(pPane)
		
	pPaneID = App.NULL_ID
	
	return 0


# Remove any mines left
def RemoveMines():
            # Grab some values
            debug(__name__ + ", RemoveMines")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()

            # Do a loop deletion of all mines
            iMine = 0
            iRemove = 1
            while iRemove == 1:
                if iMine > 25:
                    # Kill the loop
                    iRemove = 0
                    
                iMine = iMine + 1
                try:
                    pSet.DeleteObjectFromSet("Mine" + str(iMine))
                except:
                    pass
