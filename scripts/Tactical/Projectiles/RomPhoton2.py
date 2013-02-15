########################################################################
#	Filename:	RomPhoton2.py				       #
#								       #
#	Description:	Creates a Romulan Photon torpedo    	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(65.0 / 255.0, 1.000000, 50.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(81.0 / 255.0, 1.000000, 17.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.25,
					1.0,	 
					"data/Textures/Tactical/CRTorpCore.tga", 
					kGlowColor,
					3.0,	
					1.4,	 
					1.6,	
					"data/Textures/Tactical/Dur_TorpedoFlares.tga",
					kGlowColor,										
					20,		
					0.6,		
					0.4)

	pTorp.SetDamage(800.0)
	pTorp.SetDamageRadiusFactor(0.175)
	pTorp.SetGuidanceLifetime(15.0)
	pTorp.SetMaxAngularAccel(0.25)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Romulan Photon")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Photon")

def GetDamage():
	return 750.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 5.0