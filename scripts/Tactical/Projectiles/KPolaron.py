########################################################################
#	Filename:	KPolaron.py				       #
#								       #
#	Description:	Creates a large Klingon Polaron torpedo	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

    	kCoreColor = App.TGColorA()
    	kCoreColor.SetRGBA((253.0 / 255.0), (199.0 / 255.0), (253.0 / 255.0), 1.0)
    	kGlowColor = App.TGColorA()
    	kGlowColor.SetRGBA((252.0 / 255.0), (44.0 / 255.0), (252.0 / 255.0), 1.0)
    	kFlareColor = App.TGColorA()
    	kFlareColor.SetRGBA((61.0 / 255.0), (98.0 / 255.0), (239.0 / 255.0), 1.0)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.3,
					1.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					2.0,	 
					2.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					16,		
					1.2,		
					0.4)

	pTorp.SetDamage(1950.0)
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime(45.0)
	pTorp.SetMaxAngularAccel(0.55)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("Klingon Polaron")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Polaron")