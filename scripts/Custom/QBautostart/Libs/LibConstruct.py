from bcdebug import debug
import App
import loadspacehelper
import AI.Player.FlyForward
from Races import Races
from LibQBautostart import *


MP_CONSTRUCT_MSG = 207


class Construct:
        def __init__(self, pConstructingShip, sConstructingRace, lShipsToConstruct, sConstructionLocation, iIncConstructionPower, iNumParallelConstructions = 1, bIsShip = 0, bUseRaceNames = 1):
                debug(__name__ + ", __init__")
                self.iConstructingShipID = pConstructingShip.GetObjID()
                self.sConstructingRace = sConstructingRace
                self.lShipsToConstruct = lShipsToConstruct
                self.iBuildShipID = 0
                self.sConstructionLocation = sConstructionLocation
                self.iIncConstructionPower = iIncConstructionPower
                self.iNumParallelConstructions = iNumParallelConstructions
                self.iCurShipStatus = -20
		self.lBuildQueue = []
                self.sMode = "Construct"
                self.sNewMode = self.sMode
		self.MPClient = 0
		self.bIsShip = bIsShip
		self.bUseRaceNames = bUseRaceNames
		
		if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
			self.MPClient = 1
		if not self.MPClient:
                	self.pTimerProcess = None
                	self.SetupTimer()
		
        def SetMode(self, sNewMode):
                debug(__name__ + ", SetMode")
                if sNewMode == "Repair":
                        self.sNewMode = sNewMode
                else:
                        self.sNewMode = "Construct"
		if App.g_kUtopiaModule.IsMultiplayer():
			SendMPNewMode(self.iConstructingShipID, sNewMode)
        
        def GetMode(self):
		debug(__name__ + ", GetMode")
		if self:
                	return self.sMode

        def GetConstructingShip(self):
		debug(__name__ + ", GetConstructingShip")
		if self:
                	return App.ShipClass_GetObjectByID(None, self.iConstructingShipID)
        
        def GetBuildShip(self):
		debug(__name__ + ", GetBuildShip")
		if self:
                	return App.ShipClass_GetObjectByID(None, self.iBuildShipID)

        def SetupTimer(self):
                debug(__name__ + ", SetupTimer")
                if self.pTimerProcess:
                        # We already have a timer.
                        return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetDelay(1.0)
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)

        def Update(self, dTimeAvailable):
                debug(__name__ + ", Update")
                if self.iCurShipStatus < 0:
                        self.sMode = self.sNewMode
                        self.iCurShipStatus = self.iCurShipStatus + 1
                        return
                        
                # check if the Object doesn't exist anymore
                if not self.GetConstructingShip() or not self.GetConstructingShip().GetContainingSet() or self.GetConstructingShip().GetName() == "MvamTemp":
                        # delete our timer
                        self.pTimerProcess = None
                        # remove our build ship if it exits
                        if self.GetBuildShip():
                                self.GetBuildShip().DestroySystem(self.GetBuildShip().GetHull())
				self.GetBuildShip().GetContainingSet().RemoveObjectFromSet(self.GetBuildShip().GetName())
				return
                # only do anything if our Hull is > 50%
                elif self.GetConstructingShip().GetHull().GetConditionPercentage() > 0.5:
                        self.ContinueConstruction()
		
		# make sure it looks like we are constructing
		if self.GetBuildShip() and self.bIsShip:
			self.GetConstructingShip().SetAI(CreateOrbitAI(self.GetConstructingShip(),  self.GetBuildShip()))
        
        def ContinueConstruction(self):
                debug(__name__ + ", ContinueConstruction")
                if not self.GetBuildShip():
                        self.iCurShipStatus = 0
			# if we have the BuildID still set, then our ship probably exploded
			# in this case set the Status very low so we do not imediately start construction
			# process for a new ship, but in something like 10 minutes
			if self.iBuildShipID != 0:
				self.iCurShipStatus = -600;
			
                # set new mode
                if self.iCurShipStatus == 0 and self.sMode != self.sNewMode:
                        self.sMode = self.sNewMode
			if App.g_kUtopiaModule.IsMultiplayer():
				SendMPNewModeSet(self.iConstructingShipID, self.sMode)
                        
                if self.iCurShipStatus == 0 and self.sMode == "Construct":
                        self.CreateNewShip()
                elif self.iCurShipStatus == 1:
                        self.SetShipSystems(iIncC = self.iIncConstructionPower)
                elif self.iCurShipStatus == 2:
                        self.ShipLeaveDock()
                        self.iCurShipStatus = 3
                elif self.iCurShipStatus == 30:
                        self.ShipFinished()
                        self.iCurShipStatus = 31
                elif self.iCurShipStatus == 60:
                        self.iCurShipStatus = 0
                else:
                        self.iCurShipStatus = self.iCurShipStatus + 1
        
        def CreateNewShip(self):
                debug(__name__ + ", CreateNewShip")
                sShipType = self.GetNextShipToConstruct()
                if sShipType:
                        pSet = self.GetConstructingShip().GetContainingSet()
			if self.bUseRaceNames:
                        	sShipName = Races[self.sConstructingRace].GetRandomName()
			else:
				i = 1
				sShipName = sShipType + " " + str(i)
				while(MissionLib.GetShip(sShipName)):
					i = i + 1
					sShipName = sShipType + " " + str(i)
                        pNewShip = loadspacehelper.CreateShip(sShipType, pSet, sShipName, self.sConstructionLocation)
                        if not pNewShip:
                                return
			if not self.sConstructionLocation:
				kPos = FindGoodLocation(pSet, pNewShip.GetRadius() * 5)
				pNewShip.SetTranslate(kPos)
                        self.GetConstructingShip().EnableCollisionsWith(pNewShip, 0)
                        self.iBuildShipID = pNewShip.GetObjID()
                        self.iCurShipStatus = 1
                        self.SetShipSystems(iToValue = 0.00000001)
			if pNewShip.IsDead():
				return
			pNewShip.DisableGlowAlphaMaps()
                        # Make it stationary, so it doesn't move on gun fire
                        pNewShip.GetShipProperty().SetStationary(1)
        
	def GetNextShipToConstruct(self):
		# if empty, add random ship to list
		debug(__name__ + ", GetNextShipToConstruct")
		if not self.lBuildQueue:
			ship = self.GetRandomShip()
			if not ship:
				return
			self.AddShipToConstructQueue(ship)
		if App.g_kUtopiaModule.IsMultiplayer():
			SendMPRemoveFromQueue(self.iConstructingShipID, 0)
		return self.lBuildQueue.pop(0)
	
	def AddShipToConstructQueue(self, sShipType, bSendNoMessage=0):
		debug(__name__ + ", AddShipToConstructQueue")
		if App.g_kUtopiaModule.IsMultiplayer() and not bSendNoMessage:
			SendMPAppendToQueue(self.iConstructingShipID, sShipType)
		return self.lBuildQueue.append(sShipType)
	
	def GetConstructQueue(self):
		debug(__name__ + ", GetConstructQueue")
		return self.lBuildQueue
	
	def RemoveShipFromQueue(self, iPos, bSendNoMessage=0):
		debug(__name__ + ", RemoveShipFromQueue")
		if App.g_kUtopiaModule.IsMultiplayer() and not bSendNoMessage:
			SendMPRemoveFromQueue(self.iConstructingShipID, iPos)
		if self.lBuildQueue and len(self.lBuildQueue) > iPos:
			del self.lBuildQueue[iPos]
			return 0
		return -1

        def GetRandomShip(self):
                debug(__name__ + ", GetRandomShip")
		if self.lShipsToConstruct > 0:
                	iRandTypeNum = App.g_kSystemWrapper.GetRandomNumber(len(self.lShipsToConstruct))
                	return self.lShipsToConstruct[iRandTypeNum]
		return None

        def SetShipSystems(self, iToValue=0, iIncC=0):
                debug(__name__ + ", SetShipSystems")
                pShip = self.GetBuildShip()
                if not pShip:
                        self.iCurShipStatus = 0
                        return
                # disable glow every time, to make sure it hasn't been enabled
		if pShip.IsDead():
			return
                pShip.DisableGlowAlphaMaps()
                pPropSet = pShip.GetPropertySet()
                pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
                iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
                iNumConstructs = 0

                pShipSubSystemPropInstanceList.TGBeginIteration()
                for i in range(iNumItems):
                        pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                        pProperty = pShip.GetSubsystemByProperty(App.SubsystemProperty_Cast(pInstance.GetProperty()))
                        if iToValue:
                                pProperty.SetCondition(iToValue)
                        elif iIncC:
                                # break here if we have done enough for this turn
                                if iNumConstructs >= self.iNumParallelConstructions:
                                        break
                                
                                iCurCondition = pProperty.GetCondition()
                                iNewCondition = iCurCondition + iIncC
                        
                                # count number of builds
                                if iCurCondition != pProperty.GetMaxCondition():
                                        iNumConstructs = iNumConstructs + 1
                                        
                                if iCurCondition + iIncC > pProperty.GetMaxCondition():
                                        iNewCondition = pProperty.GetMaxCondition()
                                pProperty.SetCondition(iNewCondition)
                
                pShipSubSystemPropInstanceList.TGDoneIterating()
                
                # if iNumConstructs is zero, then we are done with this ship
                if iIncC and iNumConstructs == 0:
                        self.iCurShipStatus = 2

        def ShipLeaveDock(self):
                # enable Glow
                debug(__name__ + ", ShipLeaveDock")
                if App.g_kLODModelManager.AreGlowMapsEnabled() == 1 and App.g_kLODModelManager.GetDropLODLevel() == 0: # else the game will crash on not high graphics
                        App.g_kLODModelManager.SetGlowMapsEnabled(0)
                        App.g_kLODModelManager.SetGlowMapsEnabled(1)
                
                # unset stationary
                self.GetBuildShip().GetShipProperty().SetStationary(0)
                # add it to the group
                addShipToGroup(self.GetBuildShip().GetName(), getGroupFromShip(self.GetConstructingShip().GetName()))
                # set its AI if we have a fixed build location
		if self.sConstructionLocation:
                	self.GetBuildShip().SetAI(AI.Player.FlyForward.CreatePlain(self.GetBuildShip(), 0.1))

        def ShipFinished(self):
                debug(__name__ + ", ShipFinished")
                autoAI(self.GetBuildShip())
                self.iBuildShipID = 0
                if self.GetConstructingShip():
                        self.GetConstructingShip().EnableCollisionsWith(self.GetBuildShip(), 1)


def CreateMessageStream():
	debug(__name__ + ", CreateMessageStream")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)
	kStream = App.TGBufferStream()
	kStream.OpenBuffer(256)
	kStream.WriteChar(chr(MP_CONSTRUCT_MSG))
	return pMessage, kStream


def SendMessageToEveryone(pMessage, kStream):
	debug(__name__ + ", SendMessageToEveryone")
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage.SetDataFromStream(kStream)
	if not App.IsNull(pNetwork):
		if App.g_kUtopiaModule.IsHost():
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)
		else:
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage) # Host has to forward for us
	kStream.CloseBuffer()


def SendMPNewMode(iShipID, sNewMode):
	debug(__name__ + ", SendMPNewMode")
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(1)
	kStream.WriteInt(iShipID)
	iLen = len(sNewMode)
	kStream.WriteShort(iLen)
	kStream.Write(sNewMode, iLen)
	SendMessageToEveryone(pMessage, kStream)


def SendMPNewModeSet(iShipID, sMode):
	debug(__name__ + ", SendMPNewModeSet")
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(2)
	kStream.WriteInt(iShipID)
	iLen = len(sMode)
	kStream.WriteShort(iLen)
	kStream.Write(sMode, iLen)
	SendMessageToEveryone(pMessage, kStream)


def SendMPAppendToQueue(iShipID, sShipType):
	debug(__name__ + ", SendMPAppendToQueue")
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(3)
	kStream.WriteInt(iShipID)
	iLen = len(sShipType)
	kStream.WriteShort(iLen)
	kStream.Write(sShipType, iLen)
	SendMessageToEveryone(pMessage, kStream)


def SendMPRemoveFromQueue(iShipID, iPos):
	debug(__name__ + ", SendMPRemoveFromQueue")
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(4)
	kStream.WriteInt(iShipID)
	kStream.WriteInt(iPos)
	SendMessageToEveryone(pMessage, kStream)


def SendMPShipInConstructQueue(iShipID, sShipType):
	debug(__name__ + ", SendMPShipInConstructQueue")
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(5)
	kStream.WriteInt(iShipID)
	iLen = len(sShipType)
	kStream.WriteShort(iLen)
	kStream.Write(sShipType, iLen)
	SendMessageToEveryone(pMessage, kStream)


def FindGoodLocation (pSet, fRadius):
	debug(__name__ + ", FindGoodLocation")
	kPos = App.TGPoint3 ()
	# first try to find a location that's centered around (0,0,0)
	iCount = 0
	while (iCount < 50):
		x = App.g_kSystemWrapper.GetRandomNumber (200)
		x = x - 100;
		y = App.g_kSystemWrapper.GetRandomNumber (200)
		y = y - 100;
		z = App.g_kSystemWrapper.GetRandomNumber (200)
		z = z - 100;

		kPos.SetXYZ (x, y, z)

		if (pSet.IsLocationEmptyTG (kPos, fRadius, 1)):
			# Okay, found a good location.  Place it here.
			return kPos

		iCount = iCount + 1
	
	# if we're here, we failed to find a good location.  Do the offset method instead.

	# generate random offset direction.
	kOffset = App.TGPoint3 ()
	while (1):
		x = App.g_kSystemWrapper.GetRandomNumber (200) - 100
		y = App.g_kSystemWrapper.GetRandomNumber (200) - 100
		z = App.g_kSystemWrapper.GetRandomNumber (200) - 100
		x = float(x) / 10.0
		y = float(y) / 10.0
		z = float(z) / 10.0

		kOffset.SetXYZ (x, y, z)

		# make sure offset is not zero length
		if (kOffset.Length () > 1.0):
			# good.
			break

	# now add offset to kPos until we find an empty spot
	while pSet.IsLocationEmptyTG(kPos, fRadius, 1) == 0:
		kPos.Add (kOffset)

	# okay, now we've found an empty spot.
	return kPos


def CreateOrbitAI(pShip, pPlanet):
	#########################################
	# Creating PlainAI StartingOrbitScript at (241, 52)
	debug(__name__ + ", CreateOrbitAI")
	pStartingOrbitScript = App.PlainAI_Create(pShip, "StartingOrbitScript")
	pStartingOrbitScript.SetScriptModule("RunScript")
	pStartingOrbitScript.SetInterruptable(1)
	pScript = pStartingOrbitScript.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("StartingOrbit")
	pScript.SetArguments(pShip, pPlanet)
	# Done creating PlainAI StartingOrbitScript
	#########################################
	#########################################
	# Creating PlainAI CirclePlanet at (353, 55)
	pCirclePlanet = App.PlainAI_Create(pShip, "CirclePlanet")
	pCirclePlanet.SetScriptModule("CircleObject")
	pCirclePlanet.SetInterruptable(1)
	pScript = pCirclePlanet.GetScriptInstance()
	pScript.SetFollowObjectName(pPlanet.GetName())
	pScript.SetNearFacingVector(App.TGPoint3_GetModelLeft())
	pScript.SetRoughDistances(pPlanet.GetRadius() + 10, pPlanet.GetRadius() + 10)
	# Done creating PlainAI CirclePlanet
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (201, 111)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (301, 127)
	pSequence.AddAI(pStartingOrbitScript)
	pSequence.AddAI(pCirclePlanet)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating ConditionalAI CloseEnough at (210, 167)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 200.0 + pPlanet.GetRadius(),  pShip.GetName(), pPlanet.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pCloseEnough = App.ConditionalAI_Create(pShip, "CloseEnough")
	pCloseEnough.SetInterruptable(1)
	pCloseEnough.SetContainedAI(pSequence)
	pCloseEnough.AddCondition(pInRange)
	pCloseEnough.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CloseEnough
	#########################################
	#########################################
	# Creating PlainAI FlyToPlanet at (328, 183)
	pFlyToPlanet = App.PlainAI_Create(pShip, "FlyToPlanet")
	pFlyToPlanet.SetScriptModule("Intercept")
	pFlyToPlanet.SetInterruptable(1)
	pScript = pFlyToPlanet.GetScriptInstance()
	pScript.SetTargetObjectName(pPlanet.GetName())
	pScript.SetInterceptDistance(0.0)
	pScript.SetAddObjectRadius(1)
	# Done creating PlainAI FlyToPlanet
	#########################################
	#########################################
	# Creating PriorityListAI OrbitPriorityList at (156, 227)
	pOrbitPriorityList = App.PriorityListAI_Create(pShip, "OrbitPriorityList")
	pOrbitPriorityList.SetInterruptable(1)
	# SeqBlock is at (272, 228)
	pOrbitPriorityList.AddAI(pCloseEnough, 1)
	pOrbitPriorityList.AddAI(pFlyToPlanet, 2)
	# Done creating PriorityListAI OrbitPriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI OrbitAvoidObstacles at (128, 289)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pOrbitAvoidObstacles = App.PreprocessingAI_Create(pShip, "OrbitAvoidObstacles")
	pOrbitAvoidObstacles.SetInterruptable(1)
	pOrbitAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pOrbitAvoidObstacles.SetContainedAI(pOrbitPriorityList)
	# Done creating PreprocessingAI OrbitAvoidObstacles
	#########################################
	return pOrbitAvoidObstacles
