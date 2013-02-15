from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# by USS Sovereign. Mission 4 from the DS9FX Border Skirmish Campaign.

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
pPlayerShipType = None
RenegadeShips = []
pPaneID = App.NULL_ID

# Path where we should save a mission progress py file
Path  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\BorderSkirmish\\Save\\mission5.py"

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
        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Revenge Is A Dish Best Served Cold"), 0.0, 0.0, None, 1, 0.30, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Repel Dominion ships\n-Survive"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)
        
        pText = App.TGParagraph_CreateW(App.TGString("Things have gone from bad to worse, Captain. The destruction of the White facility was not the big victory we expected it to be. The Founders have dispatched a wing of ships to help you find and destroy them. Ah, there they are..."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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
            pAction = LineAction("Mission: Revenge Is A Dish Best Served Cold", pPane, 3, 6, 16)
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

# Start timers & Handlers
def MissionInitiate(pObject, pEvent):
        debug(__name__ + ", MissionInitiate")
        global pPlayerShipType, RenegadeShips
        
        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	# Player Setup
        SetupPlayer()

        # Remember player ship
	pPlayer = MissionLib.GetPlayer()
	pPlayerShipType = GetShipType(pPlayer)

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".SupportShipsIncoming", App.g_kUtopiaModule.GetGameTime() + 95, 0, 0)

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".SupportArriving", App.g_kUtopiaModule.GetGameTime() + 41, 0, 0)

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".firstEnemyWave", App.g_kUtopiaModule.GetGameTime() + 17, 0, 0)

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".secondEnemyWave", App.g_kUtopiaModule.GetGameTime() + 40, 0, 0)

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".thirdEnemyWave", App.g_kUtopiaModule.GetGameTime() + 293, 0, 0)

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".fourthEnemyWave", App.g_kUtopiaModule.GetGameTime() + 317, 0, 0)

        # Starting a handler to see if every enemy ship has been destroyed
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
        
	RenegadeShips =	["Renegade 1", "Renegade 2", "Renegade 3", "Renegade 4", "Renegade 5", "Renegade 6", "Renegade 7", "Renegade 8", "Renegade 9", "Renegade 10", "Renegade 11", "Renegade 12", "Renegade 13", "Renegade 14", "Renegade 15", "Renegade 16", "Renegade 17", "Renegade 18", "Renegade 19", "Renegade 20"]

        if pIntroVid == 1:
                # Play the DS9FX Campaign Intro Movie
                from Custom.DS9FX.DS9FXVids import DS9FXIntroVideo

                DS9FXIntroVideo.PlayMovieSeq(None, None)

        else:
                pass
        

# Let's restore the user to the ship he used in mission 3
def SetupPlayer():
            debug(__name__ + ", SetupPlayer")
            File = __import__("Save.mission4")
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


# Help has arrived
def SupportShipsIncoming(pObject, pEvent):
    
        debug(__name__ + ", SupportShipsIncoming")
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        
        # Support warping in
        import Custom.DS9FX.DS9FXShips
        loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXGalaxy, pSet, "USS Antartica", "Help1")
        
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName("USS Antartica")

        # Assign it's AI
        import Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI

        ship1 = MissionLib.GetShip("USS Antartica", pSet) 

        pship1 = App.ShipClass_Cast(ship1)

        pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship1))

        loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXMiranda, pSet, "USS Washington", "Help2")
        
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName("USS Washington")

        ship2 = MissionLib.GetShip("USS Washington", pSet) 

        pship2 = App.ShipClass_Cast(ship2)

        pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship2))

        loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDefiant, pSet, "USS Avenger", "Help3")
        
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName("USS Avenger")

        ship3 = MissionLib.GetShip("USS Avenger", pSet) 

        pship3 = App.ShipClass_Cast(ship3)

        pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXAlliedAI.CreateAI(pship3))


# 1st out of 4 wave of enemy ships. A lot don't you think?! But it will make the mission more fun :)
def firstEnemyWave(pObject, pEvent):
            # Warn the player that the enemy has entered the set
            debug(__name__ + ", firstEnemyWave")
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()
            Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
            pSequence = App.TGSequence_Create()
            pSet = App.g_kSetManager.GetSet("bridge")
            pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
            pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "EnemiesEnteringTheSet", None, 0, Database))
            pSequence.Play()
            
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Create the Attacking ship
            Att1 = "Renegade 1"
            import Custom.DS9FX.DS9FXShips
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att1, "Random 1 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Renegade 1", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Renegade 2"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att2, "Random 2 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Renegade 2", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

            # Create the Attacking ship
            Att3 = "Renegade 3"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att3, "Random 3 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Renegade 3", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Renegade 4"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "Random 4 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Renegade 4", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


            # Create the Attacking ship
            Att5 = "Renegade 5"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att5, "Random 5 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Renegade 5", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))


# 2nd Wave coming in your way
def secondEnemyWave(pObject, pEvent):
            debug(__name__ + ", secondEnemyWave")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Create the Attacking ship
            Att1 = "Renegade 6"
            import Custom.DS9FX.DS9FXShips
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att1, "Random 1 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Renegade 6", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Renegade 7"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att2, "Random 2 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Renegade 7", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

            # Create the Attacking ship
            Att3 = "Renegade 8"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att3, "Random 3 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Renegade 8", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Renegade 9"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "Random 4 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Renegade 9", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


            # Create the Attacking ship
            Att5 = "Renegade 10"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att5, "Random 5 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Renegade 10", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))


# 3rd wave of enemy ships
def thirdEnemyWave(pObject, pEvent):
            # Warn the player that the enemy has entered the set
            debug(__name__ + ", thirdEnemyWave")
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()
            Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
            pSequence = App.TGSequence_Create()
            pSet = App.g_kSetManager.GetSet("bridge")
            pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
            pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "EnemiesEnteringTheSet", None, 0, Database))
            pSequence.Play()
            
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Create the Attacking ship
            Att1 = "Renegade 11"
            import Custom.DS9FX.DS9FXShips
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att1, "Random 1 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Renegade 11", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Renegade 12"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att2, "Random 2 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Renegade 12", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

            # Create the Attacking ship
            Att3 = "Renegade 13"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att3, "Random 3 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Renegade 13", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Renegade 14"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "Random 4 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Renegade 14", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


            # Create the Attacking ship
            Att5 = "Renegade 15"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att5, "Random 5 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Renegade 15", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))
            
# Final wave of enemy ships
def fourthEnemyWave(pObject, pEvent):
            debug(__name__ + ", fourthEnemyWave")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()
            
            # Create the Attacking ship
            Att1 = "Renegade 16"
            import Custom.DS9FX.DS9FXShips
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att1, "Random 1 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker1 = MissionLib.GetShip("Renegade 16", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "Renegade 17"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, pSet, Att2, "Random 2 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker2 = MissionLib.GetShip("Renegade 17", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

            # Create the Attacking ship
            Att3 = "Renegade 18"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att3, "Random 3 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker3 = MissionLib.GetShip("Renegade 18", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "Renegade 19"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att4, "Random 4 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker4 = MissionLib.GetShip("Renegade 19", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


            # Create the Attacking ship
            Att5 = "Renegade 20"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, pSet, Att5, "Random 5 Location")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            # Assign AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            Attacker5 = MissionLib.GetShip("Renegade 20", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))


# Help is on the way capt!
def SupportArriving(pObject, pEvent):
            debug(__name__ + ", SupportArriving")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(SupportArrivingTxt(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()

# Print text on the screen!
def SupportArrivingTxt(pPane):
            # Sequence which contains only 1 line of text
            debug(__name__ + ", SupportArrivingTxt")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # prompt
            pAction = LineAction("Help is on the way Sir!", pPane, 3, 10, 12)
            pSequence.AddAction(pAction, None, 0)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()
            

# Get currently used ship type
def GetShipType(pShip):
                debug(__name__ + ", GetShipType")
                if pShip.GetScript():
                        return string.split(pShip.GetScript(), '.')[-1]
                return None

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
        if (ShipName in RenegadeShips):
            
            global RenegadeShips
            
            RenegadeShips.remove(ShipName)
            
            if (len(RenegadeShips) == 0):
                
                SaveProgress(None, None)

                ReenableAllButtons()

                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".HelpExiting", App.g_kUtopiaModule.GetGameTime() + 27, 0, 0)
                
                MissionCompletedPrompt(None, None)

                try:                
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                except:
                    pass
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")

                except:
                    pass
                    
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")


# Help signing out. We are RTB!
def HelpExiting(pObject, pEvent):
        debug(__name__ + ", HelpExiting")
        pSet = MissionLib.GetPlayer().GetContainingSet()

        try:
            pSet.DeleteObjectFromSet("USS Antartica")
        except:
            pass
        try:
            pSet.DeleteObjectFromSet("USS Washington")
        except:
            pass
        try:
            pSet.DeleteObjectFromSet("USS Avenger")

        except:
            pass
            

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


# Mission Completed
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
            pAction = LineAction("Mission Completed!\n\nYou saved us all Captain!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 5)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


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
 
            # Remove all active handlers
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".DS9Exploding")
                
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

            HelpExiting(None, None)
 
            # Remove all active handlers
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            except:
                pass
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                
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
            

# Save progress
def SaveProgress(pObject, pEvent):
            debug(__name__ + ", SaveProgress")
            global pPlayerShipType

            file = nt.open(Path, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
            nt.write(file, "Ship = " + "'" + pPlayerShipType + "'")
            nt.close(file)


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
