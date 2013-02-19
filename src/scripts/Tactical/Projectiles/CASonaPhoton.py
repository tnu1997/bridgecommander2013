#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 100.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(100.0 / 255.0, 100.0 / 255.0, 155.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CASonaPhotonCore.tga",
					kCoreColor, 
					0.4,
					8.0,	 
					"data/Textures/Tactical/CASonaPhotonGlow.tga", 
					kGlowColor,
					6.0,	
					0.4,	 
					0.44,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					2,		
					0.2,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.CASONAPHOTON)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("Sona Photon")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 5.0

def GetMaxAngularAccel():
	return 0.8
