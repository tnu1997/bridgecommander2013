

#######################################################################################################
#	In order to recognize whether a ship has a certain technology we introduce a code, based on the
#	affilliation number (ShipProperty -> Affiliation in the Model Property Editor)
#
#
#	Structure of the AffilationNumber 	
#	YYYYYYYYYY are diffent control numbers assigned for various assets as multivectral shielding,
#	ablative armour, breen drain weapon ...
#
#	current reference: AffilationNumber = ...JIHGFEDCBA
#
#	Breen Weapon: Implicit
#
#
#	A: Multivectral Shielding (Type 1 -> positionSelectorShip(pObject,1))
#		0: Off
#		1: On
#
#	B:Immune to Drainerweapon
#		0: No
#		1: Yes
#	
#	C:Ablative Armour
#		0: No
#		1: Yes + A Hull subsystem called "Ablative Armour"
#
#	D: Phase Cloak
#		0: No
#		1: Yes
#
#	E:Corbinite Reflector
#		0: No
#		1: Cast back torpedoes
#		2: Cast back torpedoes and disruptors
#
#	F:Offensive Tractors
#		0: None
#		1: Inversion Beam
#		2: UCB
#
#		
########################################################################################################	

import App

g_fTractorStartFiring	= 0.0
g_fTractorStartFiringList= []
g_dictIonWeapon= {}

#########################################################################################################
#	{Mutator(pGame)}
#
#	Replaces an expansion pack in QuickBattle.py
#
#	Args:	pGame, the game itself
#
#
#	Return:	none
#########################################################################################################


def Expansion001(pGame):
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()

	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".WeaponHit")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_CLOAK_BEGINNING, pMission, __name__+".CloakStarted")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DECLOAK_BEGINNING, pMission, __name__+".DecloakStarted")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, pMission, __name__ + ".TractorStarted")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STOPPED_HITTING, pMission, __name__ + ".TractorEnded")



#########################################################################################################
#	{Main(pObject, pEvent)}
#
#	Calls the different Utilities
#
#	Args:	pObject -> a ship
#		PEvent  -> triggering Event
#
#
#	Return:	none
#########################################################################################################

def WeaponHit(pObject, pEvent):
	# Called when a weapon hits a target
	pShip = App.ShipClass_Cast(pEvent.GetDestination())

	multiVectralShields(pShip)
	drainerWeapon(pEvent)
	ablativeArmour(pShip)
	corboniteReflector(pObject,pEvent)
	#perimeterDefense(pObject,pEvent)
	#hyperAblativeArmour(pObject,pEvent)
	#ionCannonStart(pObject,pEvent)
	
def CloakStarted(pObject, pEvent):
	# Called when a ship cloaks
	pShip = App.ShipClass_Cast(pEvent.GetDestination())

	phaseCloakOn(pShip)

def DecloakStarted(pObject, pEvent):
	# Called when a ship decloaks
	pShip = App.ShipClass_Cast(pEvent.GetDestination())

	phaseCloakOff(pShip)

def TractorStarted(pObject, pEvent):
	TractorStart(pObject,pEvent)

def TractorEnded(pObject, pEvent):
	inversionBeamMain(pObject,pEvent)
	UCBMain(pObject,pEvent)
	#assimilationBeamMain(pObject,pEvent)
	
	

###############################################################################
#	{Utility}
#	
#	The explicit codes for the Utilites
#
#	Return:	none
###############################################################################

	
def multiVectralShields(pShip):
	if(positionSelectorShip(pShip,1)>0.0):   #Check if the ship is scripted to have multivectral shields
		pShields = pShip.GetShields()		
		if (pShields != None):
			pShieldTotal=0.0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):			#Calculate the total shieldpower
				pShieldTotal=pShieldTotal+pShields.GetCurShields(ShieldDir)
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				pShields.SetCurShields(ShieldDir,pShieldTotal/6.0)  		#Redistribute shields equally

def drainerWeapon(pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())



	try:
		pTorp=App.Torpedo_Cast(pEvent.GetSource())
		pTorpName=pTorp.GetLaunchSound()
	except:
		return
	

	if not (pTorpName=="BreenTorpedoXL"):
		return
							
	if(positionSelectorShip(pShip,2)<1.0):			#Check if the tartget is immune to the drainerweapon (Klingon, Breen, Coalition (new shipline))
		pPower = pShip.GetPowerSubsystem()
		pProp = pPower.GetProperty()
		pProp.SetPowerOutput(0.0)
		powerTest(pShip,0.0)				#Warp Core doesn't produce a single Watt anymore

		pShip.DisableGlowAlphaMaps()			#Dim the lights
		pShip.CompleteStop()
								#Only the batteries hold for a short time
				
		pShields = pShip.GetShields()			#Bye, shields
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
			pShields.SetCurShields(ShieldDir,0.0)

		pPlayer = MissionLib.GetPlayer ()
		if(pPlayer.GetObjID()==pShip.GetObjID()):
			pSound1 = App.g_kSoundManager.GetSound("PowerDisabled")
			pSound1.Play()

def ablativeArmour(pShip):
	if(positionSelectorShip(pShip,3)>=1.0):
									#Check if the ship is scripted to have Ablative Armour	
			repair=0		
			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			while (pSubsystem != None):
				if(pSubsystem.GetName()=="Ablative Armour"):			#The ship needs to have a Hull property with the name "Ablative Armour", which isn't destroyed !!!
					if(pSubsystem.GetCondition()>0.0):
						repair=1
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			pShip.EndGetSubsystemMatch(pIterator)
	
			if(repair==1):
				# Repair everything instantly except the ablative armour property

				pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

				while (pSubsystem != None):
					if(pSubsystem.GetName() != "Ablative Armour"):
						if(pSubsystem.GetCondition()>0.0):
							pSubsystem.SetCondition(pSubsystem.GetMaxCondition())
							iChildren = pSubsystem.GetNumChildSubsystems()
							if (iChildren > 0):
								for iIndex in range(iChildren):
									pChild = pSubsystem.GetChildSubsystem(iIndex)
									pChild.SetCondition(pChild.GetMaxCondition())
					pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
				pShip.EndGetSubsystemMatch(pIterator)
			

		

def phaseCloakOn(pShip):						#Check if the ship is scripted to have Phase Cloak
	if(positionSelectorShip(pShip,4)>=1.0):
		App.DamageableObject_Cast(pShip).SetCollisionsOn(0)	#Set collisions off, so simple !!!
		pCloakingSys = pShip.GetCloakingSubsystem()
		pCloakingSys.InstantCloak()

		pSound = App.g_kSoundManager.GetSound("PhaseCloakOn")
		pSound.Play()

			
def phaseCloakOff(pShip):
	if(positionSelectorShip(pShip,4)>=1.0):
		App.DamageableObject_Cast(pShip).SetCollisionsOn(1)		#Set collisions on, so simple !!!
		pCloakingSys = pShip.GetCloakingSubsystem()
		pCloakingSys.InstantDecloak()

		pSound = App.g_kSoundManager.GetSound("PhaseCloakOff")
		pSound.Play()


def corboniteReflector(pObject,pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())	
	pAttacker=App.ShipClass_Cast(pEvent.GetFiringObject())

	if(positionSelectorShip(pShip,5)>=1.0):				#Check if the ship is scripted to have the Reflector
		if(pEvent.GetWeaponType()==App.WeaponHitEvent.TORPEDO):	#Check if the weapon is a torpedo
			if(pEvent.IsHullHit()==1):			#If the hull is hit, the shields are failing, so they cannot reflect
				return (0)
				
			else:
				pSet=pAttacker.GetContainingSet()			
						
				kVect0=pAttacker.GetWorldLocation()
			
				kVectNiWorldHitPoint=pEvent.GetWorldHitPoint()		#Determine where the torpedo struck the shields
				kVectNiWorldHitNormal=pEvent.GetWorldHitNormal()
								
				kVectWorldHitPoint=App.TGPoint3()			#The "above "crap functions" give some more basic form of a vector that needed be to converted (costed me a lot of time to figure out)
				kVectWorldHitPoint.SetX(kVectNiWorldHitPoint.x)
				kVectWorldHitPoint.SetY(kVectNiWorldHitPoint.y)
				kVectWorldHitPoint.SetZ(kVectNiWorldHitPoint.z)

				kVectWorldHitNormal=App.TGPoint3()
				kVectWorldHitNormal.SetX(kVectNiWorldHitNormal.x)
				kVectWorldHitNormal.SetY(kVectNiWorldHitNormal.y)
				kVectWorldHitNormal.SetZ(kVectNiWorldHitNormal.z)
				n=kVectWorldHitNormal
				n.Unitize()

				

				#Not for novices in mathematics, the following part:
				# u= vector of approach
				# n= normal vector on the shieldgrid
				#
				#(1) 	The reflected vector r is parallel the plane alpha(u,n)
				#	r // alpha(u,n)
				#(2)	The reflected vector r is must form the same angle with n as u does
				#	(u^n) = (n^r)
				#
				#(S1)	In alpha(u,n) choose a vector m perpendular on n
				#	m =(u X n) X n	(property of the double cross product)
				#
				#(S2)	If the reflected vector r must form the same angle with n as u does,
				#	then it needs to have the same n-component in its (n,m) decomposition (still following?) as r,
				#	while the m-component in its (n,m) decomposition must be the negative.
				#	
				#	u = a * n + b * m	-->	r = a * n - b * m	(a,b) the (n,m) decompositionfactors of u
				#
				#(S3)	a and b are determinated by the projections on n and m of u
				#	a = (u.n) 
				#	b = (u.m) 
				#
				#	-> r = (u.n) n - (u.m) m

					
				u=kVect0				
				u.Subtract(kVectWorldHitPoint)
				u.Unitize()

				a=u.Dot(n)
				m0=u.Cross(n)
				m=m0.Cross(n)
				b=u.Dot(m)
			
				n.Scale(a)
				m.Scale(b)
				n.Subtract(m)

				r=n

				try:
					pTorp= App.Torpedo_Cast(pEvent.GetSource())
					pTorpPath=pTorp.GetModuleName()
				except:
					try:
						if(positionSelectorShip(pShip,5)>=2.0):
							pTorp=App.PulseWeapon_Cast(pEvent.GetSource())
							pTorpPath=pTorp.GetModuleName()
						else:
							return 0
					except:
						return 0
	
				# Luckily I found this definition in MissionLib.py
			
				FireTorpFromPoint(kVectWorldHitPoint,r,pTorpPath,pAttacker.GetObjID(),pShip)


				# Remove damage caused by the torpedo, to make the shield increase more realistic, I suggest you give the ship multivectral shielding.

				fDamage=pEvent.GetDamage()*0.9	#The power to reflect the weapon causes damage, 10% of the original damage
				shieldDistributePos(pShip,fDamage)


def TractorStart(pObject, pEvent):
	
	global g_fTractorStartFiringList

	pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
	pAttacker = pProjector.GetParentShip()
		

	
	if(positionSelectorShip(pAttacker,6)>=1.0):

		pProjectorProp=pProjector.GetProperty()
		pShip=App.ShipClass_Cast(pEvent.GetDestination())
		pTractor = pAttacker.GetTractorBeamSystem()

		tTuple=pAttacker.GetObjID(), App.g_kUtopiaModule.GetGameTime()
		g_fTractorStartFiringList.append(tTuple)		
		
			
def inversionBeamMain(pObject,pEvent):
	global g_fTractorStartFiringList	
	pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker = pProjector.GetParentShip()	
	fTimeStart=App.g_kUtopiaModule.GetGameTime()
	

	if( (positionSelectorShip(pAttacker,6)>=1.0) and (positionSelectorShip(pAttacker,6)<2.0)):
		pShieldsShip=pShip.GetShields()
		pShieldsAttacker=pAttacker.GetShields()

		j=0
			
		for i in g_fTractorStartFiringList:
			tTuple=g_fTractorStartFiringList[j]
			j=j+1

			if(tTuple[0]==pAttacker.GetObjID()):
				fTimeStart=tTuple[1]
				g_fTractorStartFiringList.remove(tTuple)
				break

		fTime=App.g_kUtopiaModule.GetGameTime()-fTimeStart
	
		fDrain=0.0
		fDrain=fTime*100.0

		shieldDistributeNeg(pShip,fDrain)	
		shieldDistributePos(pAttacker,fDrain)					




def UCBMain(pObject,pEvent):
	
	global g_fTractorStartFiringList	
	pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	pAttacker = pProjector.GetParentShip()	
	fTimeStart=App.g_kUtopiaModule.GetGameTime()

	if(positionSelectorShip(pAttacker,6)>=2.0 and (positionSelectorShip(pAttacker,6)<3.0)):
	
		j=0
		
		for i in g_fTractorStartFiringList:
			tTuple=g_fTractorStartFiringList[j]
			j=j+1

			if(tTuple[0]==pAttacker.GetObjID()):
				fTimeStart=tTuple[1]
				g_fTractorStartFiringList.remove(tTuple)
				break

		fTime=App.g_kUtopiaModule.GetGameTime()-fTimeStart

		fDrain=0.0
		fDrain=fTime*100.0

		pHull=pShip.GetHull()
		fHull=pHull.GetCondition()

		if(fDrain>fHull):
			pHull.SetCondition(0.0)
		else:
			pHull.SetCondition(fHull-fDrain)



				

##############################################################################
#	{Tools}
#	
#	The explicit codes for the the Tools used by {Utilities}
#	
#	Return:	various
###############################################################################

def positionSelectorShip(pShip,p):	
	#Selects a single number from ....JIHGFEDCBA(XX)  with A,1 B,2 C,3 ... J,10 ...
	a=pShip.GetAffiliation()
	n=0.0
	n=positionSelector(a,p)
	return n

def positionSelector(a,p):
	#A tricky algorithm that requires some insights in mathematics,
	#
	# (1) 	We do a integer division (with a rest) of a=...JIHGFEDCBAXX with ten^(p) to drop the (p) less significant decimals
	#	eg.	...JIHGFEDCBA --->	...JIHGFEDC,BA - ...JIHGFEDC,00   ----> ...000,BA
	# (2)	We get the disired number (in the example = B) by multiplying the previous number with then
	#	eg.	...000,BA * 10-> ...000B,AXX
	# (3)	In the comparisons we must work with < and > instead of ==
	

	n=(((a*1.0)/(pow(10,p)*1.0))-(a/pow(10,p)))*10.0
	
	return n

def positionSelectorShipBoolean(pShip,p,n):
	bFlag=0
	if( (positionSelectorShip(pShip,p)>=n) and (positionSelectorShip(pShip,p)<n+1)):
		bFlag=1
	return bFlag
		

def pow(x,y):	
	#BC Python lacks the pow so I need to declare it explicitely
	n=x
	i=1
	if(y<0):
		n=0
	if(y==0):
		n=1
	if(y==1):
		n=x
	while((y-i)>0):
		n=n*x
		i=i+1
	return n


def powerTest(pShip,a):
	#Just for debugging, to see how far a def goes without errors
	if(a<0 or a>1):
		a=0.5
	pPower = pShip.GetPowerSubsystem()
	if (pPower != None):
		pPower.SetMainBatteryPower(a*pPower.GetMainBatteryLimit())
		pPower.SetBackupBatteryPower(a*pPower.GetBackupBatteryLimit())


def FireTorpFromPoint(kPoint,kNormal,pcTorpScriptName, idTarget ,pShip,idTargetSubsystem = App.NULL_ID,fSpeed = 0.0,pcSetName = None):

	# This is an slightly altered version of the original definition (MissionLib.py) , to suit specific needs

	pTarget = App.ObjectClass_GetObjectByID(App.SetClass_GetNull(), idTarget)

	if (pcSetName != None):
		pSet = App.g_kSetManager.GetSet(pcSetName)
	elif (pTarget != None):
		pSet = pTarget.GetContainingSet()
	else:
		# No idea what set this is supposed to be in.
		return 0

	if (pSet == None):
		# No set.
		return 0

	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)

	if (idTargetSubsystem != App.NULL_ID):
		pSubsystem = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(idTargetSubsystem))
		if (pSubsystem != None):
			pTorp.SetTargetOffset(pSubsystem.GetPosition())
		else:
			pTorp.SetTargetOffset(kPoint)
	else:
		pTorp.SetTargetOffset(kPoint)

	
	pTorp.SetParent(pShip.GetObjID())

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)

	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	if (pTarget != None):
		kTorpLocation = pTorp.GetWorldLocation()
		kTargetLocation = pTarget.GetWorldLocation()

		kFwd = kNormal
		kFwd.Unitize()
		kPerp = kFwd.Perpendicular()
		kPerp2 = App.TGPoint3()
		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

		pTorp.AlignToVectors(kFwd, kPerp2)
		pTorp.UpdateNodeOnly()

	# Give the torpedo an appropriate speed.
	kVelocity = pTorp.GetWorldForwardTG()
	kVelocity.Unitize()
	if (fSpeed == 0.0):
		kVelocity.Scale(pTorp.GetLaunchSpeed())
	else:
		kVelocity.Scale(fSpeed)

	pTorp.SetVelocity(kVelocity)

	return 0


def shieldDistributePos(pShip,fDamage):
	i=0
	L=[0.0,0.0,0.0,0.0,0.0,0.0]
	iNumber=6.0
	fYield=fDamage

	pShields=pShip.GetShields()

	if ((pShields != None) and (fYield>0) ):
		while((iNumber>0) and (fYield>0)):
			i=0
			fSum=0.0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fAdd=fYield/iNumber+pShields.GetCurShields(ShieldDir)
				fMax=pShields.GetMaxShields(ShieldDir)
				fExcess=0

				if (L[i]<=0.0):
					if(fAdd<fMax):
						pShields.SetCurShields(ShieldDir,fAdd)
					else:
						pShields.SetCurShields(ShieldDir,fMax)					
						fExcess=fAdd-fMax
						fSum=fSum+fExcess
						L[i]=fExcess
				i=i+1

			fYield=fSum
			
			iNumber=L.count(0.0)
			

def shieldDistributeNeg(pShip,fDamage):
	i=0
	L=[0.0,0.0,0.0,0.0,0.0,0.0]
	iNumber=6.0
	fYield=fDamage

	pShields=pShip.GetShields()

	if ((pShields != None) and (fYield>0) ):
		while((iNumber>0) and (fYield>0)):
			i=0
			fSum=0.0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fSus=pShields.GetCurShields(ShieldDir)-fYield/iNumber
				fExcess=0

				if (L[i]<=0.0):
					if(fSus>0):
						pShields.SetCurShields(ShieldDir,fSus)
					else:
						pShields.SetCurShields(ShieldDir,0.0)					
						fExcess=(-1.0)*fSus
						fSum=fSum+fExcess
						L[i]=fExcess
				i=i+1

			fYield=fSum
			
			iNumber=L.count(0.0)





