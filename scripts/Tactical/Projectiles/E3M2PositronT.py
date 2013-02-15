########################################################################
#	Filename:	PositronT.py				       #
#								       #
#	Description:	Creates a Kessok Positron torpedo	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(181.0 / 255.0, 230.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(65.0 / 255.0, 82.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(236.0 / 255.0, 255.0 / 255.0, 17.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.3,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					1.2,	 
					2.2,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					24,		
					1.15,		
					0.4)

	pTorp.SetDamage(600.0)
	pTorp.SetDamageRadiusFactor(0.35)
	pTorp.SetGuidanceLifetime(60.0)
	pTorp.SetMaxAngularAccel(2.0)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POSITRON)

	return(0)

def GetLaunchSpeed():
	return(10.0)

def GetLaunchSound():
	return("Positron Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Positron")