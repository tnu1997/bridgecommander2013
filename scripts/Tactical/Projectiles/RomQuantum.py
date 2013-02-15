########################################################################
#	Filename:	RomQuantum.py				       #
#								       #
#	Description:	Creates a Reman Advanced Quantum torpedo       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.255000, 0.500000, 0.800000, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.200000, 0.700000, 0.600000, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.200000, 0.700000, 0.500000, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.4,
					2.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					1.0,	
					2.4,	 
					3.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					28,		
					1.8,		
					0.2)

	pTorp.SetDamage(2000.0)
	pTorp.SetDamageRadiusFactor(0.3)
	pTorp.SetGuidanceLifetime(60.0)
	pTorp.SetMaxAngularAccel(0.65)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("Romulan Quantum")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Advanced Quantum")