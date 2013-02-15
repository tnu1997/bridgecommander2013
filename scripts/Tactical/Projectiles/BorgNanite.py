########################################################################
#	Filename:	BorgNanite.py				       #
#								       #
#	Description:	Creates a Borg Nanite torpedo		       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(149.0 / 255.0, 198.0 / 255.0, 76.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.3,
					0.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.5,	
					0.6,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					42,		
					0.3,		
					0.5)

	pTorp.SetDamage(1200.0)
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime(60.0)
	pTorp.SetMaxAngularAccel(0.7)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(80.0)

def GetLaunchSound():
	return("Nanite Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Nanite")