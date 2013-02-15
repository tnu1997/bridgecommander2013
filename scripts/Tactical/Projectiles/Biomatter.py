########################################################################
#	Filename:	Biomatter.py				       #
#								       #
#	Description:	Creates a Species 8472 Biomatter torpedo       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.850000, 1.000000, 0.600000, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.000000, 0.780000, 0.720000, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.000000, 1.000000, 0.650000, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					1.1,
					0.9,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					6.0,	
					5.2,	 
					6.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					88,		
					3.1,		
					3.0)

	pTorp.SetDamage(250000.0)
	pTorp.SetDamageRadiusFactor(0.95)
	pTorp.SetGuidanceLifetime(120.0)
	pTorp.SetMaxAngularAccel(1.0)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(75.00)

def GetLaunchSound():
	return("Biomatter Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Biomatter")