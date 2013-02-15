#########################################################################
#	Filename:	KAdvPhoton2.py				       	#
#								       	#
#	Description:	Creates a small Klingon Advanced Photon torpedo	#
#								       	#
#	Designer:	Bryan Cook				       	#
#								       	#
#	Date:		5/28/2005				       	#
#########################################################################

import App

def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(190.0 / 255.0, 49.0 / 255.0, 48.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 218.0 / 255.0, 202.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.15,
					1.6,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.6,	 
					0.7,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					16,		
					0.4,		
					0.1)

	pTorp.SetDamage(1000.0)
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime(30.0)
	pTorp.SetMaxAngularAccel(0.35)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Klingon Photon")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Advanced Photon")