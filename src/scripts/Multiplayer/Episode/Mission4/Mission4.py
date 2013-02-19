from bcdebug import debug
# Many Modifications by Defiant <mail@defiant.homedns.org>

import App
import loadspacehelper
import MissionLib
import Mission4Menus
import DynamicMusic
import loadspacehelper
import BasicAI
import Multiplayer.MissionShared
import Multiplayer.MissionMenusShared
import string
import Foundation

# print("Loading multiplayer mission5)

#global variables
NonSerializedObjects = (
"g_kKillsDictionary",
"g_kDeathsDictionary",
"g_kScoresDictionary",
"g_kDamageDictionary",
"g_kTeamDictionary",
"g_kTeamScoreDictionary",
"g_kTeamKillsDictionary",
"g_pTeam1",
"g_pTeam2",
"g_lFirepoints",
"dict_Collisions",
"dict_Probes",
"dict_Ship_to_Group",
"dReplaceModel",
"gdShipAttrs",
)

# Global variables.  

# setup scoring objects
g_kKillsDictionary = {}
g_kDeathsDictionary = {}
g_kScoresDictionary = {}
g_kDamageDictionary = {}
g_kTeamDictionary = {}
g_kTeamScoreDictionary = {}
g_kTeamKillsDictionary = {}
g_pTeam1 = None
g_pTeam2 = None
g_bEndCutsceneStarted = 0
dict_Collisions = {}
g_lFirepoints = []

# define some messages.  Start at 20 for mission specific message types
SCORE_INIT_MESSAGE = App.MAX_MESSAGE_TYPES + 20
TEAM_SCORE_MESSAGE = App.MAX_MESSAGE_TYPES + 21
TEAM_MESSAGE = App.MAX_MESSAGE_TYPES + 22
ADD_AI_TO_TEAM_MSG = App.MAX_MESSAGE_TYPES + 23
MORE_SYSTEMS_MSG = App.MAX_MESSAGE_TYPES + 24
CLIENT_OBJECT_DESTROYED = App.MAX_MESSAGE_TYPES + 54
REMOVE_POINTER_FROM_SET = 190
REMOVE_TORP_MESSAGE_AT = 191
NO_COLLISION_MESSAGE = 192
DISABLE_TRACTOR_MESSAGE = 193 # not used here but exists
SUBSYSTEM_SET_CONDITION = 194
MP_SET_TRACTOR_MODE = 195
SET_SCRIPT_MSG = 196
ET_CLIENT_SCAN = 197
MP_REMOTE_CONTROL_MSG = 198
SET_SHIELD_CONDITION = 199
MP_SET_POSITION_MSG = 200
MP_SEND_WARP_SPEED_MSG = 201
MP_SEND_PLASMA_FX = 202
PLAYER_NOW_USING_SHIP = 203
INACCURATE_PHASERS_COMMUNICATION = 204
MP_NEW_NET_PLAYER_ID = 205
MP_WARP_ETA_MSG = 206
MP_CONSTRUCT_MSG = 207
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209
ALERT_STATE_CHANGED_MSG = 210
DELETE_OBJECT_FROM_SET_MSG = 211
SET_GET_SHIP_ATTR_MSG = 212
SET_AUTO_AI_MSG = 213
SET_STOP_AI_MSG = 214
TRACTOR_STARTED_MSG = 215

# Invalid team number
INVALID_TEAM = 255
curShipNum = 1
dict_Ship_to_Group = {}
dict_Probes = {}
dReplaceModel = {}
gdShipAttrs = {}

###############################################################################
#	GetWinString()
#	
#	Returns a string that describes who won
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def GetWinString():
	debug(__name__ + ", GetWinString")
	pFBCMPDatabase = App.g_kLocalizationManager.Load("data/TGL/FBCMP.tgl")
	
	# Play the appropriate win/lose fanfare
	if g_bStarbaseDead:
		if Mission4Menus.g_iTeam == 0:
			DynamicMusic.PlayFanfare("Win")
		else:
			DynamicMusic.PlayFanfare("Lose")
	else:
		if Mission4Menus.g_iTeam == 0:
			DynamicMusic.PlayFanfare("Lose")
		else:
			DynamicMusic.PlayFanfare("Win")

	if g_bStarbaseDead:
		return pFBCMPDatabase.GetString("PlayersWin").GetCString()
	else:
		return pFBCMPDatabase.GetString("AIShipsWin").GetCString()

# Kill the Mission database
# Heavily edited by Defiant
def Terminate(pMission):
	# print("Terminating multiplayer mission 4.")
	
	debug(__name__ + ", Terminate")
	global g_pTeam1, g_pTeam2, curShipNum
	global g_kKillsDictionary 
	global g_kDeathsDictionary 
	global g_kScoresDictionary 
	global g_kDamageDictionary 
	global g_kTeamDictionary 
	global g_kTeamScoreDictionary 
	global g_kTeamKillsDictionary 
        
        import Multiplayer.MissionShared
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Delete group2.
	g_pTeam1 = None
	g_pTeam2 = None
        pEnemyGroup = MissionLib.GetEnemyGroup()
        pFriendlyGroup = MissionLib.GetFriendlyGroup()
        pEnemyGroup = None
        pFriendlyGroup = None
	
	# Terminate common stuff, which will handle delete of mission
	# menus as well.
	Multiplayer.MissionShared.Terminate (pMission)

	# Clear dictionaries
	for iKey in g_kKillsDictionary.keys ():
		del g_kKillsDictionary[iKey]		

	for iKey in g_kDeathsDictionary.keys ():
		del g_kDeathsDictionary[iKey]		

	for iKey in g_kScoresDictionary.keys ():
		del g_kScoresDictionary[iKey]		

	for iKey in g_kDamageDictionary.keys ():
		del g_kDamageDictionary[iKey]		

	for iKey in g_kTeamDictionary.keys ():
		del g_kTeamDictionary[iKey]		

	for iKey in g_kTeamKillsDictionary.keys ():
		del g_kTeamKillsDictionary[iKey]		

	for iKey in g_kTeamScoreDictionary.keys ():
		del g_kTeamScoreDictionary[iKey]		

	Mission4Menus.g_fYPixelOffset = 0.0
	Mission4Menus.g_fXPixelOffset = 0.0

	Mission4Menus.g_iTeam = 0
	Mission4Menus.g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID

	# Global pointers to user interface items
	Mission4Menus.g_pTeamButton = None
	Mission4Menus.g_pOptionsWindowBootButton = None
	Mission4Menus.g_pOptionsWindowPlayerMenu = None

        curShipNum = 1
        
        # Foundation deactivate
        if Mission4Menus.qbGameMode:
		if Mission4Menus.QBGameModeActivated:
                	Mission4Menus.qbGameMode.Deactivate()
                Mission4Menus.qbGameMode = None
        Mission4Menus.StartMissionRunOnce = 0
	Mission4Menus.QBGameModeActivated = 0
	Mission4Menus.BridgeStartOnce = 0
	Mission4Menus.Mission4StartOnce = 0
	Mission4Menus.g_iSystem = []
	Mission4Menus.lastSystem = 0


#Episode level stuff
def CreateMenus():
	debug(__name__ + ", CreateMenus")
	return 0


def RemoveHooks():
	debug(__name__ + ", RemoveHooks")
	return


###############################################################################
#	PreLoadAssets()
#	
#	This is called once, at the beginning of the mission before Initialize()
#	to allow us to add models to be pre loaded
#	
#	Args:	pMission	- the Mission object
#	
#	Return:	none
###############################################################################
def PreLoadAssets(pMission):
	debug(__name__ + ", PreLoadAssets")
	return


#Mission startup
def Initialize(pMission):
        # Set the difficulty level.
        debug(__name__ + ", Initialize")
        App.Game_SetDifficultyMultipliers(1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        
        # Make sure Engineering Extension is not loaded yet.
        Mission4Menus.LoadQBautostart(0)
        
        # print("Multiplayer mission start.")
	# Call common initialize routine
        #import Multiplayer.MissionShared
	#Multiplayer.MissionShared.Initialize(pMission)
	import LoadBridge
	LoadBridge.CreateCharacterMenus()
	### MissionShared start
	# Load database
	Multiplayer.MissionShared.g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Multiplayer.tgl")
	Multiplayer.MissionShared.g_pShipDatabase = App.g_kLocalizationManager.Load("data/TGL/Ships.tgl")
	Multiplayer.MissionShared.g_pSystemDatabase = App.g_kLocalizationManager.Load("data/TGL/Systems.tgl")

	#Setup event handlers
	#Multiplayer.MissionShared.SetupEventHandlers(pMission)
	
	Multiplayer.MissionShared.g_idTimeLeftTimer = App.NULL_ID
	Multiplayer.MissionShared.g_bGameOver = 0
	Multiplayer.MultiplayerMenus.g_bExitPressed = 0

	# Load string database
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
	pGame = App.Game_GetCurrentGame()
	pGame.LoadDatabaseSoundInGroup(pDatabase, "MiguelScan", "BridgeGeneric")
	pGame.LoadDatabaseSoundInGroup(pDatabase, "gs038", "BridgeGeneric")
	App.g_kLocalizationManager.Unload(pDatabase)
	# Now we're done.  The menu will do the work to create the ship.
	### MissionShared end

	global g_bStarbaseDead
	g_bStarbaseDead = 0

	if (App.g_kUtopiaModule.IsHost()):	
		Mission4Menus.BuildMission4Menus()

	#Setup event handlers
	SetupEventHandlers(pMission)

	if (App.g_kUtopiaModule.IsHost() and App.g_kUtopiaModule.IsClient()):
		pNetwork = App.g_kUtopiaModule.GetNetwork()
		iPlayerID = pNetwork.GetHostID()

		if (not g_kKillsDictionary.has_key(iPlayerID)):
			# Add a blank key
			global g_kKillsDictionary
			g_kKillsDictionary[iPlayerID] = 0		# No kills

		if (not g_kDeathsDictionary.has_key(iPlayerID)):
			# Add a blank key
			global g_kDeathsDictionary
			g_kDeathsDictionary[iPlayerID] = 0		# No kills

	# Initialize team scores for two teams
	global g_kTeamScoreDictionary
	g_kTeamScoreDictionary[0] = 0
	g_kTeamScoreDictionary[1] = 0

	# Create the group of Team1 Name for the Ships AI
	global g_pTeam1
	g_pTeam1 = App.ObjectGroupWithInfo()
	
	# Create the group of Team2 Name for the Ships AI
	global g_pTeam2
	g_pTeam2 = App.ObjectGroupWithInfo()


def ProbeLaunched(pObject, pEvent):
        debug(__name__ + ", ProbeLaunched")
        global dict_Probes

        list = []
        pProbe = App.ShipClass_Cast(pEvent.GetSource())
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pProbe or not pShip:
                return
        
        pLaunchingShipID = pShip.GetNetPlayerID()

        if dict_Probes.has_key(pLaunchingShipID):
                for Probe in dict_Probes[pLaunchingShipID]:
                        list.append(Probe)
        list.append(pProbe.GetName())

        dict_Probes[pLaunchingShipID] = list
        
        pObject.CallNextHandler(pEvent)


def SendSubsystemCondition(iShipObjID, sSubsystenName, iNewCondition):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", SendSubsystemCondition")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a byte buffer.
        kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SUBSYSTEM_SET_CONDITION))
        
        # send Message
        kStream.WriteInt(iShipObjID)
        for i in range(len(sSubsystenName)):
                kStream.WriteChar(sSubsystenName[i])
        # set the last char:
        kStream.WriteChar('\0')
        kStream.WriteInt(iNewCondition)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def DamageShip(pShip, kLocation, fRadius, fDamage):
	debug(__name__ + ", DamageShip")
	pPropSet = pShip.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
        iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
	
	pShipSubSystemPropInstanceList.TGBeginIteration()
	for i in range(iNumItems):
		pInstance = pShipSubSystemPropInstanceList.TGGetNext()
		pProperty = App.SubsystemProperty_Cast(pInstance.GetProperty())
		pSubsystem = pShip.GetSubsystemByProperty(pProperty)
		fNewCondition = None
		# Get Distance between Points
		vDifference = pSubsystem.GetWorldLocation()
		vDifference.Subtract(kLocation)
		fPointDist = vDifference.Length()
                # check Radius: if they overlap => Damage
		fDamageDist = pSubsystem.GetRadius() + fRadius
		
                # Damage for the Hull works a bit different
                if pSubsystem.GetName() == pShip.GetHull().GetName():
                        fdiff = pShip.GetHull().GetRadius() - fRadius / 5.0
                        if fdiff > 0.0:
                                fDamageTodo = fdiff * fDamage
                                fNewCondition = pSubsystem.GetCondition() - fDamageTodo
                        else:
                                fNewCondition = 0.0
                        
		elif fPointDist <= fDamageDist:
			# Damage Subsystem according to distance (linear)
			fDamagePercent = (0.0 - fDamage) / (fRadius - 0.0)
			# mx + b
			fDamageTodo = fDamagePercent * fPointDist / 5.0 + fDamage
			fNewCondition = pSubsystem.GetCondition() - fDamageTodo

                if fNewCondition:
                        if not App.g_kUtopiaModule.IsHost():
                                SendSubsystemCondition(pShip.GetObjID(), pSubsystem.GetName(), fNewCondition)
                        else:
			        if fNewCondition <= 0.0:
				        pShip.DestroySystem(pSubsystem)
                                else:
			                pSubsystem.SetCondition(fNewCondition)
		
	pShipSubSystemPropInstanceList.TGDoneIterating()


def ObjectCollisionHandler(pObject, pEvent):
        # Ai Ships doesn't seem to get collision damage: this is a work around
        debug(__name__ + ", ObjectCollisionHandler")
        global dict_Collisions

	pObjectHitting	= App.ObjectClass_Cast(pEvent.GetSource())
	pObjectHit	= App.ObjectClass_Cast(pEvent.GetDestination())

        pShip1 = App.ShipClass_Cast(pObjectHitting)
        pShip2 = App.ShipClass_Cast(pObjectHit)
        
        if pShip1:
                if dict_Collisions.has_key(pShip1.GetName()):
                        for lDamagePoint in dict_Collisions[pShip1.GetName()]:
                                kLocation = lDamagePoint[0]
                                fDamage = lDamagePoint[1]
                                fRadius = pShip1.GetHull().GetRadius()
                                
				if pShip2:
                                	DamageShip(pShip2, kLocation, fRadius, fDamage)
				elif dict_Collisions.has_key(pShip1.GetName()):
                                	del dict_Collisions[pShip1.GetName()]
                if pShip2:
                        # AI AI Collisions
                        if pShip1.GetNetPlayerID() < 0 and pShip2.GetNetPlayerID() < 0:
                                if pShip1.GetHull().GetCondition() > pShip2.GetHull().GetCondition():
                                        pShip1.GetHull().SetCondition(pShip1.GetHull().GetCondition() - pShip2.GetHull().GetCondition() * 5)
                                        if pShip1.GetHull().GetCondition() <= 0.0:
                                                pShip1.DestroySystem(pShip1.GetHull())
                                        pShip2.DestroySystem(pShip2.GetHull())
                                elif pShip1.GetHull().GetCondition() < pShip2.GetHull().GetCondition():
                                        pShip2.GetHull().SetCondition(pShip2.GetHull().GetCondition() - pShip1.GetHull().GetCondition())
                                        pShip1.DestroySystem(pShip1.GetHull())
                                else:
                                        pShip1.DestroySystem(pShip1.GetHull())
                                        pShip2.DestroySystem(pShip2.GetHull())

        if pShip2:
                if not pObjectHitting:
                        # ok, we have a ship that was hit, but not a ship that is the hitter
                        # good chane, that the hitter is AI ship
                        dict_Collisions[pShip2.GetName()] = []
                        for i in range(pEvent.GetNumPoints()):
                                dict_Collisions[pShip2.GetName()].append([pEvent.GetPoint(i), pEvent.GetCollisionForce()])

	pObject.CallNextHandler(pEvent)



def TractorBeamOn(pObject, pEvent):
	pTractorProjector	= App.TractorBeamProjector_Cast(pEvent.GetSource())
	pTractorSystem		= App.TractorBeamSystem_Cast(pTractorProjector.GetParentSubsystem())
	pShip 			= pTractorSystem.GetParentShip()
	
	if pShip:
		kStream = App.TGBufferStream()
        	# Open the buffer stream with a 256 byte buffer.
        	kStream.OpenBuffer(256)
        	# Write relevant data to the stream.
        	# First write message type.
        	kStream.WriteChar(chr(TRACTOR_STARTED_MSG))

		# send Message
		kStream.WriteInt(pShip.GetObjID())

        	pMessage = App.TGMessage_Create()
        	# Yes, this is a guaranteed packet
        	pMessage.SetGuaranteed(1)
        	# Okay, now set the data from the buffer stream to the message
        	pMessage.SetDataFromStream(kStream)
        	# Send the message to everybody but me.  Use the NoMe group, which
        	# is set up by the multiplayer game.
	        pNetwork = App.g_kUtopiaModule.GetNetwork()
	        if not App.IsNull(pNetwork):
        	        if App.g_kUtopiaModule.IsHost():
                	        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                	else:
                        	pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        	# We're done.  Close the buffer.
        	kStream.CloseBuffer()
	
	pObject.CallNextHandler(pEvent)


# setup any event handlers specific to this mission.
def SetupEventHandlers(pMission):
        debug(__name__ + ", SetupEventHandlers")
        if App.g_kUtopiaModule.IsHost():
                # Only hosts handling scoring.
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".DamageEventHandler")
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectKilledHandler")
        else:
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectKilledHandlerClient")
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_FIRING, pMission, __name__+ ".TractorBeamOn")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NEW_PLAYER_IN_GAME, pMission, __name__ + ".NewPlayerHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_DELETE_PLAYER, pMission, __name__ + ".DeletePlayerHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_NAME_CHANGE_EVENT, pMission, __name__ + ".ProcessNameChangeHandler")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_COLLISION, pMission, __name__ + ".ObjectCollisionHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_ALERT_LEVEL, pMission, __name__ + ".AlertStateChanged")

	# setup handler for listening for packets.
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, pMission, __name__ + ".ProcessMessageHandler")

        import Multiplayer.MissionShared
	pMission.AddPythonFuncHandlerForInstance(Multiplayer.MissionShared.ET_RESTART_GAME, __name__ + ".RestartGameHandler")

        if App.g_kUtopiaModule.IsHost():
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_LAUNCH_PROBE, pMission, __name__+ ".ProbeLaunched")


def AlertStateChanged(pObject, pEvent):
	debug(__name__ + ", AlertStateChanged")
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	
	if pShip:
		kStream = App.TGBufferStream()
        	# Open the buffer stream with a 256 byte buffer.
        	kStream.OpenBuffer(256)
        	# Write relevant data to the stream.
        	# First write message type.
        	kStream.WriteChar(chr(ALERT_STATE_CHANGED_MSG))

		# send Message
		kStream.WriteInt(pShip.GetObjID())
		kStream.WriteInt(pShip.GetAlertLevel())

        	pMessage = App.TGMessage_Create()
        	# Yes, this is a guaranteed packet
        	pMessage.SetGuaranteed(1)
        	# Okay, now set the data from the buffer stream to the message
        	pMessage.SetDataFromStream(kStream)
        	# Send the message to everybody but me.  Use the NoMe group, which
        	# is set up by the multiplayer game.
	        pNetwork = App.g_kUtopiaModule.GetNetwork()
	        if not App.IsNull(pNetwork):
        	        if App.g_kUtopiaModule.IsHost():
                	        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                	else:
                        	pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        	# We're done.  Close the buffer.
        	kStream.CloseBuffer()

	pObject.CallNextHandler(pEvent)


def ProcessNameChangeHandler(self, pEvent):
        debug(__name__ + ", ProcessNameChangeHandler")
        import Multiplayer.MissionMenusShared
	if (Multiplayer.MissionMenusShared.g_pInfoPane != None):
		# A player's name has changed.  Rebuild the info pane.
		Mission4Menus.RebuildInfoPane()
	self.CallNextHandler(pEvent)


def ProcessMessageHandler(self, pEvent):
        debug(__name__ + ", ProcessMessageHandler")
        global g_pTeam1, g_pTeam2, dict_Ship_to_Group
        import Multiplayer.MissionShared
        import Multiplayer.MissionMenusShared
	import Multiplayer.SpeciesToSystem # the imports have to stay here - the game does forget them
	pMission = MissionLib.GetMission()
	if (pMission == None):
		# Mission is over, don't process messages.
		return

	pMessage = pEvent.GetMessage()
	if pMessage:
		# Get the data from the message
		# Open a buffer stream to read the data
		kStream = pMessage.GetBufferStream();

		cType = kStream.ReadChar();

		cType = ord(cType)

		if (cType == Multiplayer.MissionShared.MISSION_INIT_MESSAGE):
			# print("Process mission init message")

			# Read the max number of players
			Multiplayer.MissionMenusShared.g_iPlayerLimit = ord(kStream.ReadChar())

			iNum = ord (kStream.ReadChar())
			if (iNum == 255):
				Multiplayer.MissionMenusShared.g_iTimeLimit = -1
			else:
				Multiplayer.MissionMenusShared.g_iTimeLimit = iNum
				iEndTime = kStream.ReadInt()
				Multiplayer.MissionShared.CreateTimeLeftTimer(iEndTime - int(App.g_kUtopiaModule.GetGameTime()))

			iNum = ord (kStream.ReadChar ())
			if (iNum == 255):
				Multiplayer.MissionMenusShared.g_iFragLimit = -1
			else:
				Multiplayer.MissionMenusShared.g_iFragLimit = iNum

			# Create the system
#			debug("Creating system")
			# Read the system species
			Mission4Menus.lastSystem = kStream.ReadInt()
			Multiplayer.MissionShared.g_pStartingSet = Multiplayer.SpeciesToSystem.CreateSystemFromSpecies(Mission4Menus.lastSystem)
			Mission4Menus.g_iSystem = []
                        while(1):
                                mySystem = kStream.ReadInt()
                                if mySystem == 0:
                                        break
				if mySystem != Mission4Menus.lastSystem:
					Mission4Menus.g_iSystem.append(mySystem)
					pSet = Multiplayer.SpeciesToSystem.CreateSystemFromSpecies(mySystem)
			
			Mission4Menus.BuildMission4Menus()

			# Update info
			Mission4Menus.ResetLimitInfo()
			Mission4Menus.RebuildInfoPane()
		elif (cType == Multiplayer.MissionShared.SCORE_CHANGE_MESSAGE):
			# print("Process score change message")

			global g_kScoresDictionary

			# Read the player id of killer
			iFiringPlayerID = kStream.ReadLong()

			iKills = 0
			if (iFiringPlayerID != 0):
				# Read the kills
				iKills = kStream.ReadLong()

				# Read the firing player's score
				g_kScoresDictionary[iFiringPlayerID] = kStream.ReadLong()

			# Read the player id of killed
			iKilledPlayerID = kStream.ReadLong()

			# Read the deaths
			iDeaths = kStream.ReadLong()

			# Read the number of players
			iScoreCount = ord(kStream.ReadChar())
			# print("Received " + str (iScoreCount) + "scores")

			while (iScoreCount > 0):
				iPlayerID = kStream.ReadLong()
				if (iPlayerID != 0):
					iPlayerScore = kStream.ReadLong()

					g_kScoresDictionary [iPlayerID] = iPlayerScore
				iScoreCount = iScoreCount - 1

			UpdateScore(iFiringPlayerID, iKills, iKilledPlayerID, iDeaths)

		elif (cType == Multiplayer.MissionShared.SCORE_MESSAGE):
			# print("Process score message")

			global g_kKillsDictionary
			global g_kDeathsDictionary
			global g_kScoresDictionary


			# Read the key id.
			iKey = kStream.ReadLong()

			# Read Kills
			iKills = kStream.ReadLong()

			# Read deaths
			iDeaths = kStream.ReadLong()
			
			# Read score
			iScore = kStream.ReadLong ()
			
			g_kKillsDictionary[iKey] = iKills
			g_kDeathsDictionary[iKey] = iDeaths
			g_kScoresDictionary[iKey] = iScore

			Mission4Menus.RebuildPlayerList()

		elif (cType == Multiplayer.MissionShared.RESTART_GAME_MESSAGE):
			print("Process restart game message")
			RestartGame()
                        
		elif (cType == SCORE_INIT_MESSAGE):
			# print("Process score init message")

			global g_kKillsDictionary
			global g_kDeathsDictionary
			global g_kScoresDictionary
			global g_kTeamDictionary

			# Read the key id.
			iKey = kStream.ReadLong()

			# Read Kills
			iKills = kStream.ReadLong()

			# Read deaths
			iDeaths = kStream.ReadLong()
			
			# Read score
			iScore = kStream.ReadLong()
			
			# Read score
			iTeam = kStream.ReadChar()
			iTeam = ord(iTeam)
			
			g_kKillsDictionary[iKey] = iKills
			g_kDeathsDictionary[iKey] = iDeaths
			g_kScoresDictionary[iKey] = iScore
			g_kTeamDictionary[iKey] = iTeam

			Mission4Menus.RebuildPlayerList()

		elif (cType == TEAM_MESSAGE):
			# print("Process team message")
			global g_kTeamDictionary

			iKey = kStream.ReadLong()
			iTeam = kStream.ReadChar()
			iTeam = ord(iTeam)

			g_kTeamDictionary[iKey] = iTeam
                        
			if (App.g_kUtopiaModule.IsHost()):
				# If I'm the host, I have to forward this information to
				# everybody else so they'll know what team this player is on
				pNetwork = App.g_kUtopiaModule.GetNetwork()
				if (pNetwork):
					pCopyMessage = pMessage.Copy()
					pNetwork.SendTGMessageToGroup("NoMe", pCopyMessage)

			Mission4Menus.RebuildPlayerList()

                # Msg from Host that a new Ship has been added and belongs to a Group.
                elif (cType == ADD_AI_TO_TEAM_MSG):
                        iName = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                iName = iName + iChar
                        iValue = kStream.ReadLong()
                        
                        # check if this ship already exists
                        pShip = MissionLib.GetShip(iName)
                        if pShip:
                                pShip.SetNetPlayerID(iValue)
                                if iValue == -1:
                                        AddNameToGroup(g_pTeam1, pShip.GetName())
                                        RemoveNameFromGroup(g_pTeam2, pShip.GetName())
                                        ResetEnemyFriendlyGroups()
                                elif iValue == -2:
                                        AddNameToGroup(g_pTeam2, pShip.GetName())
                                        RemoveNameFromGroup(g_pTeam1, pShip.GetName())
                                        ResetEnemyFriendlyGroups()
                        # else wait before it is created
                        else:
                                dict_Ship_to_Group[iName] = iValue
                        
                        
                        if App.g_kUtopiaModule.IsHost():
                                SendGroupInfo(iName, iValue)
                
                elif (cType == MORE_SYSTEMS_MSG):
			print "Error: Can't handle MORE_SYSTEMS_MSG", MORE_SYSTEMS_MSG
                
                elif cType == CLIENT_OBJECT_DESTROYED:
                        # Read the player id of killer
                        ObjectDestroyed = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                ObjectDestroyed = ObjectDestroyed + iChar
                        #print(ObjectDestroyed, "has been killed (client msg)")
                        pDestroyedShip = MissionLib.GetShip(ObjectDestroyed)
                        # finally kill it
                        if pDestroyedShip:
                                pDestroyedShip.DestroySystem(pDestroyedShip.GetHull())
                
                elif cType == REMOVE_POINTER_FROM_SET:
                        ObjectRemoved = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                ObjectRemoved = ObjectRemoved + iChar
                        #print(ObjectRemoved, "Removing Pointer")
                        
                        # Host: send message to others
                        pNetwork = App.g_kUtopiaModule.GetNetwork()
                        if App.g_kUtopiaModule.IsHost() and pNetwork:
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(REMOVE_POINTER_FROM_SET))
                                        
                                for i in range(len(ObjectRemoved)):
                                        kStream.WriteChar(ObjectRemoved[i])
                                # set the last char:
                                kStream.WriteChar('\0')

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream)

                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
                        
                        pPointerRemoved = MissionLib.GetShip(ObjectRemoved)
                        if pPointerRemoved:
                                pPointerRemoved.GetContainingSet().RemoveObjectFromSet(ObjectRemoved)
                
                elif cType == REMOVE_TORP_MESSAGE_AT:
                        SenderHostID = kStream.ReadInt()
                        
                        kLocation = App.TGPoint3()
                        posX = kStream.ReadFloat()
                        posY = kStream.ReadFloat()
                        posZ = kStream.ReadFloat()
                        
                        kLocation.SetXYZ(posX, posY, posZ)
                        
                        minD = 10
                        pTorpminD = None
                        pPlayer = MissionLib.GetPlayer()
                        if pPlayer:
                                pSet = pPlayer.GetContainingSet()
                                lObjects = pSet.GetClassObjectList(App.CT_TORPEDO)
                                for pObject in lObjects:
                                        pTorp = App.Torpedo_GetObjectByID(None, pObject.GetObjID())
                                        vDifference = pTorp.GetWorldLocation()
                                        vDifference.Subtract(kLocation)
                                        if vDifference.Length() < minD:
                                                minD = vDifference.Length()
                                                pTorpminD = pTorp
                        
                        pNetwork = App.g_kUtopiaModule.GetNetwork()
                        if pTorpminD and pNetwork and SenderHostID != pNetwork.GetLocalID():
                                pTorpminD.SetLifetime(0.9)
                                # Host: send message to others
                                if App.g_kUtopiaModule.IsHost():
                                        # Now send a message to everybody else that the score was updated.
                                        # allocate the message.
                                        pMessage2 = App.TGMessage_Create()
                                        pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                        # Setup the stream.
                                        kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                        kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                        # Write relevant data to the stream.
                                        # First write message type.
                                        kStream2.WriteChar(chr(REMOVE_TORP_MESSAGE_AT))
                                        
                                        kStream2.WriteInt(SenderHostID)
                                        kStream2.WriteFloat(pTorpminD.GetWorldLocation().GetX())
                                        kStream2.WriteFloat(pTorpminD.GetWorldLocation().GetY())
                                        kStream2.WriteFloat(pTorpminD.GetWorldLocation().GetZ())

                                        # Okay, now set the data from the buffer stream to the message
                                        pMessage2.SetDataFromStream(kStream)

                                        # Send the message to everybody but me.  Use the NoMe group, which
                                        # is set up by the multiplayer game.
                                        pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                        # We're done.  Close the buffer.
                                        kStream2.CloseBuffer()
                        
                elif cType == NO_COLLISION_MESSAGE:
                        Object1Id = kStream.ReadInt()
                        Object2Id = kStream.ReadInt()
                        CollisionYesNo = kStream.ReadInt()
                        DisableCollisionTimer(None, Object1Id, Object2Id, CollisionYesNo, 100)
                                
                        # Host: send message to others
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(NO_COLLISION_MESSAGE))
                                        
                                kStream2.WriteInt(Object1Id)
                                kStream2.WriteInt(Object2Id)
                                kStream2.WriteInt(CollisionYesNo)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
                
                elif cType == SUBSYSTEM_SET_CONDITION:
                        ObjectId = kStream.ReadInt()
                        pShip = App.ShipClass_GetObjectByID(None, ObjectId)
                        
                        sSubsystemName = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                sSubsystemName = sSubsystemName + iChar
                                
                        iNewCondition = kStream.ReadInt()
                        
                        pSubsystem = MissionLib.GetSubsystemByName(pShip, sSubsystemName)
                        if pSubsystem:
                                if iNewCondition > 0.0:
                                        pSubsystem.SetCondition(iNewCondition)
                                else:
                                        pShip.DestroySystem(pSubsystem)
                
                elif cType == SET_SHIELD_CONDITION:
                        ObjectId = kStream.ReadInt()
                        iShield = kStream.ReadInt()
                        iNewCondition = kStream.ReadInt()
                        pShip = App.ShipClass_GetObjectByID(None, ObjectId)
                        if pShip:
                                pShields = pShip.GetShields()
				if pShields:
					pShields.SetCurShields(iShield, iNewCondition)
					
                elif cType == MP_SET_TRACTOR_MODE:
                        iShipObjID = kStream.ReadInt()
                        iMode = kStream.ReadInt()
                        
                        pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
                        if pShip:
                                pTractorSystem = pShip.GetTractorBeamSystem()
                                if pTractorSystem:
                                        pTractorSystem.SetMode(iMode)
                        
                        # forward Message
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(MP_SET_TRACTOR_MODE))
                                        
                                kStream2.WriteInt(iShipObjID)
                                kStream2.WriteInt(iMode)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
		
		elif cType == SET_SCRIPT_MSG:
			iShipObjID = kStream.ReadInt()
                        sShipScript = ""
                        while(1):
                                iChar = kStream.ReadChar()
                                if iChar == '\0':
                                        break
                                sShipScript = sShipScript + iChar
		
			pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
			if pShip and not pShip.GetScript():
				pShip.SetScript(sShipScript)
			
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(SET_SCRIPT_MSG))
                                        
                                kStream2.WriteInt(iShipObjID)
                                for i in range(len(sShipScript)):
                                        kStream.WriteChar(sShipScript[i])
                                # set the last char:
                                kStream.WriteChar('\0')

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
                elif cType == ET_CLIENT_SCAN:
                        iShipObjID = kStream.ReadInt()
                        pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
                        if pShip:
                                try:
                                        import Custom.QBautostart.CloakCounterMeasures
                                        Custom.QBautostart.CloakCounterMeasures.ShipScan(pShip)
                                except:
                                        pass

		elif cType == MP_SET_POSITION_MSG:
			iShipObjID = kStream.ReadInt()
			iUpdateAlignToVectors = kStream.ReadInt()
			
			posX = kStream.ReadFloat()
			posY = kStream.ReadFloat()
			posZ = kStream.ReadFloat()
			forwardX = kStream.ReadFloat()
			forwardY = kStream.ReadFloat()
			forwardZ = kStream.ReadFloat()
			upX = kStream.ReadFloat()
			upY = kStream.ReadFloat()
			upZ = kStream.ReadFloat()
			
			pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
			kLocation = App.TGPoint3()
			kforward = App.TGPoint3()
			kup = App.TGPoint3()
			kLocation.SetXYZ(posX, posY, posZ)
			kforward.SetXYZ(forwardX, forwardY, forwardZ)
			kup.SetXYZ(upX, upY, upZ)
			if pShip:
				pShip.SetTranslate(kLocation)
				if iUpdateAlignToVectors:
					pShip.AlignToVectors(kforward, kup)
			else:
				print "Warning: Didn't found ship to set position for"
		
		elif cType == MP_SEND_PLASMA_FX:
			iShipObjID = kStream.ReadInt()
			posX = kStream.ReadFloat()
			posY = kStream.ReadFloat()
			posZ = kStream.ReadFloat()
			iEngine = kStream.ReadInt()
			fVentTime = kStream.ReadFloat()
			
			pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
			vEmitDir = App.NiPoint3(posX, posY, posZ)
			if pShip:
				try:
					from Custom.NanoFXv2.SpecialFX.PlasmaFX import CreatePlasmaFXNoEvent
					pPlasma = CreatePlasmaFXNoEvent(pShip, vEmitDir, iEngine, fVentTime)
				
					if pPlasma:
						pSequence = App.TGSequence_Create()
						pSequence.AddAction(pPlasma)
						pSequence.Play()
				
				except:
					print "No NanoFX2 found. Not creating PlasmaFX"

		elif cType == MP_NEW_NET_PLAYER_ID:
			iShipObjID = kStream.ReadInt()
			iNetID = kStream.ReadInt()
			
			pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
			if pShip:
				pShip.SetNetPlayerID(iNetID)
		
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():
				# check if we should kill the ai first
				if iNetID >= 0 and pShip and pShip.GetAI():
					print "Clearing AI of ", pShip.GetName()
					pShip.ClearAI()
				
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(MP_NEW_NET_PLAYER_ID))
                                        
                                kStream2.WriteInt(iShipObjID)
                                kStream2.WriteInt(iNetID)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
		
		elif cType == MP_WARP_ETA_MSG:
			iShipID = kStream.ReadInt()
			iETA = kStream.ReadInt()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				try:
					from Custom.QBautostart.Libs.LibWarp import dWarpScenes
					if dWarpScenes.has_key(pShip.GetName()):
						pWarp = dWarpScenes[pShip.GetName()]
						pWarp.iTimeToWarp = iETA
				except ImportError:
					pass

		elif cType == REPLACE_MODEL_MSG:
			iShipID = kStream.ReadInt()
			sNewShipScript = ""
			iLen = kStream.ReadShort()
			for i in range(iLen):
				sNewShipScript = sNewShipScript + kStream.ReadChar()
			
			SetNewModel(iShipID, sNewShipScript)

			if App.g_kUtopiaModule.IsHost():
				dReplaceModel[iShipID] = sNewShipScript
				
				# if we are host, tell others
				SentReplaceModelMessage(iShipID, sNewShipScript)

		elif cType == SET_TARGETABLE_MSG:
			iShipID = kStream.ReadInt()
			iMode = kStream.ReadInt()
			
			SetTargetableModeTimer(None, iShipID, iMode, 500)
			
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():				
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(SET_TARGETABLE_MSG))
                                        
                                kStream2.WriteInt(iShipID)
                                kStream2.WriteInt(iMode)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()
		
		elif cType == ALERT_STATE_CHANGED_MSG:
			iShipID = kStream.ReadInt()
			iLevel = kStream.ReadInt()

			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip and pShip.GetAlertLevel() != iLevel:
				pAlertEvent = App.TGIntEvent_Create()
				pAlertEvent.SetDestination(pShip)
				pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
				pAlertEvent.SetInt(iLevel)
				App.g_kEventManager.AddEvent(pAlertEvent)
				
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():				
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(ALERT_STATE_CHANGED_MSG))
                                        
                                kStream2.WriteInt(iShipID)
                                kStream2.WriteInt(iLevel)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()

		elif cType == DELETE_OBJECT_FROM_SET_MSG:
			iShipID = kStream.ReadInt()
			
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				DeleteObjectFromSet(pShip.GetContainingSet(), pShip)
				
			# if we are host, tell others
                        if App.g_kUtopiaModule.IsHost():				
                                pNetwork = App.g_kUtopiaModule.GetNetwork()
                                # Now send a message to everybody else that the score was updated.
                                # allocate the message.
                                pMessage2 = App.TGMessage_Create()
                                pMessage2.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                                # Setup the stream.
                                kStream2 = App.TGBufferStream()		# Allocate a local buffer stream.
                                kStream2.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
                                # Write relevant data to the stream.
                                # First write message type.
                                kStream2.WriteChar(chr(DELETE_OBJECT_FROM_SET_MSG))
                                        
                                kStream2.WriteInt(iShipID)

                                # Okay, now set the data from the buffer stream to the message
                                pMessage2.SetDataFromStream(kStream)
                                
                                # Send the message to everybody but me.  Use the NoMe group, which
                                # is set up by the multiplayer game.
                                pNetwork.SendTGMessageToGroup("NoMe", pMessage2)
                                # We're done.  Close the buffer.
                                kStream2.CloseBuffer()

		elif cType == SET_GET_SHIP_ATTR_MSG:
			iMode = kStream.ReadInt()
			iShipID = kStream.ReadInt()
			iShipFromID = kStream.ReadInt()
			SetGetShipAttrsTimer(None, iMode, iShipID, iShipFromID, 500)
		
		elif cType == SET_AUTO_AI_MSG:
			iShipID = kStream.ReadInt()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				autoAI(pShip)

		elif cType == SET_STOP_AI_MSG:
			iShipID = kStream.ReadInt()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				import AI.Player.Stay
				pShip.SetAI(AI.Player.Stay.CreateAI(pShip))
		
		elif cType == TRACTOR_STARTED_MSG:
			iShipID = kStream.ReadInt()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if pShip:
				pTractorSystem = pShip.GetTractorBeamSystem()
				if pTractorSystem:
					pTractorSystem.TurnOn()

		kStream.Close()


def SetGetShipAttrsTimer(pAction, iMode, iShipID, iShipFromID, iTry):
	debug(__name__ + ", SetGetShipAttrsTimer")
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if pShip:
		if iMode == 0: # get
			MPGetShipAttributes(pShip)
		elif iMode == 1: # set
			MPSetShipAttributes(pShip, iShipFromID)
	elif iTry > 0:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "SetGetShipAttrsTimer", iMode, iShipID, iShipFromID, iTry-1), 0.01)
		pSeq.Play()
	else:
		print "Was unable to set/get ship attributes"
	return 0


def SetNewModel(iShipID, sNewShipScript):
	debug(__name__ + ", SetNewModel")
	pShip = App.ShipClass_GetObjectByID(None, iShipID)

	if pShip and sNewShipScript:
		ShipScript = __import__(('ships.' + sNewShipScript))
		ShipScript.LoadModel()
		kStats = ShipScript.GetShipStats()
		pShip.SetupModel(kStats['Name'])
	else:
		print "Warning: Can not replace Model"


def SetTargetableModeTimer(pAction, iShipID, iMode, iTry):
	debug(__name__ + ", SetTargetableModeTimer")
	pShip = App.ShipClass_GetObjectByID(None, iShipID)
	if pShip:
		pShip.SetTargetable(iMode)
	elif iTry > 0:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "SetTargetableModeTimer", iShipID, iMode, iTry-1), 0.01)
		pSeq.Play()
	else:
		print "Was unable to set targetable mode"
	return 0


def DisableCollisionTimer(pAction, Object1Id, Object2Id, CollisionYesNo, iTry):
	debug(__name__ + ", DisableCollisionTimer")
	pObject1 = App.DamageableObject_GetObjectByID(None, Object1Id)
	pObject2 = App.DamageableObject_GetObjectByID(None, Object2Id)
	if pObject1 and pObject2:
		pObject1.EnableCollisionsWith(pObject2, CollisionYesNo)
		pObject2.EnableCollisionsWith(pObject1, CollisionYesNo)
	elif iTry > 0:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DisableCollisionTimer", Object1Id, Object2Id, CollisionYesNo, iTry-1), 0.1)
		pSeq.Play()
	else:
		print "Warning: Was unable to toggle collisions for objects"
	return 0


# This method is called if you are the host and a new player joins.  Use this
# method to send any relevant information about the game to the player joining.
# For example, the name of the system that the mission takes place in would
# be something the hosts decides in his menus and then sends to other players.
def InitNetwork(iToID):
	debug(__name__ + ", InitNetwork")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if (not pNetwork):
		# Huh?  No network?  bail.
		return

	###############################################################
	# Send mission init message with info needed to start mission
	# allocate the message.
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(Multiplayer.MissionShared.MISSION_INIT_MESSAGE))

	# Write the maximum number of players
	kStream.WriteChar(chr(Multiplayer.MissionMenusShared.g_iPlayerLimit))

	if (Multiplayer.MissionMenusShared.g_iTimeLimit == -1):
		kStream.WriteChar(chr(255))
	else:
		kStream.WriteChar(chr(Multiplayer.MissionMenusShared.g_iTimeLimit))
		kStream.WriteInt(Multiplayer.MissionShared.g_iTimeLeft + int(App.g_kUtopiaModule.GetGameTime()))

	if (Multiplayer.MissionMenusShared.g_iFragLimit == -1):
		kStream.WriteChar(chr(255))
	else:
		kStream.WriteChar(chr(Multiplayer.MissionMenusShared.g_iFragLimit))

	# Write the system species
	kStream.WriteInt(Mission4Menus.lastSystem)
	
	for mySystem in Mission4Menus.g_iSystem:
		kStream.WriteInt(mySystem)
	kStream.WriteInt(0)
	
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)

	# Send the message.
	pNetwork.SendTGMessage(iToID, pMessage)

	# We're done.  Close the buffer.
	kStream.CloseBuffer()

	###############################################################
	# Send the scores for each player in the dictionary
	# allocate the message.
	global g_kKillsDictionary
	global g_kDeathsDictionary
	global g_kScoresDictionary
	global g_kTeamDictionary
	global g_kTeamKillsDictionary
	global g_kTeamScoreDictionary


	# Construct a new dictionary containing the keys of 
	# people in the game.
	pDict = {}

	for iKey in g_kKillsDictionary.keys ():
		pDict[iKey] = 1

	for iKey in g_kDeathsDictionary.keys ():
		pDict[iKey] = 1

	for iKey in g_kScoresDictionary.keys ():
		pDict[iKey] = 1

	for iKey in g_kTeamDictionary.keys ():
		pDict[iKey] = 1
                
	# Now go through the keys in the new dictionary
	# and send that person's score around.

	for iKey in pDict.keys():
		iKills = 0
		iDeaths = 0
		iScore = 0
		iTeam = INVALID_TEAM
		
		if (g_kKillsDictionary.has_key(iKey)):
			iKills = g_kKillsDictionary[iKey]
					
		if (g_kDeathsDictionary.has_key(iKey)):
			iDeaths = g_kDeathsDictionary[iKey]
					
		if (g_kScoresDictionary.has_key(iKey)):
			iScore = g_kScoresDictionary[iKey]

		if (g_kTeamDictionary.has_key(iKey)):
			iTeam = g_kTeamDictionary[iKey]
				 
		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar(chr(SCORE_INIT_MESSAGE))

		# write kills and deaths
		kStream.WriteLong(iKey)
		kStream.WriteLong(iKills)
		kStream.WriteLong(iDeaths)
		kStream.WriteLong(iScore)
		kStream.WriteChar(chr(iTeam))

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message.
		pNetwork.SendTGMessage(iToID, pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()

	# Now send the team scores
	for iTeam in g_kTeamScoreDictionary.keys():
		iScore = g_kTeamScoreDictionary[iTeam]

		iKills = 0
		if (g_kTeamKillsDictionary.has_key(iTeam)):
			iKills = g_kTeamKillsDictionary[iTeam]

		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar (chr (TEAM_SCORE_MESSAGE))

		# write kills and score
		kStream.WriteChar(chr(iTeam))
		kStream.WriteLong(iKills)
		kStream.WriteLong(iScore)

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message.
		pNetwork.SendTGMessage(iToID, pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()

	return 1


def DamageEventHandler(pObject, pEvent):
	debug(__name__ + ", DamageEventHandler")
	if (pEvent.IsHullHit() == 1):
		DamageHandler(pObject, pEvent, 1)
	else:
		DamageHandler(pObject, pEvent, 0)
        pObject.CallNextHandler(pEvent)


def DamageHandler(TGObject, pEvent, bHullDamage):
        debug(__name__ + ", DamageHandler")
        import Multiplayer.Modifier
	# Damage was done.  We need to record this for scoring purposes.
	# Get the player id of the shooter.
	iHitterID = pEvent.GetFiringPlayerID()
	
	if (iHitterID == 0):
		# No player doing the hitting.  Don't record.
		return

	# Get the object id of the ship that was hit.
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if (not pShip):
		# Don't score non-ship objects
		return 

	iHitID = pShip.GetObjID()

	iHitClass = 0
	iHitterClass = 0

	# Get the hitter's ship.
	pGame = App.MultiplayerGame_Cast(App.Game_GetCurrentGame())
	pHitterShip = pGame.GetShipFromPlayerID(iHitterID)
	if (pHitterShip):
		iHitterClass = Multiplayer.SpeciesToShip.GetClassFromSpecies(pHitterShip.GetNetType())

	iHitClass = Multiplayer.SpeciesToShip.GetClassFromSpecies(pShip.GetNetType())

	# Get the amount of damage done.
	fDamage = pEvent.GetDamage()

	# Modifify damage based on ship class
	fDamage = fDamage * Multiplayer.Modifier.GetModifier(iHitterClass, iHitClass)

	# get the team of the person who did the hitting.
	iHitterTeam = INVALID_TEAM
	if (g_kTeamDictionary.has_key(iHitterID)):
		iHitterTeam = g_kTeamDictionary[iHitterID]

	# Get the team of the ship that got hit.
	if (IsSameTeam(iHitterID, pShip.GetNetPlayerID())):
		# Same team, so penalize their score
		fDamage = -fDamage		

	# Get the dictionary that stores all the people that have hit this object.
	global g_kDamageDictionary
	pDamageByDict = None
	if (g_kDamageDictionary.has_key(iHitID)):
		# This object has been hit before.  Fetch it's damage by dictionary
		pDamageByDict = g_kDamageDictionary[iHitID]
	else:
		# Create a new dictionary since this object has not been hit by a player
		# before
		pDamageByDict = {}
		g_kDamageDictionary[iHitID] = pDamageByDict


	# Update the damage by dictinary.
	fPreviousDamageDone = 0.0
	pDamageList = None
	if (pDamageByDict.has_key(iHitterID)):
		# This player has done damage before.  Fetch previous damage done.
		# Get the list from the damage dict
		pDamageList = pDamageByDict[iHitterID]
		fPreviousDamageDone = pDamageList[bHullDamage]	# zero is shield, 1 is hull
	else:
		# This player has not done damage before.  Create a new damage list
		# to add to the damage dict.
		pDamageList = [0, 0]		# List of two elements
		pDamageByDict[iHitterID] = pDamageList

	# Add in the damage done this time.
	fPreviousDamageDone = fPreviousDamageDone + fDamage

	# Store it in the database
	pDamageList[bHullDamage] = fPreviousDamageDone


def ObjectKilledHandlerClient(pObject, pEvent):
        #print "Object Silent Killed Handler"
        
        debug(__name__ + ", ObjectKilledHandlerClient")
        pKilledObject = pEvent.GetDestination()
        if (pKilledObject.IsTypeOf(App.CT_SHIP)):
                pShip = App.ShipClass_Cast(pKilledObject)
                sShipName = pShip.GetName()
                
                if string.find(string.lower(sShipName), "firepoint") != -1:
                        return
                
                #print("Killed Ship: ", sShipName)

                # Now send a message to everybody else that the score was updated.
                # allocate the message.
                pMessage = App.TGMessage_Create()
                pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet

	        # Setup the stream.
	        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	        kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
	        # Write relevant data to the stream.
	        # First write message type.
	        kStream.WriteChar(chr(CLIENT_OBJECT_DESTROYED))

                # Write the name of killed ship
                for i in range(len(sShipName)):
                        kStream.WriteChar(sShipName[i])
                # set the last char:
                kStream.WriteChar('\0')

	        # Okay, now set the data from the buffer stream to the message
	        pMessage.SetDataFromStream(kStream)

                # Send the message to everybody but me.  Use the NoMe group, which
                # is set up by the multiplayer game.
                pNetwork = App.g_kUtopiaModule.GetNetwork()
                if not App.IsNull(pNetwork):
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

	        # We're done.  Close the buffer.
	        kStream.CloseBuffer()
        pObject.CallNextHandler(pEvent)


def RemoveNameFromGroup(pGroup, sName):
        # Removing "This ship probably wont exist" will only increase the (in-)famous addship lag
        # since it will be added and added again.
        debug(__name__ + ", RemoveNameFromGroup")
        if pGroup and pGroup.IsNameInGroup(sName) and sName != "This ship probably wont exist":
                pGroup.RemoveName(sName)


def AddNameToGroup(pGroup, sName):
        debug(__name__ + ", AddNameToGroup")
        if pGroup and not pGroup.IsNameInGroup(sName):
                pGroup.AddName(sName)


# This handler updates the score when an object is killed.
def ObjectKilledHandler(pObject, pEvent):
        debug(__name__ + ", ObjectKilledHandler")
        global dict_Probes, g_lFirepoints
        
        pObject.CallNextHandler(pEvent)
        
        pKilledObject = pEvent.GetDestination()
        if (pKilledObject.IsTypeOf(App.CT_SHIP)):
                pShip = App.ShipClass_Cast(pKilledObject)
                #DoKillSubtitle(None, pShip.GetName())
                pShipID = pShip.GetNetPlayerID()

                # delete all probes of this Player:
                if dict_Probes.has_key(pShipID):
                        for ProbeName in dict_Probes[pShipID]:
                                pProbe = MissionLib.GetShip(ProbeName)
                                if pProbe:
                                        pProbe.DestroySystem(pProbe.GetHull())
                        del dict_Probes[pShipID]

		# Remove ship from group 1.
                #RemoveNameFromGroup(g_pTeam1, pShip.GetName())
                # Remove ship from group 2.
                #RemoveNameFromGroup(g_pTeam2, pShip.GetName())
                
                #pFriendlies = MissionLib.GetFriendlyGroup()
		#if pFriendlies.IsNameInGroup(pShip.GetName()):
                #        RemoveNameFromGroup(pFriendlies, pShip.GetName())
                #pEnemies = MissionLib.GetEnemyGroup()
		#if pEnemies.IsNameInGroup(pShip.GetName()):
                #        RemoveNameFromGroup(pEnemies, pShip.GetName())
        
                # if it is our ship, delete all our firepoints
                pPlayer = MissionLib.GetPlayer()
                if pPlayer and pPlayer.GetObjID() == pShip.GetObjID():
                        for sFP in g_lFirepoints:
                                pFP = MissionLib.GetShip(sFP)
                                if pFP:
                                        pFP.DestroySystem(pFP.GetHull())
                        g_lFirepoints = []
        
        # only the host has more work todo:
        if not App.g_kUtopiaModule.IsHost():
               return 
        import Multiplayer.MissionShared
	if (Multiplayer.MissionShared.g_bGameOver != 0):
		# If the game is over, then don't do anymore score processing
		return

	# Get the player ID of the firing object from the event
	iFiringPlayerID = pEvent.GetFiringPlayerID()

	# Get the player id of the player who got killed.  It could be AI object,
	# in which case the ID is zero.
	iShipID = App.NULL_ID

	pKilledObject = pEvent.GetDestination ()
	if (pKilledObject.IsTypeOf (App.CT_SHIP)):
		# Get the player id of the ship from the multiplayer game.
		iKilledPlayerID = pShip.GetNetPlayerID()
		iShipID = pShip.GetObjID()
			
	else:
		iKilledPlayerID = 0

	# At this point, we have the player id of the person who made the killing shot.
	# Award a frag to him.
	iKills = 0

	if (iFiringPlayerID != 0):
		# Get the previous frag count.
		global g_kKillsDictionary
		if (g_kKillsDictionary.has_key(iFiringPlayerID) == 1):
			# There is already this player is the kill table.  Get his previous kill total.
			iKills = g_kKillsDictionary[iFiringPlayerID]	
		else:
			# First kill.
			iKills = 0

		if (g_kTeamDictionary.has_key(iFiringPlayerID)):
			iTeam = g_kTeamDictionary[iFiringPlayerID]

			if not IsSameTeam(iFiringPlayerID, iKilledPlayerID):
				# Yes, enemy ship.  Award kill
				# Increment kills by one to count for this current kill.
				iKills = iKills + 1

				# Award kill to team as well.
				iTeamKills = 0
				if (g_kTeamKillsDictionary.has_key(iTeam)):
					iTeamKills = g_kTeamKillsDictionary[iTeam]

				iTeamKills = iTeamKills + 1

				g_kTeamKillsDictionary[iTeam] = iTeamKills
	else:
		# Self destruct?  Collision?  Still award a team kill to the Team2 Name if appropriate.
		if (g_kTeamDictionary.has_key(iKilledPlayerID)):
			# get the team that the killed player was on.
			iKilledTeam = g_kTeamDictionary[iKilledPlayerID]
			if iKilledTeam == 0:	# Attacking team died
				# award a kill to the defending team.
				iTeamKills = 0
				if g_kTeamKillsDictionary.has_key(1):
					iTeamKills = g_kTeamKillsDictionary[1]
				
				iTeamKills = iTeamKills + 1					
				g_kTeamKillsDictionary[1] = iTeamKills
			elif iKilledTeam == 1:
				iTeamKills = 0
				if g_kTeamKillsDictionary.has_key(0):
					iTeamKills = g_kTeamKillsDictionary[0]
				
				iTeamKills = iTeamKills + 1					
				g_kTeamKillsDictionary[0] = iTeamKills

	# Award a death to the person that just got killed.
	global g_kDeathsDictionary
	if (g_kDeathsDictionary.has_key(iKilledPlayerID) == 1):
		# There is already this player is the death table.  Get his previous death total.
		iDeaths = g_kDeathsDictionary[iKilledPlayerID]
	else:
		# First death
		iDeaths = 0

	# Increment Deaths by one to count for this current kill.
	iDeaths = iDeaths + 1

	# Okay, now give all the player's who damaged this object credit.
	iScoreUpdateCount = 0		# Keep track of how many players had their score changed.
	iFiringPlayerScore = 0		# Keep track of this to send the event later.
	global g_kDamageDictionary
	global g_kScoresDictionary
	global g_kTeamScoreDictionary
	global g_kTeamKillsDictionary

	pDamageByDict = None

	if (iShipID != App.NULL_ID):
		if (g_kDamageDictionary.has_key(iShipID)):
			# Okay, there are player damage points to award.
			pDamageByDict = g_kDamageDictionary[iShipID]

	if (pDamageByDict):
		# Okay, there are player damage points to award.
		pDamageByDict = g_kDamageDictionary[iShipID]

		# Loop through the player list and award score.
		for iPlayerID in pDamageByDict.keys():
			# Get shield and hull damage done by this player.
			pDamageList = pDamageByDict[iPlayerID]
			fShieldDamageDone = pDamageList[0]
			fHullDamageDone = pDamageList[1]

			# Compute damage done based on some formula.  For now
			# it is simple addition.
			fDamageDone = fShieldDamageDone + fHullDamageDone
			fDamageDone = fDamageDone / 10.0		# Reduce points by factor of 10 to keep numbers reasonable

			# Get previous score
			fScore = 0.0
			if (g_kScoresDictionary.has_key(iPlayerID)):
				fScore = g_kScoresDictionary[iPlayerID]
			
			fScore = fScore + fDamageDone

			# Count the number of non firing player scores.  This is
			# used to send the scores later.  The firing player has
			# his score sent separately, so it shouldn't to be counted.
			if (iPlayerID == iFiringPlayerID):
				iFiringPlayerScore = int(fScore)
			else:
#				# print("Counting " + str (iPlayerID))
				iScoreUpdateCount = iScoreUpdateCount + 1
											
			g_kScoresDictionary[iPlayerID] = int(fScore)

			# Update team score as well
			# Get this player's team.
			if (g_kTeamDictionary.has_key(iPlayerID)):
				iTeam = g_kTeamDictionary[iPlayerID]

				fTeamScore = 0
				if (g_kTeamScoreDictionary.has_key(iTeam)):
					fTeamScore = g_kTeamScoreDictionary[iTeam]
				
				fTeamScore = fTeamScore + fDamageDone
				g_kTeamScoreDictionary[iTeam] = int(fTeamScore)


	# Update the score
	UpdateScore(iFiringPlayerID, iKills, iKilledPlayerID, iDeaths)

	# Now send a message to everybody else that the score was updated.
	# allocate the message.
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(Multiplayer.MissionShared.SCORE_CHANGE_MESSAGE))

	# Write the player id of killer
	kStream.WriteLong(iFiringPlayerID)

	if (iFiringPlayerID != 0):
		# Write the kills
		kStream.WriteLong(iKills)

		# Write the score as a long
		kStream.WriteLong(iFiringPlayerScore)

	# Write the player id of killed
	kStream.WriteLong(iKilledPlayerID)
	
	# Write the deaths
	kStream.WriteLong(iDeaths)

	# Write out the number of score changes
	kStream.WriteChar(chr(iScoreUpdateCount))

	# Write out scores for all the players that have score changes.
	iCount = 0
	if (pDamageByDict):
		# Loop through the player list and store the score.
		for iPlayerID in pDamageByDict.keys ():
			# print("Checking " + str (iPlayerID))
			if (iPlayerID != iFiringPlayerID and iPlayerID != 0):	# firing player already has his score stored
#				# print("Writing score for " + str (iPlayerID) + " for " + str (g_kScoresDictionary [iPlayerID]) + " points.")
				kStream.WriteLong(iPlayerID)
				kStream.WriteLong(g_kScoresDictionary[iPlayerID])
				iCount = iCount + 1

	# Error condition.  Just put some filler in.
	while(iCount < iScoreUpdateCount):
		kStream.WriteLong(0)

	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)

	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if (not App.IsNull(pNetwork)):
		pNetwork.SendTGMessageToGroup("NoMe", pMessage)

	# We're done.  Close the buffer.
	kStream.CloseBuffer()

	# Clear the damage dictionary for this object since it is now
	# dead an we don't want memory wasted storing who did damage to
	# this thing anymore.
	if (iShipID != App.NULL_ID):
		if (g_kDamageDictionary.has_key(iShipID)):
			del g_kDamageDictionary[iShipID]

	# Now send the team scores
	for iTeam in g_kTeamScoreDictionary.keys():
		iScore = g_kTeamScoreDictionary[iTeam]

		iKills = 0
		if (g_kTeamKillsDictionary.has_key(iTeam)):
			iKills = g_kTeamKillsDictionary[iTeam]

		pMessage = App.TGMessage_Create()
		pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream()		# Allocate a local buffer stream.
		kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar(chr(TEAM_SCORE_MESSAGE))

		# write kills and score
		kStream.WriteChar(chr(iTeam))
		kStream.WriteLong(iKills)
		kStream.WriteLong(iScore)

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message.
		pNetwork.SendTGMessageToGroup("NoMe", pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()

	# Check frag limit to see if game is over
	#CheckFragLimit()


# Send to all people the Group of the Ship we just have added
def SendGroupInfo(ShipName, ShipID):
	debug(__name__ + ", SendGroupInfo")
	global ADD_AI_TO_TEAM_MSG
	
	# Setup the stream.
	# Allocate a local buffer stream.
	kStream = App.TGBufferStream()
	# Open the buffer stream with a byte buffer.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(ADD_AI_TO_TEAM_MSG))

	# Write out scores for all the players that have score changes.
	iCount = 0
	# Loop through the String
	for ichar in range(len(ShipName)):
		kStream.WriteChar(ShipName[iCount])
		iCount = iCount + 1

	# set the last char:
	kStream.WriteChar('\0')

	# Write the new Ship ID:
	kStream.WriteLong(ShipID)

	pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)

	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
		        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

	# We're done.  Close the buffer.
	kStream.CloseBuffer()


def TellScriptInfo(pShip):
	# Setup the stream.
	# Allocate a local buffer stream.
	debug(__name__ + ", TellScriptInfo")
	kStream = App.TGBufferStream()
	# Open the buffer stream with a byte buffer.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(SET_SCRIPT_MSG))

	kStream.WriteInt(pShip.GetObjID())
        
        sShipScript = pShip.GetScript()
	iCount = 0
	# Loop through the String
	for ichar in range(len(sShipScript)):
		kStream.WriteChar(sShipScript[iCount])
		iCount = iCount + 1
	# set the last char:
	kStream.WriteChar('\0')

	pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
	pMessage.SetGuaranteed(1)
	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)

	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
		        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)

	# We're done.  Close the buffer.
	kStream.CloseBuffer()
	

def AddShipNameToGroup(pShip):
        # Lets get the Group of our Player:
        debug(__name__ + ", AddShipNameToGroup")
        pPlayer = MissionLib.GetPlayer()
        ShipName = pShip.GetName()
        if not pPlayer:
                return
        elif ShipName == pPlayer.GetName():
                return
        ShipID = 0
        iOurTeam = Mission4Menus.g_iTeam
        pEnemyGroup = MissionLib.GetEnemyGroup()
        pFriendlyGroup = MissionLib.GetFriendlyGroup()
        ShipID = 0
        
        # case Team 1 (friendly)
        if iOurTeam == 0:
                if pFriendlyGroup.IsNameInGroup(ShipName):
                        ShipID = -1
                        AddNameToGroup(g_pTeam1, ShipName)
                elif pEnemyGroup.IsNameInGroup(ShipName):
                        ShipID = -2
                        AddNameToGroup(g_pTeam2, ShipName)
        elif iOurTeam == 1:
                if pFriendlyGroup.IsNameInGroup(ShipName):
                        ShipID = -2
                        AddNameToGroup(g_pTeam2, ShipName)
                elif pEnemyGroup.IsNameInGroup(ShipName):
                        ShipID = -1
                        AddNameToGroup(g_pTeam1, ShipName)
        
        pShip.SetNetPlayerID(ShipID)
        SendGroupInfo(ShipName, ShipID)


def CheckFragLimit():
        debug(__name__ + ", CheckFragLimit")
        import Multiplayer.MissionShared
        import Multiplayer.MissionMenusShared
	if (Multiplayer.MissionShared.g_bGameOver):
		# Don't check frag limit if game is over
		return

	iFragLimit = Multiplayer.MissionMenusShared.g_iFragLimit
	if (iFragLimit == -1):
		# There are no frag limits
		return

	bOver = 0
	if (g_kTeamKillsDictionary.has_key(1)):
		if (g_kTeamKillsDictionary[1] >= iFragLimit):
			# Yes, game is over.
			bOver = 1
	if (g_kTeamKillsDictionary.has_key(0)):
		if (g_kTeamKillsDictionary[0] >= iFragLimit):
			# Yes, game is over.
			bOver = 1

	if bOver:
		Multiplayer.MissionShared.EndGame(Multiplayer.MissionShared.END_NUM_FRAGS_REACHED)


def UpdateScore(iFiringPlayerID, iKills, iKilledPlayerID, iDeaths):
	# Set the new value in the dictionary
	debug(__name__ + ", UpdateScore")
	global g_kKillsDictionary
	global g_kDeathsDictionary

	if (iFiringPlayerID != 0):
		g_kKillsDictionary[iFiringPlayerID] = iKills

	g_kDeathsDictionary[iKilledPlayerID] = iDeaths

        # Do a little subtitle announcing the kill.
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if pNetwork:
                # Create a subtitle action to display the fact that a kill/death occurred.
                pPlayerList = pNetwork.GetPlayerList()
                pPlayer = pPlayerList.GetPlayer(iKilledPlayerID)
                if pPlayer:
                        DoKillSubtitle(iFiringPlayerID, pPlayer.GetName().GetCString())

	# Update the interface
	Mission4Menus.RebuildPlayerList()


def DoKillSubtitle(iFiringPlayerID, iKilledPlayer):
        debug(__name__ + ", DoKillSubtitle")
        pFBCMPDatabase = App.g_kLocalizationManager.Load("data/TGL/FBCMP.tgl")

        pcSubString = None
        
        pString = pFBCMPDatabase.GetString("Killed")
        pcString = pString.GetCString()
        pcSubString = pcString % (iKilledPlayer)

	if (pcSubString != None):
		# Okay, there's a subtitle to display
		pSequence = App.TGSequence_Create()
		pSubtitleAction = App.SubtitleAction_CreateC(pcSubString)
		pSubtitleAction.SetDuration(5.0)
		pSequence.AddAction(pSubtitleAction)
		pSequence.Play()

		
def NewPlayerHandler(TGObject, pEvent):
	# check if player is host and not dedicated server.  If dedicated server, don't
	# add the host in as a player.
	debug(__name__ + ", NewPlayerHandler")
	iPlayerID = pEvent.GetPlayerID()

	# Check if this player is already in the dictionary.
	global g_kKillsDictionary 
	global g_kDeathsDictionary 

	if (not g_kKillsDictionary.has_key(iPlayerID)):
		# Add a blank key
		g_kKillsDictionary[iPlayerID] = 0		# No kills

	if (not g_kDeathsDictionary.has_key (iPlayerID)):
		# Add a blank key
		g_kDeathsDictionary[iPlayerID] = 0		# No deaths

	# Rebuild the player list since a new player was added
	Mission4Menus.RebuildPlayerList()

	# send our warp speed
	#try:
	#	from Custom.QBautostart.Libs.LibWarp import MPSendMyWarpSpeed, GetCurWarpSpeed, dWarpScenes
	#	pPlayer = MissionLib.GetPlayer()
	#	if App.g_kUtopiaModule.IsHost() and pPlayer:
	#		MPSendMyWarpSpeed(pPlayer, GetCurWarpSpeed(pPlayer.GetName()))
	#		# check if somebody is currently warping
	#		for sShipName in dWarpScenes.keys():
	#			pWarp = dWarpScenes[sShipName]
	#			SendWarpETA(pWarp.pShip.GetObjID(), pWarp.iTimeToWarp)
	#except ImportError:
	#	pass

	if App.g_kUtopiaModule.IsHost():
		for iShipID in dReplaceModel.keys():
			SentReplaceModelMessage(iShipID, dReplaceModel[iShipID])

	TGObject.CallNextHandler(pEvent)


def DeletePlayerHandler(TGObject, pEvent):
	# We only handle this event if we're still connected.  If we've been disconnected,
	# then we don't handle this event since we want to preserve the score list to display
	# as the end game dialog.

	debug(__name__ + ", DeletePlayerHandler")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	if (pNetwork):
		if (pNetwork.GetConnectStatus() == App.TGNETWORK_CONNECTED or pNetwork.GetConnectStatus() == App.TGNETWORK_CONNECT_IN_PROGRESS):
			# We do not remove the player from the dictionary.  This way, if the
			# player rejoins, his score will be preserved.
			
			# Rebuild the player list since a player was removed.
			Mission4Menus.RebuildPlayerList()
	return


def DeleteSequence(pAction, pSet, pShipName):
        debug(__name__ + ", DeleteSequence")
        if MissionLib.GetShip(pShipName):
                pSet.RemoveObjectFromSet(pShipName)
                return 0
        print "Ship to delete %s not presend anymore" % pShipName
        return 1


def DeleteObjectFromSetTimer(pSet, pShipName, Time):
        debug(__name__ + ", DeleteObjectFromSetTimer")
        pSeq = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "DeleteSequence", pSet, pShipName)
        pSeq.AppendAction(pAction, Time)
        pSeq.Play()


def getGroupFromShip(sShipName):
	debug(__name__ + ", getGroupFromShip")
	pFriendlys = MissionLib.GetFriendlyGroup()
	pEnemys = MissionLib.GetEnemyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()
	if pFriendlys.IsNameInGroup(sShipName):
		return "friendly"
	elif pEnemys.IsNameInGroup(sShipName):
		return "enemy"
	elif pNeutrals.IsNameInGroup(sShipName):
		return "neutral"
	return None


def GetFoundationAI(pShip, sGroup):
	debug(__name__ + ", GetFoundationAI")
	if GetShipType(pShip):
		FdtnShips = Foundation.shipList
                sShipType = GetShipType(pShip)
                if FdtnShips.has_key(sShipType):
		        ship = FdtnShips[sShipType]
		        if sGroup == "friendly":
			        return ship.StrFriendlyAI()
		        elif sGroup == "enemy":
			        return ship.StrEnemyAI()
	        return None


def getGroup(sGroupName):
	debug(__name__ + ", getGroup")
	if sGroupName == "friendly":
		return MissionLib.GetFriendlyGroup()
	elif sGroupName == "enemy":
		return MissionLib.GetEnemyGroup()
	else:
		return MissionLib.GetNeutralGroup()


def autoAI(pShip):
	if not pShip or not App.g_kUtopiaModule.IsHost():
		return
	
	debug(__name__ + ", autoAI")
	if getGroupFromShip(pShip.GetName()) == "friendly":
		pFdtnAI = GetFoundationAI(pShip, "friendly")
                if not pFdtnAI:
                        return
		
		if pFdtnAI == "QuickBattleFriendlyAI":
			pShip.SetAI(BasicAI.CreateTeamAI(pShip, getGroup("enemy")))
		elif pFdtnAI == "StarbaseFriendlyAI":
			# Add the starbase itself to the attacker list -- the AI needs to have
			# *something* on the attacker list so as not to crash, but it won't
			# try to attack itself
			pEnemies = getGroup("enemy")
			#AddNameToGroup(pEnemies, pShip.GetName())
			pShip.SetAI(BasicAI.CreateStarbaseTeamAI(pShip, getGroup("enemy")))
			#RemoveNameFromGroup(pEnemies, pShip.GetName())
                else:
                        pAIModule = __import__("QuickBattle." + pFdtnAI)
                        try:
                                pShip.SetAI(pAIModule.CreateAI(pShip, getGroup("enemy")))
                        except:
                                pShip.SetAI(pAIModule.CreateAI(pShip))

	elif getGroupFromShip(pShip.GetName()) == "enemy":
		pFdtnAI = GetFoundationAI(pShip, "enemy")
                if not pFdtnAI:
                        return

                if pFdtnAI == "QuickBattleAI":
                        pShip.SetAI(BasicAI.CreateTeamAI(pShip, getGroup("friendly")))
                elif pFdtnAI == "StarbaseAI":
                        # Add the starbase itself to the attacker list -- the AI needs to have
                        # *something* on the attacker list so as not to crash, but it won't
                        # try to attack itself
                        pFriendlies = getGroup("friendly")
			#AddNameToGroup(pFriendlies, pShip.GetName())
                        pShip.SetAI(BasicAI.CreateStarbaseTeamAI(pShip, getGroup("friendly")))
                        #RemoveNameFromGroup(pFriendlies, pShip.GetName())
                else:
                        pAIModule = __import__("QuickBattle." + pFdtnAI)
                        try:
                                pShip.SetAI(pAIModule.CreateAI(pShip, getGroup("friendly")))
                        except:
                                pShip.SetAI(pAIModule.CreateAI(pShip))


def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        if pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None


def ReenableCollisions(pAction, iShipObjID):	
	pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
	if pShip:
		pShip.SetCollisionsOn(1)
		
	return 0


def IsEscapePod(sShipScript):
	if sShipScript:
		if string.find(string.lower(sShipScript), "defpod") != -1:
			return 1
		if string.find(string.lower(sShipScript), "galaxy escape pod") != -1:
			return 1
		if string.find(string.lower(sShipScript), "escapepod") != -1:
			return 1
		if string.find(string.lower(sShipScript), "greenmisc") != -1:
			return 1
		if string.find(string.lower(sShipScript), "card pod") != -1:
			return 1
	return 0


def ObjectCreatedHandler(pObject, pEvent):
        debug(__name__ + ", ObjectCreatedHandler")
        global g_pTeam1, g_pTeam2, dict_Ship_to_Group, g_kTeamDictionary, g_lFirepoints
	# We only care about ships.
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip:
		pShip.SetCollisionsOn(0)
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ReenableCollisions", pShip.GetObjID()), 5)
		pSeq.Play()
		
                if not pShip.GetName():
                        return
                pSet = pShip.GetContainingSet()
		
		# if we have the script info, tell it the others
		if pShip.GetScript():
			TellScriptInfo(pShip)
                
                # check if this is a firepoint
                if string.find(string.lower(pShip.GetName()), "firepoint") != -1:
                        #print "New Firepoint %s was created" % pShip.GetName()
                        # ok add another check if this firepoint was created by us and really should not be Targetable
                        pPlayer = MissionLib.GetPlayer()
                        if pPlayer and not (pShip.GetName() == "FirePoint1" + pPlayer.GetName() and pShip.IsTargetable()) and pShip.GetName()[-2:] != "_t":
                                pShip.SetTargetable(0)
                        
                        # if it is our firepoint
                        if pPlayer and string.find(pShip.GetName(), pPlayer.GetName()) != -1:
                                g_lFirepoints.append(pShip.GetName())
                        # delete object in next 2 seconds
                        #DeleteObjectFromSetTimer(pSet, pShip.GetName(), 2)
                        return
                        
                # check if this is a HiddenCore
                elif string.find(pShip.GetName(), "HiddenCore") != -1:
                        sNewName = string.replace(pShip.GetName(), "HiddenCore", "Asteroid")
                        pShip.SetName(sNewName)
                
                if dict_Ship_to_Group.has_key(pShip.GetName()):
                        pShip.SetNetPlayerID(dict_Ship_to_Group[pShip.GetName()])
                        del dict_Ship_to_Group[pShip.GetName()]
                else:
		        pEnemyGroup = MissionLib.GetEnemyGroup()
		        pFriendlyGroup = MissionLib.GetFriendlyGroup()
                        if not g_kTeamDictionary.has_key(pShip.GetName()):
                                if not pShip.IsPlayerShip() and (pEnemyGroup.IsNameInGroup(pShip.GetName()) or pFriendlyGroup.IsNameInGroup(pShip.GetName())) and not IsEscapePod(pShip.GetScript()):
                                        # looks like we created this Ship - inform all other Players
                                        AddShipNameToGroup(pShip)
                                        Mission4Menus.RebuildPlayerList()
                
                if pShip.GetNetPlayerID() == -1:
                        AddNameToGroup(g_pTeam1, pShip.GetName())
                        RemoveNameFromGroup(g_pTeam2, pShip.GetName())
                        ResetEnemyFriendlyGroups()
                elif pShip.GetNetPlayerID() == -2:
                        AddNameToGroup(g_pTeam2, pShip.GetName())
                        RemoveNameFromGroup(g_pTeam1, pShip.GetName())
                        ResetEnemyFriendlyGroups()
                
                # Set AI if it is not there
                if not pShip.GetAI() and App.g_kUtopiaModule.IsHost() and pShip.GetNetPlayerID() < 0 and not pShip.GetAI():
                        print "Setting autoAI for", pShip.GetName()
                        autoAI(pShip)

                iPlayerID = pShip.GetNetPlayerID()
		if iPlayerID >= 0:
			# print("In object created handler is player ship")
			# A player ship just got created, we need to update the info pane
			Mission4Menus.RebuildInfoPane()

                        # Figure out if it goes in the attacker group
                        if g_kTeamDictionary.has_key(iPlayerID) and not IsEscapePod(pShip.GetScript()):
			        iTeam = g_kTeamDictionary[iPlayerID]
			        if iTeam == 0:
                                        AddNameToGroup(g_pTeam1, pShip.GetName())
                                        RemoveNameFromGroup(g_pTeam2, pShip.GetName())
                                else:
                                        AddNameToGroup(g_pTeam2, pShip.GetName())
                                        RemoveNameFromGroup(g_pTeam1, pShip.GetName())
			        # A new ship has entered the world.  Reset the friendly enemy group assignments
			        ResetEnemyFriendlyGroups()

                try:
		        import Foundation
		        pEvent = App.TGEvent_Create()
		        pEvent.SetEventType(Foundation.TriggerDef.ET_FND_CREATE_SHIP)
		        pEvent.SetDestination(pShip)
		        App.g_kEventManager.AddEvent(pEvent)
                except:
                        pass
        
        pObject.CallNextHandler(pEvent)


def RestartGameHandler(pObject, pEvent):
        debug(__name__ + ", RestartGameHandler")
        import Multiplayer.MissionShared
	pNetwork = App.g_kUtopiaModule.GetNetwork()

	if (not pNetwork):
		return

	# Okay, we're restarting the game.
	
	# Send Message to everybody to restart
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream()		# Allocate a local buffer stream.
	kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with a byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar(chr(Multiplayer.MissionShared.RESTART_GAME_MESSAGE))

	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream(kStream)

	# Send the message.
	pNetwork.SendTGMessage(0, pMessage)
        
        # Load new Bridge
        #Mission4Menus.LoadBridge()
        
        # Restart Engineering
        Mission4Menus.LoadQBautostart(2)


def RestartGame():
        debug(__name__ + ", RestartGame")
        global curShipNum, g_pTeam1, g_pTeam2
        import Multiplayer.MissionShared
        import Multiplayer.MissionMenusShared
	# Reset scoreboard.
	# Clear dictionaries
	global g_kKillsDictionary 
	global g_kDeathsDictionary 
	global g_kScoresDictionary 
	global g_kDamageDictionary 
	global g_kTeamDictionary 
	global g_kTeamScoreDictionary 
	global g_kTeamKillsDictionary 
	global g_bEndCutsceneStarted

	for iKey in g_kKillsDictionary.keys ():
		g_kKillsDictionary[iKey] = 0	

	for iKey in g_kDeathsDictionary.keys ():
		g_kDeathsDictionary[iKey] = 0

	for iKey in g_kScoresDictionary.keys ():
		g_kScoresDictionary[iKey] = 0

	for iKey in g_kDamageDictionary.keys ():
		g_kDamageDictionary[iKey] = 0

	for iKey in g_kTeamDictionary.keys ():
		g_kTeamDictionary[iKey] = 0

	for iKey in g_kTeamKillsDictionary.keys ():
		g_kTeamKillsDictionary[iKey] = 0

	for iKey in g_kTeamScoreDictionary.keys ():
		g_kTeamScoreDictionary[iKey] = 0

	# Clear game over flag
	Multiplayer.MissionShared.g_bGameOver = 0

	# Clear ships again just in case
	Multiplayer.MissionShared.ClearShips()

	# Make sure we've killed the Ship1, even if it's exploding
	ClearShips(1)

	# Rebuild score board
	Mission4Menus.RebuildPlayerList()

	global g_bStarbaseDead
	g_bStarbaseDead = 0

	g_bEndCutsceneStarted = 0

	# Reset time limit
	if (Multiplayer.MissionMenusShared.g_iTimeLimit != -1):
		Multiplayer.MissionShared.g_iTimeLeft = Multiplayer.MissionMenusShared.g_iTimeLimit * 60

	# Recreate the Ships
	if (App.g_kUtopiaModule.IsHost()):
		CreateShips()
	
	# Clear the Attacker group.
	if g_pTeam1:
		g_pTeam1.RemoveAllNames()
		
	# Clear the Defender group.
	if g_pTeam2:
		g_pTeam2.RemoveAllNames()

        pEnemyGroup = MissionLib.GetEnemyGroup()
        pFriendlyGroup = MissionLib.GetFriendlyGroup()
        
        pEnemyGroup.RemoveAllNames()
        pFriendlyGroup.RemoveAllNames()
        
        # we can start with a Ship with number 1 again...
        curShipNum = 1

	# Turn off the chat window and put it back where it belongs
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	pChatWindow = pMultWindow.GetChatWindow()
	pChatWindow.SetPosition(0.0, 0.0, 0)
	if pChatWindow.IsVisible():
		pMultWindow.ToggleChatWindow()

	# Treat as if ship got killed, so go to select ship screen.
	Multiplayer.MissionMenusShared.ShowShipSelectScreen()

        # Load new Bridge
        #Mission4Menus.LoadBridge()
        
        # Restart Engineering
        Mission4Menus.LoadQBautostart(2)


def ResetEnemyFriendlyGroups():
        debug(__name__ + ", ResetEnemyFriendlyGroups")
        global g_pTeam2, g_pTeam1
	# Go through all the ships in the world, assigned them to
	# friendly/enemy based on team assignment
	iOurTeam = Mission4Menus.g_iTeam

	# Go through player list, trying to find all the ships
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pGame = App.MultiplayerGame_Cast(App.Game_GetCurrentGame())
	if (pNetwork and pGame):
		pMission = MissionLib.GetMission()
		pEnemyGroup = MissionLib.GetEnemyGroup()
		pFriendlyGroup = MissionLib.GetFriendlyGroup()

		# First clear the groups.  We will be readding everybody
		# so we want to start with an empty group.
                # Warning: if we clear the groups we will have problems
                # to assign ships to their correct group
		#pEnemyGroup.RemoveAllNames()
		#pFriendlyGroup.RemoveAllNames()

		pPlayerList = pNetwork.GetPlayerList()
		iNumPlayers = pPlayerList.GetNumPlayers()


                for sShipName in g_pTeam1.GetNameTuple():
                        if iOurTeam == 0:
                                AddNameToGroup(pFriendlyGroup, sShipName)
                                RemoveNameFromGroup(pEnemyGroup, sShipName)
                        else:
                                AddNameToGroup(pEnemyGroup, sShipName)
                                RemoveNameFromGroup(pFriendlyGroup, sShipName)
			pShip = MissionLib.GetShip(sShipName)
			if pShip and not pShip.GetNetPlayerID() > 0:
				autoAI(pShip)
                                        
                for sShipName in g_pTeam2.GetNameTuple():
                        if iOurTeam == 0: # We're attackers
                                AddNameToGroup(pEnemyGroup, sShipName)
                                RemoveNameFromGroup(pFriendlyGroup, sShipName)
                        else:
                                AddNameToGroup(pFriendlyGroup, sShipName)
                                RemoveNameFromGroup(pEnemyGroup, sShipName)
			pShip = MissionLib.GetShip(sShipName)
			if pShip and not pShip.GetNetPlayerID() > 0:
				autoAI(pShip)


def IsSameTeam(iObj1PlayerID, iObj2PlayerID):
	# Get the team of the obj1
	debug(__name__ + ", IsSameTeam")
	if(iObj1PlayerID != 0):
		if(iObj2PlayerID != 0):
			# Okay, these are player ships.  Determine if they're
			# on the same team
			iObj1Team = INVALID_TEAM
			iObj2Team = INVALID_TEAM
								
			if (g_kTeamDictionary.has_key(iObj1PlayerID)):
				iObj1Team = g_kTeamDictionary[iObj1PlayerID]

				if (g_kTeamDictionary.has_key(iObj2PlayerID)):
					iObj2Team = g_kTeamDictionary[iObj2PlayerID]

					# Okay got both teams
					if (iObj1Team == iObj2Team):
						return 1
					else:
						return 0


def MPSendCreatePlasma(pShip, vEmitDir, iEngine, fVentTime):
	debug(__name__ + ", MPSendCreatePlasma")
	if not pShip:
		return
	
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)
	kStream = App.TGBufferStream()
	kStream.OpenBuffer(256)
	kStream.WriteChar(chr(MP_SEND_PLASMA_FX))

	kStream.WriteInt(pShip.GetObjID())
	kStream.WriteFloat(vEmitDir.x)
	kStream.WriteFloat(vEmitDir.y)
	kStream.WriteFloat(vEmitDir.z)
	kStream.WriteInt(iEngine)
	kStream.WriteFloat(fVentTime)

        pMessage.SetDataFromStream(kStream)
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
        kStream.CloseBuffer()


def SendWarpETA(iShipID, iTimeToWarp):
	debug(__name__ + ", SendWarpETA")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)
	kStream = App.TGBufferStream()
	kStream.OpenBuffer(256)
	kStream.WriteChar(chr(MP_WARP_ETA_MSG))

	kStream.WriteInt(iShipID)
	kStream.WriteFloat(iTimeToWarp)

        pMessage.SetDataFromStream(kStream)
        if not App.IsNull(pNetwork):
		pNetwork.SendTGMessageToGroup("NoMe", pMessage)
        kStream.CloseBuffer()


###############################################################################
#	CreateShips()
#	
#	Creates the Ships
#	
#	Args:	None
#	
#	Return:	None
#
#	Fully Defiant Modified!
#
###############################################################################
def CreateShips():
	#print("In create Ships")
        debug(__name__ + ", CreateShips")
        import Multiplayer.SpeciesToShip
	
	if not App.g_kUtopiaModule.IsHost():
		#print("The client isn't supposed to create AI ships")
		return

	# Add a Dummy Ship to the Attacker Group for the AI only
        if not g_pTeam1.GetNameTuple():
                g_pTeam1.AddName("This ship probably wont exist")
        if not g_pTeam2.GetNameTuple():
                g_pTeam2.AddName("This ship probably wont exist")

        i = -1
        check_i = 0
        while check_i < len(Mission4Menus.groupTeam2.keys()):
            i = i + 1
            if not Mission4Menus.groupTeam2.has_key(i):
                continue
            check_i = check_i + 1
            Ship = Multiplayer.SpeciesToShip.GetScriptFromSpecies(Mission4Menus.groupTeam2[i])
            CreateAIShip(Ship, "Team2")
        
        i = -1
        check_i = 0
        while check_i < len(Mission4Menus.groupTeam1.keys()):
            i = i + 1
            if not Mission4Menus.groupTeam1.has_key(i):
                continue
            check_i = check_i + 1
            Ship = Multiplayer.SpeciesToShip.GetScriptFromSpecies(Mission4Menus.groupTeam1[i])
            CreateAIShip(Ship, "Team1")

        Mission4Menus.groupTeam2 = {}
        Mission4Menus.RebuildEnemyMenu()
        Mission4Menus.groupTeam1 = {}
        Mission4Menus.RebuildFriendlyMenu()

	#print("Done with CreateShips")


# Give a Position to the AI-Ship
def CreateAIPosition(g_pAIShip, pSet):
	debug(__name__ + ", CreateAIPosition")
	kLocation = App.TGPoint3()
	X = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0 + 50 # for testing!!!!!!!!!!!!!!!!!
	X = X * (App.g_kSystemWrapper.GetRandomNumber(50) + 1)
	Y = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	Y = Y * (App.g_kSystemWrapper.GetRandomNumber(50) + 1)
	Z = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0 - 50
	Z = Z * (App.g_kSystemWrapper.GetRandomNumber(50) + 1)
	kLocation.SetXYZ(X, Y, Z)
	
	while ( pSet.IsLocationEmptyTG(kLocation, g_pAIShip.GetRadius()*2, 1) == 0):
		print("Correcting Position for AI Ship")
		X = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
		X = X * (App.g_kSystemWrapper.GetRandomNumber(50) + 1)
		Y = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
		Y = Y * (App.g_kSystemWrapper.GetRandomNumber(50) + 1)
		Z = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
		Z = Z * (App.g_kSystemWrapper.GetRandomNumber(50) + 1)
		kLocation.SetXYZ(X, Y, Z)

	g_pAIShip.SetTranslate(kLocation)
	g_pAIShip.UpdateNodeOnly()


# Create the AI Ship
def CreateAIShip(ShipType, Team):
        debug(__name__ + ", CreateAIShip")
        import Multiplayer.MissionShared
        global curShipNum, g_pTeam1, g_pTeam2
        
	pSet = Multiplayer.MissionShared.g_pStartingSet

	if (pSet):			
		pcName = ShipType + " - " + str(curShipNum)
                curShipNum = curShipNum + 1
		g_pAIShip = loadspacehelper.CreateShip(ShipType, pSet, pcName, "")
		CreateAIPosition(g_pAIShip, pSet)
                g_pAIShip.UpdateNodeOnly()

		if (Team == "Team2"):
			if g_pAIShip.GetShipProperty().IsStationary():
                                # Add the starbase itself to the attacker list -- the AI needs to have
		                # *something* on the attacker list so as not to crash, but it won't
		                # try to attack itself
                                #AddNameToGroup(g_pTeam1, pcName)
				g_pAIShip.SetAI(BasicAI.CreateStarbaseTeamAI(g_pAIShip, g_pTeam1))
                                #RemoveNameFromGroup(g_pTeam1, pcName)
			else:
				g_pAIShip.SetAI(BasicAI.CreateTeamAI(g_pAIShip, g_pTeam1))
                        AddNameToGroup(g_pTeam2, pcName)
			ShipID = -2
		elif (Team == "Team1"):
			if g_pAIShip.GetShipProperty().IsStationary():
                                # Add the starbase itself to the attacker list -- the AI needs to have
		                # *something* on the attacker list so as not to crash, but it won't
		                # try to attack itself
                                #AddNameToGroup(g_pTeam2, pcName)
				g_pAIShip.SetAI(BasicAI.CreateStarbaseTeamAI(g_pAIShip, g_pTeam2))
                                #RemoveNameFromGroup(g_pTeam2, pcName)
			else:
				g_pAIShip.SetAI(BasicAI.CreateTeamAI(g_pAIShip, g_pTeam2))
                        AddNameToGroup(g_pTeam1, pcName)
			ShipID = -1

		g_pAIShip.SetNetPlayerID(ShipID)
		SendGroupInfo(pcName, ShipID)


def SentReplaceModelMessage(iShipID, sNewShipScript):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", SentReplaceModelMessage")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(REPLACE_MODEL_MSG))

	# send Message
	kStream.WriteInt(iShipID)
	iLen = len(sNewShipScript)
	kStream.WriteShort(iLen)
	kStream.Write(sNewShipScript, iLen)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def DeleteObjectFromSet(pSet, pShip):
	debug(__name__ + ", RemoveObjectFromSet")
	
	pShip.SetDead()
	if pSet:
		pSet.RemoveObjectFromSet(pShip.GetName())

	pNetwork = App.g_kUtopiaModule.GetNetwork()
	
        # Now send a message to everybody else that the score was updated.
        # allocate the message.
        pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
	               
        # Setup the stream.
        kStream = App.TGBufferStream()		# Allocate a local buffer stream.
        kStream.OpenBuffer(Multiplayer.MissionShared.NET_BUFFER_SIZE)				# Open the buffer stream with byte buffer.
	
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(DELETE_OBJECT_FROM_SET_MSG))
                                        
        kStream.WriteInt(pShip.GetObjID())

        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)

        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()

# returns ship status values, such as damage and shield status in a dictionary
def getShipAttributes(pShip):
        debug(__name__ + ", getShipAttributes")
        dict_ShipAttrs = {}
        pPropSet = pShip.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
        if pShipSubSystemPropInstanceList:
                iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
                pShipSubSystemPropInstanceList.TGBeginIteration()
                for i in range(iNumItems):
                        pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                        pProperty = App.SubsystemProperty_Cast(pInstance.GetProperty())
                        sName = pProperty.GetName().GetCString()
                        # bad - find a better way!
                        pSubsystem = MissionLib.GetSubsystemByName(pShip, sName)
                        dict_ShipAttrs[sName] = pSubsystem.GetConditionPercentage()
                pShipSubSystemPropInstanceList.TGDoneIterating()
        
        dict_ShipAttrs["MiscAttributes"] = {}
        # shields
        dict_ShipAttrs["MiscAttributes"]["shields"] = {}
        for iShield in range(App.ShieldClass.NUM_SHIELDS):
                dict_ShipAttrs["MiscAttributes"]["shields"][iShield] = pShip.GetShields().GetCurShields(iShield)
        
        return dict_ShipAttrs


def MPGetShipAttributes(pShip):
	debug(__name__ + ", MPGetShipAttributes")
	
	global gdShipAttrs
	
	if App.g_kUtopiaModule.IsHost():
		gdShipAttrs[pShip.GetObjID()] = getShipAttributes(pShip)
	else:
        	# Setup the stream.
        	# Allocate a local buffer stream.
        	kStream = App.TGBufferStream()
        	# Open the buffer stream with a 256 byte buffer.
        	kStream.OpenBuffer(256)
        	# Write relevant data to the stream.
        	# First write message type.
        	kStream.WriteChar(chr(SET_GET_SHIP_ATTR_MSG))

		# send Message
		kStream.WriteInt(0) # get
		kStream.WriteInt(pShip.GetObjID())
		kStream.WriteInt(0)

        	pMessage = App.TGMessage_Create()
       	 	# Yes, this is a guaranteed packet
		pMessage.SetGuaranteed(1)
        	# Okay, now set the data from the buffer stream to the message
        	pMessage.SetDataFromStream(kStream)
        	# Send the message to everybody but me.  Use the NoMe group, which
        	# is set up by the multiplayer game.
	        pNetwork = App.g_kUtopiaModule.GetNetwork()
        	if not App.IsNull(pNetwork):
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        	# We're done.  Close the buffer.
        	kStream.CloseBuffer()


def RestoreShipAttributes(pShip, dict_ShipAttrs):
        debug(__name__ + ", RestoreShipAttributes")
        for sSubsystemName in dict_ShipAttrs.keys():
                if sSubsystemName != "MiscAttributes":
                        pSubsystem = MissionLib.GetSubsystemByName(pShip, sSubsystemName)
                        if pSubsystem:
                                pSubsystem.SetConditionPercentage(dict_ShipAttrs[sSubsystemName])
        # shields
        dict_Shields = dict_ShipAttrs["MiscAttributes"]["shields"]
        for iShield in range(App.ShieldClass.NUM_SHIELDS):
                pShip.GetShields().SetCurShields(iShield, dict_Shields[iShield])


def MPSetShipAttributes(pShip, iShipFromID):
	debug(__name__ + ", MPSetShipAttributes")
		
	if App.g_kUtopiaModule.IsHost():
		if gdShipAttrs.has_key(iShipFromID):
			RestoreShipAttributes(pShip, gdShipAttrs[iShipFromID])
	else:
        	# Setup the stream.
        	# Allocate a local buffer stream.
        	kStream = App.TGBufferStream()
        	# Open the buffer stream with a 256 byte buffer.
        	kStream.OpenBuffer(256)
        	# Write relevant data to the stream.
        	# First write message type.
        	kStream.WriteChar(chr(SET_GET_SHIP_ATTR_MSG))

		# send Message
		kStream.WriteInt(1) # set
		kStream.WriteInt(pShip.GetObjID())
		kStream.WriteInt(iShipFromID)

        	pMessage = App.TGMessage_Create()
       	 	# Yes, this is a guaranteed packet
		pMessage.SetGuaranteed(1)
        	# Okay, now set the data from the buffer stream to the message
        	pMessage.SetDataFromStream(kStream)
        	# Send the message to everybody but me.  Use the NoMe group, which
        	# is set up by the multiplayer game.
	        pNetwork = App.g_kUtopiaModule.GetNetwork()
        	if not App.IsNull(pNetwork):
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        	# We're done.  Close the buffer.
        	kStream.CloseBuffer()
