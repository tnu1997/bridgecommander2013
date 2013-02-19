#script modified by Dragon

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(10.0 / 255.0, 10.0 / 255.0, 55.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CASonaCore.tga",
					kCoreColor, 
					0.4,
					2.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					1.0,	
					0.1,	 
					0.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.2,		
					0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.CASONA)

	return(0)

def GetLaunchSpeed():
	return(10.0)

def GetLaunchSound():
	return("Sona Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Nitrolitic Burst")

def GetDamage():
	return 2000.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.5
