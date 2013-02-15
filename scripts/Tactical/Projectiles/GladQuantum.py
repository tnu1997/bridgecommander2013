###############################################################################
#	Filename:	PhotonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a photon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 0.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(40.0 / 255.0, 40.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(200.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 0.100000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					4.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					7.0,	
					0.1,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,								100,		
					0.15,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Advanced Quantum")

def GetDamage():
	return 1500.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 0.4
