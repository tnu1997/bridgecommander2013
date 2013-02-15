from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# by USS Sovereign, Mission: Retake DS9 (Canon)

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
Enemies = []
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
        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Retake DS9 (Canon)"), 0.0, 0.0, None, 1, 0.30, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Defeat 35 enemy ships to takeover DS9\n-Survive the battle"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("Captain, it's time now to return to DS9. We have received word that the Dominion is about to disarm the cloaked minefield we have placed. If this happens the Dominion will be able to receive reinforcements from the Gamma Quadrant. We can't let this happen. You and your ship, the USS Defiant, are ordered to join the task force. We do no expect the Klingons to join us so you will be on your own. Goodspeed Captain."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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
            pAction = LineAction("Mission: Retake DS9 (Canon)", pPane, 3, 6, 16)
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

            try:
                    pSet.DeleteObjectFromSet("Deep_Space_9")
            except:
                pass
            

            # Player Setup
            SetupPlayer()

            MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

            # Starting handlers
            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

            ObjectivesPrompt(None, None)

            MissionSetup()

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
            pShip = Custom.DS9FX.DS9FXShips.HistoricMission4Player


            pPlayer = MissionLib.GetPlayer()
            pPlayerName = pPlayer.GetName()
            pSet = pPlayer.GetContainingSet()
            pSet.DeleteObjectFromSet(pPlayerName)
            
            loadspacehelper.CreateShip(pShip, pSet, pPlayerName, "RetakePlayerPos")
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
                bDock = DS9FXMenuLib.GetButton("Dock To DS9", "Helm", "DS9FX")
                    
                bDock.SetDisabled()

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

            RemoveShips()

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
                bDock = DS9FXMenuLib.GetButton("Dock To DS9", "Helm", "DS9FX")
                    
                bDock.SetEnabled()

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
            pAction = LineAction("This is it Captain!\nLet's go down in history!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# Mission setup
def MissionSetup():
            debug(__name__ + ", MissionSetup")
            global Enemies

            # Grab some values
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()
            
            Enemies = ["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8", "Enemy 9", "Enemy 10", "Enemy 11", "Enemy 12", "Enemy 13", "Enemy 14", "Enemy 15", "Enemy 16", "Enemy 17", "Enemy 18", "Enemy 19", "Enemy 20", "Enemy 21", "Enemy 22", "Enemy 23", "Enemy 24", "Enemy 25", "Enemy 26", "Enemy 27", "Enemy 28", "Enemy 29", "Enemy 30", "Enemy 31", "Enemy 32", "Enemy 33", "Enemy 34", "Enemy 35"]  

            SpawnShips()

            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")


# Spawn ships
def SpawnShips():
            # Get some values
            debug(__name__ + ", SpawnShips")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()

            import Custom.DS9FX.DS9FXShips
            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXAkira, pSet, "USS Argus", "FriendlyPos1")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("USS Argus")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship1 = MissionLib.GetShip("USS Argus", pSet)

            pship1 = App.ShipClass_Cast(ship1)

            pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXExcelsior, pSet, "USS Iconia", "FriendlyPos2")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("USS Iconia")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship2 = MissionLib.GetShip("USS Iconia", pSet)

            pship2 = App.ShipClass_Cast(ship2)

            pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship2))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXNebula, pSet, "USS Rotterdam", "FriendlyPos3")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("USS Rotterdam")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship3 = MissionLib.GetShip("USS Rotterdam", pSet)

            pship3 = App.ShipClass_Cast(ship3)

            pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship3))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXMiranda, pSet, "USS Monaco", "FriendlyPos4")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("USS Monaco")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship4 = MissionLib.GetShip("USS Monaco", pSet)

            pship4 = App.ShipClass_Cast(ship4)

            pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship4))

            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXMiranda, pSet, "USS Rapid", "FriendlyPos5")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("USS Rapid")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship5 = MissionLib.GetShip("USS Rapid", pSet)

            pship5 = App.ShipClass_Cast(ship5)

            pship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship5))

            # Create the Attacking ship
            Att1 = "Enemy 1"
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXKeldon, pSet, Att1, "EnemyPos1")

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
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att2, "EnemyPos2")

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
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att3, "EnemyPos3")

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
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "EnemyPos4")

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
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att5, "EnemyPos5")

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
            pAtt6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att6, "EnemyPos6")

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
            pAtt7 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att7, "EnemyPos7")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att7)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker7 = MissionLib.GetShip("Enemy 7", pSet) 

            pAttacker7 = App.ShipClass_Cast(Attacker7)

            pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))


# Next wave of enemy ships coming in. The best way to simulate BIG battles in BC!
def SpawnSecondWave():
            # Get some values
            debug(__name__ + ", SpawnSecondWave")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Create the Attacking ship
            Att1 = "Enemy 8"
            import Custom.DS9FX.DS9FXShips
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att1, "EnemyPos1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Enemy 8", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Enemy 9"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att2, "EnemyPos2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Enemy 9", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


            # Create the Attacking ship
            Att3 = "Enemy 10"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att3, "EnemyPos3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Enemy 10", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Enemy 11"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "EnemyPos4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Enemy 11", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

            # Create the Attacking ship
            Att5 = "Enemy 12"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att5, "EnemyPos5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Enemy 12", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

            # Create the Attacking ship
            Att6 = "Enemy 13"
            pAtt6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att6, "EnemyPos6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att6)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker6 = MissionLib.GetShip("Enemy 13", pSet) 

            pAttacker6 = App.ShipClass_Cast(Attacker6)

            pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))


            # Create the Attacking ship
            Att7 = "Enemy 14"
            pAtt7 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att7, "EnemyPos7")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att7)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker7 = MissionLib.GetShip("Enemy 14", pSet) 

            pAttacker7 = App.ShipClass_Cast(Attacker7)

            pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))


# 3rd wave
def SpawnThirdWave():
            # Get some values
            debug(__name__ + ", SpawnThirdWave")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Create the Attacking ship
            Att1 = "Enemy 15"
            import Custom.DS9FX.DS9FXShips
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att1, "EnemyPos1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Enemy 15", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Enemy 16"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXKeldon, pSet, Att2, "EnemyPos2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Enemy 16", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


            # Create the Attacking ship
            Att3 = "Enemy 17"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att3, "EnemyPos3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Enemy 17", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Enemy 18"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "EnemyPos4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Enemy 18", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

            # Create the Attacking ship
            Att5 = "Enemy 19"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att5, "EnemyPos5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Enemy 19", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

            # Create the Attacking ship
            Att6 = "Enemy 20"
            pAtt6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att6, "EnemyPos6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att6)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker6 = MissionLib.GetShip("Enemy 20", pSet) 

            pAttacker6 = App.ShipClass_Cast(Attacker6)

            pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))


            # Create the Attacking ship
            Att7 = "Enemy 21"
            pAtt7 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att7, "EnemyPos7")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att7)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker7 = MissionLib.GetShip("Enemy 21", pSet) 

            pAttacker7 = App.ShipClass_Cast(Attacker7)

            pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))
            

def SpawnFourthWave():
            # Get some values
            debug(__name__ + ", SpawnFourthWave")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Create the Attacking ship
            Att1 = "Enemy 22"
            import Custom.DS9FX.DS9FXShips
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXKeldon, pSet, Att1, "EnemyPos1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Enemy 22", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Enemy 23"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att2, "EnemyPos2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Enemy 23", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


            # Create the Attacking ship
            Att3 = "Enemy 24"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXKeldon, pSet, Att3, "EnemyPos3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Enemy 24", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Enemy 25"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "EnemyPos4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Enemy 25", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

            # Create the Attacking ship
            Att5 = "Enemy 26"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att5, "EnemyPos5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Enemy 26", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

            # Create the Attacking ship
            Att6 = "Enemy 27"
            pAtt6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att6, "EnemyPos6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att6)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker6 = MissionLib.GetShip("Enemy 27", pSet) 

            pAttacker6 = App.ShipClass_Cast(Attacker6)

            pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))


            # Create the Attacking ship
            Att7 = "Enemy 28"
            pAtt7 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att7, "EnemyPos7")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att7)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker7 = MissionLib.GetShip("Enemy 28", pSet) 

            pAttacker7 = App.ShipClass_Cast(Attacker7)

            pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))
            

def SpawnFifthWave():
            # Get some values
            debug(__name__ + ", SpawnFifthWave")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Create the Attacking ship
            Att1 = "Enemy 29"
            import Custom.DS9FX.DS9FXShips
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXKeldon, pSet, Att1, "EnemyPos1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Enemy 29", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Enemy 30"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att2, "EnemyPos2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Enemy 30", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


            # Create the Attacking ship
            Att3 = "Enemy 31"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalor, pSet, Att3, "EnemyPos3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Enemy 31", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Enemy 32"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "EnemyPos4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Enemy 32", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

            # Create the Attacking ship
            Att5 = "Enemy 33"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att5, "EnemyPos5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Enemy 33", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

            # Create the Attacking ship
            Att6 = "Enemy 34"
            pAtt6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXHideki, pSet, Att6, "EnemyPos6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att6)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker6 = MissionLib.GetShip("Enemy 34", pSet) 

            pAttacker6 = App.ShipClass_Cast(Attacker6)

            pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))


            # Create the Attacking ship
            Att7 = "Enemy 35"
            pAtt7 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXKeldon, pSet, Att7, "EnemyPos7")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att7)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker7 = MissionLib.GetShip("Enemy 35", pSet) 

            pAttacker7 = App.ShipClass_Cast(Attacker7)

            pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))

            
# In all their glory the Klingons have arrived to save your federation asses
def KlingonArrival():
            # Get some values
            debug(__name__ + ", KlingonArrival")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Get some values
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            import Custom.DS9FX.DS9FXShips
            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, "IKV Ykir", "FriendlyPos1")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("IKV Ykir")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship1 = MissionLib.GetShip("IKV Ykir", pSet)

            pship1 = App.ShipClass_Cast(ship1)

            pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXD7Ktinga, pSet, "IKV Nawrya", "FriendlyPos2")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("IKV Nawrya")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship2 = MissionLib.GetShip("IKV Nawrya", pSet)

            pship2 = App.ShipClass_Cast(ship2)

            pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship2))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, "IKV Tumultuous", "FriendlyPos3")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("IKV Tumultuous")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship3 = MissionLib.GetShip("IKV Tumultuous", pSet)

            pship3 = App.ShipClass_Cast(ship3)

            pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship3))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXVorcha, pSet, "IKV Hunter", "FriendlyPos4")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("IKV Hunter")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship4 = MissionLib.GetShip("IKV Hunter", pSet)

            pship4 = App.ShipClass_Cast(ship4)

            pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship4))

            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXVorcha, pSet, "IKV Invincible", "FriendlyPos5")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName("IKV Invincible")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

            ship5 = MissionLib.GetShip("IKV Invincible", pSet)

            pship5 = App.ShipClass_Cast(ship5)

            pship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship5))


# Object is exploding, let's check it's name
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
        if (ShipName in Enemies):
            
            global Enemies
            
            Enemies.remove(ShipName)

            if (len(Enemies) == 28):
                SpawnSecondWave()

            elif (len(Enemies) == 21):
                SpawnThirdWave()

            elif (len(Enemies) == 16):
                KlingonsPrompt(None, None) 
                KlingonArrival()

            elif (len(Enemies) == 14):
                SpawnFourthWave()

            elif (len(Enemies) == 7):
                SpawnFifthWave()

            elif (len(Enemies) == 0):

                from Custom.DS9FX.DS9FXObjects import DS9Ships

                DS9Ships.DS9SetShips()

                from Custom.DS9FX.DS9FXObjects import DS9Stations

                DS9Stations.DS9SetStations()
                
                ReenableAllButtons()

                RemoveShips()

                MissionWin(None, None)

                try:                
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                except:
                    pass
                
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")

            else:
                pObject.CallNextHandler(pEvent)
               

# Klingons have arrived
def KlingonsPrompt(pObject, pEvent):
            debug(__name__ + ", KlingonsPrompt")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(KlingonsSequence(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()
            

# Print the text to the screen
def KlingonsSequence(pPane):
            # Sequence which contains only 1 line of text
            debug(__name__ + ", KlingonsSequence")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # prompt
            pAction = LineAction("The Klingons, Sir!\nThey have arrived!!!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()

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
            pAction = LineAction("DS9 is ours once again!\n\nTime to celebrate!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


# Remove ships
def RemoveShips():
            debug(__name__ + ", RemoveShips")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            try:
                    pSet.DeleteObjectFromSet("USS Argus")
            except:
                pass
            try:
                    pSet.DeleteObjectFromSet("USS Iconia")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("USS Rotterdam")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("USS Monaco")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("USS Rapid")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("IKV Ykir")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("IKV Nawrya")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("IKV Tumultuous")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("IKV Hunter")
            except:
                pass

            try:
                    pSet.DeleteObjectFromSet("IKV Invincible")
            except:
                pass


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
            
# Kill the pane, fixes the crashing bug and several other bugs
def KillPane(pAction):
        debug(__name__ + ", KillPane")
        global pPaneID
        
        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
	App.g_kRootWindow.DeleteChild(pPane)
		
	pPaneID = App.NULL_ID
	
	return 0
