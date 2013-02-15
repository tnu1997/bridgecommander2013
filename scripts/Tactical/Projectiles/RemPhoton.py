########################################################################
#	Filename:	RemPhoton.py				       #
#								       #
#	Description:	Creates a Reman Advanced Photon torpedo        #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.166667, 0.992157, 1.000000, 0.800000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.166667, 0.992157, 0.821569, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.166667, 0.992157, 0.751569, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.3,
					1.0,	 
					"data/Textures/Tactical/CRTorpCore.tga", 
					kGlowColor,
					3.0,	
					1.6,	 
					1.8,	
					"data/Textures/Tactical/Dur_TorpedoFlares.tga",
					kFlareColor,										
					20,		
					0.7,		
					0.4)

	pTorp.SetDamage(1250.0)
	pTorp.SetDamageRadiusFactor(0.175)
	pTorp.SetGuidanceLifetime(30.0)
	pTorp.SetMaxAngularAccel(0.4)

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
	return("Advanced Photon")