from bcdebug import debug
###############################################################
###############################################################
##  	 DS9FXmain.py                                        ##
##                                                           ##
##       DS9FX Version Signature: 3.0                        ##
##                                                           ##
##       This is the main file of DS9FX, it simply           ##
##       does most of the work here. And it                  ##
##       heavily relies on Timer usage.                      ##
##                                                           ##
##       by USS Sovereign                                    ##
##                                                           ##
##       All Rights Reserved.                                ##
##                                                           ##
##       PERMISSIONS: Do not modify without                  ##
##       permission. Do not use the code without             ##
##       permission. It's polite to ask!                     ##
###############################################################
###############################################################


# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pRandomEnemyFleetAttacks = pModule.RandomEnemyFleetAttacks
pDomIS = pModule.DomIS
pDS9Music = pModule.DS9Music
pWormholeMusic = pModule.WormholeMusic
pGammaMusic = pModule.GammaMusic
pFederationSide = pModule.FederationSide
pDominionTimeSpan = pModule.DominionTimeSpan
pDominionSide = pModule.DominionSide
pDS9Selection = pModule.DS9Selection



# Imports
import App
import MissionLib
import DS9FXLib.DS9FXMenuLib
import Bridge.BridgeUtils
import loadspacehelper
import Actions.ShipScriptActions
import Bridge.BridgeMenus
import Custom.DS9FX.DS9FXShips


# Events
ET_CAMPAIGN = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION = App.UtopiaModule_GetNextEventType()
ET_CLOSE = App.UtopiaModule_GetNextEventType()
ET_WINDOW_CLOSE = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_1 = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_2 = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_3 = App.UtopiaModule_GetNextEventType()
ET_BACK = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_4 = App.UtopiaModule_GetNextEventType()
ET_BORDER_SKIRMISH_5 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_1 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_1 = App.UtopiaModule_GetNextEventType()
ET_WINDOW_CLOSE_2 = App.UtopiaModule_GetNextEventType()
ET_WINDOW_CLOSE_3 = App.UtopiaModule_GetNextEventType()
ET_UNAVAILABLE = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_2 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_3 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_4 = App.UtopiaModule_GetNextEventType()
ET_HISTORIC_MISSION_5 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_2 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_3 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_4 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_5 = App.UtopiaModule_GetNextEventType()
ET_MINI_MISSION_6 = App.UtopiaModule_GetNextEventType()


# Button Variables
mHelm = None
bEnter = None
bExitToGamma = None
bExitToDS9 = None
bDockToDS9 = None
bHail = None
bCloseChannel = None

# Wormhole Scale
Scale = 0
ExitingScale = 4

# Scale Timer
ScaleTimer = None
ExitingScaleTimer = None

# Scale Distance Timer
ScaleDistanceTimer = None

# Wormhole Distance Check
DistanceCheckCondition = None

# Dominion Antiproton Scan values
Firepoint = None

# Attach Object Timer
AttachTimer = None

# Inside Wormhole Timer
InsideWormholeTimer = None

# Random attack timer
RandomAttackTimer = None

if pDominionTimeSpan == 1:
    
        # Enemy fleet random values
        RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 240
        
        

elif pDominionTimeSpan == 2:
        # Enemy fleet random values
        RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 360
        

else:
        # Enemy fleet random values
        RandomEnemyFleet = App.g_kSystemWrapper.GetRandomNumber(120) + 120


# Handler overflow prevention, important new factor in DS9FX
iHandlerOverflow = 0
DS9Timer = 30
ScaleWormholePrevention = 0


# Mission Selection Values
MissionWindow = None
MissionWindow2 = None
MissionWindow3 = None

# Pane ID
pPaneID = App.NULL_ID



# Similar to qbautostart we use init function which is called directly from the autoload file at mission start
def init():
        debug(__name__ + ", init")
        global mHelm, bEnter, bExitToGamma, bExitToDS9, bDockToDS9, SecHandler, bHail, bCloseChannel, ET_WINDOW_CLOSE, ET_BORDER_SKIRMISH_1, ET_BORDER_SKIRMISH_2, ET_BORDER_SKIRMISH_3, ET_BORDER_SKIRMISH_4, ET_BORDER_SKIRMISH_5, ET_BACK, pPerson, ET_HISTORIC_MISSION_1, ET_MINI_MISSION_1, ET_MINI_MISSION_2, ET_MINI_MISSION_3, ET_MINI_MISSION_4, ET_MINI_MISSION_5, ET_MINI_MISSION_6, ET_WINDOW_CLOSE_2, ET_WINDOW_CLOSE_3, ET_UNAVAILABLE, ET_HISTORIC_MISSION_2, ET_HISTORIC_MISSION_3, ET_HISTORIC_MISSION_4, ET_HISTORIC_MISSION_5

	pMissionDatabase = MissionLib.GetMission().SetDatabase("data/TGL/QuickBattle/QuickBattle.tgl")
        pSaffiQB = GetMenuButton("Commander", pMissionDatabase.GetString("End Simulation").GetCString())
        
        if not pSaffiQB:
            print "DS9FX: DS9FX is only compatible with QuickBattle mode. If you are running QB Mode, please consult BCS: TNG"
            return

        # Make the options global
        global pRandomEnemyFleetAttacks, pDomIS, pDS9Music, pWormholeMusic, pGammaMusic, pFederationSide, pDominionTimeSpan, pDominionSide, pDS9Selection

        # Reload UMM Customization options
        reload(pModule)
        pRandomEnemyFleetAttacks = pModule.RandomEnemyFleetAttacks
        pDomIS = pModule.DomIS
        pDS9Music = pModule.DS9Music
        pWormholeMusic = pModule.WormholeMusic
        pGammaMusic = pModule.GammaMusic
        pFederationSide = pModule.FederationSide
        pDominionTimeSpan = pModule.DominionTimeSpan
        pDominionSide = pModule.DominionSide
        pDS9Selection = pModule.DS9Selection
        
        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	# Set a mission database
        pMissionDatabase = pMission.SetDatabase("data/TGL/DS9FXMissionMenu.tgl")

        # Create character set
	pKiraSet = MissionLib.SetupBridgeSet("KiraSet", "data/Models/Sets/StarbaseControl/starbasecontrolRM.nif", -40, 65, -1.55)
	pKira = App.CharacterClass_GetObject(pKiraSet, "Kira")
	if not pKira:
            pKira = MissionLib.SetupCharacter("Bridge.Characters.DS9FXMajorKira", "KiraSet", 0, 0, 5)

        # Create buttons
	pKiraMenu = Bridge.BridgeMenus.CreateBlankCharacterMenu(pMissionDatabase.GetString("MainMenu"), 0.28, 0.4, 0.7, 0.1)
	pKira.SetMenu(pKiraMenu)

	pKira.AddPythonFuncHandlerForInstance(ET_CAMPAIGN, __name__ + ".ChooseCampaign")
	pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("BorderSkirmish"), ET_CAMPAIGN, 0, pKira))

	pKira.AddPythonFuncHandlerForInstance(ET_MINI_MISSION, __name__ + ".ChooseMiniMission")
	pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("MiniMissions"), ET_MINI_MISSION, 0, pKira))

	pKira.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION, __name__ + ".ChooseHistoric")
	pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("HistoricMissions"), ET_HISTORIC_MISSION, 0, pKira))

	pKira.AddPythonFuncHandlerForInstance(ET_CLOSE, __name__ + ".CloseChannel")
	pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("Close"), ET_CLOSE, 0, pKira))


        # First start the QBR double menu fix
        RemoveDS9FXMenu()

        # Buttons
        mHelm = DS9FXLib.DS9FXMenuLib.CreateMenu("DS9FX", "Helm")
        bEnter = DS9FXLib.DS9FXMenuLib.CreateButton("Enter Wormhole", "Helm", __name__ + ".EnterSeq", "DS9FX")
        bExitToGamma = DS9FXLib.DS9FXMenuLib.CreateButton("Exit To Gamma", "Helm", __name__ + ".ExitToGammaSeq", "DS9FX")
        bExitToDS9 = DS9FXLib.DS9FXMenuLib.CreateButton("Exit To DS9", "Helm", __name__ + ".ExitToDS9Seq", "DS9FX")
        

        # If you pick federation as an enemy then you cannot dock to DS9 station
        if pFederationSide == 1:
            
                    # Docking function won't exist in a Kobayashi Maru Installation
                    try:
                            pKobMaruModule = __import__("gameinfo")

                            pKobMaru = pKobMaruModule.GAME_TYPE

                            if pKobMaru == "KM":

                                if pDominionSide == 1:

                                    print "DS9FX: You have set Dominion to be friendly. For mission purposes they have to be set as enemy. Hailing function won't initialize!" 

                                    print "DS9FX: Kobayashi Maru is Installed. Deleting DS9FX Docking Function!"

                                else:
                                    
                                    if pDS9Selection == 1:

                                        bCloseChannel = DS9FXLib.DS9FXMenuLib.CreateButton("Close Channel", "Helm", __name__ + ".CloseChannel", "DS9FX")

                                        bHail = DS9FXLib.DS9FXMenuLib.CreateButton("Hail DS9", "Helm", __name__ + ".HailDS9", "DS9FX")

                                    else:

                                        print "DS9FX: DS9 has not been enabled, hailing function won't initialize"
                                        
                                    print "DS9FX: Kobayashi Maru is Installed. Deleting DS9FX Docking Function!"


                            # Psycho might want to kill me for missing this. Sry I forgot that you had to update gameinfo.py :(
                            elif pKobMaru == "KM PIMPED":

                                if pDominionSide == 1:

                                    print "DS9FX: You have set Dominion to be friendly. For mission purposes they have to be set as enemy. Hailing function won't initialize!" 

                                    print "DS9FX: Kobayashi Maru Pimped is Installed. Deleting DS9FX Docking Function!"

                                else:
                                    
                                    if pDS9Selection == 1:

                                        bCloseChannel = DS9FXLib.DS9FXMenuLib.CreateButton("Close Channel", "Helm", __name__ + ".CloseChannel", "DS9FX")

                                        bHail = DS9FXLib.DS9FXMenuLib.CreateButton("Hail DS9", "Helm", __name__ + ".HailDS9", "DS9FX")

                                    else:

                                        print "DS9FX: DS9 has not been enabled, hailing function won't initialize"
                                    
                                    print "DS9FX: Kobayashi Maru Pimped is Installed. Deleting DS9FX Docking Function!"

                            else:

                                print "DS9FX: You don't have a valid Kobayashi Maru installation. Some DS9FX Functions will not initialize!"


                    except:
                
                            if pDominionSide == 1:
                                
                                print "DS9FX: You have set Dominion to be friendly. For mission purposes they have to be set as enemy. Hailing function won't initialize!" 
        
                            else:
                                
                                if pDS9Selection == 1:

                                    bDockToDS9 = DS9FXLib.DS9FXMenuLib.CreateButton("Dock To DS9", "Helm", __name__ + ".DockToDS9", "DS9FX")

                                    bCloseChannel = DS9FXLib.DS9FXMenuLib.CreateButton("Close Channel", "Helm", __name__ + ".CloseChannel", "DS9FX")

                                    bHail = DS9FXLib.DS9FXMenuLib.CreateButton("Hail DS9", "Helm", __name__ + ".HailDS9", "DS9FX")

                                else:

                                    print "DS9FX: DS9 has not been enabled, hailing function won't initialize"
                            
                            print "DS9FX: No Kobayashi Maru Installed. Installing DS9FX Docking Function!"

        else:
                            print "DS9FX: Federation is an enemy, Docking and Hailing functions won't initialize!"
                            
                            
	# Every option is disabled and most functions are reenabled when entering the correct system
	bExitToGamma.SetDisabled()
	bExitToDS9.SetDisabled()
	bEnter.SetDisabled()

	if bHail == None:
            pass

        else:
            bHail.SetDisabled()

        if bCloseChannel == None:
            pass

        else:
            bCloseChannel.SetDisabled()

	# Dock button doesn't have to exist
	if bDockToDS9 == None:
            pass

        else:
            bDockToDS9.SetDisabled()


        SecHandler = 30

        # Mission Selection Menu details ;)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow2", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow3", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)

    
        pPersonSet = App.g_kSetManager.GetSet("KiraSet")
	pPerson = App.CharacterClass_GetObject(pPersonSet, "Kira")

        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE, pMission, __name__ + ".Window")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE_2, pMission, __name__ + ".Window2")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE_3, pMission, __name__ + ".Window3")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_1, __name__ + ".BorderSkirmishMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_2, __name__ + ".BorderSkirmishMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_3, __name__ + ".BorderSkirmishMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_4, __name__ + ".BorderSkirmishMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_5, __name__ + ".BorderSkirmishMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_1, __name__ + ".DS9FXHistoricMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_2, __name__ + ".DS9FXHistoricMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_3, __name__ + ".DS9FXHistoricMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_4, __name__ + ".DS9FXHistoricMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_5, __name__ + ".DS9FXHistoricMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_1, __name__ + ".DS9FXMiniMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_2, __name__ + ".DS9FXMiniMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_3, __name__ + ".DS9FXMiniMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_4, __name__ + ".DS9FXMiniMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_5, __name__ + ".DS9FXMiniMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_6, __name__ + ".DS9FXMiniMission6")
        pPerson.AddPythonFuncHandlerForInstance(ET_BACK, __name__ + ".BackToHailMenu")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow2")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow3")
        pPerson.AddPythonFuncHandlerForInstance(ET_UNAVAILABLE, __name__ + ".MissionUnavailable")



# A restart trigger which is simply called when a player ship is recreated and now modified to fix BP issues.
# In other words heavily modified
def RestartTrigger():
        debug(__name__ + ", RestartTrigger")
        global iHandlerOverflow

	pMissionDatabase = MissionLib.GetMission().SetDatabase("data/TGL/QuickBattle/QuickBattle.tgl")
        pSaffiQB = GetMenuButton("Commander", pMissionDatabase.GetString("End Simulation").GetCString())
        
        if not pSaffiQB:
            return

        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	# Preload ships now for every mission, this line was simply moved from init()
        from Custom.DS9FX.DS9FXObjects import DS9FXPreLoadedShips

        DS9FXPreLoadedShips.PreLoadEverything(pMission)

        # Handler overflow protection turned on
        iHandlerOverflow = 1

        # Delete leftover timers
	DeleteAllDS9FXTimers()

	# Reenable warp button incase you pressed end combat in gamma quadrant map
        RestoreWarpButton()
               
	# Set a mission database
        pMissionDatabase = pMission.SetDatabase("data/TGL/DS9FXMissionMenu.tgl")

        # Create character set
	pKiraSet = MissionLib.SetupBridgeSet("KiraSet", "data/Models/Sets/StarbaseControl/starbasecontrolRM.nif", -40, 65, -1.55)
	pKira = App.CharacterClass_GetObject(pKiraSet, "Kira")
	if not pKira:
            pKira = MissionLib.SetupCharacter("Bridge.Characters.DS9FXMajorKira", "KiraSet", 0, 0, 5)

        # Create buttons
	pKiraMenu = Bridge.BridgeMenus.CreateBlankCharacterMenu(pMissionDatabase.GetString("MainMenu"), 0.28, 0.4, 0.7, 0.1)
	pKira.SetMenu(pKiraMenu)

	pKira.AddPythonFuncHandlerForInstance(ET_CAMPAIGN, __name__ + ".ChooseCampaign")
	pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("BorderSkirmish"), ET_CAMPAIGN, 0, pKira))

	pKira.AddPythonFuncHandlerForInstance(ET_MINI_MISSION, __name__ + ".ChooseMiniMission")
	pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("MiniMissions"), ET_MINI_MISSION, 0, pKira))

	pKira.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION, __name__ + ".ChooseHistoric")
	pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("HistoricMissions"), ET_HISTORIC_MISSION, 0, pKira))

	pKira.AddPythonFuncHandlerForInstance(ET_CLOSE, __name__ + ".CloseChannel")
	pKiraMenu.AddChild(CreateBridgeMenuButton(pMissionDatabase.GetString("Close"), ET_CLOSE, 0, pKira))
	
	

        # Delay the event, for 0.1 seconds. In other words we're now detecting via timer if the game has loaded then we decide to load the models in
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".RestartTriggerActivated", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)


# Restart trigger activated
def RestartTriggerActivated(pObject, Event):
        debug(__name__ + ", RestartTriggerActivated")
        global ET_WINDOW_CLOSE, ET_BORDER_SKIRMISH_1, ET_BORDER_SKIRMISH_2 , ET_BORDER_SKIRMISH_3, ET_BORDER_SKIRMISH_4, ET_BORDER_SKIRMISH_5, ET_BACK, pPerson, ET_HISTORIC_MISSION_1, ET_MINI_MISSION_1, ET_MINI_MISSION_2, ET_MINI_MISSION_3, ET_MINI_MISSION_4, ET_MINI_MISSION_5, ET_MINI_MISSION_6, ET_WINDOW_CLOSE_2, ET_WINDOW_CLOSE_3, ET_UNAVAILABLE, ET_HISTORIC_MISSION_2, ET_HISTORIC_MISSION_3, ET_HISTORIC_MISSION_4, ET_HISTORIC_MISSION_5
        
    
        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        # Stop overriding music, a bug I noticed recently
        import DynamicMusic
        DynamicMusic.StopOverridingMusic()
    
	# First thing is first, try to remove the listener, if for some reason it was still active
	try:
            # Not activated anymore over here but it might be still active so deactivate it and allow use of manual activation
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".ActivateDS9FXPlacement")
        except:
            pass

        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".MusicListener")
        except:
            pass


        # We'll do a little trick ;) simulate manually End Combat Event, QB only but QBR anyway recreates all ships that were created if you don't specify it what to do
	pMissionDatabase = MissionLib.GetMission().SetDatabase("data/TGL/QuickBattle/QuickBattle.tgl")
        pSaffiQB = GetMenuButton("Commander", pMissionDatabase.GetString("End Simulation").GetCString())
        
        if pSaffiQB:
            if pSaffiQB.IsEnabled():
                # With BP we've lost the ability to load in the background models that we need in DS9FX
                ManuallyActivateDS9FXPlacement(None, None)
                # Basically a hack. We need to compromise cause of MovePlayer function
                MoveShipsFromObsoleteSets()
                TerminateObsoleteSets()
                # I'll need 2 sets of prints
                print "DS9FX: QB Mission Mode Enabled. DS9 Set is reachable by Warp!"

            else:
                # print "DS9FX: QB button is disabled, I won't load in the models"
                ManualShipCleanup(None, None)
                # A hack
                DeleteAllDS9FXTimers()
                # Rename set names
                RenameSets(None, None)
                MovePlayer(None, None)
                # Now you simply cannot visit DS9 if you haven't started a mission
                RemoveDeepSpace9Menu()
                # I really hate to do this... But next time when I ask for a console report I'll have a proof that the person did a really stupid thing!
                print "DS9FX: You're not currently running a QB Mission. DS9 Set cannot be reached by Warp!"


        # Mission Selection Menu details ;)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow2", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow3", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)

    
        pPersonSet = App.g_kSetManager.GetSet("KiraSet")
	pPerson = App.CharacterClass_GetObject(pPersonSet, "Kira")

        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE, pMission, __name__ + ".Window")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE_2, pMission, __name__ + ".Window2")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_WINDOW_CLOSE_3, pMission, __name__ + ".Window3")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_1, __name__ + ".BorderSkirmishMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_2, __name__ + ".BorderSkirmishMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_3, __name__ + ".BorderSkirmishMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_4, __name__ + ".BorderSkirmishMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_BORDER_SKIRMISH_5, __name__ + ".BorderSkirmishMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_1, __name__ + ".DS9FXHistoricMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_2, __name__ + ".DS9FXHistoricMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_3, __name__ + ".DS9FXHistoricMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_4, __name__ + ".DS9FXHistoricMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_HISTORIC_MISSION_5, __name__ + ".DS9FXHistoricMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_1, __name__ + ".DS9FXMiniMission1")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_2, __name__ + ".DS9FXMiniMission2")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_3, __name__ + ".DS9FXMiniMission3")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_4, __name__ + ".DS9FXMiniMission4")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_5, __name__ + ".DS9FXMiniMission5")
        pPerson.AddPythonFuncHandlerForInstance(ET_MINI_MISSION_6, __name__ + ".DS9FXMiniMission6")
        pPerson.AddPythonFuncHandlerForInstance(ET_BACK, __name__ + ".BackToHailMenu")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow2")
        pPerson.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".CloseWindow3")
        pPerson.AddPythonFuncHandlerForInstance(ET_UNAVAILABLE, __name__ + ".MissionUnavailable")

        
	# An additional listener which is used for DynamicMusic
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".MusicListener")


        # Restore handler overflow back to its original value
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".RestoreHandlerOverflow", App.g_kUtopiaModule.GetGameTime() + 3, 0, 0)


            

# Restoring handler overflow protection
def RestoreHandlerOverflow(pObject, pEvent):
        debug(__name__ + ", RestoreHandlerOverflow")
        global iHandlerOverflow
    

        # Restoring handler overflow to 0. Or in other words shutting it down
        iHandlerOverflow = None
        iHandlerOverflow = 0


        # print "DS9FX: iHandlerOverflow deactivated"



# A restart trigger which is simply called when we enter DS9, Gamma Quadrant or Bajoran Wormhole set, same as RestartTrigger only without warp button being reenabled
def EnterSetTrigger():
        debug(__name__ + ", EnterSetTrigger")
        global iHandlerOverflow

	pMissionDatabase = MissionLib.GetMission().SetDatabase("data/TGL/QuickBattle/QuickBattle.tgl")
        pSaffiQB = GetMenuButton("Commander", pMissionDatabase.GetString("End Simulation").GetCString())
        
        if not pSaffiQB:
            return

        # Handler is protecting overflows, gives a positive effect on the mod
        if iHandlerOverflow == 1:
            # print "DS9FX: iHandlerOverflow blocking..."
            return
        

        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        # Delete leftover timers
	DeleteAllDS9FXTimers()


	# First thing is first, try to remove the listener, if for some reason it was still active
	try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".ActivateDS9FXPlacement")
        except:
            pass

        try:
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".MusicListener")
        except:
            pass
        
        # Listener that additionaly creates an object, as you can see we add them when entering the correct set
	# we're not adding them in the selected system. It's the same, only executed differently!
	# Plus we need to execute it this way cause of UMM customization options
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".ActivateDS9FXPlacement")

	# An additional listener which is used for DynamicMusic
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".MusicListener")




# Sequence which is called when activating Enter Wormhole
def EnterSeq(pObject, pEvent):
        debug(__name__ + ", EnterSeq")
        global ScaleDistanceTimer

        # Dialog overflow prevention
        iDialogOverflow = None
        iDialogOverflow = 0

        # Get the player
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0                

	# Okay see if we are in DS9 set, if so transfer us to Wormhole set
	# If only this is as easy as it sounds
        pSet = pPlayer.GetContainingSet()

        # A bug fix insert game would crash if you would go in the wormhole using a system specific ship
        PlayerName = pPlayer.GetName()

        if PlayerName == "Bajoran Wormhole":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "USS Excalibur":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "Deep_Space_9":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "USS Defiant":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "USS Oregon":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "USS_Lakota":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "Bugship 1":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "Bugship 2":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "Bugship 3":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return

        elif PlayerName == "Comet Alpha":
            print "DS9FX: System specific object, cannot enter wormhole. Game will crash!"
            return


        # Do a Engine status check. If the state is below 65 percent, don't allow the user to go in the Wormhole
        # This checks individual engines, not total stats. So if a single engine is below 65% you won't be able to enter the Wormhole
        # Useful I think. You have a station nearby so Dock with it for repairs!
        pImpulse = pPlayer.GetImpulseEngineSubsystem()

        if not pImpulse:
            return

        for iCounter in range(pImpulse.GetNumChildSubsystems()):
            pChild = pImpulse.GetChildSubsystem(iCounter)
            pImpulseStats = pChild.GetConditionPercentage()

            if pImpulseStats <= 0.65:
                if iDialogOverflow == 0:
                    ImpulsePrompt()
                iDialogOverflow = None
                iDialogOverflow = 1
                print "DS9FX: Repair impulse engines in order to enter the wormhole!"
                return

                       	 
        if (pSet.GetName() == "DeepSpace91"):

                     # Grab the set's name directly from the set file
                     DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
                     DS9Set = DS9.GetSet()

                     # Grab the wormhole model
                     pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set)
                     pDS9FXWormholeID = pDS9FXWormhole.GetObjID()

                     # Check if we are in range 
                     if DistanceCheck(pDS9FXWormhole) > 300:
                                        FelixWarnPrompt()
                                        print "DS9FX: To far out to enter Wormhole!"
                                        return

                     # Enter wormhole range has been changed, range should be around 10 km now for a reason.
                     elif DistanceCheck(pDS9FXWormhole) < 50:
                                        FelixWarnPrompt()
                                        print "DS9FX: To close to enter Wormhole!"
                                        return                     

                     # Bugfix insert repair the wormhole fully incase we fired on it earlier
                     Actions.ShipScriptActions.RepairShipFully(None, pDS9FXWormholeID)

                     # Bugfix insert
                     TranslatePlayer()

                     # All systems go you can go in, then delete RandomAttackTimer
                     DeleteRandomAttackTimer(None, None)
                     
                     # Disable engineer's menu. I know what I'm doing, small bug poped up
                     DisableEngineerMenu()

                     # Assign an AI to the player (DS9FXEnterWormholeAI)
                     import Custom.DS9FX.DS9FXAILib.DS9FXEnterWormholeAI
                     PlayerCast = App.ShipClass_Cast(pPlayer)
                     PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnterWormholeAI.CreateAI(PlayerCast))

                     # Go to Red Alert
                     pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

                     # Removing ability of the player to make any input
                     RemoveKeyboardControl()

                     # Create a pretty cutscene
                     pPlayer = App.Game_GetCurrentPlayer()    
                     pSequence = App.TGSequence_Create ()
                     pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                     pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                     pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                     pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                     pSequence.Play()

                     # A timer based event which is called to check distance from the wormhole in order to activate the transfering sequence
                     # A line no longer used since BC cannot seem to support 2 distance checks at once
                     # DistanceTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnterCheck", App.g_kUtopiaModule.GetGameTime() + 0)

                     # A second timer which will increase the scale of the wormhole, called instantly but scaled when we get to the right distance.
                     # Very similar to DistanceTimer, well the same 
                     ScaleDistanceTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime()+ 0)

                    

        # Check if we are in Gamma Quadrant set, if this is true transfer us to Wormhole set
        # I already stressed that this isn't as easy as it sounds
        elif (pSet.GetName() == "GammaQuadrant1"):
            
                     # Get the Gamma Quadrant set's name directly from the set file
                     Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")   
                     GammaSet = Gamma.GetSet()

                     # Grab the wormhole model this time in Gamma Quadrant set
                     pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet)
                     pDS9FXWormholeID = pDS9FXWormhole.GetObjID()
                     

                     # Compare distance between player and the wormhole
                     if DistanceCheck(pDS9FXWormhole) > 300:
                                        FelixWarnPrompt()
                                        print "DS9FX: To far out to enter Wormhole!"
                                        return

                     # Enter wormhole range has been changed, range should be around 10 km now for a reason.
                     elif DistanceCheck(pDS9FXWormhole) < 50:
                                        FelixWarnPrompt()
                                        print "DS9FX: To close to enter Wormhole!"
                                        return                 


                     # Bugfix insert repair the wormhole fully incase we fired on it earlier
                     Actions.ShipScriptActions.RepairShipFully(None, pDS9FXWormholeID)

                     # Bugfix insert
                     TranslatePlayer()

                     # All systems go you can go in, then delete RandomAttackTimer
                     DeleteRandomAttackTimer(None, None)

                     # Disable engineer's menu. I know what I'm doing
                     DisableEngineerMenu()

                     # Assign an DS9FXEnterWormholeAI to the player
                     import Custom.DS9FX.DS9FXAILib.DS9FXEnterWormholeAI
                     PlayerCast = App.ShipClass_Cast(pPlayer)
                     PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnterWormholeAI.CreateAI(PlayerCast))

                     # Go to Red Alert
                     pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

                     # Removing ability of the player to make any input
                     RemoveKeyboardControl()
                    
                     # Create a pretty cutscene
                     pPlayer = App.Game_GetCurrentPlayer()    
                     pSequence = App.TGSequence_Create ()
                     pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                     pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                     pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                     pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                     pSequence.Play()


                     # A timer based event which is called to check distance from the wormhole in order to activate the transfering sequence
                     # A line no longer used since BC cannot seem to support 2 distance checks at once
                     # DistanceTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnterCheck", App.g_kUtopiaModule.GetGameTime() + 0)

                     # A second timer which will increase the scale of the wormhole, called instantly but scaled when we get to the right distance.
                     # Very similar to DistanceTimer, well the same 
                     ScaleDistanceTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 0)

        # In worst case scenario pass
        else:
                    pass


# Sequence which is called when pressing Exit To DS9 button
def ExitToDS9Seq(pObject, pEvent):
                
        # Get the player
        debug(__name__ + ", ExitToDS9Seq")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0                

        # Check if we are in the proper set
        pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "BajoranWormhole1"):

                # First assign an AI to the player to move the ship forward, that's all
                # We have no need need for a distance check over here actually
                import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
                PlayerCast = App.ShipClass_Cast(pPlayer)
                PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))

                # Go to Red Alert
                pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

                # Create a pretty cutscene
                pPlayer = App.Game_GetCurrentPlayer()    
                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                # pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                # Add a new view when exiting the wormhole
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChaseCam", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                pSequence.Play()

                # Again disable also over here engineer's menu
                DisableEngineerMenu()

                # Create a timer which will after 15 seconds skip to another function
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitToDS9Seq2", App.g_kUtopiaModule.GetGameTime() + 15, 0, 0)

        # In worst case scenario pass
        else:
            pass


# Part 2 of the simplified sequence which calls for a video sequence and masked set transfer
def ExitToDS9Seq2(pObject, pEvent):
             
         # Grab some values
         debug(__name__ + ", ExitToDS9Seq2")
         pPlayer = App.Game_GetCurrentPlayer()    
         pSequence = App.TGSequence_Create ()

         # A bug so we maintain cinematic mode
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))

         # Play the sound
         pSound = App.TGSound_Create("sfx/Custom/DS9FX/WormholeLoop.wav", "WormLoop", 0)
         pSound.SetSFX(0) 
         pSound.SetInterface(1) 
         App.g_kSoundManager.PlaySound("WormLoop")

         # Do the next sequence
         pSequence.AppendAction(ExitBackToDS9(None, None), 1.0)

         pSequence.Play()



# Revised exit sequence, now the wormhole closes to give the similar effect as the wormhole entry sequence
# Anyway not the last sequence anymore
def ExitToDS9Seq3(pObject, pEvent):
         debug(__name__ + ", ExitToDS9Seq3")
         global ExitingScaleTimer, pPlayer

         # Grab some values
         pNewPlayer = App.Game_GetCurrentPlayer()
         
         # Switch to outside view, meaning start cinematic mode again to override currently forced bridge view
         pSequence = App.TGSequence_Create ()
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pNewPlayer.GetContainingSet().GetName ()))
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pNewPlayer.GetContainingSet().GetName(), "Bajoran Wormhole"))  
         pSequence.Play()


         # Move the player away from the wormhole
         import Custom.DS9FX.DS9FXAILib.DS9FXWormholeExitingSeqAI
         PlayerCast = App.ShipClass_Cast(pPlayer)
         PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXWormholeExitingSeqAI.CreateAI(PlayerCast))

         # First again kill the scalling timer, which could still be active
         StopScaleWormhole(None, None)

         # Now initiate wormhole reduction
         ExitingScaleTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitingWormholeScaling", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)

      

# Scale the DS9 Set wormhole down to 0.01 scale
def ExitingWormholeScaling(pObject, pEvent):               
        # Get the player
        debug(__name__ + ", ExitingWormholeScaling")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)

        
        # Mateo reported a bug... In his own words the wormhole didn't close properly sometimes. It happened only once but I figure that the timer wasn't killed. So do it one more time to make sure.
        StopScaleWormhole(None, None)


        # Safety measure to only trigger this event if the wormhole is there and then start manually scaling the wormhole
        if pDS9FXWormhole:
            
            App.g_kSoundManager.StopSound("WormLoop")
            
            from Custom.DS9FX.DS9FXLib import DS9FXWormholeScalingHelperLib

            DS9FXWormholeScalingHelperLib.StartScaling()


        # Else just play the sound and end the cutscene
        else:

            App.g_kSoundManager.StopSound("WormLoop")

            # Play the sound
            pSound = App.TGSound_Create("sfx/Custom/DS9FX/WormholeClose.wav", "WormClose", 0)
            pSound.SetSFX(0) 
            pSound.SetInterface(1) 
            App.g_kSoundManager.PlaySound("WormClose")

            # End the cutscene, it shouldn't ever happen but you never know            
            GlobalCutsceneEnding(None, None)



# Over here we move back to DS9 set map
def ExitBackToDS9(pObject, pEvent):
        debug(__name__ + ", ExitBackToDS9")
        global bEnter, bExitToGamma, bExitToDS9, bDockToDS9, bHail, bCloseChannel
        
    	# Get the player
    	pPlayer = App.Game_GetCurrentPlayer()    	
	if not pPlayer:
		return 0
	
        # Double check if we're in the right set
	pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "BajoranWormhole1"):

            # Play the video sequence now
            from Custom.DS9FX.DS9FXWormholeVid import DS9FXWormholeVideo

            DS9FXWormholeVideo.PlayMovieSeq(None, None)

            # Force bridge view, for gameplay purposes when we exit the video screen
            pSequence = App.TGSequence_Create ()
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
            pSequence.Play()

            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CheckVideoExitingDS9", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

            # Disable or reenable buttons
            bEnter.SetEnabled()
            bExitToGamma.SetDisabled()
            bExitToDS9.SetDisabled()
            
            if bHail == None:
                pass

            else:
                bHail.SetEnabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetEnabled()
                
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetEnabled()

        # Also pass in worst case scenario
        else:
            pass



# Sequence which is called when pressing Exit To Gamma button
def ExitToGammaSeq(pObject, pEvent):
        # Get the player
        debug(__name__ + ", ExitToGammaSeq")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0                

        # Check if we are in the proper set
        pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "BajoranWormhole1"):

                # First assign an AI to the player to move the ship forward, that's all
                # We have no need need for a distance check over here actually
                import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
                PlayerCast = App.ShipClass_Cast(pPlayer)
                PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))

                # Go to Red Alert
                pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

                # Create a pretty cutscene
                pPlayer = App.Game_GetCurrentPlayer()    
                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                # pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                # Add a new view when exiting wormhole
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChaseCam", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
                pSequence.Play()

                # Just disable the damn menu
                DisableEngineerMenu()

                # Create a timer which will after 15 seconds skip to another function
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitToGammaSeq2", App.g_kUtopiaModule.GetGameTime() + 15, 0, 0)

        # In worst case scenario pass
        else:
            pass



# 2nd part of the ExitToGammaSeq
def ExitToGammaSeq2(pObject, pEvent):
                 
         # Grab some values
         debug(__name__ + ", ExitToGammaSeq2")
         pPlayer = App.Game_GetCurrentPlayer()    
         pSequence = App.TGSequence_Create ()

         # Maintain cinematic mode
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))

         # Play the sound
         pSound = App.TGSound_Create("sfx/Custom/DS9FX/WormholeLoop.wav", "WormLoop", 0)
         pSound.SetSFX(0) 
         pSound.SetInterface(1) 
         App.g_kSoundManager.PlaySound("WormLoop")

         # Do the next sequence
         pSequence.AppendAction(ExitBackToGamma(None, None), 1.0)

         pSequence.Play()



# Also a revised version of the exiting sequence, much better looking now
# Not the last sequence anymore
def ExitToGammaSeq3(pObject, pEvent):
         debug(__name__ + ", ExitToGammaSeq3")
         global ExitingScaleTimer, pPlayer

         # Grab some values
         pNewPlayer = App.Game_GetCurrentPlayer()
         
         # Switch to outside view, meaning start cinematic mode again to override currently forced bridge view
         pSequence = App.TGSequence_Create ()
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pNewPlayer.GetContainingSet().GetName ()))
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pNewPlayer.GetContainingSet().GetName(), "Bajoran Wormhole"))         
         pSequence.Play()
         

         # Move the player away from the wormhole
         import Custom.DS9FX.DS9FXAILib.DS9FXWormholeExitingSeqAI
         PlayerCast = App.ShipClass_Cast(pPlayer)
         PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXWormholeExitingSeqAI.CreateAI(PlayerCast))
         

         # First again kill the scalling timer, which could still be active
         StopScaleWormhole(None, None)

         # Now initiate wormhole reduction
         ExitingScaleTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ExitingWormholeScaling", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)



# Global cutscene ending for both Gamma and DS9 Set exiting, called when the wormhole is reduced properly
def GlobalCutsceneEnding(pObject, pEvent):
         debug(__name__ + ", GlobalCutsceneEnding")
         global ScaleWormholePrevention
    
         # Grab some values and play final part of the sequence
         pPlayer = App.Game_GetCurrentPlayer()    
         pSequence = App.TGSequence_Create ()
         pSet = pPlayer.GetContainingSet()

         # Maintain cinematic mode
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))

         # Set wormholes scale to 0.01, just to be safe
         pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
         pDS9FXWormhole.SetScale(0.01)
         pDS9FXWormhole.SetHidden(1)
        
         # And finally stop the player and clear all AI's
         import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
         PlayerCast = App.ShipClass_Cast(pPlayer)
         PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

         # End the cutscene camera
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ()))

         # Switch to bridge view
         if App.g_kSetManager.GetSet("bridge"):
                  pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                  pSequence.AppendAction(pAction)
         pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))

         # Play the sequence
         pSequence.Play()

         # Reenable the menu
         EnableEngineerMenu()

         # Restoring ScaleWormholePrevention back to 0 to allow future wormhole scallings
         ScaleWormholePrevention = None
         ScaleWormholePrevention = 0


# Over here we activate the video sequence and call in a function which transfers you and allied ships to gamma quadrant map
def ExitBackToGamma(pObject, pEvent):
        debug(__name__ + ", ExitBackToGamma")
        global bEnter, bExitToGamma, bExitToDS9, bDockToDS9, bHail, bCloseChannel
        
    	# Get the player
    	pPlayer = App.Game_GetCurrentPlayer()    	
	if not pPlayer:
		return 0
	
        # Double check if we're in the right set
	pSet = pPlayer.GetContainingSet()
        if (pSet.GetName() == "BajoranWormhole1"):

            # Play the video sequence now
            from Custom.DS9FX.DS9FXWormholeVid import DS9FXWormholeVideo

            DS9FXWormholeVideo.PlayMovieSeq(None, None)

            # Force bridge view, for gameplay purposes when we exit the video screen
            pSequence = App.TGSequence_Create ()
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
            pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
            pSequence.Play()
            
            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CheckVideoExitingGamma", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

            # Disable or reenable buttons
            bEnter.SetEnabled()
            bExitToGamma.SetDisabled()
            bExitToDS9.SetDisabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()
            
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetDisabled()

        # Also pass in worst case scenario
        else:
            pass



# Well, we'll now trick BC. Compensations are needed oh well, BC is one fucked up thing
def EnterCheckDummyCreation(pObject, pEvent):
    
        # Get the player
        debug(__name__ + ", EnterCheckDummyCreation")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0

        # Get the set
        pSet = pPlayer.GetContainingSet()
        
        loadspacehelper.CreateShip("Distortion", pSet, "Bajoran Wormhole Dummy", "Wormhole Location")

        pDS9FXWormholeDummy = MissionLib.GetShip("Bajoran Wormhole Dummy", pSet)

        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)

        # Disable any ship collisions with the nav beacon well sort off, sigh... why is BC so stubborn sometimes
        for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(pSet, kShip.GetName())
                pDS9FXWormholeDummy.EnableCollisionsWith(pShip, 0)

        # Now call in the EnterCheck def
        EnterCheck(None, None)
        


# Well now instead of a Distance check we use ConditionInRange, which pretty much cannot fuck up.
def EnterCheck(pObject, pEvent):
        debug(__name__ + ", EnterCheck")
        global DistanceCheckCondition

        # Get the player
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0

        # Grab some values
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

        # Dummies name
        pDS9FXWormhole = "Bajoran Wormhole Dummy"


        # Start the condition script
        DistanceCheckCondition = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 5, pPlayer.GetName(), pDS9FXWormhole)
        MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "Redirect", DistanceCheckCondition)



# Redirect us to EnterSeq2 function
def Redirect(bInRange):
        # Deactivate the condition script
        debug(__name__ + ", Redirect")
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "Redirect")
        
        # Call in the EnterSeq2
        EnterSeq2(None, None)



# This is very similar to EnterCheck def, just it calls for a different function which scales the wormhole
def ScaleWormholeDistanceCheck(pObject, pEvent):
        debug(__name__ + ", ScaleWormholeDistanceCheck")
        global ScaleDistanceTimer

        # Get the player
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0

        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Grab the wormhole model
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)

        # When the distance is smaller than 40 we call for the next sequence and play the sound
        if PlayerScaleWormholeDistance(pDS9FXWormhole) <= 40:

                # First delete the timer, again this line is returned in active state
                ScaleDistanceTimerDelete(None, None)

                # Okay a new way to make an enter check, make a dummy firepoint to navigate and check the distance from that dummy and use ConditionsInRange
                EnterCheckDummyCreation(None, None)
            
                # Play the sound
                pSound = App.TGSound_Create("sfx/Custom/DS9FX/WormoleOpen.wav", "WormOpen", 0)
                pSound.SetSFX(0) 
                pSound.SetInterface(1) 
                App.g_kSoundManager.PlaySound("WormOpen")

                # Change cutscene camera view
                pSequence = App.TGSequence_Create ()
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "TargetWatch", pPlayer.GetContainingSet().GetName(), pPlayer.GetName (), "Bajoran Wormhole"))
                pSequence.Play()

                # Make a nice little action and create the flash effect
                from Custom.DS9FX.DS9FXWormholeFlash.DS9FXEnterWormholeFlash import StartGFX, CreateGFX
                
                StartGFX()
                for i in range(1):
                    CreateGFX(pDS9FXWormhole)

                pDS9FXWormhole.SetHidden(0)

                # Do our animations and make sure that the timer is properly deleted
                # From now on delay scaling due to flash effect first for 2 seconds
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormhole", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)


        # If we still aren't at the right coordinates continue to repeat the timer and continue to position the wormhole
        # towards the player until we reach distance of 40 units
        else:
                # Position the Wormhole to face the player in order to aid the Artificial Intelligence
                # I also then don't need to make navpoints then, the wormhole simply faces the player instead
                pPlayerBackward = pPlayer.GetWorldBackwardTG()
                pPlayerDown = pPlayer.GetWorldDownTG()

                pDS9FXWormhole.AlignToVectors(pPlayerBackward, pPlayerDown)
                pDS9FXWormhole.UpdateNodeOnly()

            
                ScaleDistanceTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 0)




# This function deletes the scale distance timer
def ScaleDistanceTimerDelete(pObject, pEvent):
        debug(__name__ + ", ScaleDistanceTimerDelete")
        global ScaleDistanceTimer

        # Just simply delete the distance timer that's all
        try:
                    App.g_kTimerManager.DeleteTimer(ScaleDistanceTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(ScaleDistanceTimer.GetObjID())
                    # ScaleDistanceTimer = None
        except:
                    pass
     


# 2nd part of the sequence
def EnterSeq2(pObject, pEvent):
         # Problems showed up, retry to delete the timer over here also
         # DeleteDistanceTimer(None, None)
                 
         # Grab some values
         debug(__name__ + ", EnterSeq2")
         pPlayer = App.Game_GetCurrentPlayer()    
         pSequence = App.TGSequence_Create ()


         # Maintain cinematic mode
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
         pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))

         # Play the sound
         pSound = App.TGSound_Create("sfx/Custom/DS9FX/WormholeLoop.wav", "WormLoop", 0)
         pSound.SetSFX(0) 
         pSound.SetInterface(1) 
         App.g_kSoundManager.PlaySound("WormLoop")

         # Do the next sequence
         pSequence.AppendAction(Enter(None, None), 1.0)

         pSequence.Play()



# 3rd and final part of the sequence
def EnterSeq3(pObject, pEvent):
         debug(__name__ + ", EnterSeq3")
         global SecHandler

         if SecHandler > DS9Timer:
            ReturnKeyboardControl()
            return

         elif SecHandler < DS9Timer:
            ReturnKeyboardControl()
            return

         else:
             
                 App.g_kSoundManager.StopSound("WormLoop")
                         
                 # Play the sound
                 pSound = App.TGSound_Create("sfx/Custom/DS9FX/WormholeClose.wav", "WormClose", 0)
                 pSound.SetSFX(0) 
                 pSound.SetInterface(1) 
                 App.g_kSoundManager.PlaySound("WormClose")

                 # Grab some values and play final part of the sequence
                 pPlayer = App.Game_GetCurrentPlayer()    
                 pSequence = App.TGSequence_Create ()
                 pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
                 pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
                 pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ()))


                 # Switch to bridge view
                 if App.g_kSetManager.GetSet("bridge"):
                          pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge")
                          pSequence.AppendAction(pAction)
                 pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))


                 # Play the sequence
                 pSequence.Play()


                 # And finally reenable engineer's menu
                 EnableEngineerMenu()

                 # Restore keyboard control
                 ReturnKeyboardControl()

                 # Bugfix insert clear AI first
                 pPlayer.ClearAI()
                 
                 # Clear the HelmAI and tell it to stop
                 import AI.Player.Stay
		 MissionLib.SetPlayerAI("Helm", AI.Player.Stay.CreateAI(pPlayer))

                 # Problem showed up so we have to once again order the player to move forward
                 import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
                 PlayerCast = App.ShipClass_Cast(pPlayer)
                 PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))




# Wowbagger reported a bug so we reworked the entry seqeunce
def Enter(pObject, pEvent):
        debug(__name__ + ", Enter")
        global bEnter, bExitToGamma, bExitToDS9, bDockToDS9, bHail, bCloseChannel
        
    	# Get the player
    	pPlayer = App.Game_GetCurrentPlayer()    	
	if not pPlayer:
		return 0

	# Okay see if we are in DS9 and transfer us to wormhole set if this is true
	# It never hurts to double check
	pSet = pPlayer.GetContainingSet()
	if (pSet.GetName() == "DeepSpace91"):

	
            # Disable or reenable buttons
            bEnter.SetDisabled()
            bExitToGamma.SetEnabled()
            bExitToDS9.SetEnabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()
                
            if bDockToDS9 == None:
                pass 

            else:
                bDockToDS9.SetDisabled()

            # Call in TransferShips function, not much else over here anymore
            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferShips", App.g_kUtopiaModule.GetGameTime() + 0, 0, 0)



	# Check if we are in Gamma Quadrant set, if this is true transfer us to Wormhole set
	elif (pSet.GetName() == "GammaQuadrant1"):


            # Disable or reenable buttons
            bEnter.SetDisabled()
            bExitToGamma.SetEnabled()
            bExitToDS9.SetEnabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()
                
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetDisabled()

            # Call in TransferShips function, not much else over here anymore
            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferShips", App.g_kUtopiaModule.GetGameTime() + 0, 0, 0)


            
        # Also a safety measure, in worst case scenario pass
        else:
            pass



# Activate DS9FX Set Placement when we enter one of desired sets
def ActivateDS9FXPlacement(pObject, pEvent):
        debug(__name__ + ", ActivateDS9FXPlacement")
        global RandomEnemyFleet, RandomAttackTimer
        global InsideWormholeTimer
        global bEnter, bExitToGamma, bExitToDS9, bDockToDS9, bHail, bCloseChannel
        
        # Grab some values
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()


        
        # Only and only activate placement if we are in DS9 set
        if (pSet.GetName() == "DeepSpace91"):
            
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            try:
                    pSet.RemoveObjectFromSet("Bajoran Wormhole")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Excalibur")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Deep_Space_9")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Defiant")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Oregon")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS_Lakota")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 3")
            except:
                pass
            try:
                    # Remove the dummy wormhole object also
                    pSet.RemoveObjectFromSet("Bajoran Wormhole Dummy")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Comet Alpha")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 3")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 4")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 5")
            except:
                pass


            # Call in the file which holds info about the wormhole and other objects, if there are any available
            from Custom.DS9FX.DS9FXObjects import DS9Objects
            
            DS9Objects.DS9SetObjects()

            # Call in the file which holds info about stations
            from Custom.DS9FX.DS9FXObjects import DS9Stations

            DS9Stations.DS9SetStations()

            # Call in the file which holds info about ships in DS9 set
            from Custom.DS9FX.DS9FXObjects import DS9Ships

            DS9Ships.DS9SetShips()

            # Grab the set's name directly from the set file
            DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
            DS9Set = DS9.GetSet()

            # Grab the wormhole model
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set)

            # Disable collisions with player and the Wormhole
            pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)

            # Disable any ship collisions with the wormhole
            for kShip in DS9Set.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(DS9Set, kShip.GetName())
                pDS9FXWormhole.EnableCollisionsWith(pShip, 0)

            # Reenable warp button
            RestoreWarpButton()

            if pRandomEnemyFleetAttacks == 1:
                    # Start counting until the enemy fleet arrives
                    RandomAttackTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnemyFleetArrives", App.g_kUtopiaModule.GetGameTime() + RandomEnemyFleet)

                    # print "DS9FX: Starting Random Enemy Fleet Attack Countdown!"
            

            if pDS9Music == 1:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music" + ".mp3", "DS9Music", 2.0)
                    DynamicMusic.dsMusicTypes["DS9Music"] = "DS9Music"
                    DynamicMusic.OverrideMusic("DS9Music")

            elif pDS9Music == 2:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9MusicAlternate" + ".mp3", "DS9MusicAlternate", 2.0)
                    DynamicMusic.dsMusicTypes["DS9MusicAlternate"] = "DS9MusicAlternate"
                    DynamicMusic.OverrideMusic("DS9MusicAlternate")

            elif pDS9Music == 3:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music2" + ".mp3", "DS9Music2", 2.0)
                    DynamicMusic.dsMusicTypes["DS9Music2"] = "DS9Music2"
                    DynamicMusic.OverrideMusic("DS9Music2")

            elif pDS9Music == 4:
                    # Do a random music selection, by choosing a random number
                    pDS9MusicSelection = GetRandomDS9Music(1)
                    if pDS9MusicSelection <= 33:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music" + ".mp3", "DS9Music", 2.0)
                                DynamicMusic.dsMusicTypes["DS9Music"] = "DS9Music"
                                DynamicMusic.OverrideMusic("DS9Music")

                    elif pDS9MusicSelection <= 66 and pDS9MusicSelection > 33:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9MusicAlternate" + ".mp3", "DS9MusicAlternate", 2.0)
                                DynamicMusic.dsMusicTypes["DS9MusicAlternate"] = "DS9MusicAlternate"
                                DynamicMusic.OverrideMusic("DS9MusicAlternate")

                    elif pDS9MusicSelection > 66:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music2" + ".mp3", "DS9Music2", 2.0)
                                DynamicMusic.dsMusicTypes["DS9Music2"] = "DS9Music2"
                                DynamicMusic.OverrideMusic("DS9Music2")

            # Disable or reenable buttons
            bEnter.SetEnabled()
            bExitToGamma.SetDisabled()
            bExitToDS9.SetDisabled()
            if bHail == None:
                pass

            else:
                bHail.SetEnabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetEnabled()
                
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetEnabled()

            
            try:
                # Remove the listener
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".ActivateDS9FXPlacement")

            except:
                pass

        elif (pSet.GetName() == "GammaQuadrant1"):
            
            
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            try:
                    pSet.RemoveObjectFromSet("Bajoran Wormhole")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Excalibur")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Deep_Space_9")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Defiant")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Oregon")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS_Lakota")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 3")
            except:
                pass
            try:
                    # Remove the dummy wormhole object also
                    pSet.RemoveObjectFromSet("Bajoran Wormhole Dummy")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Comet Alpha")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 3")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 4")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 5")
            except:
                pass



            # Load Gamma Quadrant Objects
            from Custom.DS9FX.DS9FXObjects import GammaObjects

            GammaObjects.GammsSetObjects()
            
            # Load Gamma Quadrant ships 
            from Custom.DS9FX.DS9FXObjects import GammaShips

            GammaShips.GammaSetShips()

            # Grab the system name from the set file
            Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
            GammaSet = Gamma.GetSet()

            # Grab the wormhole model
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet)

            # Disable collisions with player and the Wormhole
            pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)

            # Disable any ship collisions with the wormhole
            for kShip in GammaSet.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(GammaSet, kShip.GetName())
                pDS9FXWormhole.EnableCollisionsWith(pShip, 0)

            # Grab the ship that has antiproton scan ability
            APShip = MissionLib.GetShip("Bugship 1", GammaSet)
            APShip2 = MissionLib.GetShip("Bugship 2", GammaSet)
            APShip3 = MissionLib.GetShip("Bugship 2", GammaSet)

            if pDomIS == 1:
                    # If this ship exists initiate antiprotonscan
                    if APShip:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                    elif APShip2:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                    elif APShip3:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                
            # Disable warp button
            DisableWarpButton()

            if pGammaMusic == 1:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusic" + ".mp3", "GammaMusic", 2.0)
                    DynamicMusic.dsMusicTypes["GammaMusic"] = "GammaMusic"
                    DynamicMusic.OverrideMusic("GammaMusic")

            elif pGammaMusic == 2:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusicAlternate" + ".mp3", "GammaMusicAlternate", 2.0)
                    DynamicMusic.dsMusicTypes["GammaMusicAlternate"] = "GammaMusicAlternate"
                    DynamicMusic.OverrideMusic("GammaMusicAlternate")

            elif pGammaMusic == 3:
                    # Do a random music selection, by choosing a random number
                    pGammaMusicSelection = GetRandomGammaMusic(1)
                    if pGammaMusicSelection <= 33:
                                    # Start a nice piece of music
                                    import DynamicMusic
                                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusic" + ".mp3", "GammaMusic", 2.0)
                                    DynamicMusic.dsMusicTypes["GammaMusic"] = "GammaMusic"
                                    DynamicMusic.OverrideMusic("GammaMusic")

                    elif pGammaMusicSelection > 33:
                                    # Start a nice piece of music
                                    import DynamicMusic
                                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusicAlternate" + ".mp3", "GammaMusicAlternate", 2.0)
                                    DynamicMusic.dsMusicTypes["GammaMusicAlternate"] = "GammaMusicAlternate"
                                    DynamicMusic.OverrideMusic("GammaMusicAlternate")

            # Disable or reenable buttons
            bEnter.SetEnabled()
            bExitToGamma.SetDisabled()
            bExitToDS9.SetDisabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()
                
            if bDockToDS9 == None:
                pass 

            else:
                bDockToDS9.SetDisabled()

            
            # Bugfix insert when not in DS9 Set delete random attack timer
            DeleteRandomAttackTimer(None, None)


            try:
                # Remove the listener
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".ActivateDS9FXPlacement")

            except:
                pass


        elif (pSet.GetName() == "BajoranWormhole1"):

            
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            try:
                    pSet.RemoveObjectFromSet("Bajoran Wormhole")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Excalibur")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Deep_Space_9")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Defiant")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Oregon")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS_Lakota")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 3")
            except:
                pass
            try:
                    # Remove the dummy wormhole object also
                    pSet.RemoveObjectFromSet("Bajoran Wormhole Dummy")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Comet Alpha")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 3")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 4")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 5")
            except:
                pass




            # Get the wormhole set
            Wormhole = __import__("Systems.BajoranWormhole.BajoranWormhole1")
            
            # Get set's name directly from the wormhole
            WormholeSet = Wormhole.GetSet()

            # Load placements
            from Custom.DS9FX.DS9FXObjects import WormholeObjects

            WormholeObjects.WormholeSetObjects()

            # Grab the wormhole model
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet)
            pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)

            # Position the wormhole so that it appears you're inside the wormhole
            pPlayerBackward = pPlayer.GetWorldBackwardTG()
            pPlayerDown = pPlayer.GetWorldDownTG()
            pPlayerPosition = pPlayer.GetWorldLocation()

            pDS9FXWormhole.AlignToVectors(pPlayerBackward, pPlayerDown)
            pDS9FXWormhole.SetTranslate(pPlayerPosition)
            pDS9FXWormhole.UpdateNodeOnly()

            pDS9FXWormhole2.AlignToVectors(pPlayerBackward, pPlayerDown)
            pDS9FXWormhole2.SetTranslate(pPlayerPosition)
            pDS9FXWormhole2.UpdateNodeOnly()


            # Disable player <=> cone collision
            pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)
            pDS9FXWormhole2.EnableCollisionsWith(pPlayer, 0)
            
            # Disable any ship collisions with the cone
            for kShip in WormholeSet.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(WormholeSet, kShip.GetName())
                pDS9FXWormhole.EnableCollisionsWith(pShip, 0)
                pDS9FXWormhole2.EnableCollisionsWith(pShip, 0)

            # Stop the player 
            import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
            PlayerCast = App.ShipClass_Cast(pPlayer)
            PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

            # Move the player forward. We use StopAI first to clear any AI that might be interfering
            import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
            PlayerCast = App.ShipClass_Cast(pPlayer)
            PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))
              
     	
            # Disable warp button
            DisableWarpButton()


            # Disable or reenable buttons
            bEnter.SetDisabled()
            bExitToGamma.SetEnabled()
            bExitToDS9.SetEnabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()
            
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetDisabled()


            if pWormholeMusic == 1:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusic" + ".mp3", "WormholeMusic", 2.0)
                    DynamicMusic.dsMusicTypes["WormholeMusic"] = "WormholeMusic"
                    DynamicMusic.OverrideMusic("WormholeMusic")

            elif pWormholeMusic == 2:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusicAlternate" + ".mp3", "WormholeMusicAlternate", 2.0)
                    DynamicMusic.dsMusicTypes["WormholeMusicAlternate"] = "WormholeMusicAlternate"
                    DynamicMusic.OverrideMusic("WormholeMusicAlternate")

            elif pWormholeMusic == 3:
                    pWormholeMusicSelection = GetRandomWormholeMusic(1)
                    if pWormholeMusicSelection <= 33:
                        # Start a nice piece of music
                        import DynamicMusic
                        App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusic" + ".mp3", "WormholeMusic", 2.0)
                        DynamicMusic.dsMusicTypes["WormholeMusic"] = "WormholeMusic"
                        DynamicMusic.OverrideMusic("WormholeMusic")
                    elif pWormholeMusicSelection > 33:
                        # Start a nice piece of music
                        import DynamicMusic
                        App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusicAlternate" + ".mp3", "WormholeMusicAlternate", 2.0)
                        DynamicMusic.dsMusicTypes["WormholeMusicAlternate"] = "WormholeMusicAlternate"
                        DynamicMusic.OverrideMusic("WormholeMusicAlternate")
                    
            
            # Bugfix insert when not in DS9 Set delete random attack timer
            DeleteRandomAttackTimer(None, None)

            # Start a timer which will every few seconds check players distance from the wormhole, delayed for a few secs due to some bugs
            InsideWormholeTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".InsideWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 15)
   
            try:
                # Remove the listener
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".ActivateDS9FXPlacement")

            except:
                pass


        else:
            # MLeo EDIT: When the interface hasn't been loaded yet, call the next handler and exit
            if not bExitToGamma or not bExitToDS9 or not bDockToDS9:
                # Sov Edit Note: this caused an error in KM 1.0
                try:
                    pObject.CallNextHandler(pEvent)
                except:
                    pass
		return
	    
            # Else just disable all buttons	
            bExitToGamma.SetDisabled()
            bExitToDS9.SetDisabled()
            bEnter.SetDisabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()

            # Dock button doesn't have to exist
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetDisabled()


# Activate DS9FX Set Placement when we enter one of desired sets of course manually, while ActivateDS9FXPlacement and this function may seem similar, they are quite different in many aspects
def ManuallyActivateDS9FXPlacement(pObject, pEvent):
        debug(__name__ + ", ManuallyActivateDS9FXPlacement")
        global RandomEnemyFleet, RandomAttackTimer
        global InsideWormholeTimer
        global bEnter, bExitToGamma, bExitToDS9, bDockToDS9, bHail, bCloseChannel
        
        # Grab some values
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()


        
        # Only and only activate placement if we are in DS9 set
        if (pSet.GetName() == "DeepSpace91"):

            
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            try:
                    pSet.RemoveObjectFromSet("Bajoran Wormhole")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Excalibur")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Deep_Space_9")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Defiant")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Oregon")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS_Lakota")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 3")
            except:
                pass
            try:
                    # Remove the dummy wormhole object also
                    pSet.RemoveObjectFromSet("Bajoran Wormhole Dummy")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Comet Alpha")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 3")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 4")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 5")
            except:
                pass


            # Call in the file which holds info about the wormhole and other objects, if there are any available
            from Custom.DS9FX.DS9FXObjects import DS9Objects
            
            DS9Objects.DS9SetObjects()

            # Call in the file which holds info about stations
            from Custom.DS9FX.DS9FXObjects import DS9Stations

            DS9Stations.DS9SetStations()

            # Call in the file which holds info about ships in DS9 set
            from Custom.DS9FX.DS9FXObjects import DS9Ships

            DS9Ships.DS9SetShips()

            # Grab the set's name directly from the set file
            DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
            DS9Set = DS9.GetSet()

            # Grab the wormhole model
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set)

            # Disable collisions with player and the Wormhole
            pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)

            # Disable any ship collisions with the wormhole
            for kShip in DS9Set.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(DS9Set, kShip.GetName())
                pDS9FXWormhole.EnableCollisionsWith(pShip, 0)

            # Reenable warp button
            RestoreWarpButton()

            if pRandomEnemyFleetAttacks == 1:
                    # Start counting until the enemy fleet arrives
                    RandomAttackTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnemyFleetArrives", App.g_kUtopiaModule.GetGameTime() + RandomEnemyFleet)

                    # print "DS9FX: Starting Random Enemy Fleet Attack Countdown!"
            

            if pDS9Music == 1:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music" + ".mp3", "DS9Music", 2.0)
                    DynamicMusic.dsMusicTypes["DS9Music"] = "DS9Music"
                    DynamicMusic.OverrideMusic("DS9Music")

            elif pDS9Music == 2:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9MusicAlternate" + ".mp3", "DS9MusicAlternate", 2.0)
                    DynamicMusic.dsMusicTypes["DS9MusicAlternate"] = "DS9MusicAlternate"
                    DynamicMusic.OverrideMusic("DS9MusicAlternate")

            elif pDS9Music == 3:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music2" + ".mp3", "DS9Music2", 2.0)
                    DynamicMusic.dsMusicTypes["DS9Music2"] = "DS9Music2"
                    DynamicMusic.OverrideMusic("DS9Music2")
                    
            elif pDS9Music == 4:
                    # Do a random music selection, by choosing a random number
                    pDS9MusicSelection = GetRandomDS9Music(1)
                    if pDS9MusicSelection <= 33:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music" + ".mp3", "DS9Music", 2.0)
                                DynamicMusic.dsMusicTypes["DS9Music"] = "DS9Music"
                                DynamicMusic.OverrideMusic("DS9Music")

                    elif pDS9MusicSelection <= 66 and pDS9MusicSelection > 33:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9MusicAlternate" + ".mp3", "DS9MusicAlternate", 2.0)
                                DynamicMusic.dsMusicTypes["DS9MusicAlternate"] = "DS9MusicAlternate"
                                DynamicMusic.OverrideMusic("DS9MusicAlternate")

                    elif pDS9MusicSelection > 66:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music2" + ".mp3", "DS9Music2", 2.0)
                                DynamicMusic.dsMusicTypes["DS9Music2"] = "DS9Music2"
                                DynamicMusic.OverrideMusic("DS9Music2")
    

            # Disable or reenable buttons
            bEnter.SetEnabled()
            bExitToGamma.SetDisabled()
            bExitToDS9.SetDisabled()
            if bHail == None:
                pass

            else:
                bHail.SetEnabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetEnabled()
                
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetEnabled()

            
        elif (pSet.GetName() == "GammaQuadrant1"):

            
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            try:
                    pSet.RemoveObjectFromSet("Bajoran Wormhole")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Excalibur")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Deep_Space_9")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Defiant")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Oregon")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS_Lakota")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 3")
            except:
                pass
            try:
                    # Remove the dummy wormhole object also
                    pSet.RemoveObjectFromSet("Bajoran Wormhole Dummy")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Comet Alpha")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 3")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 4")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 5")
            except:
                pass


            
            # Load Gamma Quadrant Objects
            from Custom.DS9FX.DS9FXObjects import GammaObjects

            GammaObjects.GammsSetObjects()
            
            # Load Gamma Quadrant ships 
            from Custom.DS9FX.DS9FXObjects import GammaShips

            GammaShips.GammaSetShips()

            # Grab the system name from the set file
            Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
            GammaSet = Gamma.GetSet()

            # Grab the wormhole model
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet)

            # Disable collisions with player and the Wormhole
            pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)

            # Disable any ship collisions with the wormhole
            for kShip in GammaSet.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(GammaSet, kShip.GetName())
                pDS9FXWormhole.EnableCollisionsWith(pShip, 0)

            # Grab the ship that has antiproton scan ability
            APShip = MissionLib.GetShip("Bugship 1", GammaSet)
            APShip2 = MissionLib.GetShip("Bugship 2", GammaSet)
            APShip3 = MissionLib.GetShip("Bugship 2", GammaSet)

            if pDomIS == 1:
                    # If this ship exists initiate antiprotonscan
                    if APShip:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                    elif APShip2:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                    elif APShip3:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                
            # Disable warp button
            DisableWarpButton()

            if pGammaMusic == 1:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusic" + ".mp3", "GammaMusic", 2.0)
                    DynamicMusic.dsMusicTypes["GammaMusic"] = "GammaMusic"
                    DynamicMusic.OverrideMusic("GammaMusic")

            elif pGammaMusic == 2:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusicAlternate" + ".mp3", "GammaMusicAlternate", 2.0)
                    DynamicMusic.dsMusicTypes["GammaMusicAlternate"] = "GammaMusicAlternate"
                    DynamicMusic.OverrideMusic("GammaMusicAlternate")

            elif pGammaMusic == 3:
                    # Do a random music selection, by choosing a random number
                    pGammaMusicSelection = GetRandomGammaMusic(1)
                    if pGammaMusicSelection <= 33:
                                    # Start a nice piece of music
                                    import DynamicMusic
                                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusic" + ".mp3", "GammaMusic", 2.0)
                                    DynamicMusic.dsMusicTypes["GammaMusic"] = "GammaMusic"
                                    DynamicMusic.OverrideMusic("GammaMusic")

                    elif pGammaMusicSelection > 33:
                                    # Start a nice piece of music
                                    import DynamicMusic
                                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusicAlternate" + ".mp3", "GammaMusicAlternate", 2.0)
                                    DynamicMusic.dsMusicTypes["GammaMusicAlternate"] = "GammaMusicAlternate"
                                    DynamicMusic.OverrideMusic("GammaMusicAlternate")
                                    

            # Disable or reenable buttons
            bEnter.SetEnabled()
            bExitToGamma.SetDisabled()
            bExitToDS9.SetDisabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()
                
            if bDockToDS9 == None:
                pass 

            else:
                bDockToDS9.SetDisabled()

            
            # Bugfix insert when not in DS9 Set delete random attack timer
            DeleteRandomAttackTimer(None, None)



        elif (pSet.GetName() == "BajoranWormhole1"):

            
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            try:
                    pSet.RemoveObjectFromSet("Bajoran Wormhole")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Excalibur")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Deep_Space_9")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Defiant")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS Oregon")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("USS_Lakota")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Bugship 3")
            except:
                pass
            try:
                    # Remove the dummy wormhole object also
                    pSet.RemoveObjectFromSet("Bajoran Wormhole Dummy")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Comet Alpha")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 1")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 2")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 3")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 4")
            except:
                pass
            try:
                    pSet.RemoveObjectFromSet("Attacker 5")
            except:
                pass



            # Get the wormhole set
            Wormhole = __import__("Systems.BajoranWormhole.BajoranWormhole1")
            
            # Get set's name directly from the wormhole
            WormholeSet = Wormhole.GetSet()

            # Load placements
            from Custom.DS9FX.DS9FXObjects import WormholeObjects

            WormholeObjects.WormholeSetObjects()

            # Grab the wormhole model
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet)
            pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)

            # Position the wormhole so that it appears you're inside the wormhole
            pPlayerBackward = pPlayer.GetWorldBackwardTG()
            pPlayerDown = pPlayer.GetWorldDownTG()
            pPlayerPosition = pPlayer.GetWorldLocation()

            pDS9FXWormhole.AlignToVectors(pPlayerBackward, pPlayerDown)
            pDS9FXWormhole.SetTranslate(pPlayerPosition)
            pDS9FXWormhole.UpdateNodeOnly()

            pDS9FXWormhole2.AlignToVectors(pPlayerBackward, pPlayerDown)
            pDS9FXWormhole2.SetTranslate(pPlayerPosition)
            pDS9FXWormhole2.UpdateNodeOnly()


            # Disable player <=> cone collision
            pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)
            pDS9FXWormhole2.EnableCollisionsWith(pPlayer, 0)
            
            # Disable any ship collisions with the cone
            for kShip in WormholeSet.GetClassObjectList(App.CT_SHIP):
                pShip = App.ShipClass_GetObject(WormholeSet, kShip.GetName())
                pDS9FXWormhole.EnableCollisionsWith(pShip, 0)
                pDS9FXWormhole2.EnableCollisionsWith(pShip, 0)

            # Stop the player 
            import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
            PlayerCast = App.ShipClass_Cast(pPlayer)
            PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

            # Move the player forward. We use StopAI first to clear any AI that might be interfering
            import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
            PlayerCast = App.ShipClass_Cast(pPlayer)
            PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))
              
     	
            # Disable warp button
            DisableWarpButton()


            # Disable or reenable buttons
            bEnter.SetDisabled()
            bExitToGamma.SetEnabled()
            bExitToDS9.SetEnabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()
            
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetDisabled()


            if pWormholeMusic == 1:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusic" + ".mp3", "WormholeMusic", 2.0)
                    DynamicMusic.dsMusicTypes["WormholeMusic"] = "WormholeMusic"
                    DynamicMusic.OverrideMusic("WormholeMusic")

            elif pWormholeMusic == 2:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusicAlternate" + ".mp3", "WormholeMusicAlternate", 2.0)
                    DynamicMusic.dsMusicTypes["WormholeMusicAlternate"] = "WormholeMusicAlternate"
                    DynamicMusic.OverrideMusic("WormholeMusicAlternate")

            elif pWormholeMusic == 3:
                    pWormholeMusicSelection = GetRandomWormholeMusic(1)
                    if pWormholeMusicSelection <= 33:
                        # Start a nice piece of music
                        import DynamicMusic
                        App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusic" + ".mp3", "WormholeMusic", 2.0)
                        DynamicMusic.dsMusicTypes["WormholeMusic"] = "WormholeMusic"
                        DynamicMusic.OverrideMusic("WormholeMusic")
                    elif pWormholeMusicSelection > 33:
                        # Start a nice piece of music
                        import DynamicMusic
                        App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusicAlternate" + ".mp3", "WormholeMusicAlternate", 2.0)
                        DynamicMusic.dsMusicTypes["WormholeMusicAlternate"] = "WormholeMusicAlternate"
                        DynamicMusic.OverrideMusic("WormholeMusicAlternate")
                
            
            # Bugfix insert when not in DS9 Set delete random attack timer
            DeleteRandomAttackTimer(None, None)

            # Start a timer which will every few seconds check players distance from the wormhole, delayed for a few secs due to some bugs
            InsideWormholeTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".InsideWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 15)


        else:
            # MLeo EDIT: When the interface hasn't been loaded yet, call the next handler and exit
            if not bExitToGamma or not bExitToDS9 or not bDockToDS9:
		# Sov Edit Note: this caused an error in KM 1.0
                try:
                    pObject.CallNextHandler(pEvent)
                except:
                    pass
		return
                
            # Else just disable all buttons	
            bExitToGamma.SetDisabled()
            bExitToDS9.SetDisabled()
            bEnter.SetDisabled()
            if bHail == None:
                pass

            else:
                bHail.SetDisabled()

            if bCloseChannel == None:
                pass

            else:
                bCloseChannel.SetDisabled()
                
            # Dock button doesn't have to exist
            if bDockToDS9 == None:
                pass

            else:
                bDockToDS9.SetDisabled()

# Moving all ships to players set. We compromise manually for users :P I hate that but hey I cannot leave it like it was (it was crap).
def MoveShipsFromObsoleteSets(pAction = None):
        # Grab some values
	debug(__name__ + ", MoveShipsFromObsoleteSets")
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pPlayer.GetContainingSet()

	# Grab obsolete sets
        DS9 = App.g_kSetManager.GetSet("DeepSpace91Obsolete")
        Gamma = App.g_kSetManager.GetSet("GammaQuadrant1Obsolete")
        Wormhole = App.g_kSetManager.GetSet("BajoranWormhole1Obsolete")

	# This will work for DS9 Set
        if (pSet.GetName() == "DeepSpace91"):

            if DS9:

                for kShip in DS9.GetClassObjectList(App.CT_SHIP): 
                    DS9.RemoveObjectFromSet(kShip.GetName()) 
                    pSet.AddObjectToSet(kShip, kShip.GetName())


        # Theoretically it should work for this system also. Further testing will be required
        elif (pSet.GetName() == "GammaQuadrant1"):

            if Gamma:
            
                for kShip in Gamma.GetClassObjectList(App.CT_SHIP): 
                    Gamma.RemoveObjectFromSet(kShip.GetName()) 
                    pSet.AddObjectToSet(kShip, kShip.GetName())



        # Theoretically it should work for this system also. Further testing will be required
        elif (pSet.GetName() == "BajoranWormhole1"):

            if Wormhole:

                for kShip in Wormhole.GetClassObjectList(App.CT_SHIP): 
                    Wormhole.RemoveObjectFromSet(kShip.GetName()) 
                    pSet.AddObjectToSet(kShip, kShip.GetName())
            


        else:
            return
        

# Now we terminate these sets we're not using
def TerminateObsoleteSets(pAction = None):

	# Grab all obsolete sets
        debug(__name__ + ", TerminateObsoleteSets")
        DS9 = App.g_kSetManager.GetSet("DeepSpace91Obsolete")
        Gamma = App.g_kSetManager.GetSet("GammaQuadrant1Obsolete")
        Wormhole = App.g_kSetManager.GetSet("BajoranWormhole1Obsolete")

        # If some sets were initialized then just delete them
        if DS9:

                App.g_kSetManager.DeleteSet("DeepSpace91Obsolete")

        # A possible bug in the future is that the game might crash if we destroy a set which had some ships in it
        # Keeping an eye out for testing reports
        if Gamma:

                App.g_kSetManager.DeleteSet("GammaQuadrant1Obsolete")

        # A possible bug in the future is that the game might crash if we destroy a set which had some ships in it
        # Keeping an eye out for testing reports
        if Wormhole:

                App.g_kSetManager.DeleteSet("BajoranWormhole1Obsolete")


                

# Sometimes in BC the best thing to do is do it manually, oh well... Kinda sucks but the best alternative :P
def ManualShipCleanup(pObject, pEvent):
        # As always we're grabbing the values that we need
        debug(__name__ + ", ManualShipCleanup")
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()

	# Possible bugfix
        PlayerName = pPlayer.GetName()
        
        if (pSet.GetName() == "DeepSpace91"):
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            # Added in support for all ships in the map
            try:
                for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                    if (kShip.GetName() == PlayerName):
                        continue            
                    pSet.RemoveObjectFromSet(kShip.GetName())
                    

            except:
                        pass

        elif (pSet.GetName() == "GammaQuadrant1"):
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            # Added in support for all ships in the map
            try:
                for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                    if (kShip.GetName() == PlayerName):
                        continue            
                    pSet.RemoveObjectFromSet(kShip.GetName())
                    

            except:
                        pass

        elif (pSet.GetName() == "BajoranWormhole1"):
            # This tends to cause crash to some people so 1st try to remove objects that are system specific and reload them later on
            # Added in support for all ships in the map
            try:
                for kShip in pSet.GetClassObjectList(App.CT_SHIP):
                    if (kShip.GetName() == PlayerName):
                        continue            
                    pSet.RemoveObjectFromSet(kShip.GetName())
                    

            except:
                        pass

        else:
            return


# Limit set renaming only to our systems that DS9FX uses
def RenameSets(pObject, pEvent):
        debug(__name__ + ", RenameSets")
        DS9 = App.g_kSetManager.GetSet("DeepSpace91")
        Gamma = App.g_kSetManager.GetSet("GammaQuadrant1")
        Wormhole = App.g_kSetManager.GetSet("BajoranWormhole1")

        if DS9:
            DS9Name = DS9.GetName() + "Obsolete"
            DS9.SetName(DS9Name)

            # print "DS9FX: System 1 renamed"

        if Gamma:
            GammaName = Gamma.GetName() + "Obsolete"
            Gamma.SetName(GammaName)

            # print "DS9FX: System 2 renamed"

        if Wormhole:
            WormholeName = Wormhole.GetName() + "Obsolete"
            Wormhole.SetName(WormholeName)

            # print "DS9FX: System 3 renamed"


def MovePlayer(pObject, pEvent):        
        # As always we're grabbing the values that we need
        debug(__name__ + ", MovePlayer")
        pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()


        if (pSet.GetName() == "DeepSpace91Obsolete"):
            # Get the set
            DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
        
            # Initialize the set
            DS9SetInitialize = DS9.Initialize()
        
            # Get set's name directly from the set file
            DS9Set = DS9.GetSet()

            for kShip in pSet.GetClassObjectList(App.CT_SHIP): 
		pSet.RemoveObjectFromSet(kShip.GetName()) 
		DS9Set.AddObjectToSet(kShip, kShip.GetName())
            

        elif (pSet.GetName() == "GammaQuadrant1Obsolete"):

            # Get the Gamma Quadrant set's name directly from the set file
            Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")

            GammaInitialize = Gamma.Initialize()
            
            GammaSet = Gamma.GetSet()

            for kShip in pSet.GetClassObjectList(App.CT_SHIP): 
		pSet.RemoveObjectFromSet(kShip.GetName()) 
		GammaSet.AddObjectToSet(kShip, kShip.GetName())
            


        elif (pSet.GetName() == "BajoranWormhole1Obsolete"):

            # Get the wormhole set
            Wormhole = __import__("Systems.BajoranWormhole.BajoranWormhole1")
        
            # Initialize the set
            WormholeSetInitialize = Wormhole.Initialize()
        
            # Get set's name directly from the wormhole
            WormholeSet = Wormhole.GetSet()

            for kShip in pSet.GetClassObjectList(App.CT_SHIP): 
		pSet.RemoveObjectFromSet(kShip.GetName()) 
		WormholeSet.AddObjectToSet(kShip, kShip.GetName())
            


        else:
            return

# Seperate distance checks for each function, to prevent game's confusion as I used to get a bit of a weird behaviour  
def DistanceCheck(pObject):
	debug(__name__ + ", DistanceCheck")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()


# Seperate distance checks for each function, to prevent game's confusion as I used to get a bit of a weird behaviour  
def DS9DistanceCheck(pObject):
	debug(__name__ + ", DS9DistanceCheck")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()



# Distance check so we can determine if we can actually engage Wormhole Travel Option or if we can activate some sequences, a very important function in this script
def PlayerScaleWormholeDistance(pObject):
        debug(__name__ + ", PlayerScaleWormholeDistance")
        pPlayer = App.Game_GetCurrentGame().GetPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()


# Distance check which is used in Bajoran Wormhole System, it sometimes can (when using one of inside wormhole options) return an attribute error so we compromise
def InsideWormholePlayerWormholeDistance(pObject):
    
        debug(__name__ + ", InsideWormholePlayerWormholeDistance")
        pPlayer = App.Game_GetCurrentGame().GetPlayer()
        # Try to get the value
	try:
            vDifference = pObject.GetWorldLocation()

        # Problems showed up, we compromise and 'trick' the game
	except:
            return 10
        
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()
        

# QBR menu fix, a standard
def RemoveDS9FXMenu():
        debug(__name__ + ", RemoveDS9FXMenu")
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/DS9FXMenuString.tgl")
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pHelm	= App.CharacterClass_GetObject(pBridge, "Helm")
        pHelmMenu = g_pHelm.GetMenu()
	if (pHelmMenu != None):
		pButton = pHelmMenu.GetSubmenu("DS9FX")
		if (pButton != None):
			pHelmMenu.DeleteChild(pButton)


# Let's remove DS9 Set Warp Menu, I have no freakin' choice
def RemoveDeepSpace9Menu():
        debug(__name__ + ", RemoveDeepSpace9Menu")
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/DS9FXMenuString.tgl")
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pHelm	= App.CharacterClass_GetObject(pBridge, "Helm")
        pHelmMenu = g_pHelm.GetMenu()
	if (pHelmMenu != None):
                pSetCourse = pHelmMenu.GetSubmenuW(g_pDatabase.GetString("Set Course"))
                if pSetCourse:
                    pButton = pSetCourse.GetSubmenu("DeepSpace9")
                    if (pButton != None):
                            pSetCourse.DeleteChild(pButton)
    	    

# New code which is much more cleaner and more effective
def TransferShips(pObject, pEvent):
        debug(__name__ + ", TransferShips")
        global InsideWormholeTimer
        global Dummy, pPlayer

        Timer = DS9Timer

        # Let's hack in the game and delete simply all active timers that are 'signed' in DS9FX Lib
        DeleteAllDS9FXTimers()
        

        # Get the wormhole set
        Wormhole = __import__("Systems.BajoranWormhole.BajoranWormhole1")
        
        # Initialize the set
        WormholeSetInitialize = Wormhole.Initialize()
        
        # Get set's name directly from the wormhole
        WormholeSet = Wormhole.GetSet()

        # Grab some values
        pPlayer = App.Game_GetCurrentPlayer()
	if not pPlayer:
		return 0
	
	pSet = pPlayer.GetContainingSet()

	pPlayerPosition = pPlayer.GetWorldLocation()

	# Define dummy, used as a major bugfix thanks to Aragorn for noticing that this fix has a critical effect over one major bug in the mod	
        Dummy = "Dummy"
                
        CreateDummy = loadspacehelper.CreateShip("DS9FXDummy", pSet, Dummy, None)
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName(Dummy)

        # Disable collisions the original player and make the ship invincible
        GetDummy = MissionLib.GetShip(Dummy, pSet)
        GetDummy.SetInvincible(1)
        GetDummy.SetHurtable(0)
        GetDummy.EnableCollisionsWith(pPlayer, 0)

        GetDummy.SetTranslate(pPlayerPosition)
        GetDummy.UpdateNodeOnly()

        # Set the new temporary player
        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(GetDummy)

        # print "DS9FX: Setting up a dummy ship!"
                
        # Stop the player 
        import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

        # Now remove DS9 (Gamma) set ships, of course try to delete them
        try:
            pSet.RemoveObjectFromSet("Bajoran Wormhole")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("USS Excalibur")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("Deep_Space_9")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("USS Defiant")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("USS Oregon")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("USS_Lakota")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("Bugship 1")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("Bugship 2")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("Bugship 3")
        except:
            pass
        try:
            # Remove the dummy wormhole object also
            pSet.RemoveObjectFromSet("Bajoran Wormhole Dummy")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("Comet Alpha")
        except:
            pass
            


        # Now transfer ships that are in the set to the Bajoran Wormhole set
	for kShip in pSet.GetClassObjectList(App.CT_SHIP): 
		pSet.RemoveObjectFromSet(kShip.GetName()) 
		WormholeSet.AddObjectToSet(kShip, kShip.GetName())
		            
                # Get location of the player
		pLocation = pPlayer.GetWorldLocation() 

                # New way to choose new location
                kShipX = pLocation.GetX()
                
                kShipY = pLocation.GetY()
                
                kShipZ = pLocation.GetZ()

                RateX = GetRandomRate(1)

                RateY = GetRandomRate(1)

                RateZ = GetRandomRate(1)

                pXCoord = kShipX + RateX

                pYCoord = kShipY + RateY

                pZCoord = kShipZ + RateZ

                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                kShip.UpdateNodeOnly() 


                # Update proximity manager info
                ProximityManager = WormholeSet.GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(kShip) 


        # Load placements
        from Custom.DS9FX.DS9FXObjects import WormholeObjects

        WormholeObjects.WormholeSetObjects()


        # Grab the wormhole model
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet)
        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)

        # Position the wormhole so that it appears you're inside the wormhole
        pPlayerBackward = pPlayer.GetWorldBackwardTG()
        pPlayerDown = pPlayer.GetWorldDownTG()
        pPlayerPosition = pPlayer.GetWorldLocation()

        pDS9FXWormhole.AlignToVectors(pPlayerBackward, pPlayerDown)
        pDS9FXWormhole.SetTranslate(pPlayerPosition)
        pDS9FXWormhole.UpdateNodeOnly()

        pDS9FXWormhole2.AlignToVectors(pPlayerBackward, pPlayerDown)
        pDS9FXWormhole2.SetTranslate(pPlayerPosition)
        pDS9FXWormhole2.UpdateNodeOnly()

        # Disable player collision with the cone
        pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)
        pDS9FXWormhole2.EnableCollisionsWith(pPlayer, 0)

        # Disable any ship collisions with the cone
        for kShip in WormholeSet.GetClassObjectList(App.CT_SHIP):
            pShip = App.ShipClass_GetObject(WormholeSet, kShip.GetName())
            pDS9FXWormhole.EnableCollisionsWith(pShip, 0)
            pDS9FXWormhole2.EnableCollisionsWith(pShip, 0)

        # Bugfix insert clear AI
        pPlayer.ClearAI()

        # Move the player forward
        import Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExitWormholeAI.CreateAI(PlayerCast))


        # Disable warp button
        DisableWarpButton()

        if pWormholeMusic == 1:    	
                # Start a nice piece of music
                import DynamicMusic
                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusic" + ".mp3", "WormholeMusic", 2.0)
                DynamicMusic.StopOverridingMusic()
                DynamicMusic.dsMusicTypes["WormholeMusic"] = "WormholeMusic"
                DynamicMusic.OverrideMusic("WormholeMusic")

        elif pWormholeMusic == 2:
                # Start a nice piece of music
                import DynamicMusic
                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusicAlternate" + ".mp3", "WormholeMusicAlternate", 2.0)
                DynamicMusic.dsMusicTypes["WormholeMusicAlternate"] = "WormholeMusicAlternate"
                DynamicMusic.OverrideMusic("WormholeMusicAlternate")

        elif pWormholeMusic == 3:
                    pWormholeMusicSelection = GetRandomWormholeMusic(1)
                    if pWormholeMusicSelection <= 33:
                        # Start a nice piece of music
                        import DynamicMusic
                        App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusic" + ".mp3", "WormholeMusic", 2.0)
                        DynamicMusic.dsMusicTypes["WormholeMusic"] = "WormholeMusic"
                        DynamicMusic.OverrideMusic("WormholeMusic")
                    elif pWormholeMusicSelection > 33:
                        # Start a nice piece of music
                        import DynamicMusic
                        App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "WormholeMusicAlternate" + ".mp3", "WormholeMusicAlternate", 2.0)
                        DynamicMusic.dsMusicTypes["WormholeMusicAlternate"] = "WormholeMusicAlternate"
                        DynamicMusic.OverrideMusic("WormholeMusicAlternate")

        
        # Removing ability of the player to make any input
        RemoveKeyboardControl()
        # Start a new cutscene view, chase cam seems as a perfect choice
        pSequence = App.TGSequence_Create ()
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
        pSequence.AppendAction (App.TGScriptAction_Create("MissionLib", "StartCutscene"))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pPlayer.GetContainingSet().GetName ()))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChaseCam", pPlayer.GetContainingSet().GetName(), pPlayer.GetName ()))
        pSequence.Play()

        # Purge memory when transfering between sets
        App.g_kLODModelManager.Purge()
        
        # Bugfix insert when not in DS9 Set delete random attack timer
        DeleteRandomAttackTimer(None, None)

        # Start a timer which will delete the dummy ship and reset engineering menu, works as a support to detachcrewmenus def
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteDummy", App.g_kUtopiaModule.GetGameTime() + 25, 0, 0)

        if Timer == 30:
            # Add a 30 second timer
            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnterSeq3", App.g_kUtopiaModule.GetGameTime() + Timer, 0, 0)

        else:
            ReturnKeyboardControl()
            
        # Start a timer which will every few seconds check players distance from the wormhole and move it 
        InsideWormholeTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".InsideWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 45)



# New code which is much more cleaner and more effective
def TransferShips2(pObject, pEvent):
        debug(__name__ + ", TransferShips2")
        global RandomEnemyFleet, RandomAttackTimer
        global Dummy, pPlayer
        global ScaleWormholePrevention

        # I think that this will hopefully fix the wormhole non closing issue
        ScaleWormholePrevention = 1
        
        # Let's hack in the game and delete simply all active timers that are 'signed' in DS9FX Lib
        DeleteAllDS9FXTimers()
        
        # Get the set
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
        
        # Initialize the set
        DS9SetInitialize = DS9.Initialize()
        
        # Get set's name directly from the set file
        DS9Set = DS9.GetSet()
        
        # Grab some values
        pPlayer = App.Game_GetCurrentPlayer()    	
	if not pPlayer:
		return 0
	
	pSet = pPlayer.GetContainingSet()

        pPlayerPosition = pPlayer.GetWorldLocation()
        
        # Define dummy, used as a major bugfix thanks to Aragorn for noticing that this fix has a critical effect over one major bug in the mod
        Dummy = "Dummy"
                
        CreateDummy = loadspacehelper.CreateShip("DS9FXDummy", pSet, Dummy, None)
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName(Dummy)

        # Disable collisions the original player and make the ship invincible
        GetDummy = MissionLib.GetShip(Dummy, pSet)
        GetDummy.SetInvincible(1)
        GetDummy.SetHurtable(0)
        GetDummy.EnableCollisionsWith(pPlayer, 0)

        GetDummy.SetTranslate(pPlayerPosition)
        GetDummy.UpdateNodeOnly()

        # print "DS9FX: Setting up a dummy ship!"

      
        # Now remove Wormhole Set Objects, of course try to remove them
        try:
            pSet.RemoveObjectFromSet("Bajoran Wormhole Outer")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("Bajoran Wormhole Inner")
        except:
            pass

        # Now transfer ships that are in the set to the DS9 set
	for kShip in pSet.GetClassObjectList(App.CT_SHIP): 
		pSet.RemoveObjectFromSet(kShip.GetName()) 
		DS9Set.AddObjectToSet(kShip, kShip.GetName())

                # Get location of the player
		pLocation = pPlayer.GetWorldLocation() 

                # New way to choose new location
                kShipX = pLocation.GetX()
                
                kShipY = pLocation.GetY()
                
                kShipZ = pLocation.GetZ()

                RateX = GetRandomRate(1)

                RateY = GetRandomRate(1)

                RateZ = GetRandomRate(1)

                pXCoord = kShipX + RateX

                pYCoord = kShipY + RateY

                pZCoord = kShipZ + RateZ

                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                kShip.UpdateNodeOnly() 


                # Update proximity manager info
                ProximityManager = DS9Set.GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(kShip)


        # Call in the file which holds info about the wormhole and other objects, if there are any available
        from Custom.DS9FX.DS9FXObjects import DS9Objects
            
        DS9Objects.DS9SetObjects()

        # Call in the file which holds info about stations
        from Custom.DS9FX.DS9FXObjects import DS9Stations

        DS9Stations.DS9SetStations()

        # Call in the file which holds info about ships in DS9 set
        from Custom.DS9FX.DS9FXObjects import DS9Ships

        DS9Ships.DS9SetShips()

        # Set the new temporary player
        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(GetDummy)
                
        # Stop the player 
        import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

        # Grab the wormhole model
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set)

        # Disable collisions with player and the Wormhole
        pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)

        # Disable any ship collisions with the wormhole
        for kShip in DS9Set.GetClassObjectList(App.CT_SHIP):
            pShip = App.ShipClass_GetObject(DS9Set, kShip.GetName())                
            pDS9FXWormhole.EnableCollisionsWith(pShip, 0)

        
	# Get the exit location placement from the file and translate player over there, other ships need to be far away.
	# If they're not, then we do have a major issue, of ships randomly crashing into each other. It's just not safe!
        pWormholePlacement = App.PlacementObject_GetObject(DS9Set, "ExitPoint Location")               
        pPlayer.SetTranslate(pWormholePlacement.GetWorldLocation())
        pPlayer.SetMatrixRotation(pWormholePlacement.GetWorldRotation())                
                
        pPlayer.UpdateNodeOnly() 

        # Reenable warp button
        RestoreWarpButton()

        if pDS9Music == 1:            
                # Start a nice piece of music
                import DynamicMusic
                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music" + ".mp3", "DS9Music", 2.0)
                DynamicMusic.StopOverridingMusic()
                DynamicMusic.dsMusicTypes["DS9Music"] = "DS9Music"
                DynamicMusic.OverrideMusic("DS9Music")

        elif pDS9Music == 2:
                # Start a nice piece of music
                import DynamicMusic
                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9MusicAlternate" + ".mp3", "DS9MusicAlternate", 2.0)
                DynamicMusic.dsMusicTypes["DS9MusicAlternate"] = "DS9MusicAlternate"
                DynamicMusic.OverrideMusic("DS9MusicAlternate")

        elif pDS9Music == 3:
                    # Start a nice piece of music
                    import DynamicMusic
                    App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music2" + ".mp3", "DS9Music2", 2.0)
                    DynamicMusic.dsMusicTypes["DS9Music2"] = "DS9Music2"
                    DynamicMusic.OverrideMusic("DS9Music2")

        elif pDS9Music == 4:
                    # Do a random music selection, by choosing a random number
                    pDS9MusicSelection = GetRandomDS9Music(1)
                    if pDS9MusicSelection <= 33:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music" + ".mp3", "DS9Music", 2.0)
                                DynamicMusic.dsMusicTypes["DS9Music"] = "DS9Music"
                                DynamicMusic.OverrideMusic("DS9Music")

                    elif pDS9MusicSelection <= 66 and pDS9MusicSelection > 33:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9MusicAlternate" + ".mp3", "DS9MusicAlternate", 2.0)
                                DynamicMusic.dsMusicTypes["DS9MusicAlternate"] = "DS9MusicAlternate"
                                DynamicMusic.OverrideMusic("DS9MusicAlternate")

                    elif pDS9MusicSelection > 66:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "DS9Music2" + ".mp3", "DS9Music2", 2.0)
                                DynamicMusic.dsMusicTypes["DS9Music2"] = "DS9Music2"
                                DynamicMusic.OverrideMusic("DS9Music2")
                                

        if pRandomEnemyFleetAttacks == 1:
                # Start counting until the enemy fleet arrives
                RandomAttackTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnemyFleetArrives", App.g_kUtopiaModule.GetGameTime() + RandomEnemyFleet)
                        
                # print "DS9FX: Starting Random Enemy Fleet Attack Countdown!"

        # Purge memory when transfering between sets
        App.g_kLODModelManager.Purge()

        # Set the wormholes scale to 4 for us to be able to reduce it
        pDS9FXWormhole.SetScale(ExitingScale)
        pDS9FXWormhole.SetHidden(0)

        # Multiple attempts to delete the timer are recommended in such large scale mods
        StopScaleWormhole(None, None)

        # Call in Exiting Sequence
        ExitToDS9Seq3(None, None)


        # Start a timer which will delete the dummy ship and reset engineering menu, works as a support to detachcrewmenus def
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteDummy", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
    


# New code which is much more cleaner and more effective
def TransferShips3(pObject, pEvent):
        debug(__name__ + ", TransferShips3")
        global Dummy, pPlayer
        global ScaleWormholePrevention

        # I think that this will hopefully fix the wormhole non closing issue
        ScaleWormholePrevention = 1

        # Let's hack in the game and delete simply all active timers that are 'signed' in DS9FX Lib
        DeleteAllDS9FXTimers()

        # Get the set
        Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
        
        # Initialize the set
        GammaSetInitialize = Gamma.Initialize()
        
        # Get set's name directly from the set file
        GammaSet = Gamma.GetSet()
        
        
        # Grab some values
        pPlayer = App.Game_GetCurrentPlayer()    	
	if not pPlayer:
		return 0
	
	pSet = pPlayer.GetContainingSet()

	pPlayerPosition = pPlayer.GetWorldLocation()

	# Define dummy, used as a major bugfix thanks to Aragorn for noticing that this fix has a critical effect over one major bug in the mod	
        Dummy = "Dummy"
                
        CreateDummy = loadspacehelper.CreateShip("DS9FXDummy", pSet, Dummy, None)
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pMission.GetFriendlyGroup().AddName(Dummy)

        # Disable collisions the original player and make the ship invincible
        GetDummy = MissionLib.GetShip(Dummy, pSet)
        GetDummy.SetInvincible(1)
        GetDummy.SetHurtable(0)
        GetDummy.EnableCollisionsWith(pPlayer, 0)

        GetDummy.SetTranslate(pPlayerPosition)
        GetDummy.UpdateNodeOnly()

        # Set the new temporary player
        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(GetDummy)

        # print "DS9FX: Setting up a dummy ship!"
    
            

        # Now remove Wormhole Set Objects, of course try to remove them
        try:
            pSet.RemoveObjectFromSet("Bajoran Wormhole Outer")
        except:
            pass
        try:
            pSet.RemoveObjectFromSet("Bajoran Wormhole Inner")
        except:
            pass

        # Now transfer ships that are in the set to the Gamma set
	for kShip in pSet.GetClassObjectList(App.CT_SHIP): 
		pSet.RemoveObjectFromSet(kShip.GetName()) 
		GammaSet.AddObjectToSet(kShip, kShip.GetName())

                # Get location of the player
		pLocation = pPlayer.GetWorldLocation() 

                # New way to choose new location
                kShipX = pLocation.GetX()
                
                kShipY = pLocation.GetY()
                
                kShipZ = pLocation.GetZ()

                RateX = GetRandomRate(1)

                RateY = GetRandomRate(1)

                RateZ = GetRandomRate(1)

                pXCoord = kShipX + RateX

                pYCoord = kShipY + RateY

                pZCoord = kShipZ + RateZ

                kShip.SetTranslateXYZ(pXCoord, pYCoord, pZCoord)

                kShip.UpdateNodeOnly() 


                # Update proximity manager info
                ProximityManager = GammaSet.GetProximityManager() 
                if (ProximityManager): 
                        ProximityManager.UpdateObject(kShip)


        # Load Gamma Quadrant Objects
        from Custom.DS9FX.DS9FXObjects import GammaObjects

        GammaObjects.GammsSetObjects()
            
        # Load Gamma Quadrant ships 
        from Custom.DS9FX.DS9FXObjects import GammaShips

        GammaShips.GammaSetShips()

                
        # Stop the player 
        import Custom.DS9FX.DS9FXAILib.DS9FXStayAI
        PlayerCast = App.ShipClass_Cast(pPlayer)
        PlayerCast.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXStayAI.CreateAI(PlayerCast))

        # Grab the wormhole model
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet)

        # Disable collisions with player and the Wormhole
        pDS9FXWormhole.EnableCollisionsWith(pPlayer, 0)

        # Disable any ship collisions with the wormhole
        for kShip in GammaSet.GetClassObjectList(App.CT_SHIP):
            pShip = App.ShipClass_GetObject(GammaSet, kShip.GetName())                
            pDS9FXWormhole.EnableCollisionsWith(pShip, 0)

        
	# Get the exit location placement from the file and translate player over there, other ships need to be far away.
	# If they're not, then we do have a major issue, of ships randomly crashing into each other. It's just not safe!
        pWormholePlacement = App.PlacementObject_GetObject(GammaSet, "ExitPoint Location")               
        pPlayer.SetTranslate(pWormholePlacement.GetWorldLocation())
        pPlayer.SetMatrixRotation(pWormholePlacement.GetWorldRotation())                
                
        pPlayer.UpdateNodeOnly() 

        
        # Grab the ship that has antiproton scan ability
        APShip = MissionLib.GetShip("Bugship 1", GammaSet)
        APShip2 = MissionLib.GetShip("Bugship 2", GammaSet)
        APShip3 = MissionLib.GetShip("Bugship 2", GammaSet)

        if pDomIS == 1:
                # If this ship exists initiate antiprotonscan
                if APShip:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                elif APShip2:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                elif APShip3:
                        # Initiate Antiproton scanning
                        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)


        # Disable warp button
        DisableWarpButton()


        if pGammaMusic == 1:
            
                # Start a nice piece of music
                import DynamicMusic
                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusic" + ".mp3", "GammaMusic", 2.0)
                DynamicMusic.StopOverridingMusic()
                DynamicMusic.dsMusicTypes["GammaMusic"] = "GammaMusic"
                DynamicMusic.OverrideMusic("GammaMusic")

        elif pGammaMusic == 2:
                # Start a nice piece of music
                import DynamicMusic
                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusicAlternate" + ".mp3", "GammaMusicAlternate", 2.0)
                DynamicMusic.dsMusicTypes["GammaMusicAlternate"] = "GammaMusicAlternate"
                DynamicMusic.OverrideMusic("GammaMusicAlternate")
                    

        elif pGammaMusic == 3:
                # Do a random music selection, by choosing a random number
                pGammaMusicSelection = GetRandomGammaMusic(1)
                if pGammaMusicSelection <= 33:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusic" + ".mp3", "GammaMusic", 2.0)
                                DynamicMusic.dsMusicTypes["GammaMusic"] = "GammaMusic"
                                DynamicMusic.OverrideMusic("GammaMusic")

                elif pGammaMusicSelection > 33:
                                # Start a nice piece of music
                                import DynamicMusic
                                App.g_kMusicManager.LoadMusic("sfx/Custom/DS9FX/" + "GammaMusicAlternate" + ".mp3", "GammaMusicAlternate", 2.0)
                                DynamicMusic.dsMusicTypes["GammaMusicAlternate"] = "GammaMusicAlternate"
                                DynamicMusic.OverrideMusic("GammaMusicAlternate")

        # Purge memory when transfering between sets
        App.g_kLODModelManager.Purge()

        # Set the wormholes scale to 4 for us to be able to reduce it
        pDS9FXWormhole.SetScale(ExitingScale)
        pDS9FXWormhole.SetHidden(0)
        
        # Bugfix insert when not in DS9 Set delete random attack timer
        DeleteRandomAttackTimer(None, None)

        # Multiple attempts to delete the timer are recommended in such large scale mods
        StopScaleWormhole(None, None)
        

        # Call in Exiting Sequence
        ExitToGammaSeq3(None, None)


        # Start a timer which will delete the dummy ship and reset engineering menu, works as a support to detachcrewmenus def
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteDummy", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
 
        


# We do a distance check in order to determine when to translate inside wormhole graphics cone to match the players position
def InsideWormholeDistanceCheck(pObject, pEvent):
        debug(__name__ + ", InsideWormholeDistanceCheck")
        global InsideWormholeTimer
        
        # Grab some values
        pPlayer = App.Game_GetCurrentPlayer()    	
	if not pPlayer:
		return 0
	
	pSet = pPlayer.GetContainingSet()

        # Get the wormhole set
        Wormhole = __import__("Systems.BajoranWormhole.BajoranWormhole1")

        # Get set's name directly from the wormhole
        WormholeSet = Wormhole.GetSet()

        # Grab the wormhole model
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet)
        pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
        
        # Kill the timer if we are not in the Bajoran Wormhole map also
        if not (pSet.GetName() == "BajoranWormhole1"):
                KillInsideWormholeTimer(None, None)

        # Do a distance check between the cone and the player
        if InsideWormholePlayerWormholeDistance(pDS9FXWormhole) > 1500:
                TranslateWormholeCone(pDS9FXWormhole)
                TranslateWormholeCone(pDS9FXWormhole2)

        # Repeat the timer also
        InsideWormholeTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".InsideWormholeDistanceCheck", App.g_kUtopiaModule.GetGameTime() + 10)




# Translate the wormhole cone to match the player's position
def TranslateWormholeCone(pShip):
        debug(__name__ + ", TranslateWormholeCone")
        pPlayer = App.Game_GetCurrentPlayer() 

        pPlayerPosition = pPlayer.GetWorldLocation()

        # Move the desired object
	pShip.SetTranslate(pPlayerPosition)

        pShip.UpdateNodeOnly()



# Kill the timer if we are not in this damned set
def KillInsideWormholeTimer(pObject, pEvent):
        debug(__name__ + ", KillInsideWormholeTimer")
        global InsideWormholeTimer

        # Just simply delete the timer, that's all
        try:
                    App.g_kTimerManager.DeleteTimer(InsideWormholeTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(InsideWormholeTimer.GetObjID())
                    # InsideWormholeTimer = None
        except:
                    pass



# Over here we scale the wormhole and manipulate it's size		
def ScaleWormhole(pObject, pEvent):
        debug(__name__ + ", ScaleWormhole")
        global Scale, ScaleTimer
        global ScaleWormholePrevention

        # To prevent problems that may show up we just simply call one more time ScaleDistanceTimerDelete def, just to be safe
        ScaleDistanceTimerDelete(None, None)

        # This function seems to be recalled over and over, I keep trying to destroy the timer based event but it's still ever present. 
        # So a small workaround, when we're exiting the wormhole this function will not be able to initiate because we're preventing it to do so. 
        if ScaleWormholePrevention == 1:
            # print "DS9FX: Preventing unathorized wormhole scalling..."
            return

        # Get the player
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
        Scale = Scale + 0.015

        # Wormhole may or may not be here
        try:
            pDS9FXWormhole.SetScale(Scale)

        # If we get an attribute error just delete the timer
        except AttributeError:
            StopScaleWormhole(None, None)

        # We don't want to overgrow the Wormhole
        if Scale >= 4:
            StopScaleWormhole(None, None)

        else:
            # A timer which calls itself repeatedly
            ScaleTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".ScaleWormhole", App.g_kUtopiaModule.GetGameTime() + 0.05)




# Over here we delete the timer and reset the scale
def StopScaleWormhole(pObject, pEvent):
        debug(__name__ + ", StopScaleWormhole")
        global Scale, ScaleTimer

        # First thing is first delete the ScaleTimer
        try:
                    App.g_kTimerManager.DeleteTimer(ScaleTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(ScaleTimer.GetObjID())
                    ScaleTimer = None
        except:
                    pass

        # Scale value is returned to its original value 
        Scale = 0



# Deactivate DynamicMusic Overriding using ET_WARP_BUTTON_PRESSED Handler
def MusicListener(pObject, pEvent):
        # Grab some values
        debug(__name__ + ", MusicListener")
        pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	# We tag along in this function, since the comet alpha can cause some very weird issue we'll remove it from the set if we are it DS9 Set
	# This function is perfect
	pPlayer = App.Game_GetCurrentPlayer()    
        pSet = pPlayer.GetContainingSet()

        # Make an attempt in deleting the comet of course
        if (pSet.GetName() == "DeepSpace91"):
            try:
                
                pSet.RemoveObjectFromSet("Comet Alpha")

            except:
                pass

        # Remove the listener
        App.g_kEventManager.RemoveBroadcastHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".MusicListener")

        # Stop Overriding music
        import DynamicMusic
        DynamicMusic.StopOverridingMusic()

        # Reactivate the listener again
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WARP_BUTTON_PRESSED, pMission, __name__ + ".MusicListener")
    



# AI antiproton scan def, heavily stripped to add simplicity to the script. 80% success ratio
def AntiprotonScan(pObject, pEvent):
                # Grab the gamma set directly from the system file
                debug(__name__ + ", AntiprotonScan")
                Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")   
                GammaSet = Gamma.GetSet()
    
                # Predefined values
                PlayerSelection = 5
                PredefinedValue = 1

                # If the randomly selected value is greater than PlayerSelection then we try to assign a firepoint onto a friendly ship
                if GetRandomRate(PredefinedValue) > PlayerSelection:
                            # Grab some values
                            pGame = App.Game_GetCurrentGame()
                            pEpisode = pGame.GetCurrentEpisode()
                            pMission = pEpisode.GetCurrentMission()
                            pPlayer = MissionLib.GetPlayer()
                            pSet = GammaSet
                            pFriendlies = pMission.GetFriendlyGroup()
                            lpFriendlies = pFriendlies.GetActiveObjectTupleInSet(pSet)
                            # Now we'll try to attach a firepoint onto a friendly ship
                            for pFriendlies in lpFriendlies:
                                    APChance = App.g_kSystemWrapper.GetRandomNumber(99) + 1
                                    pTargetattr	= App.ShipClass_Cast(pFriendlies)
                                    if (pTargetattr.IsCloaked()):
                                                if (APChance < 80):
                                                        BuildFirepoint(pTargetattr)
                                                                    
                                    else:
                                            pass

                # Now if the value is smaller than PlayerSelection value we attach the firepoint onto a player ship. Also 80% success ratio
                else:
                            # Grab some values
                            pPlayer = MissionLib.GetPlayer()
                            APChance = App.g_kSystemWrapper.GetRandomNumber(99) + 1
                            if pPlayer.IsCloaked():
                                if (APChance < 80):
                                    BuildFirepoint(pPlayer)
                                    # Also say the line and warn the player that he's been detected
                                    PlayerDetected()

                            else:
                                pass

                # Grab the system name from the set file
                Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
                GammaSet = Gamma.GetSet()

                # Grab the ship that has antiproton scan ability
                APShip = MissionLib.GetShip("Bugship 1", GammaSet)
                APShip2 = MissionLib.GetShip("Bugship 2", GammaSet)
                APShip3 = MissionLib.GetShip("Bugship 2", GammaSet)

                if pDomIS == 1:
                        # If this ship exists initiate antiprotonscan
                        if APShip:
                                # Initiate Antiproton scanning
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                        elif APShip2:
                                # Initiate Antiproton scanning
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)

                        elif APShip3:
                                # Initiate Antiproton scanning
                                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AntiprotonScan", App.g_kUtopiaModule.GetGameTime() + 60, 0, 0)




# We Build a firepoint over here and after 40 secs delete the firepoint, or sensor anomaly
def BuildFirepoint(pObject):
                debug(__name__ + ", BuildFirepoint")
                global Firepoint, CloakedShipSet, CloakedShipName, FirepointValue, AttachTimer, GetFirepoint
                
                # Grab some values
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                
                # Define firepoint name
                Firepoint = "Sensor Anomaly"
                
                # Get firepoints set
                CloakedShipSet = pObject.GetContainingSet()
                
                # Create firepoint and add it to a friendly group, since it's the enemy who's doing scanning on you.
                # And to 'trick' the AI in order to attack the cloaked ship
                CreateFirepoint = loadspacehelper.CreateShip("Distortion", CloakedShipSet, Firepoint, None)
                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                pMission.GetFriendlyGroup().AddName(Firepoint)
                
                # Disable collisions with it's parent and attach it onto the ship + make it targetable and invincible
                GetFirepoint = MissionLib.GetShip(Firepoint, CloakedShipSet)
                GetFirepoint.SetTargetable(1)
                GetFirepoint.SetInvincible(1)
                GetFirepoint.SetHurtable(0)
                GetFirepoint.EnableCollisionsWith(pObject, 0)
                pObject.AttachObject(GetFirepoint)

                # Ship value
                FirepointValue = pObject

                # Used in handlers for comparison purposes
                CloakedShip = App.ShipClass_Cast(pObject)
                
                # Make sure to reset before remembering the name, the sequence is being recalled all over again. So this saves us time
                CloakedShipName = None
                CloakedShipName = CloakedShip.GetName()

                # Handlers which delete the firepoint if the ship is exploding or starting to decloak       
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING, pMission, __name__ + ".ObjectDecloaking")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")

                # After a certain ammount of time delete the firepoint, 40 seconds to be exact
                MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".DeleteFirepoint", App.g_kUtopiaModule.GetGameTime() + 40, 0, 0)


                # Big bugfix sometimes a firepoint can cause us trouble, big trouble so we'll try to reattach the firepoint onto the ship
                AttachTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AttachFirepoint", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)




# Delete the firepoint, simple. Very simple
def DeleteFirepoint(pObject, pEvent):
        debug(__name__ + ", DeleteFirepoint")
        global Firepoint, CloakedShipSet
        
        try: 
            CloakedShipSet.RemoveObjectFromSet(Firepoint)

        except:
            pass



# We randomize number selection with this little def
def GetRandomRate(Number):
    
        debug(__name__ + ", GetRandomRate")
        return App.g_kSystemWrapper.GetRandomNumber(9) + Number
    


# Compare if the name of the decloaking ship matches the name of the ship which has the firepoint attached on
def ObjectDecloaking(pObject, pEvent):
        debug(__name__ + ", ObjectDecloaking")
        global CloakedShipName, FirepointValue

        # Grab some values
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        # Grab the ship that is decloaking        
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
		return
	    
        ShipName = pShip.GetName()

        # Match the names and if they are the same just kill the firepoint
        if (ShipName == CloakedShipName):
            DeleteFirepoint(None, None)
            FirepointValue.SetTargetable(1)
            
            # Remove the handler which is also later reactivated
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_DECLOAK_BEGINNING, pMission, __name__ + ".ObjectDecloaking")
            


# Similar to object decloaking only we use this def when a ship is exploding
def ObjectExploding(pObject, pEvent):
        debug(__name__ + ", ObjectExploding")
        global CloakedShipName, FirepointValue

        # Grab some values
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()

        # Grab the ship that is exploding        
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if (pShip == None):
		return
	    
        ShipName = pShip.GetName()

        # Match the names and like in the ObjectDecloking kill the firepoint if the names match
        if (ShipName == CloakedShipName):
            DeleteFirepoint(None, None)
            FirepointValue.SetTargetable(1)
            
            # Remove the handler which is also later reactivated
            App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")



# We will just reattach a firepoint onto a cloaked ship, we'll try. The fix seems to work so it's best to leave it. It won't kill your game, I hope at least!
def AttachFirepoint(pObject, pEvent):
        debug(__name__ + ", AttachFirepoint")
        global FirepointValue, AttachTimer, GetFirepoint

        try:
            FirepointValue.AttachObject(GetFirepoint)
            GetFirepoint.SetTargetable(1)
            GetFirepoint.SetInvincible(1)
            GetFirepoint.SetHurtable(0)
            GetFirepoint.EnableCollisionsWith(FirepointValue, 0)
            

        except:
            pass

        # Repeat the timer endlesly, it's not gonna be a problem to any system out there since it's a small background script
        AttachTimer = MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".AttachFirepoint", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)



# Just simply warn the user that he should get in range in order to enter the wormhole
def FelixWarnPrompt(pObject = None, pEvent = None):
                debug(__name__ + ", FelixWarnPrompt")
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
                pSequence = App.TGSequence_Create()
                pSet = App.g_kSetManager.GetSet("bridge")
                pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
                pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "WarnPrompt", None, 0, Database))
                pSequence.Play()
                

# Can't enter the wormhole, impulse are below 50%
def ImpulsePrompt(pObject = None, pEvent = None):
                debug(__name__ + ", ImpulsePrompt")
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
                pSequence = App.TGSequence_Create()
                pSet = App.g_kSetManager.GetSet("bridge")
                pEng = App.CharacterClass_GetObject(pSet, "Engineer")
                pSequence.AppendAction(App.CharacterAction_Create(pEng, App.CharacterAction.AT_SAY_LINE, "Impulse", None, 0, Database))
                pSequence.Play()


# A simple def which will disable a warp button, needed for inside wormhole purposes
def DisableWarpButton():
                debug(__name__ + ", DisableWarpButton")
                Bridge.BridgeUtils.DisableButton(None, "Helm", "Set Course")
        	Bridge.BridgeUtils.DisableWarpButton()
        	


# Opposite of DisableWarpButton def, it restores warp buttons
def RestoreWarpButton():
                debug(__name__ + ", RestoreWarpButton")
                Bridge.BridgeUtils.EnableButton(None, "Helm", "Set Course")
        	Bridge.BridgeUtils.RestoreWarpButton()


# Return random number for coordinate choosing
def GetRandomRate(Number):
    
        debug(__name__ + ", GetRandomRate")
        return App.g_kSystemWrapper.GetRandomNumber(150) + Number


# Over here we'll define what will happen when an enemy fleet arrives
def EnemyFleetArrives(pObject, pEvent):
            debug(__name__ + ", EnemyFleetArrives")
            global RandomEnemyFleet, RandomAttackTimer

            # Get the player
            pPlayer = App.Game_GetCurrentPlayer()    	
            if not pPlayer:
                     return 0
                    
            # Planned bugfix check if the player is in DS9 Set and then initiate the enemy fleet
            pSet = pPlayer.GetContainingSet()
            if (pSet.GetName() == "DeepSpace91"):
                    # Warn the player that the enemy has entered the set
                    pGame = App.Game_GetCurrentGame()
                    pEpisode = pGame.GetCurrentEpisode()
                    pMission = pEpisode.GetCurrentMission()
                    Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
                    pSequence = App.TGSequence_Create()
                    pSet = App.g_kSetManager.GetSet("bridge")
                    pTactical = App.CharacterClass_GetObject(pSet, "Tactical")
                    pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, "EnemiesEnteringTheSet", None, 0, Database))
                    pSequence.Play()

                    # Import all ship locations and that's it            
                    from Custom.DS9FX.DS9FXObjects import DS9RandomAttackFleet

                    DS9RandomAttackFleet.DS9SetEnemyShips()

                    # Repeat the timer
                    RandomAttackTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnemyFleetArrives", App.g_kUtopiaModule.GetGameTime() + RandomEnemyFleet)
                    
                    # print "DS9FX: Enemy Fleet Entering the Set!"
            else:
                     # Else JUST Repeat the timer
                     RandomAttackTimer = DS9FXLib.DS9FXMenuLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".EnemyFleetArrives", App.g_kUtopiaModule.GetGameTime() + RandomEnemyFleet)

                     # print "DS9FX: Not in the correct set, just repeating the timer!"



# A bugfix. When we're not in DS9 Set just delete the timer
def DeleteRandomAttackTimer(pObject, pEvent):
        debug(__name__ + ", DeleteRandomAttackTimer")
        global RandomAttackTimer
        
        # Just simply delete the distance timer that's all
        try:
                    App.g_kTimerManager.DeleteTimer(RandomAttackTimer.GetObjID())
                    App.g_kRealtimeTimerManager.DeleteTimer(RandomAttackTimer.GetObjID())
                    RandomAttackTimer = None
                    # print "DS9FX: Deleting RandomAttackTimer!"
        except:
                    pass
         


# Let's implement dockable DS9 Station into the mod :)
def DockToDS9(pObject, pEvent):
        # Grab some values
        debug(__name__ + ", DockToDS9")
        pPlayer = App.Game_GetCurrentPlayer()
	pDS9 = GetDS9(pPlayer)
	
	if (pDS9 is None):
		return

	pGraffAction = None

        # Import the docking AI
	import AI.Compound.DockWithStarbase
	MissionLib.SetPlayerAI("Helm", AI.Compound.DockWithStarbase.CreateAI(pPlayer, pDS9, pGraffAction, NoRepair = 0, FadeEnd = 1))



# Get the DS9 Station
def GetDS9(pShip):
	debug(__name__ + ", GetDS9")
	if pShip:
                # Grab some values of course
		pDS9Set = pShip.GetContainingSet()
		if(pDS9Set is None):
			return

                # Grab the base
                pDS9Base = MissionLib.GetShip("Deep_Space_9", pDS9Set)
		
		if(pDS9Base is None):
			return

		# Return the base
		return pDS9Base



# Bugs showed up in the sequence, so we fix it by disabling the engineers menu. While the sequence is active 
def DisableEngineerMenu():
        # Since DisableEngineerMenu is already being called in proper places we'll just call DetachMenus from here to save us time
        # Just let's call DetachMenu's first
        debug(__name__ + ", DisableEngineerMenu")
        DetachMenus(None, None)
        
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Engineer"))
	App.g_kLocalizationManager.Unload(pDatabase)

	pMenu.SetDisabled()

        
        

# Reenable engineering menu, BC at this point really makes no sense. I hate that!
def EnableEngineerMenu():
        # Same goes for ReatachMenus as for DetachMenus
        debug(__name__ + ", EnableEngineerMenu")
        ReatachMenus(None, None)
        
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString("Engineer"))
	App.g_kLocalizationManager.Unload(pDatabase)

	pMenu.SetEnabled()




# We badly need this since BC simply refuses to delete all active timers, reason unknown
def DeleteAllDS9FXTimers():
    
        debug(__name__ + ", DeleteAllDS9FXTimers")
        DS9FXLib.DS9FXMenuLib.DeleteAlTimers()

        # print "DS9FX: Deleting all timers!"




# Saffi will now warn the user when an enemy detects a player
def PlayerDetected(pObject = None, pEvent = None):
                debug(__name__ + ", PlayerDetected")
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
                pSequence = App.TGSequence_Create()
                pSet = App.g_kSetManager.GetSet("bridge")
                pXO = App.CharacterClass_GetObject(pSet, "XO")
                pSequence.AppendAction(App.CharacterAction_Create(pXO, App.CharacterAction.AT_SAY_LINE, "CloakDetect", None, 0, Database))
                pSequence.Play()
        


# Another bugfix, well actually a major bugfix. This is the baby that fixes all issues, yaaay. We detach crew menus when the sequence is
# activated and later on reatach menus
def DetachMenus(pObject, pEvent):
        # Grab some the set and all bridge characters
        debug(__name__ + ", DetachMenus")
        pSet = App.g_kSetManager.GetSet("bridge")
        pEngineer = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
        pScience = App.CharacterClass_Cast(pSet.GetObject("Science"))
        pXO = App.CharacterClass_Cast(pSet.GetObject("XO"))
        pTactical = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
        pHelm = App.CharacterClass_Cast(pSet.GetObject("Helm"))

        # Now let's detach crew menus
	if pEngineer:
            import Bridge.EngineerCharacterHandlers
            Bridge.EngineerCharacterHandlers.DetachMenuFromEngineer(pEngineer)

        # Problems showed up when we implemented a suppliment bugfix (Dummy ship) so we'll just detach the troubling menu, Engineers

        # if pScience:
        #     import Bridge.ScienceCharacterHandlers
        #     Bridge.ScienceCharacterHandlers.DetachMenuFromScience(pScience)

        # if pXO:
        #     import Bridge.XOCharacterHandlers
        #     Bridge.XOCharacterHandlers.DetachMenuFromXO(pXO)

        # if pTactical:
        #     import Bridge.TacticalCharacterHandlers
        #     Bridge.TacticalCharacterHandlers.DetachMenuFromTactical(pTactical)

        # if pHelm:
        #    import Bridge.HelmCharacterHandlers
        #     Bridge.HelmCharacterHandlers.DetachMenuFromHelm(pHelm)
            

        # print "DS9FX: Detaching Crew Menus!"



# Opposite of DetachMenus(), we reatach menus
def ReatachMenus(pObject, pEvent):
        # Grab some the set and all bridge characters
        debug(__name__ + ", ReatachMenus")
        pSet = App.g_kSetManager.GetSet("bridge")
        pEngineer = App.CharacterClass_Cast(pSet.GetObject("Engineer"))
        pScience = App.CharacterClass_Cast(pSet.GetObject("Science"))
        pXO = App.CharacterClass_Cast(pSet.GetObject("XO"))
        pTactical = App.CharacterClass_Cast(pSet.GetObject("Tactical"))
        pHelm = App.CharacterClass_Cast(pSet.GetObject("Helm"))

        # Reatach bridge menus
	if pEngineer:
            import Bridge.EngineerCharacterHandlers
            Bridge.EngineerCharacterHandlers.AttachMenuToEngineer(pEngineer)

        # Just reatach the only detached menu, Engineers menu

        # if pScience:
        #     import Bridge.ScienceCharacterHandlers
        #     Bridge.ScienceCharacterHandlers.AttachMenuToScience(pScience)

        # if pXO:
        #     import Bridge.XOCharacterHandlers
        #     Bridge.XOCharacterHandlers.AttachMenuToXO(pXO)

        # if pTactical:
        #     import Bridge.TacticalCharacterHandlers
        #     Bridge.TacticalCharacterHandlers.AttachMenuToTactical(pTactical)

        # if pHelm:
        #     import Bridge.HelmCharacterHandlers
        #     Bridge.HelmCharacterHandlers.AttachMenuToHelm(pHelm)
            

        # print "DS9FX: Reataching Crew Menus!"



# Delete the dummy ship
def DeleteDummy(pObject, pEvent):
        debug(__name__ + ", DeleteDummy")
        global Dummy, pPlayer

        NewPlayer = App.Game_GetCurrentPlayer()
	if not NewPlayer:
		return 0
	
	NewSet = NewPlayer.GetContainingSet()
         
        NewSet.RemoveObjectFromSet(Dummy)

	# Return the original player
        pGame = App.Game_GetCurrentGame()
        pGame.SetPlayer(pPlayer)

        # print "DS9FX: Removing dummy player ship!"


# Removing keyboard control
def RemoveKeyboardControl(pAction = None):
    
        # Grab some values
	debug(__name__ + ", RemoveKeyboardControl")
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return None

	pTopWindow.SetNotVisible()

        # Do not allow user tampering
	pTopWindow.DisableOptionsMenu(1)
	pTopWindow.AllowKeyboardInput(0)
	pTopWindow.AllowMouseInput(0)

	return 0
    


# Return keyboard control
def ReturnKeyboardControl(pAction = None):
    
        debug(__name__ + ", ReturnKeyboardControl")
        pTopWindow = App.TopWindow_GetTopWindow()
        if (pTopWindow == None):
                return None

	pTopWindow.SetVisible()

        # Restore all options back to default
	pTopWindow.DisableOptionsMenu(0)
	pTopWindow.AllowKeyboardInput(1)
	pTopWindow.AllowMouseInput(1)

	return 0


# Hailing DS9. 
def HailDS9(pObject, pEvent):
    
        debug(__name__ + ", HailDS9")
        Player = App.Game_GetCurrentPlayer()
	if not Player:
		return 0
	
	Set = Player.GetContainingSet()
	
        pDS9 = MissionLib.GetShip("Deep_Space_9", Set)

        # Check if we are in range 
        if DistanceCheck(pDS9) > 900:
                    FelixWarnPrompt()
                    print "DS9FX: To far out to Hail DS9!"
                    return
                
        pSequence = MissionLib.NewDialogueSequence()
	pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOn", "KiraSet", "Kira", 200)
	pSequence.AppendAction(pAction)
	MissionLib.QueueActionToPlay(pSequence)

	ForceCamOn()
        
       	pSequence2 = MissionLib.NewDialogueSequence()
       	pSequence2.AppendAction(App.TGScriptAction_Create(__name__, "MenuUp"))
       	pSequence2.Play()

        WelcomeToDS9Line()

# This func complements ForceCamOff
def ForceCamOn():
	debug(__name__ + ", ForceCamOn")
	pBridge = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
	pLookAtSet = App.g_kSetManager.GetSet("KiraSet")
	pMainCamera = pLookAtSet.GetCamera("maincamera")
	if (pBridge):
		pViewScreen = pBridge.GetViewScreen()
		if (pViewScreen):
			pViewScreen.SetRemoteCam(pMainCamera)
			pViewScreen.SetIsOn(1)
			

# Bring the menu up
def MenuUp(pAction):
    
        debug(__name__ + ", MenuUp")
        pKiraSet = App.g_kSetManager.GetSet("KiraSet")
	pKira = App.CharacterClass_GetObject (pKiraSet, "Kira")

	pAction = App.CharacterAction_Create(pKira, App.CharacterAction.AT_MENU_UP)
	pAction.Play()

        return 0


# Close the menu
def MenuClose(pAction):
    
        debug(__name__ + ", MenuClose")
        pKiraSet = App.g_kSetManager.GetSet("KiraSet")
	pKira = App.CharacterClass_GetObject (pKiraSet, "Kira")

	pAction = App.CharacterAction_Create(pKira, App.CharacterAction.AT_MENU_DOWN)
	pAction.Play()

    	return 0


# Speak Major Kira and welcome us to DS9 
def WelcomeToDS9Line(pObject = None, pEvent = None):
                debug(__name__ + ", WelcomeToDS9Line")
                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
                pSequence = App.TGSequence_Create()
                pKiraSet = App.g_kSetManager.GetSet("KiraSet")
                pKira = App.CharacterClass_GetObject (pKiraSet, "Kira")
                pKira.SetCharacterName("Kira")
                pSequence.AppendAction(App.CharacterAction_Create(pKira, App.CharacterAction.AT_SAY_LINE, "welcome", None, 0, Database))
                pSequence.Play()



# Create bridge menu button. Original code by Totally Games
def CreateBridgeMenuButton(pName, eType, iSubType, pCharacter):
	debug(__name__ + ", CreateBridgeMenuButton")
	pEvent = App.TGIntEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pCharacter)
	pEvent.SetInt(iSubType)
	BridgeMenuButton = App.STButton_CreateW(pName, pEvent)
	return BridgeMenuButton


# Grab a menu button
def GetMenuButton(sMenuName, sButtonName):
        debug(__name__ + ", GetMenuButton")
        pMenu = GetBridgeMenu(sMenuName)
        if not pMenu:
                return

        # Grab the starting button.    
        pButton = pMenu.GetButton(sButtonName)
        if not pButton:
                pButton = pMenu.GetSubmenu(sButtonName)
                if not pButton: 
                        return
        return pButton


# Grab any menu
def GetBridgeMenu(menuName):
	debug(__name__ + ", GetBridgeMenu")
	pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
	if(pDatabase is None):
		return
	return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))
    

# Call in the window which will create a mission menu    
def ChooseCampaign(pObject, pEvent):

        # A bugfix, taken from CWS 2.0's GUI Code.
        debug(__name__ + ", ChooseCampaign")
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveWindowContents", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

        # Now with each click we recreate the Mission Windows. We can show now which Missions are available to user and which aren't.
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindowPartII", App.g_kUtopiaModule.GetGameTime() + 0.02, 0, 0)

        # Now bring up the window, delay the event for 0.1 seconds
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".Window", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)


# Call in the window which will create a mission menu    
def ChooseMiniMission(pObject, pEvent):

        # A bugfix, taken from CWS 2.0's GUI Code.
        debug(__name__ + ", ChooseMiniMission")
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveWindow2Contents", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)        

        # Now with each click we recreate the Mission Windows. We can show now which Missions are available to user and which aren't.
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow2PartII", App.g_kUtopiaModule.GetGameTime() + 0.02, 0, 0)

        # Now bring up the window, delay the event for 0.1 seconds
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".Window2", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)


# Call in the window which will create a mission menu    
def ChooseHistoric(pObject, pEvent):

        # A bugfix, taken from CWS 2.0's GUI Code.
        debug(__name__ + ", ChooseHistoric")
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".RemoveWindow3Contents", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

        # Now with each click we recreate the Mission Windows. We can show now which Missions are available to user and which aren't.
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CreateWindow3PartII", App.g_kUtopiaModule.GetGameTime() + 0.02, 0, 0)

        # Now bring up the window, delay the event for 0.1 seconds
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".Window3", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)


def RemoveWindowContents(pObject, pEvent):
	debug(__name__ + ", RemoveWindowContents")
	global MissionWindow, pText1, pText2, pText3, pText4, pText5, pText6, pButton1, pButton2, pButton3, pButton4, pButton5, pButton6, pButton7

	if MissionWindow:
	                MissionWindow.DeleteChild(pText1)
	                MissionWindow.DeleteChild(pText2)
	                MissionWindow.DeleteChild(pButton1)
	                MissionWindow.DeleteChild(pText3)
	                MissionWindow.DeleteChild(pButton2)
	                MissionWindow.DeleteChild(pText4)
	                MissionWindow.DeleteChild(pButton3)
	                MissionWindow.DeleteChild(pText5)
	                MissionWindow.DeleteChild(pButton4)
	                MissionWindow.DeleteChild(pText6)
	                MissionWindow.DeleteChild(pButton5)
	                MissionWindow.DeleteChild(pButton6)
	                MissionWindow.DeleteChild(pButton7)


def RemoveWindow2Contents(pObject, pEvent):
	debug(__name__ + ", RemoveWindow2Contents")
	global MissionWindow2, pText7, pText8, pButton8, pButton9, pButton10, pText15, pButton18, pText16, pButton19, pText17, pButton20, pText18, pButton21, pText19, pButton22

	if MissionWindow2:
	                MissionWindow2.DeleteChild(pText7)
	                MissionWindow2.DeleteChild(pText8)
	                MissionWindow2.DeleteChild(pText15)
	                MissionWindow2.DeleteChild(pText16)
	                MissionWindow2.DeleteChild(pText17)
	                MissionWindow2.DeleteChild(pText18)
	                MissionWindow2.DeleteChild(pText19)
	                MissionWindow2.DeleteChild(pButton8)
	                MissionWindow2.DeleteChild(pButton9)
	                MissionWindow2.DeleteChild(pButton10)
	                MissionWindow2.DeleteChild(pButton18)
	                MissionWindow2.DeleteChild(pButton19)
	                MissionWindow2.DeleteChild(pButton20)
	                MissionWindow2.DeleteChild(pButton21)
	                MissionWindow2.DeleteChild(pButton22)


def RemoveWindow3Contents(pObject, pEvent):
	debug(__name__ + ", RemoveWindow3Contents")
	global MissionWindow3, pText9, pText10, pText11, pText13, pButton11, pButton12, pButton13, pButton14, pText12, pButton15, pButton16, pText14, pButton17

	if MissionWindow3:
	                MissionWindow3.DeleteChild(pText9)
			MissionWindow3.DeleteChild(pText10)
			MissionWindow3.DeleteChild(pText11)
			MissionWindow3.DeleteChild(pText12)
			MissionWindow3.DeleteChild(pText13)
			MissionWindow3.DeleteChild(pText14)
			MissionWindow3.DeleteChild(pButton11)
			MissionWindow3.DeleteChild(pButton12)
			MissionWindow3.DeleteChild(pButton13)
                        MissionWindow3.DeleteChild(pButton14)
                        MissionWindow3.DeleteChild(pButton15)
                        MissionWindow3.DeleteChild(pButton16)
                        MissionWindow3.DeleteChild(pButton17)


# Closing the channel
def CloseChannel(pObject, pEvent):
        debug(__name__ + ", CloseChannel")
        CloseChannels(None, None)
        
        pSeq = MissionLib.NewDialogueSequence()
	pAction = App.TGScriptAction_Create(__name__, "MenuClose")
	pSeq.AppendAction(pAction)
	pSeq.Play()

        ChannelClosing()
        

# Closing the channel
def ChannelClosing():        
        debug(__name__ + ", ChannelClosing")
        pSeq = MissionLib.NewDialogueSequence()
	pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
	pSeq.AppendAction(pAction)
	MissionLib.QueueActionToPlay(pSeq)

        # Manually turn off the screen also. Small bug poped up
        ForceCamOff()

	# print "DS9FX: Channel Closed!"


# A bugfix if you do a stupid thing like pressing Hail DS9 without closing the channel 1st to remove Kira from the screen!	
def ForceCamOff():
        debug(__name__ + ", ForceCamOff")
        pGame = App.Game_GetCurrentGame()
	if not pGame:
		return 0
	pCamera = pGame.GetPlayerCamera()
	if not pCamera:
		return 0

	pBridge = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
	if (pBridge):
		pViewScreen = pBridge.GetViewScreen()
		if (pViewScreen):
			pViewScreen.SetRemoteCam(pCamera)
			pViewScreen.SetIsOn(1)

			if (pViewScreen.IsStaticOn()):
				pViewScreen.SetStaticIsOn(0)



# Create the window
def CreateWindow(pObject, pEvent):
        debug(__name__ + ", CreateWindow")
        global MissionWindow

        MissionWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Campaign Mission Selection Menu"), 0.0, 0.0, None, 1, 0.50, 0.65, App.g_kMainMenuBorderMainColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(MissionWindow, 0.25, 0.25)

        MissionWindow.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        MissionWindow.SetNotVisible()
        
        CreateWindowPartII(None, None)


# Create the window
def CreateWindow2(pObject, pEvent):
        debug(__name__ + ", CreateWindow2")
        global MissionWindow2

        MissionWindow2 = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Mini Mission Selection Menu"), 0.0, 0.0, None, 1, 0.50, 0.65, App.g_kMainMenuBorderMainColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(MissionWindow2, 0.25, 0.25)

        MissionWindow2.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        MissionWindow2.SetNotVisible()
        
        CreateWindow2PartII(None, None)


# Create the window
def CreateWindow3(pObject, pEvent):
        debug(__name__ + ", CreateWindow3")
        global MissionWindow3

        MissionWindow3 = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Historic Mission Selection Menu"), 0.0, 0.0, None, 1, 0.50, 0.65, App.g_kMainMenuBorderMainColor)
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        pTCW.AddChild(MissionWindow3, 0.25, 0.25)

        MissionWindow3.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".MousePass")
        MissionWindow3.SetNotVisible()
        
        CreateWindow3PartII(None, None)



# Mouse Pass over the Window is handeled in this function
def MousePass(Window, pEvent):
        debug(__name__ + ", MousePass")
        Window.CallNextHandler(pEvent)

        if pEvent.EventHandled() == 0:
                pEvent.SetHandled()
                


# Create the buttons and define events in the window
def CreateWindowPartII(pObject, pEvent):
            debug(__name__ + ", CreateWindowPartII")
            global ET_WINDOW_CLOSE, ET_BORDER_SKIRMISH_1, ET_BORDER_SKIRMISH_2, ET_BORDER_SKIRMISH_3, ET_BORDER_SKIRMISH_4, ET_BORDER_SKIRMISH_5, ET_BACK, MissionWindow, pPerson, MissionWindow2, ET_UNAVAILABLE
            global pText1, pText2, pText3, pText4, pText5, pText6, pButton1, pButton2, pButton3, pButton4, pButton5, pButton6, pButton7

            # Do a check on all files
            try:
                
                # Load up the default file which must exist
                pConfig = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.defaultsavedconfig")

                # Check if this is an authentic file
                Ship = pConfig.Ship

                if Ship == None:
                
                    pass
            
                else:
                
                    print "DS9FX: This isn't an authentic DS9FX Saved Config, destroying Campaign Selection Menu!"
                    MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CloseChannels", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)
                    return


                # Set Mission Progress
                MissionProgress = None
                MissionProgress = 1
                

            except:
                
                pass


            try:
                
                # Check if the next file exists for the 2nd mission. Its being created during the mission progress
                pConfig2 = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.mission2")

                # Reset Mission Progress
                MissionProgress = None
                MissionProgress = 2
                

            except:
                
                pass

            try:
                
                # Check if the next file exists for the 2nd mission. Its being created during the mission progress
                pConfig3 = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.mission3")

                # Reset Mission Progress
                MissionProgress = None
                MissionProgress = 3
                

            except:
                
                pass


            try:
                
                # Check if the next file exists for the 2nd mission. Its being created during the mission progress
                pConfig4 = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.mission4")

                # Reset Mission Progress
                MissionProgress = None
                MissionProgress = 4
                

            except:
                
                pass


            try:
                
                # Check if the next file exists for the 2nd mission. Its being created during the mission progress
                pConfig5 = __import__("DS9FXMissions.CampaignMode.BorderSkirmish.Save.mission5")

                # Reset Mission Progress
                MissionProgress = None
                MissionProgress = 5
                

            except:
                
                pass

            
            x = 0
            y = 0.01
            pText6 = App.TGParagraph_CreateW(App.TGString("Please Select a Mission. Remember that the Campaign Mode remembers your last used ship and you cannot switch ships later. Missions have to be unlocked one by one."), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow.AddChild(pText6, x, y, 0)

            if MissionProgress == 1:
                textx = 0
                texty = 0.10
                pText1 = App.TGParagraph_CreateW(App.TGString("Mission 1: Patrol Duty"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText1, textx, texty, 0)

                x = 0.35
                y = y + 0.08
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_1)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton1 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton1.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton1.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton1.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton1.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton1.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton1, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText2 = App.TGParagraph_CreateW(App.TGString("Mission 2: Investigations"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText2, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton2 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton2.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton2.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton2.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton2.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton2.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton2, x, y, 0)


                textx = 0
                texty = texty + 0.06
                pText3 = App.TGParagraph_CreateW(App.TGString("Mission 3: A Time To Fight"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText3, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton3 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton3.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton3.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton3.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton3.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton3.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton3, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText4 = App.TGParagraph_CreateW(App.TGString("Mission 4: Revenge Is A Dish Best Served Cold"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText4, textx, texty, 0)


                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton4 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton4.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton4.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton4.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton4.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton4.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton4, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText5 = App.TGParagraph_CreateW(App.TGString("Mission 5: Once More Unto The Breach"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText5, textx, texty, 0)

            
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton5 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton5.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton5.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton5.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton5.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton5.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton5, x, y, 0)
                

            elif MissionProgress == 2:

                textx = 0
                texty = 0.10
                pText1 = App.TGParagraph_CreateW(App.TGString("Mission 1: Patrol Duty"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText1, textx, texty, 0)

                x = 0.35
                y = y + 0.08
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_1)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton1 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton1.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton1.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton1.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton1.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton1.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton1, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText2 = App.TGParagraph_CreateW(App.TGString("Mission 2: Investigations"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText2, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_2)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton2 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton2.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton2.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton2.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton2.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton2.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton2, x, y, 0)


                textx = 0
                texty = texty + 0.06
                pText3 = App.TGParagraph_CreateW(App.TGString("Mission 3: A Time To Fight"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText3, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton3 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton3.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton3.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton3.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton3.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton3.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton3, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText4 = App.TGParagraph_CreateW(App.TGString("Mission 4: Revenge Is A Dish Best Served Cold"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText4, textx, texty, 0)


                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton4 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton4.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton4.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton4.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton4.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton4.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton4, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText5 = App.TGParagraph_CreateW(App.TGString("Mission 5: Once More Unto The Breach"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText5, textx, texty, 0)

            
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton5 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton5.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton5.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton5.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton5.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton5.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton5, x, y, 0)
                
                

            elif MissionProgress == 3:
                textx = 0
                texty = 0.10
                pText1 = App.TGParagraph_CreateW(App.TGString("Mission 1: Patrol Duty"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText1, textx, texty, 0)

                x = 0.35
                y = y + 0.08
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_1)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton1 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton1.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton1.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton1.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton1.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton1.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton1, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText2 = App.TGParagraph_CreateW(App.TGString("Mission 2: Investigations"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText2, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_2)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton2 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton2.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton2.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton2.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton2.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton2.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton2, x, y, 0)


                textx = 0
                texty = texty + 0.06
                pText3 = App.TGParagraph_CreateW(App.TGString("Mission 3: A Time To Fight"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText3, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_3)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton3 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton3.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton3.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton3.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton3.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton3.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton3, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText4 = App.TGParagraph_CreateW(App.TGString("Mission 4: Revenge Is A Dish Best Served Cold"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText4, textx, texty, 0)


                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton4 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton4.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton4.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton4.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton4.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton4.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton4, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText5 = App.TGParagraph_CreateW(App.TGString("Mission 5: Once More Unto The Breach"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText5, textx, texty, 0)

            
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton5 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton5.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton5.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton5.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton5.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton5.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton5, x, y, 0)
                
                

            elif MissionProgress == 4:

                textx = 0
                texty = 0.10
                pText1 = App.TGParagraph_CreateW(App.TGString("Mission 1: Patrol Duty"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText1, textx, texty, 0)

                x = 0.35
                y = y + 0.08
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_1)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton1 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton1.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton1.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton1.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton1.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton1.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton1, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText2 = App.TGParagraph_CreateW(App.TGString("Mission 2: Investigations"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText2, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_2)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton2 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton2.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton2.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton2.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton2.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton2.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton2, x, y, 0)


                textx = 0
                texty = texty + 0.06
                pText3 = App.TGParagraph_CreateW(App.TGString("Mission 3: A Time To Fight"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText3, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_3)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton3 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton3.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton3.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton3.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton3.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton3.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton3, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText4 = App.TGParagraph_CreateW(App.TGString("Mission 4: Revenge Is A Dish Best Served Cold"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText4, textx, texty, 0)


                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_4)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton4 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton4.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton4.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton4.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton4.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton4.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton4, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText5 = App.TGParagraph_CreateW(App.TGString("Mission 5: Once More Unto The Breach"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText5, textx, texty, 0)

            
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_UNAVAILABLE)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton5 = App.STRoundedButton_CreateW(App.TGString("Mission Locked"), pEvent, 0.13125, 0.034583)
                pButton5.SetNormalColor(App.g_kSTMenu1Disabled)
                pButton5.SetHighlightedColor(App.g_kSTMenu1Disabled)
                pButton5.SetSelectedColor(App.g_kSTMenu1Disabled)
                pButton5.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton5.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton5, x, y, 0)

                

            else:

                textx = 0
                texty = 0.10
                pText1 = App.TGParagraph_CreateW(App.TGString("Mission 1: Patrol Duty"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText1, textx, texty, 0)

                x = 0.35
                y = y + 0.08
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_1)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton1 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton1.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton1.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton1.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton1.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton1.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton1, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText2 = App.TGParagraph_CreateW(App.TGString("Mission 2: Investigations"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText2, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_2)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton2 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton2.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton2.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton2.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton2.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton2.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton2, x, y, 0)


                textx = 0
                texty = texty + 0.06
                pText3 = App.TGParagraph_CreateW(App.TGString("Mission 3: A Time To Fight"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText3, textx, texty, 0)

                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_3)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton3 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton3.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton3.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton3.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton3.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton3.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton3, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText4 = App.TGParagraph_CreateW(App.TGString("Mission 4: Revenge Is A Dish Best Served Cold"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText4, textx, texty, 0)


                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_4)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton4 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton4.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton4.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton4.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton4.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton4.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton4, x, y, 0)

                textx = 0
                texty = texty + 0.06
                pText5 = App.TGParagraph_CreateW(App.TGString("Mission 5: Once More Unto The Breach"), MissionWindow.GetMaximumInteriorWidth(), None, '', MissionWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
                MissionWindow.AddChild(pText5, textx, texty, 0)

            
                x = 0.35
                y = y + 0.06
                pEvent = App.TGIntEvent_Create()
                pEvent.SetEventType(ET_BORDER_SKIRMISH_5)
                pEvent.SetDestination(pPerson)
                pEvent.SetInt(0)
                pButton5 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
                pButton5.SetNormalColor(App.g_kMainMenuButtonColor)
                pButton5.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
                pButton5.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
                pButton5.SetDisabledColor(App.g_kSTMenu1Disabled)
                pButton5.SetColorBasedOnFlags()
                MissionWindow.AddChild(pButton5, x, y, 0)

                        

            x = 0
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_BACK)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton6 = App.STRoundedButton_CreateW(App.TGString("Back To Main Menu"), pEvent, 0.13125, 0.034583)
            pButton6.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton6.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton6.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton6.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton6.SetColorBasedOnFlags()
            MissionWindow.AddChild(pButton6, x, y, 0)


            x = 0
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_WINDOW_CLOSE)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton7 = App.STRoundedButton_CreateW(App.TGString("Close Channel"), pEvent, 0.13125, 0.034583)
            pButton7.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton7.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton7.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton7.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton7.SetColorBasedOnFlags()
            MissionWindow.AddChild(pButton7, x, y, 0)

            MissionWindow.InteriorChangedSize()
            MissionWindow.Layout()



# Create us Mission Window 2
def CreateWindow2PartII(pObject, pEvent):
            debug(__name__ + ", CreateWindow2PartII")
            global ET_BACK, MissionWindow, pPerson, ET_MINI_MISSION_1, ET_MINI_MISSION_2, MissionWindow2, ET_WINDOW_CLOSE_2, ET_MINI_MISSION_3, ET_MINI_MISSION_4, ET_MINI_MISSION_5, ET_MINI_MISSION_6
            global pText7, pText8, pButton8, pButton9, pButton10, pText15, pButton18, pText16, pButton19, pText17, pButton20, pText18, pButton21, pText19, pButton22
    
            x = 0
            y = 0.01
            pText7 = App.TGParagraph_CreateW(App.TGString("Please Select a Mission. Unlike Campaign Mode you can freely pick any ship you wish! These are just small missions for fun."), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow2.AddChild(pText7, x, y, 0)


            textx = 0
            texty = 0.10
            pText8 = App.TGParagraph_CreateW(App.TGString("Mission: Procure Ketracel White"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow2.AddChild(pText8, textx, texty, 0)

            x = 0.35
            y = y + 0.08
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_MINI_MISSION_1)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton8 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton8.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton8.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton8.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton8.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton8.SetColorBasedOnFlags()
            MissionWindow2.AddChild(pButton8, x, y, 0)


            textx = 0
            texty = texty + 0.06
            pText15 = App.TGParagraph_CreateW(App.TGString("Mission: Anomalous Readings"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow2.AddChild(pText15, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_MINI_MISSION_2)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton19 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton19.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton19.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton19.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton19.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton19.SetColorBasedOnFlags()
            MissionWindow2.AddChild(pButton19, x, y, 0)


            textx = 0
            texty = texty + 0.06
            pText16 = App.TGParagraph_CreateW(App.TGString("Mission: The tides of Idran"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow2.AddChild(pText16, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_MINI_MISSION_3)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton18 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton18.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton18.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton18.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton18.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton18.SetColorBasedOnFlags()
            MissionWindow2.AddChild(pButton18, x, y, 0)


            textx = 0
            texty = texty + 0.06
            pText17 = App.TGParagraph_CreateW(App.TGString("Mission: The Dogs of War"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow2.AddChild(pText17, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_MINI_MISSION_4)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton20 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton20.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton20.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton20.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton20.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton20.SetColorBasedOnFlags()
            MissionWindow2.AddChild(pButton20, x, y, 0)

            textx = 0
            texty = texty + 0.06
            pText18 = App.TGParagraph_CreateW(App.TGString("Mission: Valiant"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow2.AddChild(pText18, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_MINI_MISSION_5)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton21 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton21.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton21.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton21.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton21.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton21.SetColorBasedOnFlags()
            MissionWindow2.AddChild(pButton21, x, y, 0)

            textx = 0
            texty = texty + 0.06
            pText19 = App.TGParagraph_CreateW(App.TGString("Mission: Section 31"), MissionWindow2.GetMaximumInteriorWidth(), None, '', MissionWindow2.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow2.AddChild(pText19, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_MINI_MISSION_6)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton22 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton22.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton22.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton22.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton22.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton22.SetColorBasedOnFlags()
            MissionWindow2.AddChild(pButton22, x, y, 0)

            
            x = 0
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_BACK)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton9 = App.STRoundedButton_CreateW(App.TGString("Back To Main Menu"), pEvent, 0.13125, 0.034583)
            pButton9.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton9.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton9.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton9.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton9.SetColorBasedOnFlags()
            MissionWindow2.AddChild(pButton9, x, y, 0)


            x = 0
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_WINDOW_CLOSE_2)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton10 = App.STRoundedButton_CreateW(App.TGString("Close Channel"), pEvent, 0.13125, 0.034583)
            pButton10.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton10.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton10.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton10.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton10.SetColorBasedOnFlags()
            MissionWindow2.AddChild(pButton10, x, y, 0)

            MissionWindow2.InteriorChangedSize()
            MissionWindow2.Layout()



# Create Historic Mission Window
def CreateWindow3PartII(pObject, pEvent):
            debug(__name__ + ", CreateWindow3PartII")
            global ET_BACK, MissionWindow, pPerson, ET_HISTORIC_MISSION_1, MissionWindow3, ET_WINDOW_CLOSE_3, ET_HISTORIC_MISSION_2, ET_HISTORIC_MISSION_3, ET_HISTORIC_MISSION_4, ET_HISTORIC_MISSION_5
            global pText9, pText10, pText11, pText12, pText13, pButton11, pButton12, pButton13, pButton14, pButton15, pButton16, pText14, pButton17

            
            x = 0
            y = 0.01
            pText9 = App.TGParagraph_CreateW(App.TGString("Please Select a Mission. Historic Mission Mode pays tribute to DS9. You can play a lot of historic missions seen in the show. All missions are available to you but your ship class varies from mission to mission."), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow3.AddChild(pText9, x, y, 0)


            textx = 0
            texty = 0.12
            pText10 = App.TGParagraph_CreateW(App.TGString("Mission: Plant the minefield"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow3.AddChild(pText10, textx, texty, 0)


            x = 0.35
            y = y + 0.10
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_HISTORIC_MISSION_1)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton11 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton11.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton11.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton11.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton11.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton11.SetColorBasedOnFlags()
            MissionWindow3.AddChild(pButton11, x, y, 0)

            textx = 0
            texty = texty + 0.06
            pText11 = App.TGParagraph_CreateW(App.TGString("Mission: Retake DS9"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow3.AddChild(pText11, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_HISTORIC_MISSION_2)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton14 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton14.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton14.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton14.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton14.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton14.SetColorBasedOnFlags()
            MissionWindow3.AddChild(pButton14, x, y, 0)

            textx = 0
            texty = texty + 0.06
            pText12 = App.TGParagraph_CreateW(App.TGString("Mission: USS Odyssey"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow3.AddChild(pText12, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_HISTORIC_MISSION_3)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton15 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton15.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton15.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton15.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton15.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton15.SetColorBasedOnFlags()
            MissionWindow3.AddChild(pButton15, x, y, 0)

            textx = 0
            texty = texty + 0.06
            pText13 = App.TGParagraph_CreateW(App.TGString("Mission: Retake DS9 (Canon)"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow3.AddChild(pText13, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_HISTORIC_MISSION_4)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton16 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton16.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton16.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton16.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton16.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton16.SetColorBasedOnFlags()
            MissionWindow3.AddChild(pButton16, x, y, 0)

            textx = 0
            texty = texty + 0.06
            pText14 = App.TGParagraph_CreateW(App.TGString("Mission: The Way of the Warrior"), MissionWindow3.GetMaximumInteriorWidth(), None, '', MissionWindow3.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
            MissionWindow3.AddChild(pText14, textx, texty, 0)

            x = 0.35
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_HISTORIC_MISSION_5)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton17 = App.STRoundedButton_CreateW(App.TGString("Mission Briefing"), pEvent, 0.13125, 0.034583)
            pButton17.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton17.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton17.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton17.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton17.SetColorBasedOnFlags()
            MissionWindow3.AddChild(pButton17, x, y, 0)
            
            x = 0
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_BACK)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton12 = App.STRoundedButton_CreateW(App.TGString("Back To Main Menu"), pEvent, 0.13125, 0.034583)
            pButton12.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton12.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton12.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton12.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton12.SetColorBasedOnFlags()
            MissionWindow3.AddChild(pButton12, x, y, 0)


            x = 0
            y = y + 0.06
            pEvent = App.TGIntEvent_Create()
            pEvent.SetEventType(ET_WINDOW_CLOSE_3)
            pEvent.SetDestination(pPerson)
            pEvent.SetInt(0)
            pButton13 = App.STRoundedButton_CreateW(App.TGString("Close Channel"), pEvent, 0.13125, 0.034583)
            pButton13.SetNormalColor(App.g_kMainMenuButtonColor)
            pButton13.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
            pButton13.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
            pButton13.SetDisabledColor(App.g_kSTMenu1Disabled)
            pButton13.SetColorBasedOnFlags()
            MissionWindow3.AddChild(pButton13, x, y, 0)

            MissionWindow3.InteriorChangedSize()
            MissionWindow3.Layout()




# Should I bring the window up or close it?!
def Window(pObject, pEvent):
        debug(__name__ + ", Window")
        global MissionWindow, MissionWindow2, MissionWindow3 
        
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not MissionWindow:
                # print "DS9FX: Window Function - No window present!"
                return
        
        if MissionWindow.IsVisible():
                if MissionWindow2.IsVisible():
                    pTCW.MoveToBack(MissionWindow2)
                    MissionWindow2.SetNotVisible()

                if MissionWindow3.IsVisible():
                    pTCW.MoveToBack(MissionWindow3)
                    MissionWindow3.SetNotVisible()
                
                pTCW.MoveToBack(MissionWindow)
                MissionWindow.SetNotVisible()

                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # print "DS9FX: Window Function - Window is already present... deleting it!"

                
        else:
                if MissionWindow2.IsVisible():
                    pTCW.MoveToBack(MissionWindow2)
                    MissionWindow2.SetNotVisible()

                if MissionWindow3.IsVisible():
                    pTCW.MoveToBack(MissionWindow3)
                    MissionWindow3.SetNotVisible()
                    
                MissionWindow.SetVisible()
                pTCW.MoveToFront(MissionWindow)                
                pTCW.MoveTowardsBack(MissionWindow)


                # print "DS9FX: Window Function - Window should be visible!"

                
                
# Should I bring the window up or close it?!
def Window2(pObject, pEvent):
        debug(__name__ + ", Window2")
        global MissionWindow2, MissionWindow, MissionWindow3
        
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not MissionWindow2:
                # print "DS9FX: Window Function - No window present!"
                return
        
        if MissionWindow2.IsVisible():
                if MissionWindow.IsVisible():
                    pTCW.MoveToBack(MissionWindow)
                    MissionWindow.SetNotVisible()

                if MissionWindow3.IsVisible():
                    pTCW.MoveToBack(MissionWindow3)
                    MissionWindow3.SetNotVisible()
                    
                pTCW.MoveToBack(MissionWindow2)
                MissionWindow2.SetNotVisible()

                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()
                    

                # print "DS9FX: Window Function - Window is already present... deleting it!"
                
        else:
                if MissionWindow.IsVisible():
                    pTCW.MoveToBack(MissionWindow)
                    MissionWindow.SetNotVisible()

                if MissionWindow3.IsVisible():
                    pTCW.MoveToBack(MissionWindow3)
                    MissionWindow3.SetNotVisible()
                
                MissionWindow2.SetVisible()
                pTCW.MoveToFront(MissionWindow2)                
                pTCW.MoveTowardsBack(MissionWindow2)

                    
                # print "DS9FX: Window Function - Window should be visible!"
                


# Should I bring the window up or close it?!
def Window3(pObject, pEvent):
        debug(__name__ + ", Window3")
        global MissionWindow3, MissionWindow, MissionWindow2
        
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

        if not MissionWindow3:
                # print "DS9FX: Window Function - No window present!"
                return
        
        if MissionWindow3.IsVisible():
                if MissionWindow.IsVisible():
                    pTCW.MoveToBack(MissionWindow)
                    MissionWindow.SetNotVisible()

                if MissionWindow2.IsVisible():
                    pTCW.MoveToBack(MissionWindow2)
                    MissionWindow2.SetNotVisible()
                    
                pTCW.MoveToBack(MissionWindow3)
                MissionWindow3.SetNotVisible()

                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()
                    
                # print "DS9FX: Window Function - Window is already present... deleting it!"
                

        else:
                if MissionWindow.IsVisible():
                    pTCW.MoveToBack(MissionWindow)
                    MissionWindow.SetNotVisible()

                if MissionWindow2.IsVisible():
                    pTCW.MoveToBack(MissionWindow2)
                    MissionWindow2.SetNotVisible()
                
                MissionWindow3.SetVisible()
                pTCW.MoveToFront(MissionWindow3)                
                pTCW.MoveTowardsBack(MissionWindow3)

                    
                # print "DS9FX: Window Function - Window should be visible!"
                


# Just close the damn window                
def CloseWindow(pObject, pEvent):
        debug(__name__ + ", CloseWindow")
        global MissionWindow

        if not MissionWindow:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        if MissionWindow.IsVisible():
                pTCW.MoveToBack(MissionWindow)
                MissionWindow.SetNotVisible()
                

        pObject.CallNextHandler(pEvent)
        
        

# Just close the damn window                
def CloseWindow2(pObject, pEvent):
        debug(__name__ + ", CloseWindow2")
        global MissionWindow2

        if not MissionWindow2:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        if MissionWindow2.IsVisible():
                pTCW.MoveToBack(MissionWindow2)
                MissionWindow2.SetNotVisible()
                

        pObject.CallNextHandler(pEvent)

        

# Just close the damn window                
def CloseWindow3(pObject, pEvent):
        debug(__name__ + ", CloseWindow3")
        global MissionWindow3

        if not MissionWindow3:
                return

        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        if MissionWindow3.IsVisible():
                pTCW.MoveToBack(MissionWindow3)
                MissionWindow3.SetNotVisible()
                

        pObject.CallNextHandler(pEvent)
        


# Manually close the window if for some reason it was still up. Just to be safe
def CloseChannels(pObject, pEvent):
        debug(__name__ + ", CloseChannels")
        global MissionWindow, MissionWindow2, MissionWindow3

        if MissionWindow:
                
            pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
            if MissionWindow.IsVisible():
                    pTCW.MoveToBack(MissionWindow)
                    MissionWindow.SetNotVisible()

        if MissionWindow2:
                
            pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
            if MissionWindow2.IsVisible():
                    pTCW.MoveToBack(MissionWindow2)
                    MissionWindow2.SetNotVisible()

        if MissionWindow3:
                
            pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
            if MissionWindow3.IsVisible():
                    pTCW.MoveToBack(MissionWindow3)
                    MissionWindow3.SetNotVisible()


# Call in Mission 1 file & Close menus     
def BorderSkirmishMission1(pObject, pEvent):
           
                debug(__name__ + ", BorderSkirmishMission1")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()
                
                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission1

                Mission1.Briefing()
                

# Call in Mission 2 file & Close menus  
def BorderSkirmishMission2(pObject, pEvent):
        
                debug(__name__ + ", BorderSkirmishMission2")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission2

                Mission2.Briefing()
                

# Call in Mission 3 file & Close menus  
def BorderSkirmishMission3(pObject, pEvent):
               
        
                debug(__name__ + ", BorderSkirmishMission3")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission3

                Mission3.Briefing()
                

# Call in Mission 4 file & Close menus  
def BorderSkirmishMission4(pObject, pEvent):                
        
                debug(__name__ + ", BorderSkirmishMission4")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission4

                Mission4.Briefing()
                

# Call in Mission 5 file & Close menus  
def BorderSkirmishMission5(pObject, pEvent):
                      
                debug(__name__ + ", BorderSkirmishMission5")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission5

                Mission5.Briefing()
                

# Call in Mission file & Close menus  
def DS9FXHistoricMission1(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXHistoricMission1")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission1

                HistoricMission1.Briefing()


# Call in Mission file & Close menus  
def DS9FXHistoricMission2(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXHistoricMission2")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission2

                HistoricMission2.Briefing()


# Call in Mission file & Close menus  
def DS9FXHistoricMission3(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXHistoricMission3")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission3

                HistoricMission3.Briefing()


# Call in Mission file & Close menus  
def DS9FXHistoricMission4(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXHistoricMission4")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission4

                HistoricMission4.Briefing()


# Call in Mission file & Close menus  
def DS9FXHistoricMission5(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXHistoricMission5")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Briefing Menu
                
                from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission5

                HistoricMission5.Briefing()


# Call in Mission file & Close menus  
def DS9FXMiniMission1(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXMiniMission1")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Import Mission
                from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission1

                MiniMission1.Briefing()


# Call in Mission file & Close menus  
def DS9FXMiniMission2(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXMiniMission2")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Import Mission
                from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission2

                MiniMission2.Briefing()


# Call in Mission file & Close menus  
def DS9FXMiniMission3(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXMiniMission3")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Import Mission
                from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission3

                MiniMission3.Briefing()


# Call in Mission file & Close menus  
def DS9FXMiniMission4(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXMiniMission4")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Import Mission
                from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission4

                MiniMission4.Briefing()


# Call in Mission file & Close menus  
def DS9FXMiniMission5(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXMiniMission5")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Import Mission
                from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission5

                MiniMission5.Briefing()


# Call in Mission file & Close menus  
def DS9FXMiniMission6(pObject, pEvent):
                      
                debug(__name__ + ", DS9FXMiniMission6")
                pSeq = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create(__name__, "MenuClose")
                pSeq.AppendAction(pAction)
                pSeq.Play()

                pSeq2 = MissionLib.NewDialogueSequence()
                pAction = App.TGScriptAction_Create("MissionLib", "ViewscreenOff")
                pSeq2.AppendAction(pAction)
                MissionLib.QueueActionToPlay(pSeq2)

                ForceCamOff()

                # Import Mission
                from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission6

                MiniMission6.Briefing()
                
       
                
# Tell the user that he can't choose this mission. This function is for stuborn people who think that by clicking on a button which says: "Mission Locked" will get them somewhere.
def MissionUnavailable(pObject, pEvent):
            debug(__name__ + ", MissionUnavailable")
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
            
            # 1 second warning prompt
            pAction = LineAction("Mission Unavailable", pPane, 4, 1, 16)
            pSequence.AddAction(pAction, None, 0)
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
    

# We've pressed the Back Button so let's get back
def BackToHailMenu(pObject, pEvent):
        # Just kill the windows
        debug(__name__ + ", BackToHailMenu")
        MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CloseChannels", App.g_kUtopiaModule.GetGameTime() + 0.1, 0, 0)



# Quit function which kills the Mission Selection Menu Windows
def DS9FXExit():
        debug(__name__ + ", DS9FXExit")
        global MissionWindow, MissionWindow2, MissionWindow3 

	debug(__name__ + ", DS9FXExit Alive 1")
        if MissionWindow:
                MissionWindow.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                #pTCW.DeleteChild(MissionWindow)

	debug(__name__ + ", DS9FXExit Alive 2")
        if MissionWindow2:
                MissionWindow2.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                #pTCW.DeleteChild(MissionWindow2)

	debug(__name__ + ", DS9FXExit Alive 3")
        if MissionWindow3:
                MissionWindow3.KillChildren()
                pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
                #pTCW.DeleteChild(MissionWindow3)

	debug(__name__ + ", DS9FXExit Alive 4")
        from Custom.DS9FX.DS9FXMissions import MissionQuitHelper

	debug(__name__ + ", DS9FXExit Alive 5")
        MissionQuitHelper.Exiting()
	debug(__name__ + ", DS9FXExit End")
                

# Video Mode Exit Checking
def CheckVideoExitingDS9(pObject, pEvent):        
        debug(__name__ + ", CheckVideoExitingDS9")
        from Custom.DS9FX.DS9FXWormholeVid import DS9FXWormholeVideo

        VideoMode = DS9FXWormholeVideo.CheckExitFromVideo()

        if VideoMode == 1:
            # Timer based event to call transfer seq
            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferShips2", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

        else:   
            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CheckVideoExitingDS9", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)


# Video Mode Exit Checking
def CheckVideoExitingGamma(pObject, pEvent):        
        debug(__name__ + ", CheckVideoExitingGamma")
        from Custom.DS9FX.DS9FXWormholeVid import DS9FXWormholeVideo

        VideoMode = DS9FXWormholeVideo.CheckExitFromVideo()

        if VideoMode == 1:            
	    # Timer based event to call transfer seq,
            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".TransferShips3", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)

        else:   
            MissionLib.CreateTimer(DS9FXLib.DS9FXMenuLib.GetNextEventType(), __name__ + ".CheckVideoExitingGamma", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)


# Well... 0.1% bug fixed now, translate the player to a preset location to aid the AI.
def TranslatePlayer():
        debug(__name__ + ", TranslatePlayer")
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pPlacement = App.PlacementObject_GetObject(pSet, "Entry Location")
        if pPlacement:            
                        pPlayer.SetTranslate(pPlacement.GetWorldLocation())
			pPlayer.UpdateNodeOnly()


def GetRandomDS9Music(sNum):
        debug(__name__ + ", GetRandomDS9Music")
        return App.g_kSystemWrapper.GetRandomNumber(98) + sNum

def GetRandomGammaMusic(sNum):
        debug(__name__ + ", GetRandomGammaMusic")
        return App.g_kSystemWrapper.GetRandomNumber(65) + sNum

def GetRandomWormholeMusic(sNum):
        debug(__name__ + ", GetRandomWormholeMusic")
        return App.g_kSystemWrapper.GetRandomNumber(65) + sNum


# Kill the pane, fixes the crashing bug and several other bugs
def KillPane(pAction):
        debug(__name__ + ", KillPane")
        global pPaneID
        
        pPane = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(pPaneID))
	App.g_kRootWindow.DeleteChild(pPane)
		
	pPaneID = App.NULL_ID
	
	return 0
    

# Sometimes BC doesn't acknowledge AI so we 'force' him to do so       
def CreateAI(pShip):
	debug(__name__ + ", CreateAI")
	pPlayer = MissionLib.GetPlayer()

        Random = lambda fMin, fMax : App.g_kSystemWrapper.GetRandomNumber((fMax - fMin) * 1000.0) / 1000.0 - fMin
        # Range values used in the AI.
        fInRange = 150.0 + Random(-25, 20)

	#########################################
	# Creating PlainAI Intercept at (279, 253)
	pIntercept = App.PlainAI_Create(pShip, "Intercept")
	pIntercept.SetScriptModule("Intercept")
	pIntercept.SetInterruptable(1)
	pScript = pIntercept.GetScriptInstance()
	pScript.SetTargetObjectName(pPlayer.GetName())
	# Done creating PlainAI Intercept
	#########################################
	#########################################
	# Creating ConditionalAI ConditionIntercept at (148, 273)
	## Conditions:
	#### Condition HaveToIntercept
	pHaveToIntercept = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fInRange, pPlayer.GetName(), pShip.GetName())
	## Evaluation function:
	def EvalFunc(bHaveToIntercept):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bHaveToIntercept:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionIntercept = App.ConditionalAI_Create(pShip, "ConditionIntercept")
	pConditionIntercept.SetInterruptable(1)
	pConditionIntercept.SetContainedAI(pIntercept)
	pConditionIntercept.AddCondition(pHaveToIntercept)
	pConditionIntercept.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionIntercept
	#########################################
	#########################################
	# Creating PlainAI Follow at (280, 181)
	pFollow = App.PlainAI_Create(pShip, "Follow")
	pFollow.SetScriptModule("FollowObject")
	pFollow.SetInterruptable(1)
	pScript = pFollow.GetScriptInstance()
	pScript.SetFollowObjectName(pPlayer.GetName())
	pScript.SetRoughDistances(10,20,30)
	# Done creating PlainAI Follow
	#########################################
	#########################################
	# Creating ConditionalAI PlayerInSameSet at (164, 201)
	## Conditions:
	#### Condition InSet
	pInSet = App.ConditionScript_Create("Conditions.ConditionAllInSameSet", "ConditionAllInSameSet", pShip.GetName(), pPlayer.GetName())
	## Evaluation function:
	def EvalFunc(bInSet):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInSet:
			# Player is in the same set as we are.
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pPlayerInSameSet = App.ConditionalAI_Create(pShip, "PlayerInSameSet")
	pPlayerInSameSet.SetInterruptable(1)
	pPlayerInSameSet.SetContainedAI(pFollow)
	pPlayerInSameSet.AddCondition(pInSet)
	pPlayerInSameSet.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI PlayerInSameSet
	#########################################
	#########################################
	# Creating CompoundAI FollowWarp at (281, 125)
	import AI.Compound.FollowThroughWarp
	pFollowWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName())
	# Done creating CompoundAI FollowWarp
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (47, 125)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (139, 132)
	pPriorityList.AddAI(pConditionIntercept, 1)
	pPriorityList.AddAI(pPlayerInSameSet, 2)
	pPriorityList.AddAI(pFollowWarp, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (6, 188)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
