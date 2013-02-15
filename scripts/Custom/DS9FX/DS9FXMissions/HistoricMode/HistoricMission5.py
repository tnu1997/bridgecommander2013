from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# by USS Sovereign, Mission: The Way of the Warrior

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
        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: The Way of the Warrior"), 0.0, 0.0, None, 1, 0.30, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Take control of DS9\n-Hold off the Klingon ships until reinforcements arrive"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("The Klingons have withdrawn from the Khitomer Accords after we have found out about their plans to invade Cardassia. The Klingon fleet which was briefly stationed here is turning against us. Take control of the DS9 to repel the invaders. You only need to hold them off until Federation Starships can arrive. "), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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
            pAction = LineAction("Mission: The Way of the Warrior", pPane, 3, 6, 16)
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

            MissionSetup()

            if pIntroVid == 1:
                    # Play the DS9FX Intro Movie
                    from Custom.DS9FX.DS9FXVids import DS9FXIntroVideo

                    DS9FXIntroVideo.PlayMovieSeq(None, None)

            else:
                    pass


# Set the new player
def SetupPlayer():
            debug(__name__ + ", SetupPlayer")
            pPlayer = MissionLib.GetPlayer()
            pPlayerName = pPlayer.GetName()
            pSet = pPlayer.GetContainingSet()
            pSet.DeleteObjectFromSet(pPlayerName)
                    
            GetPlayer = MissionLib.GetShip('Deep_Space_9', pSet)
            
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


# Mission setup
def MissionSetup():
            debug(__name__ + ", MissionSetup")
            global sShips

            # Grab some values
            pGame = App.Game_GetCurrentGame()
            pEpisode = pGame.GetCurrentEpisode()
            pMission = pEpisode.GetCurrentMission()

            # 1st Remove any ships that are not supposed to be in the mission
            pPlayer = MissionLib.GetPlayer().GetName()
            pSet = MissionLib.GetPlayer().GetContainingSet()
            
            for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                if kShip.GetName() == pPlayer:
                    continue
                # Oops I forgot about the comet and the wormhole lol
                elif kShip.GetName() == 'Bajoran Wormhole':
                    continue
                elif kShip.GetName() == 'Comet Alpha':
                    continue
                else:
                    pSet.DeleteObjectFromSet(kShip.GetName())
            
            sShips = ["IKS TuQmeh", "IKS Jawbogh", "IKS NabVad", "IKS Qu'ta'Dl'Hegh", "IKS QumHa'bogh", "IKS Qochbe'meH", "IKS QuSmey", "IKS Dotlh", "IKS Vuplu'bejnes", "IKS Qo'Joh", "IKS Satlho'Qu'tlh", "IKS IwwIj'ay'Hom"]  

            SpawnShips()

            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")



# Spawn ships
def SpawnShips():
            # Get some values
            debug(__name__ + ", SpawnShips")
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()

            import Custom.DS9FX.DS9FXShips
            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, "IKS TuQmeh", "FriendlyPos1")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("IKS TuQmeh")

            # Assign it's AI
            import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

            ship1 = MissionLib.GetShip("IKS TuQmeh", pSet)

            pship1 = App.ShipClass_Cast(ship1)

            pship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship1))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, "IKS Jawbogh", "FriendlyPos2")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("IKS Jawbogh")

            ship2 = MissionLib.GetShip("IKS Jawbogh", pSet)

            pship2 = App.ShipClass_Cast(ship2)

            pship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship2))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, "IKS NabVad", "FriendlyPos3")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("IKS NabVad")

            ship3 = MissionLib.GetShip("IKS NabVad", pSet)

            pship3 = App.ShipClass_Cast(ship3)

            pship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship3))


            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXD7Ktinga, pSet, "IKS Qu'ta'Dl'Hegh", "FriendlyPos4")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("IKS Qu'ta'Dl'Hegh")

            ship4 = MissionLib.GetShip("IKS Qu'ta'Dl'Hegh", pSet)

            pship4 = App.ShipClass_Cast(ship4)

            pship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship4))

            loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXD7Ktinga, pSet, "IKS QumHa'bogh", "FriendlyPos5")
            
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName("IKS QumHa'bogh")

            ship5 = MissionLib.GetShip("IKS QumHa'bogh", pSet)

            pship5 = App.ShipClass_Cast(ship5)

            pship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pship5))

            # Create the Attacking ship
            Att1 = "IKS Qochbe'meH"
            pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXVorcha, pSet, Att1, "EnemyPos1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att1)

            Attacker1 = MissionLib.GetShip("IKS Qochbe'meH", pSet) 

            pAttacker1 = App.ShipClass_Cast(Attacker1)

            pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

            # Create the Attacking ship
            Att2 = "IKS QuSmey"
            pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, Att2, "EnemyPos2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att2)

            Attacker2 = MissionLib.GetShip("IKS QuSmey", pSet) 

            pAttacker2 = App.ShipClass_Cast(Attacker2)

            pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


            # Create the Attacking ship
            Att3 = "IKS Dotlh"
            pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXNeghvar, pSet, Att3, "EnemyPos3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att3)


            Attacker3 = MissionLib.GetShip("IKS Dotlh", pSet) 

            pAttacker3 = App.ShipClass_Cast(Attacker3)

            pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


            # Create the Attacking ship
            Att4 = "IKS Vuplu'bejnes"
            pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, Att4, "EnemyPos4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att4)


            Attacker4 = MissionLib.GetShip("IKS Vuplu'bejnes", pSet) 

            pAttacker4 = App.ShipClass_Cast(Attacker4)

            pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))

            # Create the Attacking ship
            Att5 = "IKS Qo'Joh"
            pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, Att5, "EnemyPos5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att5)

            Attacker5 = MissionLib.GetShip("IKS Qo'Joh", pSet) 

            pAttacker5 = App.ShipClass_Cast(Attacker5)

            pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

            # Create the Attacking ship
            Att6 = "IKS Satlho'Qu'tlh"
            pAtt6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, Att6, "EnemyPos6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att6)

            Attacker6 = MissionLib.GetShip("IKS Satlho'Qu'tlh", pSet) 

            pAttacker6 = App.ShipClass_Cast(Attacker6)

            pAttacker6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker6))


            # Create the Attacking ship
            Att7 = "IKS IwwIj'ay'Hom"
            pAtt7 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXBirdOfPrey, pSet, Att7, "EnemyPos7")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Att7)

            Attacker7 = MissionLib.GetShip("IKS IwwIj'ay'Hom", pSet) 

            pAttacker7 = App.ShipClass_Cast(Attacker7)

            pAttacker7.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker7))
            

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

            if (len(sShips) == 3):
                from Custom.DS9FX.DS9FXObjects import DS9Ships

                DS9Ships.DS9SetShips()

                ReenableAllButtons()

                RemoveShips()

                RestoreToDefault()

                MissionWin(None, None)

                try:                
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                except:
                    pass
                
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")

            else:
                pObject.CallNextHandler(pEvent)


# Remove leftover enemy ships
def RemoveShips():
            debug(__name__ + ", RemoveShips")
            global sShips
            pPlayer = MissionLib.GetPlayer()
            pSet = pPlayer.GetContainingSet()

            for ship in sShips:
                    pSet.DeleteObjectFromSet(ship)



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
            pAction = LineAction("Federation support has arrived sir!\n\nMission Completed!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 10)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()


def RestoreToDefault():
            debug(__name__ + ", RestoreToDefault")
            import Custom.DS9FX.DS9FXShips
            pShip = Custom.DS9FX.DS9FXShips.HistoricMission5Player


            pPlayer = MissionLib.GetPlayer()
            pPlayerName = pPlayer.GetName()
            pName = "Player"
            pSet = pPlayer.GetContainingSet()
            pSet.DeleteObjectFromSet(pPlayerName)
            
            loadspacehelper.CreateShip(pShip, pSet, pName, "Player Start")
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetFriendlyGroup().AddName(pName)
        
            GetPlayer = MissionLib.GetShip(pName, pSet)
            
            # Set the new player
            pGame = App.Game_GetCurrentGame()
            pGame.SetPlayer(GetPlayer)

            # Restore fully armed DS9
            from Custom.DS9FX.DS9FXObjects import DS9Stations

            DS9Stations.DS9SetStations()


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
