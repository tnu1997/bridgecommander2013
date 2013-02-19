###############################################################################
#	Filename:	PositronTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of positron torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a positron torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 10.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 10.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CAKessok.tga",
					kCoreColor, 
					0.8,
					5.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					5.0,	
					0.3,	 
					0.8,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					50,		
					0.1,		
					0.05)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POSITRON)

	return(0)

def GetLaunchSpeed():
	return(20)

def GetLaunchSound():
	return("Positron Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Positron")

def GetDamage():
	return 3000.0

def GetGuidanceLifetime():
	return 40.0

def GetMaxAngularAccel():
	return 3.0
