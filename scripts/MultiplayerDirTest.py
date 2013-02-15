import App
import Multiplayer
import Multiplayer.MultiplayerMenus
import MainMenu.mainmenu

badfilelist = (
"Agamemnon",
"Akira2",
"Akira",
"Alioth1",
"Alioth1_S",
"Alioth2",
"Alioth2_S",
"Alioth3",
"Alioth3_S",
"Alioth4",
"Alioth4_S",
"Alioth5",
"Alioth5_S",
"Alioth6",
"Alioth6_S",
"Alioth7",
"Alioth7_S",
"Alioth8",
"Alioth8_S",
"Alioth",
"Amagon",
"Ambassador",
"Asteroid1",
"Asteroid2",
"Asteroid3",
"Asteroidh1",
"Asteroidh2",
"Asteroidh3",
"Asteroid",
"Badlands1",
"Badlands1_S",
"Badlands",
"BiranuStation",
"BirdOfPrey",
"BombFreighter",
"BridgeHandlers",
"C2Valdore",
"CardFacility",
"CardFreighter",
"CardHybrid",
"CardOutpost",
"CardSpecificSetup",
"CardStarbase",
"CardStation",
"Cheyenne",
"CommArray",
"CommLight",
"Copy (2) of Copy of __init__",
"Copy (2) of Copy of MissionMenusShared",
"Copy (2) of Copy of MissionShared",
"Copy (2) of MultiplayerGame",
"Copy (2) of SpeciesToSystem",
"Copy (2) SFX Cortez is #1",
"Copy (3) of MultiplayerGame",
"Copy (3) of SpeciesToSystem",
"Copy (3) SFX Cortez is #1",
"Copy (4) of MultiplayerGame",
"Copy (4) of SpeciesToSystem",
"Copy (5) of MultiplayerGame",
"Copy (5) of SpeciesToSystem",
"Copy of Copy of Copy of __init__",
"Copy of Copy of Copy of MissionMenusShared",
"Copy of Copy of Copy of MissionShared",
"Copy of Copy of __init__",
"Copy of Copy of MissionMenusShared",
"Copy of Copy of MissionShared",
"Copy of Copy of Modifier",
"Copy of Copy of MultiplayerGame",
"Copy of Copy of MultiplayerMenus",
"Copy of Copy of SpeciesToShip",
"Copy of Copy of SpeciesToSystem",
"Copy of __init__",
"COPY_OF___INIT__",
"Copy of MissionMenusShared",
"COPY_OF_MISSIONMENUSSHARED",
"Copy of MissionShared",
"COPY_OF_MISSIONSHARED",
"Copy of Modifier",
"COPY_OF_MODIFIER",
"Copy of MultiplayerGame",
"COPY_OF_MULTIPLAYERGAME",
"Copy of MultiplayerMenus",
"COPY_OF_MULTIPLAYERMENUS",
"Copy of SpeciesToShip",
"COPY_OF_SPECIESTOSHIP",
"Copy of SpeciesToSystem",
"COPY_OF_SPECIESTOSYSTEM",
"Copy of SpeciesToTorp",
"COPY_OF_SPECIESTOTORP",
"CUBE",
"D-7",
"DamGalor",
"Decoy",
"DefenseNoTarget",
"Defense",
"DestroyAft",
"DestroyAftSeparate",
"DestroyFaceSide",
"DestroyForeClose",
"DestroyFore",
"DestroyFreelyClose",
"DestroyFreelyMaintain",
"DestroyFreely",
"DestroyFreelySeparate",
"DestroyFromSide",
"DisableAft",
"DisableAftSeparate",
"DisableFaceSide",
"DisableForeClose",
"DisableFore",
"DisableFreelyClose",
"DisableFreelyMaintain",
"DisableFreely",
"DisableFreelySeparate",
"DisableFromSide",
"DryDock",
"DynamicMusic",
"E2M0Warbird",
"EnterpriseB",
"Enterprise",
"EscapePod",
"Eximius",
"FedOutpost",
"FedStarbase",
"FlyForward",
"FoundationConfig",
"Freighter",
"GalaxyX",
"Galor",
"GenericTemplate",
"Geronimo",
"InterceptTarget",
"Intrepid",
"IonicTorpedo2",
"ISS",
"Itari1",
"Itari1_S",
"Itari2",
"Itari2_S",
"Itari3",
"Itari3_S",
"Itari4",
"Itari4_S",
"Itari5",
"Itari5_S",
"Itari6",
"Itari6_S",
"Itari7",
"Itari7_S",
"Itari8",
"Itari8_S",
"Itari",
"Keldon",
"KessokHeavy",
"KessokLight",
"KessokMine",
"KeyboardConfig",
"KlingonTorpedo",
"KlingTorpSound",
"LoadTacticalSounds",
"Maelstrom",
"Marauder",
"MatanKeldon",
"MatrixCube",
"MaTriXIIMenus",
"MaTriXIIName",
"MaTriXII",
"Mission1Menus",
"Mission1Name",
"Mission1",
"Mission2Menus",
"Mission2Name",
"Mission2",
"Mission3Menus",
"Mission3Name",
"Mission3",
"Mission5Menus",
"Mission5Name",
"Mission5",
"000-Fixes20030305-FoundationTriggers",
)


# Create a Info Box, Basics crom mainmenu.py
def CreateInfoBoxShutdown(String):
        pDialogWindow = CreateInfoBox(String)

        pDialogWindow.AddPythonFuncHandlerForInstance(ET_BOX_OKAY, __name__ + ".shutdown")


def CreateInfoBox(String):
    ET_BOX_OKAY = App.UtopiaModule_GetNextEventType()
    
    pTopWindow = App.TopWindow_GetTopWindow()
    pDialogWindow = App.ModalDialogWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MODAL_DIALOG))
    
    if (pDialogWindow):
        # Create a okay and cancel events
        pOkayEvent = App.TGIntEvent_Create()
        pOkayEvent.SetEventType(ET_BOX_OKAY)
        pOkayEvent.SetDestination(pDialogWindow)
        
        pTitle = App.TGString("Error Box")		
        pOkay = App.TGString("OK")
        pText = App.TGString(String)

        pDialogWindow.Run(pTitle, pText, pOkay, pOkayEvent, None, None)
        return pDialogWindow


def check():
        for file in badfilelist:
                dir_dirty = 1
                try:
                        __import__("Multiplayer." + file)
                except ImportError:
                        dir_dirty = 0
                if dir_dirty == 1:
                        return 1
        return 0


def ProcessMessageHandler(pObject, pEvent):
        pMessage = pEvent.GetMessage()
        
        if App.IsNull(pMessage):
                return
        
        # Get the data from the message
        # Open a buffer stream to read the data
        kStream = pMessage.GetBufferStream();
        cType = kStream.ReadChar();
        cType = ord(cType)
        kStream.Close()
        
        if cType == App.FILE_MESSAGE:
                pSeq = App.TGSequence_Create()
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AbortLoad", pObject, pEvent), 0.1)
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AbortLoadShowInfo"), 1.0)
                pSeq.Play()


def AbortLoad(pAction, pObject, pEvent):
        #pTopWindow = App.TopWindow_GetTopWindow()
        #pPane = pTopWindow.GetFirstChild()
        #pTopWindow.DeleteChild(pPane)
        
	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	if pNetwork:
		pNetwork.Disconnect()

        Multiplayer.MultiplayerMenus.HandleCancelConnect(pObject, pEvent)
        MainMenu.mainmenu.g_bMultiplayerMenusRebuiltAfterResChange = 0 # yes, thats dirty
        MainMenu.mainmenu.SwitchMiddlePane("Multiplayer")

        return 0

def AbortLoadShowInfo(pAction):
        myString = "The Host you were trying to connect to, doesn't use the same version as you!\n\nTo make sure your Game keeps clean, the connection has been terminated."
        CreateInfoBox(myString)
        
        return 0


def shutdown(pObject, pEvent):
        import sys
        sys.exit()


def checkMultplayerFiles():
        myString = "Your Multiplayer folder is dirty!\nI can't let you play with this one.\nPlease clean it up.\n\nGame shutdown!"
        if check() == 1:
                CreateInfoBoxShutdown(myString)

        # add listener
        pTopWindow = App.TopWindow_GetTopWindow()
        pWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, pTopWindow, __name__ + ".ProcessMessageHandler")
