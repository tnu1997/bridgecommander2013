########################################################################
#	Filename:	Antimatter.py				       #
#								       #
#	Description:	Creates a Cardassian Antimatter torpedo	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.500000, 0.5000000, 1.000000, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.294118, 0.184314, 0.811765, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.700000, 0.500000, 1.000000, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.2,
					1.3,	 
					"data/Textures/Tactical/CRTorpCore.tga", 
					kGlowColor,
					4.0,	
					1.6,	 
					2.0,	
					"data/Textures/Tactical/Dur_TorpedoFlares.tga",
					kFlareColor,										
					25,		
					0.75,		
					0.1)

	pTorp.SetDamage(1200.0)
	pTorp.SetDamageRadiusFactor(0.35)
	pTorp.SetGuidanceLifetime(45.0)
	pTorp.SetMaxAngularAccel(0.5)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.ANTIMATTER)

	return(0)

def GetLaunchSpeed():
	return(60.0)

def GetLaunchSound():
	return("Antimatter Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Antimatter")