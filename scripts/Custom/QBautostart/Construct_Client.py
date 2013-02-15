from bcdebug import debug
import App
import MissionLib
import Libs.LibEngineering
from Libs.LibQBautostart import *
from Construct import *


sButtonName = "Construct Control"
pPlayer = None
pConstructWindow = None
ET_CLOSE = Libs.LibEngineering.GetEngineeringNextEventType()
ET_MODE = Libs.LibEngineering.GetEngineeringNextEventType()
ET_SELECT_SHIP_TYPE = Libs.LibEngineering.GetEngineeringNextEventType()
ET_SELECT_SHIP_IN_CONSTRUCT_QUEUE = Libs.LibEngineering.GetEngineeringNextEventType()
ET_ADD_SHIP = Libs.LibEngineering.GetEngineeringNextEventType()
ET_DEL_SHIP = Libs.LibEngineering.GetEngineeringNextEventType()
CLOSE_X_POS                             = 0.3
CLOSE_Y_POS                             = 0
MODE_X_POS                             = 0.3
MODE_Y_POS                             = 0.1
SHIPS_SUBPANE_WIDTH			= 0.22
QUEUE_X_POS			= 0.5390625
QUEUE_Y_POS			= 0.0083333
ADD_X_POS			= 0.250025
ADD_Y_POS			= 0.52
ADD_WIDTH		= 0.2515625
ADD_HEIGHT		= 0.0354167
DEL_X_POS			= 0.250025
DEL_Y_POS			= 0.64
DEL_WIDTH			= 0.2515625
DEL_HEIGHT			= 0.0354167
iSelectedSpecies = 0
iSelectedShipInQueue = 0
pModeButton = None
pConstructQueueButton = None
pSubPane = None

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }


NonSerializedObjects = (
"pPlayer",
"pConstructWindow",
"ET_CLOSE",
"ET_MODE",
"ET_SELECT_SHIP_TYPE",
"pModeButton",
"pConstructQueueButton",
"ET_SELECT_SHIP_IN_CONSTRUCT_QUEUE",
"ET_ADD_SHIP",
"ET_DEL_SHIP",
"pSubPane",
)


def RebuildConstructQueue():
	debug(__name__ + ", RebuildConstructQueue")
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip)
	if not pConstructor:
		return
		
	pConstructQueueButton.KillChildren()
	i = 0
	for sShipType in pConstructor.GetConstructQueue():
		FdtnShip = Foundation.shipList[sShipType]
		sShipLongName = FdtnShip.name
		
		pEvent = App.TGIntEvent_Create()
        	pEvent.SetEventType(ET_SELECT_SHIP_IN_CONSTRUCT_QUEUE)
        	pEvent.SetInt(i)
        	pEvent.SetDestination(pConstructWindow)
                
        	pButton = App.STButton_CreateW(App.TGString(sShipLongName), pEvent)
        	pConstructQueueButton.AddChild(pButton)
		i = i+1
	pConstructQueueButton.Open()
	

def GenerateConstructQueue():
	debug(__name__ + ", GenerateConstructQueue")
	global pConstructQueueButton	
	pConstructQueueButton = App.STCharacterMenu_Create("Construct Queue")
	pConstructWindow.AddChild(pConstructQueueButton, QUEUE_X_POS, QUEUE_Y_POS)


def ConstructControl(pObject, pEvent):
	debug(__name__ + ", ConstructControl")
	if not pConstructWindow:
		CreateConstructWindow()
		CreateWindowInterieur()
	else:
		if pConstructWindow.IsVisible():
			pConstructWindow.SetNotVisible()
			DestroyWindowInterieur()
		else:
			pConstructWindow.SetVisible()
			CreateWindowInterieur()
	
	
def DestroyWindowInterieur():
	debug(__name__ + ", DestroyWindowInterieur")
	if pConstructWindow:
		pSubPane.KillChildren()
		pConstructQueueButton.KillChildren()
		pConstructWindow.KillChildren()


def CreateWindowInterieur():
	debug(__name__ + ", CreateWindowInterieur")
	global pModeButton
	
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip)
	if not pConstructor:
		return
	
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetDestination(pConstructWindow)
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pButton, CLOSE_X_POS, CLOSE_Y_POS, 0)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_MODE)
        pEvent.SetDestination(pConstructWindow)
        pEvent.SetInt(0)
	if pConstructor.GetMode() == "Construct":
		s = "Mode Construct"
	else:
		s = "Mode Repair"
        pModeButton = App.STRoundedButton_CreateW(App.TGString(s), pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pModeButton, MODE_X_POS, MODE_Y_POS, 0)
	
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_ADD_SHIP)
        pEvent.SetDestination(pConstructWindow)
        pButton = App.STRoundedButton_CreateW(App.TGString("Add To Queue"), pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pButton, ADD_X_POS, ADD_Y_POS, 0)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_DEL_SHIP)
        pEvent.SetDestination(pConstructWindow)
        pButton = App.STRoundedButton_CreateW(App.TGString("Del From Queue"), pEvent, 0.13125, 0.034583)
        pConstructWindow.AddChild(pButton, DEL_X_POS, DEL_Y_POS, 0)
	
	BuildShipSelectWindow(pConstructor)
	GenerateConstructQueue()
	RebuildConstructQueue()


def ToggleMode(pObject, pEvent):	
	debug(__name__ + ", ToggleMode")
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip)
	if not pConstructor:
		return
	if pConstructor.GetMode() == "Construct":
		pConstructor.SetMode("Repair")
		s = "Mode Repair"
	else:
		pConstructor.SetMode("Construct")
		s = "Mode Construct"
	if pModeButton:
		pModeButton.SetName(App.TGString(s))


def CreateConstructWindow():
	debug(__name__ + ", CreateConstructWindow")
	global pConstructWindow
	
	pConstructWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Add ships Window"), 0.0, 0.0, None, 1, 0.8, 0.8, App.g_kMainMenuBorderMainColor)
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pTacticalControlWindow.AddChild(pConstructWindow, 0.1, 0.1)
        pConstructWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".PassMouse")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_CLOSE, __name__ + ".ConstructControl")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_MODE, __name__ + ".ToggleMode")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_TYPE, __name__ + ".SelectShipType")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_SELECT_SHIP_IN_CONSTRUCT_QUEUE, __name__ + ".SelectShipInQueue")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_ADD_SHIP, __name__ + ".AddShipToQueue")
	pConstructWindow.AddPythonFuncHandlerForInstance(ET_DEL_SHIP, __name__ + ".DelShipFromQueue")
	
        pConstructWindow.SetVisible()
	pTacticalControlWindow.MoveToFront(pConstructWindow)
	pTacticalControlWindow.MoveTowardsBack(pConstructWindow) # one step back


def AddShipToQueue(pObject, pEvent):
	debug(__name__ + ", AddShipToQueue")
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip)
	if not pConstructor:
		return
	
	sShipType = pConstructor.lShipsToConstruct[iSelectedSpecies]
	pConstructor.AddShipToConstructQueue(sShipType)
	RebuildConstructQueue()


def DelShipFromQueue(pObject, pEvent):
	debug(__name__ + ", DelShipFromQueue")
	global iSelectedShipInQueue
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer or not pPlayer.GetTarget() or not App.ShipClass_Cast(pPlayer.GetTarget()):
		return
	pShip = App.ShipClass_Cast(pPlayer.GetTarget())
	pConstructor = GetConstructInstanceFor(pShip)
	if not pConstructor:
		return
	
	lQueue = pConstructor.GetConstructQueue()
	if iSelectedShipInQueue > len(lQueue)-1:
		iSelectedShipInQueue = len(lQueue)-1
	pConstructor.RemoveShipFromQueue(iSelectedShipInQueue)
	RebuildConstructQueue()

def SelectShipType(pObject, pEvent):
	debug(__name__ + ", SelectShipType")
	global iSelectedSpecies
	iSelectedSpecies = pEvent.GetInt()


def SelectShipInQueue(pObject, pEvent):
	debug(__name__ + ", SelectShipInQueue")
	global iSelectedShipInQueue
	iSelectedShipInQueue = pEvent.GetInt()


def BuildShipSelectWindow(pConstructor):
	debug(__name__ + ", BuildShipSelectWindow")
	global pSubPane
	pSubPane = App.STSubPane_Create(SHIPS_SUBPANE_WIDTH, 500.0, 0)
	
	for iIndex in range(len(pConstructor.lShipsToConstruct)):
		Ship = pConstructor.lShipsToConstruct[iIndex]
		FdtnShip = Foundation.shipList[Ship]
		ShipLongName = FdtnShip.name
		
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_SELECT_SHIP_TYPE)
                pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
                pEvent.SetDestination(pConstructWindow)
		
		pButton = App.STButton_CreateW(App.TGString(ShipLongName), pEvent)
		pEvent.SetSource(pButton)
		
		pSubPane.AddChild(pButton, 0, 0, 0)
        pSubPane.Layout()
        pConstructWindow.AddChild(pSubPane)
	

def IsTargetAFriendlyConstructShip(pPlayer, pShip):
	debug(__name__ + ", IsTargetAFriendlyConstructShip")
	if not pShip:
		return 0
	return GetConstructInstanceFor(pShip) and IsSameGroup(pPlayer, pShip)


def TargetChanged(pObject, pEvent):
	debug(__name__ + ", TargetChanged")
	pPlayer = MissionLib.GetPlayer()
	pTarget = pPlayer.GetTarget()
	pMenu = Libs.LibEngineering.GetBridgeMenu("Helm")

	if pMenu:
		pButton = Libs.LibEngineering.GetButton(sButtonName, pMenu)
		if not pTarget or not IsTargetAFriendlyConstructShip(pPlayer, App.ShipClass_Cast(pTarget)) and pButton:
			pMenu.DeleteChild(pButton)
		elif IsTargetAFriendlyConstructShip(pPlayer, App.ShipClass_Cast(pTarget)) and not pButton:
			pButton = Libs.LibEngineering.CreateMenuButton(sButtonName, "Helm", __name__ + ".ConstructControl")
	
	pObject.CallNextHandler(pEvent)
	

def init():
	debug(__name__ + ", init")
	global pPlayer
	
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	
	pPlayer = MissionLib.GetPlayer()
	pPlayer.AddPythonFuncHandlerForInstance(App.ET_TARGET_WAS_CHANGED, __name__+ ".TargetChanged")
	

def exit():
	debug(__name__ + ", exit")
	global pConstructWindow
	
	if not pPlayer:
		return
	
	pPlayer.RemoveHandlerForInstance(App.ET_TARGET_WAS_CHANGED, __name__+ ".TargetChanged")
	if pConstructWindow:
		pConstructWindow.KillChildren()
		pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
		pTacticalControlWindow.DeleteChild(pConstructWindow)
		pConstructWindow = None
	
	
def NewPlayerShip():
	debug(__name__ + ", NewPlayerShip")
	global pPlayer
	if pPlayer:
		pPlayer.RemoveHandlerForInstance(App.ET_TARGET_WAS_CHANGED, __name__+ ".TargetChanged")
	pPlayer = MissionLib.GetPlayer()
	if pPlayer:
		pPlayer.AddPythonFuncHandlerForInstance(App.ET_TARGET_WAS_CHANGED, __name__+ ".TargetChanged")


def Restart():
	debug(__name__ + ", Restart")
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	NewPlayerShip()


# handle mouse clicks in empty space
def PassMouse(pWindow, pEvent):
        debug(__name__ + ", PassMouse")
        pWindow.CallNextHandler(pEvent)

        if pEvent.EventHandled() == 0:
                pEvent.SetHandled()
