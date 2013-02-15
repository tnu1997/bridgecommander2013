###############################################################################
#	Filename:	PoleronTorp.py
#	By:		edtheborg
###############################################################################
# This torpedo uses the FTA mod...
#
# it actually passes through shields and damages whatever subsystem it was
# targeted at
#
# please refer to the bottom of this file for details on changing effects
###############################################################################

import App
pWeaponLock = {}

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(174.0 / 255.0, 152.0 / 255.0, 154.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(168.0 / 255.0, 115.0 / 255.0, 93.0 / 255.0, 0.200000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(169.0 / 255.0, 136.0 / 255.0, 140.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/PhqCore.tga",
					kCoreColor,
					0.1,
					1.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.2,	 
					0.3,	
					"data/Textures/Tactical/PhqFlares.tga",
					kFlareColor,										
					300,		
					0.1,		
					0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(22)

def GetLaunchSound():
	return("ftsChronoton")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Chroniton")

def GetDamage():
	return 0.00001

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 700

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.025

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.11

def TargetHit(pObject, pEvent):
	global pWeaponLock
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pShip==None):
		return
	try:
		id=pTorp.GetObjID()
		pSubsystem=pWeaponLock[id]
		del pWeaponLock[id]
	except:
		pSubsystem=pShip.GetHull()
	if (pSubsystem==None):
		return
	Dmg=pSubsystem.GetMaxCondition()*GetPercentage()
	if (Dmg<GetMinDamage()):
		Dmg=GetMinDamage()
	if (pSubsystem.GetCondition()>Dmg):
		pSubsystem.SetCondition(pSubsystem.GetCondition()-Dmg)
	else:
		pShip.DestroySystem(pSubsystem)
	return

def WeaponFired(pObject, pEvent):
	global pWeaponLock
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pTube=App.TorpedoTube_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pTube==None):
		return
	pShip=pTube.GetParentShip()
	if (pShip==None):
		return
	try:
		pWeaponLock[pTorp.GetObjID()]=pShip.GetTargetSubsystem()
	except:
		return
	return
