########################################################################
#	Filename:	CardPhoton.py				       #
#								       #
#	Description:	Creates a Cardassian Photon torpedo	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(1.000000, 0.647059, 0.192157, 0.666667)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(1.000000, 0.647059, 0.192157, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 200.0 / 255.0, 202.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.2,	 
					"data/Textures/Tactical/CRTorpCore.tga", 
					kGlowColor,
					3.0,	
					1.3,	 
					1.6,	
					"data/Textures/Tactical/Dur_TorpedoFlares.tga",
					kFlareColor,										
					12,		
					0.6,		
					0.4)

	pTorp.SetDamage(950.0)
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime(15.0)
	pTorp.SetMaxAngularAccel(0.2)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.CARDTORP)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("Cardassian Photon")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Photon")
