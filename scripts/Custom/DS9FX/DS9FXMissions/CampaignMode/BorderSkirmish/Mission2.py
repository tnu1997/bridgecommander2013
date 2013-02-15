from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# by USS Sovereign. Mission 2 from the DS9FX Border Skirmish Campaign.

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
pPaneID = App.NULL_ID

# Path where we should save a mission progress py file
Path  = "scripts\\Custom\\DS9FX\\DS9FXMissions\\CampaignMode\\BorderSkirmish\\Save\\mission3.py"

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
        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: Investigations"), 0.0, 0.0, None, 1, 0.30, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Return to Gamma Quadrant\n-Do not engage any enemy ships\n-Wait for 5 minutes for the scan to complete"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)
        
        pText = App.TGParagraph_CreateW(App.TGString("The data recorder you retrieved from the rogue Jem'Hadar bugship has proven extremely useful for us to get a lead on their Ketracel White facility. You are to return to the Gamma Quadrant and perform a long-range scan in order for us to confirm the location of the base. Do not, I repeat DO NOT engage the enemy, you are to return to DS9 at once."), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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
            pAction = LineAction("Mission: Investigations", pPane, 3, 6, 16)
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
    
        Custom.DS9FX.DS9FXmain.DisableWarpButton()
        
        
    except:
        
        pass


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

        # Remember player ship
	pPlayer = MissionLib.GetPlayer()
	pPlayerShipType = GetShipType(pPlayer)

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

        # Start up all needed handlers
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
        
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

        if pIntroVid == 1:
                # Play the DS9FX Campaign Intro Movie
                from Custom.DS9FX.DS9FXVids import DS9FXIntroVideo

                DS9FXIntroVideo.PlayMovieSeq(None, None)

        else:
                pass

# Let's restore the user to the ship he used in mission 1
def SetupPlayer():
            debug(__name__ + ", SetupPlayer")
            File = __import__("Save.mission2")
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
            
            # Remove all active handlers
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
            except:
                pass
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
            except:
                pass
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
            except:
                pass
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")
                
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


# Mission has started, spawn 2 additional bugships. 
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
            Bug1 = "Bugship 4"
	    import Custom.DS9FX.DS9FXShips
            pBug1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug1, "Location 1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug1)

            # Assign it's AI. We will reuse the Bugship 1 AI.
            import Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI

            Bugship1 = MissionLib.GetShip(Bug1, GammaSet) 

            pBugship1 = App.ShipClass_Cast(Bugship1)

            pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship1))

            # 2nd ship      
            Bug2 = "Bugship 5"
            pBug2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug2, "Location 2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug2)

            Bugship2 = MissionLib.GetShip(Bug2, GammaSet) 

            pBugship2 = App.ShipClass_Cast(Bugship2)

            pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship2))
           

            # Kill the handler
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")

            # Start a 5 minute timer. That is how long you will have to suffer enemy fire.
            MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".AreaScanned", App.g_kUtopiaModule.GetGameTime() + 300, 0, 0)

            # Wait prompt
            Wait(None, None)

            # User musn't fire a single shot
            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")
                        

        else:
            return

# Check the source of the firing 
def FiringHandler(pObject, pEvent):
        debug(__name__ + ", FiringHandler")
        global bEnter
        
        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())
	pPlayer = MissionLib.GetPlayer()
        if pAttacker.GetName() == pPlayer.GetName():
                pSet = pPlayer.GetContainingSet()
                
                try:
                    pSet.DeleteObjectFromSet("Bugship 4")

                except:
                    pass
                
                try:
                    pSet.DeleteObjectFromSet("Bugship 5")
                    
                except:
                    pass
                
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionStart")
                except:
                    pass
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
                except:
                    pass
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
                except:
                    pass
                try:
                    App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")
                 
                except:
                    pass
                
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")
                            
                FailedTxt(None, None)

                try:
                   bEnter.SetEnabled()
                   
                except:
                    pass

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
            
# Scan the area
def AreaScanned(pObject, pEvent):
            debug(__name__ + ", AreaScanned")
            global bEnter, pPaneID
            
            try:
               bEnter.SetEnabled()
            except:
                pass
            

            AdditionalHandlersStarted(None, None)
            
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(MissionLog(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()
            

# Tell the user he can move on
def MissionLog(pPane):
            debug(__name__ + ", MissionLog")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("Area Scanned Captain!\n\nWe should return to DS9!", pPane, 6, 10, 12)
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
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".FiringHandler")
            except:
                pass

            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

            except:
                pass

            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")

            SaveProgress(None, None)
            
            MissionCompletedPrompt(None, None)
            
        else:
            return

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
            pAction = LineAction("Mission Completed!\n\nScans are being analyzed!\n\nExcellent job Captain!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 30)
            pAction = App.TGScriptAction_Create(__name__, "KillPane")
            pSequence.AppendAction(pAction, 0.1)
            pSequence.Play()



# Wait sequence
def Wait(pObject, pEvent):
            debug(__name__ + ", Wait")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(Wait5mins(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# Display txt mssg to the user  
def Wait5mins(pPane):
            debug(__name__ + ", Wait5mins")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("It will take us\n5 mins to conduct a scan.\nWe mustn't engage the enemy!!!", pPane, 6, 10, 12)
            pSequence.AddAction(pAction, None, 30)
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
            
        
# Get currently used ship type
def GetShipType(pShip):
                debug(__name__ + ", GetShipType")
                if pShip.GetScript():
                        return string.split(pShip.GetScript(), '.')[-1]
                return None

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
                
