#####################################################################
#   This code was developed from scratch by me. Almost nothing      #
#   from the former code is in here.                                #
#                                                                   #
#   Original Author: Nanobyte                                       #
#                                                                   #
#   Redesign: USS Sovereign (BCS:TNG)                               #
#                                                                   #
#   License: This file has been modified with the permission from   #
#   the original author. To modify or use the current code, you     #
#   need to ask Nanobyte to modify NanoFX and me to modify this     #
#   current code. Any usage of this code in any other mod needs     #
#   to be credited.                                                 #
#####################################################################


##### Imports
import App
import Foundation
import MissionLib
import string

##### Events
ET_CLOSE = App.UtopiaModule_GetNextEventType()
ET_CREATE_WINDOW = App.UtopiaModule_GetNextEventType()
ET_WARP_SPEED_CHANGED = App.UtopiaModule_GetNextEventType()
ET_TIMER = App.UtopiaModule_GetNextEventType()
ET_TIMER_2 = App.UtopiaModule_GetNextEventType()

##### Vars
pWindow = None
WarpSpeed = 6.0


##### Dummy Function, so we don't have to override LoadNanoFX.py
def SetupWarpSpeedButtons(iMaxWarp = 9):
        return
    

##### Main Function
def SetupButtons():
        global pHelm

        ##### A small QBR Quick Fix
        DeleteMenuButton("Helm", "Warp Speed")

        ##### Main Button        
        pButton = CreateMenuButton("Warp Speed", "Helm", __name__ + ".Window")

        ##### Event Types        
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pBridge = App.g_kSetManager.GetSet("bridge")
        pHelm = App.CharacterClass_GetObject(pBridge, "Helm")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".CloseWindow")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WARP_SPEED_CHANGED, pMission, __name__ + ".UpdateSlider")
	if App.g_kSetManager.GetSet("bridge"):
        	pHelm.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow")

        ##### Timer
        CreateTimer(ET_TIMER, __name__ + ".CreateWindow", App.g_kUtopiaModule.GetGameTime() + 2)



##### Create Window Frame                
def CreateWindow(pObject, pEvent):
        global pWindow

        pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Warp Speed Selector"), 0.0, 0.0, None, 1, 0.3, 0.4, App.g_kMainMenuBorderMainColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(pWindow, 0.3, 0.3)

        pWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        pWindow.SetNotVisible()


##### Create Buttons in Window        
def CreateWindowPartII():
        global pWindow, pText, pSlider, maxWarp, cruiseWarp, pCurrentWarpText, pMaxWarpText, pButton
        
        x = 0.02
        y = 0.04
        pSlider = CreateWarpSlidebar(App.TGString("Warp Bar"), ET_WARP_SPEED_CHANGED, 0.0)
        pSlider.Resize(0.25, 0.04, 0)
        SetWarpSpeed(0.1)
        pWindow.AddChild(pSlider, x, y, 0)

        x = 0.02
        y = y + 0.08
        pText = App.TGParagraph_CreateW(App.TGString("Selected Warp Speed: 0.1"), pWindow.GetMaximumInteriorWidth(), None, '', pWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pWindow.AddChild(pText, x, y, 0)

        MaximumWarp = maxWarp * 10
        MaxmimumWarp = float(str(MaximumWarp)[0:3+1])
        if MaximumWarp > 9.99:
            MaximumWarp = 9.99
            
        x = 0.02
        y = y + 0.04
        pMaxWarpText = App.TGParagraph_CreateW(App.TGString("Ships Max Warp Speed: " + str(MaximumWarp)), pWindow.GetMaximumInteriorWidth(), None, '', pWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pWindow.AddChild(pMaxWarpText, x, y, 0)

        CruisingWarp = cruiseWarp * 10
        CruisingWarp = float(str(CruisingWarp)[0:3+1])
        if CruisingWarp > 9.99:
            CruisingWarp = 9.99
            
        x = 0.02
        y = y + 0.04
        pCurrentWarpText = App.TGParagraph_CreateW(App.TGString("Ships Cruise Warp Speed: " + str(CruisingWarp)), pWindow.GetMaximumInteriorWidth(), None, '', pWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
        pWindow.AddChild(pCurrentWarpText, x, y, 0)

        x = 0.02
        y = y + 0.06
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetDestination(pHelm)
        pEvent.SetInt(0)
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.13125, 0.034583)
        pButton.SetNormalColor(App.g_kMainMenuButtonColor)
        pButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
        pButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
        pButton.SetDisabledColor(App.g_kSTMenu1Disabled)
        pButton.SetColorBasedOnFlags()
        pWindow.AddChild(pButton, x, y, 0)
        

        pWindow.InteriorChangedSize()
        
        pWindow.Layout()



##### Display Selected Warp Speed        
def UpdateSlider(pObject, pEvent):
        global pText, pWindow, pSlider

        
        try:
            fValue = pEvent.GetFloat()

        except AttributeError:
            return

        if fValue < 0.01:
            fValue = 0.01

        elif fValue > 0.9999:
            fValue = 0.9999

        fSpeed = fValue * 10

        fSpeed = float(str(fSpeed)[0:3+1])
        
        pText.SetString("Selected Warp Speed: " + str(fSpeed))

        fWarpSpeed = fSpeed

        SetWarpSpeed(fWarpSpeed)

        pSlider.Resize(0.25, 0.04, 0)

        pSlider.SetValue(fValue)

        pWindow.InteriorChangedSize()
        
        pWindow.Layout()

	pObject.CallNextHandler(pEvent)


##### Mouse Pass Over The Window	
def MousePass(Window, pEvent):
    
        Window.CallNextHandler(pEvent)

        if pEvent.EventHandled() == 0:
                pEvent.SetHandled()


##### Close Window        
def CloseWindow(pObject, pEvent):
        global pWindow, pText, pSlider, pCurrentWarpText, pMaxWarpText, pButton

        if not pWindow:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        
        if pWindow.IsVisible():
                pTCW.MoveToBack(pWindow)
                pWindow.SetNotVisible()
                pWindow.DeleteChild(pText)
                pWindow.DeleteChild(pSlider)
                pWindow.DeleteChild(pCurrentWarpText)
                pWindow.DeleteChild(pMaxWarpText)
                pWindow.DeleteChild(pButton)

        pObject.CallNextHandler(pEvent)


##### Open Window Function      
def Window(pObject, pEvent):
        global pWindow
        
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not pWindow:
                return

        if not pWindow.IsVisible():
                CreateWindowPartII()
                pWindow.SetVisible()
                pTCW.MoveToFront(pWindow)                
                pTCW.MoveTowardsBack(pWindow)


##### Mostly from SetVolumeButton made by Totally Games
def CreateWarpSlidebar (pName, eType, fValue):
        global maxWarp, cruiseWarp
        
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pBar = App.STNumericBar_Create()

        ##### Grab specific ship speed values
	maxWarp = GetMaxWarp()
	cruiseWarp = GetCruiseWarp()

        ##### Set Our Range. 
	pBar.SetRange(0.0, maxWarp)
	pBar.SetKeyInterval(0.01)
	pBar.SetMarkerValue(cruiseWarp)
	pBar.SetValue(fValue)
	pBar.SetUseMarker(0)
	pBar.SetUseAlternateColor(0)
	pBar.SetUseButtons(0)

	kNormalColor = App.g_kSTMenu3NormalBase
	kEmptyColor = App.g_kSTMenu3Disabled

	pBar.SetNormalColor(kNormalColor)
	pBar.SetEmptyColor(kEmptyColor)
	pText = pBar.GetText()
	pText.SetStringW(pName)

	pBar.Resize(0.25, 0.04, 0)

	pEvent = App.TGFloatEvent_Create()
	pEvent.SetDestination(pOptionsWindow)
	pEvent.SetFloat(fValue)
	pEvent.SetEventType(eType)

	pBar.SetUpdateEvent(pEvent)

	return pBar
    


##### Called At Exiting                
def exiting(pObject, pEvent):
        global pWindow

        if pWindow:
                pWindow.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                pTCW.DeleteChild(pWindow)



##### The stuff here will create a Button                
def CreateMenuButton(ButtonName, Person, Function, EventInt = 0):        
        pMenu = GetBridgeMenu(Person)
        ET_EVENT = App.Mission_GetNextEventType()

        pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, Function)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_EVENT)
        pEvent.SetDestination(pMenu)
        pEvent.SetInt(EventInt)
        pButton = App.STButton_CreateW(App.TGString(ButtonName), pEvent)

        pMenu.AddChild(pButton)
        
        pLowest = FindLowestChild(pMenu)
	pButton.SetPosition(pLowest.GetLeft(), pLowest.GetBottom(), 0)

        pMenu.AddChild(None) 

        return pButton


##### Find the lowest child for the new button position
def FindLowestChild(Pane):
        Index = Pane.GetTrueNumChildren() - 1
        iBottom = 0
        LowestChild = None
        Current = None
        while Index >= 0:
            Current = Pane.GetTrueNthChild(Index)
            CurrentBottom = Current.GetBottom()
            if(CurrentBottom > iBottom):
                iBottom = CurrentBottom
                LowestChild = Current
            Index = Index - 1
        return LowestChild
    


##### Deletes specified menu button
def DeleteMenuButton(sMenuName, sButtonName, sSubMenuName = None):
                pMenu   = GetBridgeMenu(sMenuName)
                pButton = pMenu.GetButton(sButtonName)
                if sSubMenuName != None:
                        pMenu = pMenu.GetSubmenu(sSubMenuName)
                        pButton = pSubMenu.GetButton(sButtonName)

                pMenu.DeleteChild(pButton)


##### Get Bridge Menu Button    
def GetBridgeMenu(Person):
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString(Person))
        App.g_kLocalizationManager.Unload(pDatabase)
        return pMenu
    

##### Create Timer    
def CreateTimer(event, sFunctionHandler, fStart):
	# Setup the handler function.
	pGame = App.Game_GetCurrentGame()
	if (pGame == None):
		return None
	pEpisode = pGame.GetCurrentEpisode()
	if (pEpisode == None):
		return None
	pMission = pEpisode.GetCurrentMission()
	if (pMission == None):
		return None

	pMission.AddPythonFuncHandlerForInstance(event, sFunctionHandler)

	# Create the event and the event timer.
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(event)
	pEvent.SetDestination(pMission)
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(fStart)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pEvent)

        # Add the timer to the game.
	App.g_kTimerManager.AddTimer(pTimer)
	
	return pTimer


##### Reset Warp Speed    
def ResetWarpSpeed():
	global WarpSpeed
	SetWarpSpeed(6.0)


##### Set Warp Speed
def SetWarpSpeed(i):
	global WarpSpeed
	WarpSpeed=i
	
	try:
		from Custom.QBautostart.Libs.LibWarp import SetCurWarpSpeed
		SetCurWarpSpeed(MissionLib.GetPlayer(), WarpSpeed)
	except ImportError:
		pass


##### Get Warp Speed	
def GetWarpSpeed():
	return WarpSpeed


##### Returns Cruising Speed of the ship
def ReturnCruiseSpeed():
        cruiseWarp = GetCruiseWarp()
        CruisingWarp = cruiseWarp * 10
        CruisingWarp = float(str(CruisingWarp)[0:3+1])
        if CruisingWarp > 9.99:
            CruisingWarp = 9.99
            
        return CruisingWarp
    

##### Get Max Warp Speed From The Ships Foundation File
def GetMaxWarp():
        pPlayer = MissionLib.GetPlayer()
        pShip = GetShipType(pPlayer)

	if Foundation.shipList.has_key(pShip):
            pFoundationShip = Foundation.shipList[pShip]
            if pFoundationShip and hasattr(pFoundationShip, "fMaxWarp"):
                        pScale = pFoundationShip.fMaxWarp / 10
                        if pScale > 1.0:
                            pScale = 1.0
			return pScale
		    
	    else:
                return 0.6
            
	else:
            return 0.6
        

##### Get Cruise Warp Speed
def GetCruiseWarp():
        pPlayer = MissionLib.GetPlayer()
        pShip = GetShipType(pPlayer)

	if Foundation.shipList.has_key(pShip):
            pFoundationShip = Foundation.shipList[pShip]
            if pFoundationShip and hasattr(pFoundationShip, "fCruiseWarp"):
                        pScale = pFoundationShip.fCruiseWarp / 10
                        if pScale > 1.0:
                            pScale = 1.0
			return pScale
		    
	    else:
                return 0.6
            
	else:
            return 0.6


##### It returns currently used Ship HP
def GetShipType(pShip):
                if pShip.GetScript():
                        return string.split(pShip.GetScript(), '.')[-1]
                return None
