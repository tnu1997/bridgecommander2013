from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# by USS Sovereign, Mission: The tides of Idran

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
        pIconWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mission: The tides of Idran"), 0.0, 0.0, None, 1, 0.30, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pIconWindow, 0, 0)

        pObjectivesWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Objectives"), 0.0, 0.0, None, 1, 0.29, 0.30, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pObjectivesWindow, 0.31, 0)

        pBriefingWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Briefing"), 0.0, 0.0, None, 1, 0.60, 0.25, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pBriefingWindow, 0, 0.31)

        pButtonWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Please Select"), 0.0, 0.0, None, 1, 0.60, 0.08, App.g_kMainMenuBorderMainColor)
        pMainPane.AddChild(pButtonWindow, 0, 0.57)

        pText = App.TGParagraph_CreateW(App.TGString("-Go to Gamma Quadrant\n-Stop waves of Dominion ships trying to get through the wormhole\n-Once the objectives are met, return to DS9"), pObjectivesWindow.GetMaximumInteriorWidth(), None, '', pObjectivesWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pObjectivesWindow.AddChild(pText, 0, 0.01)

        pText = App.TGParagraph_CreateW(App.TGString("This is a difficult assignment, Captain. You are required to enter the wormhole and stop incoming Jem'Hadar ships before they can enter the Alpha Quadrant. We suspect that this is one desperate attempt of the Dominion to send reinforcements to their friends in the Alpha Quadrant. Stop them at ALL costs!"), pBriefingWindow.GetMaximumInteriorWidth(), None, '', pBriefingWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
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
            pAction = LineAction("Mission: The tides of Idran", pPane, 3, 6, 16)
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
        
        # Grab some values
        debug(__name__ + ", MissionInitiate")
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

        # Start up a Mission Placement Handler
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionPlacement")

        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
        
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

        if pIntroVid == 1:
                # Play the DS9FX Intro Movie
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


# Let's define Mission Placement Handler
def MissionPlacement(pObject, pEvent):
        debug(__name__ + ", MissionPlacement")
        global sShips

        sShips = ['Dominion 1','Dominion 2', 'Dominion 3', 'Dominion 4', 'Dominion 5', 'Dominion 6', 'Dominion 7', 'Dominion 8', 'Dominion 9', 'Dominion 10', 'Dominion 11', 'Dominion 12', 'Dominion 13', 'Dominion 14', 'Dominion 15', 'Dominion 16', 'Dominion 17', 'Dominion 18']
        
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        if (pSet.GetName() == "GammaQuadrant1"):
            
            # Disable enter wormhole Button, you have to fight
            MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableEnterButton", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)
                        
            Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
            GammaSet = Gamma.GetSet()

            # 18 ships in total       
            Bug1 = "Dominion 1"
            import Custom.DS9FX.DS9FXShips
            pBug1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug1, "Location 6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug1)

            # Assign it's AI.
            import Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI

            Bugship1 = MissionLib.GetShip(Bug1, GammaSet) 

            pBugship1 = App.ShipClass_Cast(Bugship1)

            pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship1))

            # 18 ships in total       
            Bug2 = "Dominion 2"
            pBug2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug2, "Location 5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug2)

            Bugship2 = MissionLib.GetShip(Bug2, GammaSet) 

            pBugship2 = App.ShipClass_Cast(Bugship2)

            pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship2))

            # 18 ships in total       
            Bug3 = "Dominion 3"
            pBug3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug3, "Location 4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug3)

            Bugship3 = MissionLib.GetShip(Bug3, GammaSet) 

            pBugship3 = App.ShipClass_Cast(Bugship3)

            pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship3))

            # 18 ships in total       
            Bug4 = "Dominion 4"
            pBug4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug4, "Location 3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug4)

            Bugship4 = MissionLib.GetShip(Bug4, GammaSet) 

            pBugship4 = App.ShipClass_Cast(Bugship4)

            pBugship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship4))

            # 18 ships in total       
            Bug5 = "Dominion 5"
            pBug5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug5, "Location 2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug5)

            Bugship5 = MissionLib.GetShip(Bug5, GammaSet) 

            pBugship5 = App.ShipClass_Cast(Bugship5)

            pBugship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship5))

            # 18 ships in total       
            Bug6 = "Dominion 6"
            pBug6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug6, "Location 1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug6)

            Bugship6 = MissionLib.GetShip(Bug6, GammaSet) 

            pBugship6 = App.ShipClass_Cast(Bugship6)

            pBugship6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship6))


            # Kill the handler
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionPlacement")

            # Ship destroyed
            App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                        

        else:
            return


def DisableEnterButton(pObject, pEvent):
            debug(__name__ + ", DisableEnterButton")
            global bEnter
            
            try:
        
                bEnter = DS9FXMenuLib.GetButton("Enter Wormhole", "Helm", "DS9FX")
            
                bEnter.SetDisabled()

            
            except:
            
                pass


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
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionPlacement")
            except:
                pass
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")
            except:
                pass
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
            except:
                pass
            try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".DisableButtons")
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


# Object is exploding
def ObjectExploding(pObject, pEvent):
        debug(__name__ + ", ObjectExploding")
        global sShip, bEnter
        
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
        if (ShipName in sShips):
            
            global sShips
            
            sShips.remove(ShipName)

            if (len(sShips) == 12):
                SpawnSecondWave()

            elif (len(sShips) == 6):
                SpawnThirdWave()

            elif (len(sShips) == 0):
                try:
                   bEnter.SetEnabled()
                except:
                    pass
                
                ObjectiveCompleted(None, None)
                AdditionalHandlersStarted(None, None)
            
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")


# 2nd wave
def SpawnSecondWave():
            debug(__name__ + ", SpawnSecondWave")
            Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
            GammaSet = Gamma.GetSet()

            # 18 ships in total       
            Bug1 = "Dominion 7"
            import Custom.DS9FX.DS9FXShips
            pBug1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug1, "Location 6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug1)

            # Assign it's AI.
            import Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI

            Bugship1 = MissionLib.GetShip(Bug1, GammaSet) 

            pBugship1 = App.ShipClass_Cast(Bugship1)

            pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship1))

            # 18 ships in total       
            Bug2 = "Dominion 8"
            pBug2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug2, "Location 5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug2)

            Bugship2 = MissionLib.GetShip(Bug2, GammaSet) 

            pBugship2 = App.ShipClass_Cast(Bugship2)

            pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship2))

            # 18 ships in total       
            Bug3 = "Dominion 9"
            pBug3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug3, "Location 4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug3)

            Bugship3 = MissionLib.GetShip(Bug3, GammaSet) 

            pBugship3 = App.ShipClass_Cast(Bugship3)

            pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship3))

            # 18 ships in total       
            Bug4 = "Dominion 10"
            pBug4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug4, "Location 3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug4)

            Bugship4 = MissionLib.GetShip(Bug4, GammaSet) 

            pBugship4 = App.ShipClass_Cast(Bugship4)

            pBugship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship4))

            # 18 ships in total       
            Bug5 = "Dominion 11"
            pBug5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug5, "Location 2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug5)

            Bugship5 = MissionLib.GetShip(Bug5, GammaSet) 

            pBugship5 = App.ShipClass_Cast(Bugship5)

            pBugship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship5))

            # 18 ships in total       
            Bug6 = "Dominion 12"
            pBug6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug6, "Location 1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug6)

            Bugship6 = MissionLib.GetShip(Bug6, GammaSet) 

            pBugship6 = App.ShipClass_Cast(Bugship6)

            pBugship6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship6))
        

# 3rd wave
def SpawnThirdWave():
            debug(__name__ + ", SpawnThirdWave")
            Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
            GammaSet = Gamma.GetSet()

            # 18 ships in total       
            Bug1 = "Dominion 13"
            import Custom.DS9FX.DS9FXShips
            pBug1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug1, "Location 6")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug1)

            # Assign it's AI.
            import Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI

            Bugship1 = MissionLib.GetShip(Bug1, GammaSet) 

            pBugship1 = App.ShipClass_Cast(Bugship1)

            pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship1))

            # 18 ships in total       
            Bug2 = "Dominion 14"
            pBug2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug2, "Location 5")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug2)

            Bugship2 = MissionLib.GetShip(Bug2, GammaSet) 

            pBugship2 = App.ShipClass_Cast(Bugship2)

            pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship2))

            # 18 ships in total       
            Bug3 = "Dominion 15"
            pBug3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug3, "Location 4")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug3)

            Bugship3 = MissionLib.GetShip(Bug3, GammaSet) 

            pBugship3 = App.ShipClass_Cast(Bugship3)

            pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship3))

            # 18 ships in total       
            Bug4 = "Dominion 16"
            pBug4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug4, "Location 3")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug4)

            Bugship4 = MissionLib.GetShip(Bug4, GammaSet) 

            pBugship4 = App.ShipClass_Cast(Bugship4)

            pBugship4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship4))

            # 18 ships in total       
            Bug5 = "Dominion 17"
            pBug5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug5, "Location 2")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug5)

            Bugship5 = MissionLib.GetShip(Bug5, GammaSet) 

            pBugship5 = App.ShipClass_Cast(Bugship5)

            pBugship5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship5))

            # 18 ships in total       
            Bug6 = "Dominion 18"
            pBug6 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug6, "Location 1")

            # Add it to a enemy group
            pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
            pMission.GetEnemyGroup().AddName(Bug6)

            Bugship6 = MissionLib.GetShip(Bug6, GammaSet) 

            pBugship6 = App.ShipClass_Cast(Bugship6)

            pBugship6.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship6))
        

# You're done
def ObjectiveCompleted(pObject, pEvent):
            debug(__name__ + ", ObjectiveCompleted")
            global pPaneID
            # Attach a pane
            pPane = App.TGPane_Create(1.0, 1.0)
            App.g_kRootWindow.PrependChild(pPane)

            # Create a sequence and play it
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            pSequence.AppendAction(ObjectiveCompletedTxt(pPane))
            pPaneID = pPane.GetObjID()
            pSequence.Play()


# txt
def ObjectiveCompletedTxt(pPane):
            debug(__name__ + ", ObjectiveCompletedTxt")
            pSequence = App.TGSequence_Create()
            pSequence.SetUseRealTime (1)
            
            # warning prompt
            pAction = LineAction("Objectives completed sir, we should return to DS9!", pPane, 6, 10, 12)
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
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".BackToDS9")

            try:                
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".PlayerExploding")

            except:
                pass

         
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
            
            # 6 second warning prompt
            pAction = LineAction("Mission Completed!", pPane, 6, 6, 12)
            pSequence.AddAction(pAction, None, 30)
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
