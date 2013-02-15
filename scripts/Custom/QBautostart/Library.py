import App
import MissionLib
import Foundation
import Lib.LibEngineering
from Custom.QBautostart.Libs.Races import Races

ET_CLOSE = None
ET_CATEGORY = None
ET_TOPIC = None
sLibraryName = "Interstellar Library"
pTopicMenu = None
pBodyMenu = None
SelectedCategory = 0

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.1",
                "License": "BSD",
                "Description": "Interstellar Library for BC",
                "needBridge": 0
            }


def CreateBodyMenu(pLibraryWindow):
        global pBodyMenu
        WIDTH = 0.3
        HEIGHT = 0.6
        X_POS = 0.35
        Y_POS = 0.01
        
        pBodyMenu = App.STSubPane_Create(WIDTH, HEIGHT)
        pLibraryWindow.AddChild(pBodyMenu, X_POS, Y_POS)
        

def CreateTopicMenu(pLibraryWindow):
        global pTopicMenu
        WIDTH = 0.1
        HEIGHT = 0.6
        X_POS = 0.13
        Y_POS = 0.01
        
        pTopicMenu = App.STSubPane_Create(WIDTH, HEIGHT)
        pLibraryWindow.AddChild(pTopicMenu, X_POS, Y_POS)


def CreateCategoryMenu(pLibraryWindow):
        WIDTH = 0.1
        HEIGHT = 0.3
        X_POS = 0.01
        Y_POS = 0.01
        
        pCategoryMenu = App.STSubPane_Create(WIDTH, HEIGHT)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CATEGORY)
        pEvent.SetDestination(pLibraryWindow)
        pEvent.SetInt(1)
        pButton = App.STCharacterMenu_Create("Ships")
        pButton.SetActivationEvent(pEvent)
        pButton.SetNotOpenable()
        pCategoryMenu.AddChild(pButton)
        
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CATEGORY)
        pEvent.SetDestination(pLibraryWindow)
        pEvent.SetInt(2)
        pButton = App.STCharacterMenu_Create("Systems")
        pButton.SetActivationEvent(pEvent)
        pButton.SetNotOpenable()
        pCategoryMenu.AddChild(pButton)
        
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CATEGORY)
        pEvent.SetDestination(pLibraryWindow)
        pEvent.SetInt(3)
        pButton = App.STCharacterMenu_Create("Races")
        pButton.SetActivationEvent(pEvent)
        pButton.SetNotOpenable()
        pCategoryMenu.AddChild(pButton)

	pCategoryMenu.ResizeToContents()
        
        pLibraryWindow.AddChild(pCategoryMenu, X_POS, Y_POS)


def CreateShipsSelect(pTopicMenu):
        pLibraryWindow = GetLibraryWindow()
        FdtnShips = Foundation.shipList
        g_pShipsDatabase = App.g_kLocalizationManager.Load("data/TGL/Ships.tgl")
                
        for iIndex in range(len(FdtnShips)):
                if iIndex == 0:
                        continue
                Ship = FdtnShips[iIndex]
                ShipLongName = Ship.name
                if not g_pShipsDatabase.HasString(Ship.GetShipFile()):
                        continue
                
                # Setup the event for when this button is clicked
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_TOPIC)
                pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
                pEvent.SetDestination(pLibraryWindow)
                
                pButton = App.STRoundedButton_CreateW(g_pShipsDatabase.GetString(Ship.GetShipFile()), pEvent, 0.20, 0.02)
                pButton.SetActivationEvent(pEvent)
                pTopicMenu.AddChild(pButton)
                
                pEvent.SetSource(pButton)
        App.g_kLocalizationManager.Unload(g_pShipsDatabase)
        

def CreateSystemSelect(pTopicMenu):
        pLibraryWindow = GetLibraryWindow()
        FdtnSystems = Foundation.systemList
        pSystemsDatabase = App.g_kLocalizationManager.Load("data/TGL/Systems.tgl")

        for iIndex in range(len(FdtnSystems)):
                if iIndex == 0:
                        continue
                mySystem = FdtnSystems[iIndex]
                LongName = mySystem.name

                if not pSystemsDatabase.HasString(mySystem.name):
                        continue

                # Setup the event for when this button is clicked
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_TOPIC)
                pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
                pEvent.SetDestination(pLibraryWindow)
                
                pButton = App.STRoundedButton_CreateW(pSystemsDatabase.GetString(mySystem.name), pEvent, 0.20, 0.02)
                pButton.SetActivationEvent(pEvent)
                pTopicMenu.AddChild(pButton)
                
                pEvent.SetSource(pButton)
                
        App.g_kLocalizationManager.Unload(pSystemsDatabase)


def CreateRacesSelect(pTopicMenu):
        pLibraryWindow = GetLibraryWindow()
        pRaceDatabase = App.g_kLocalizationManager.Load("data/TGL/Races.tgl")
        
        i = 0
        for race in Races.keys():
                if race != "GodShips":
                        if pRaceDatabase and pRaceDatabase.HasString(race):
                                RaceTGS = pRaceDatabase.GetString(race)
                        else:
                                RaceTGS = App.TGString(race)
                        
                        # Setup the event for when this button is clicked
                        pEvent = App.TGIntEvent_Create()
                        pEvent.SetEventType(ET_TOPIC)
                        pEvent.SetInt(i)		# store the index so we know which button was clicked.
                        pEvent.SetDestination(pLibraryWindow)
                
                        pButton = App.STRoundedButton_CreateW(RaceTGS, pEvent, 0.20, 0.02)
                        pButton.SetActivationEvent(pEvent)
                        pTopicMenu.AddChild(pButton)
                
                        pEvent.SetSource(pButton)
                
                i = i + 1

        # Other ships
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_TOPIC)
        pEvent.SetInt(99)
        pEvent.SetDestination(pLibraryWindow)
        pButton = App.STRoundedButton_CreateW(App.TGString("Minor Races"), pEvent, 0.20, 0.02)
        pButton.SetActivationEvent(pEvent)
        pTopicMenu.AddChild(pButton)
        pEvent.SetSource(pButton)
        
        App.g_kLocalizationManager.Unload(pRaceDatabase)
                


def SelectCategory(pObject, pEvent):
        global SelectedCategory
        SelectedCategory = pEvent.GetInt()
        if SelectedCategory and pTopicMenu:
                pTopicMenu.KillChildren()
                pBodyMenu.KillChildren()
                if SelectedCategory == 1:
                        CreateShipsSelect(pTopicMenu)
                if SelectedCategory == 2:
                        CreateSystemSelect(pTopicMenu)
                if SelectedCategory == 3:
                        CreateRacesSelect(pTopicMenu)
                pTopicMenu.ResizeToContents()
        

def SelectTopic(pObject, pEvent):
        SHIP_IMAGE_WIDTH			= 0.2515625
        SHIP_IMAGE_HEIGHT			= 0.2458333

        SelectedTopic = pEvent.GetInt()
        if SelectedTopic:
                pLibraryWindow = GetLibraryWindow()
                pLibraryWindow.ScrollToTop()
                pBodyMenu.KillChildren()
                if SelectedCategory == 1:
                        FdtnShips = Foundation.shipList
                        myship = FdtnShips[SelectedTopic]
                        g_pShipsDatabase = App.g_kLocalizationManager.Load("data/TGL/Ships.tgl")
                        pShipsHeader = App.TGParagraph_Create("", 0.1, None, "", 0.1, App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                        pShipsHeader.SetStringW(g_pShipsDatabase.GetString(myship.GetShipFile()))
                        pBodyMenu.AddChild(pShipsHeader)

                        pIcon = App.TGIcon_Create("ShipIcons", App.SPECIES_UNKNOWN)
                        pIcon.Resize(SHIP_IMAGE_WIDTH, SHIP_IMAGE_HEIGHT)
                        iIconNumber = myship.GetIconNum()
	                pIcon.SetVisible()
	                pIcon.SetIconNum(iIconNumber)
	                pIcon.SizeToArtwork()
                        pBodyMenu.AddChild(pIcon)
                        
                        pShipsText = App.TGParagraph_Create("", 0.3, None, "", 1.0, App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                        pShipsText.SetStringW(g_pShipsDatabase.GetString(myship.GetShipFile() + " Description"))
                        pBodyMenu.AddChild(pShipsText)
                        App.g_kLocalizationManager.Unload(g_pShipsDatabase)
                elif SelectedCategory == 2:
                        FdtnSystems = Foundation.systemList
                        mySystem = FdtnSystems[SelectedTopic]
                        pSystemsDatabase = App.g_kLocalizationManager.Load("data/TGL/Systems.tgl")
                        pSystemsHeader = App.TGParagraph_Create("", 0.1, None, "", 0.1, App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                        pSystemsHeader.SetStringW(pSystemsDatabase.GetString(mySystem.name))
                        pBodyMenu.AddChild(pSystemsHeader)

		        pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
		        pcLCARS = pGraphicsMode.GetLcarsString()
                        pIcon = App.TGIcon_Create(pcLCARS, 800)
                        pIcon.Resize(SHIP_IMAGE_WIDTH, SHIP_IMAGE_HEIGHT)
	                pIcon.SetVisible()
	                pIcon.SizeToArtwork()
                        pBodyMenu.AddChild(pIcon)
                        
                        pSystemsText = App.TGParagraph_Create("", 0.3, None, "", 1.0, App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                        pSystemsText.SetStringW(pSystemsDatabase.GetString(mySystem.name + " Description"))
                        pBodyMenu.AddChild(pSystemsText)

                        App.g_kLocalizationManager.Unload(pSystemsDatabase)
                elif SelectedCategory == 3:
                        pRaceDatabase = App.g_kLocalizationManager.Load("data/TGL/Races.tgl")
        
                        i = 0
                        iIconNumber = 0
                        myRace = None
                        for race in Races.keys():
                                print i, race
                                if race != "GodShips":
                                        if SelectedTopic == i:
                                                myRace = race
                                                iIconNumber = i
                                                break
                                        elif SelectedTopic == 99:
                                                myRace = "Other"
                                                iIconNumber = 99
                                                break
                                i = i + 1

                        pRacesHeader = App.TGParagraph_Create("", 0.1, None, "", 0.1, App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                        if pRaceDatabase and pRaceDatabase.HasString(myRace):
                                pRacesHeader.SetStringW(pRaceDatabase.GetString(myRace))
                        else:
                                pRacesHeader.SetStringW(App.TGString(myRace))
                        pBodyMenu.AddChild(pRacesHeader)

                        pIcon = App.TGIcon_Create("RacesIcons", App.SPECIES_UNKNOWN)
                        pIcon.Resize(SHIP_IMAGE_WIDTH, SHIP_IMAGE_HEIGHT)
	                pIcon.SetVisible()
	                pIcon.SetIconNum(iIconNumber)
	                pIcon.SizeToArtwork()
                        pBodyMenu.AddChild(pIcon)

                        if pRaceDatabase and pRaceDatabase.HasString(myRace + " Description"):
                                pRacesText = App.TGParagraph_Create("", 0.3, None, "", 1.0, App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                                pRacesText.SetStringW(pRaceDatabase.GetString(myRace + " Description"))
                                pBodyMenu.AddChild(pRacesText)
                
        
                        App.g_kLocalizationManager.Unload(pRaceDatabase)


# ceate the window interior here!
def CreateWindowInterior(pLibraryWindow):
        CreateCategoryMenu(pLibraryWindow)
        CreateTopicMenu(pLibraryWindow)
        CreateBodyMenu(pLibraryWindow)
        
        pMission = MissionLib.GetMission()
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetDestination(pMission)
        pEvent.SetInt(0)
        pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.1, 0.03)
        pButton.SetNormalColor(App.g_kMainMenuButtonColor)
        pLibraryWindow.AddChild(pButton, 0.01, 0.5, 0)
        
        pLibraryWindow.InteriorChangedSize()
        pLibraryWindow.Layout()
        

def GetLibraryWindow():
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()

        # cycle all
        curChild = pTacticalControlWindow.GetFirstChild()
        while curChild:
                curWindow = App.STStylizedWindow_Cast(curChild)
                if curWindow:
                        kString = curWindow.GetName()
                        if (kString.GetCString() == sLibraryName):
                                return curWindow
                curChild = pTacticalControlWindow.GetNextChild(curChild)


# handle mouse clicks in empty space
def PassMouse(pWindow, pEvent):
        pWindow.CallNextHandler(pEvent)

        if pEvent.EventHandled() == 0:
                pEvent.SetHandled()


def WindowOpenClose(pObject, pEvent):
        pLibraryWindow = GetLibraryWindow()
        if not pLibraryWindow:
                pLibraryWindow = CreateLibraryWindow(None, None)

        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        if pLibraryWindow.IsVisible():
                pTacticalControlWindow.MoveToBack(pLibraryWindow)
                pLibraryWindow.SetNotVisible()
        else:
                pLibraryWindow.SetVisible()
                pTacticalControlWindow.MoveToFront(pLibraryWindow)
                # Not so agressiv to the front - only give us problems!
                pTacticalControlWindow.MoveTowardsBack(pLibraryWindow)


def WindowClose(pObject, pEvent):
        pLibraryWindow = GetLibraryWindow()
        if pLibraryWindow:
                pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
                if pLibraryWindow.IsVisible():
                        pTacticalControlWindow.MoveToBack(pLibraryWindow)
                        pLibraryWindow.SetNotVisible()
        
        pObject.CallNextHandler(pEvent)


def CreateLibraryWindow(pObject, pEvent):
        pLibraryWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString(sLibraryName), 0.0, 0.0, None, 1, 0.7, 0.6, App.g_kMainMenuBorderMainColor)
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pTacticalControlWindow.AddChild(pLibraryWindow, 0.15, 0.1)

        pLibraryWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".PassMouse")
        pLibraryWindow.SetNotVisible()
        
        pLibraryWindow.AddPythonFuncHandlerForInstance(ET_CATEGORY, __name__ + ".SelectCategory")
        pLibraryWindow.AddPythonFuncHandlerForInstance(ET_TOPIC, __name__ + ".SelectTopic")
        
        CreateWindowInterior(pLibraryWindow)
        
        return pLibraryWindow


def init():
        global ET_CLOSE, ET_CATEGORY, ET_TOPIC
        
        pMission = MissionLib.GetMission()
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pScience = App.CharacterClass_GetObject(pBridge, "Science")
        ET_CLOSE = Lib.LibEngineering.GetEngineeringNextEventType()
        ET_CATEGORY = Lib.LibEngineering.GetEngineeringNextEventType()
        ET_TOPIC = Lib.LibEngineering.GetEngineeringNextEventType()
        
        Lib.LibEngineering.CreateMenuButton(sLibraryName, "Science", __name__ + ".WindowOpenClose")
        #MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".CreateLibraryWindow", App.g_kUtopiaModule.GetGameTime() + 2.0, 0, 0)
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".WindowOpenClose")
        if g_pScience:
                g_pScience.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".WindowClose")
