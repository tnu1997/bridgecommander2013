from bcdebug import debug
import App

class RaceInfo:
	def __init__(self, Race):
		debug(__name__ + ", __init__")
		self.myFriendlys = []
	        self.myEnemys = []
        	self.myNames = []
		self.myShips = []
		self.myEscorts = {}
                self.peaceVal = 0.5
		self.PlayerRanks = {}
		self.BuildShips = {}
		self.dResources = {}
		self.Systems = []
        
	def AddName(self, Name):
		debug(__name__ + ", AddName")
		self.myNames.append(Name)
	
	def GetNames(self):
		debug(__name__ + ", GetNames")
		return self.myNames

	def GetRandomName(self):
		debug(__name__ + ", GetRandomName")
		num = len(self.myNames)
		if (num <= 0):
			return None
		rand = App.g_kSystemWrapper.GetRandomNumber(num)
		return self.myNames[rand]
		
    	def GetFriendlys(self):
	        debug(__name__ + ", GetFriendlys")
	        return self.myFriendlys

	def AddFriendly(self, Friendly):
        	debug(__name__ + ", AddFriendly")
        	self.myFriendlys.append(Friendly)

	def GetEnemys(self):
	        debug(__name__ + ", GetEnemys")
	        return self.myEnemys

	def AddEnemy(self, Enemy):
        	debug(__name__ + ", AddEnemy")
        	self.myEnemys.append(Enemy)
        
	def IsFriendlyRace(self, match):
		debug(__name__ + ", IsFriendlyRace")
		for race in self.myFriendlys:
			if (race == match):
                		return 1
	        return 0
        
	def IsEnemyRace(self, match):
        	debug(__name__ + ", IsEnemyRace")
        	for race in self.myEnemys:
			if (race == match):
				return 1
	        return 0

	def AddShip(self, Ship):
		debug(__name__ + ", AddShip")
		self.myShips.append(Ship)
	
	def GetShips(self):
		debug(__name__ + ", GetShips")
		return self.myShips

	def IsOurRace(self, match):
		debug(__name__ + ", IsOurRace")
		for ship in self.myShips:
			if (ship == match):
				return 1
		return 0

	def AddEscort(self, Name, Escort):
		debug(__name__ + ", AddEscort")
		if not self.myEscorts.has_key(Name):
			self.myEscorts[Name] = []
		self.myEscorts[Name].append(Escort)
		
	def GetEscort(self, Name):
		debug(__name__ + ", GetEscort")
		if not self.myEscorts.has_key(Name):
			return None
		return self.myEscorts[Name]

        def SetPeaceValue(self, Num):
                debug(__name__ + ", SetPeaceValue")
                self.peaceVal = Num
        
        def GetPeaceValue(self):
                debug(__name__ + ", GetPeaceValue")
                return self.peaceVal

	def BuildShip(self, sShipType):
		debug(__name__ + ", BuildShip")
		self.BuildShips[sShipType] = self.NumFreeShips(sShipType) + 1
			
	def NumFreeShips(self, sShipType):
		debug(__name__ + ", NumFreeShips")
		iNum = 0
		if self.BuildShips.has_key(sShipType):
			iNum = self.BuildShips[sShipType]
		return iNum

	def SetNumFreeShips(self, sShipType, iNum):	
		debug(__name__ + ", SetNumFreeShips")
		self.BuildShips[sShipType] = iNum

	def BuildShipToPlayerShip(self, sShipType):
		debug(__name__ + ", BuildShipToPlayerShip")
		self.BuildShips[sShipType] = self.NumFreeShips(sShipType) - 1
		if self.NumFreeShips(sShipType) < 0:
			self.BuildShips[sShipType] = 0

	def AddResource(self, sResource, fAmount):
		debug(__name__ + ", AddResource")
		if not self.dResources.has_key(sResource):
			self.dResources[sResource] = fAmount
		else:
			self.dResources[sResource] = self.dResources[sResource] + fAmount

	# return: the amount of resources really removed
	def RemoveResource(self, sResource, fAmount):
		debug(__name__ + ", RemoveResource")
		if not self.dResources.has_key(sResource):
			return 0.0
		
		# we have enough
		if fAmount <= self.dResources[sResource]:
			self.dResources[sResource] = self.dResources[sResource] - fAmount
			return fAmount
		
		# we do not have enough
		fAmount = self.dResources[sResource]
		self.dResources[sResource] = 0.0
		return fAmount

	def AddSystem(self, sSystemName):
		debug(__name__ + ", AddSystem")
		if not sSystemName in self.Systems:
			self.Systems.append(sSystemName)

	def RemoveSystem(self, sSystemName):
		debug(__name__ + ", RemoveSystem")
		if sSystemName in self.Systems:
			self.Systems.remove(sSystemName)

	def GetSystems(self):
		debug(__name__ + ", GetSystems")
		return self.Systems
