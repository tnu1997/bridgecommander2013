########################################################################
#	Filename:	FerePhoton.py				       #
#								       #
#	Description:	Creates a large Ferengi Photon torpedo         #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(1.000000, 0.500000, 0.000000, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(1.000000, 0.800000, 0.000000, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(1.000000, 0.750000, 0.000000, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.25,
					1.2,	 
					"data/Textures/Tactical/CRTorpCore.tga", 
					kGlowColor,
					3.4,	
					1.5,	 
					1.8,	
					"data/Textures/Tactical/Dur_TorpedoFlares.tga",
					kGlowColor,										
					16,		
					0.75,		
					0.4)

	pTorp.SetDamage(1000.0)
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime(30.0)
	pTorp.SetMaxAngularAccel(0.3)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(35.0)

def GetLaunchSound():
	return("Ferengi Photon")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Photon")