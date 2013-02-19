#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 100.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 100.0 / 255.0, 0.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CAFlame.tga",
					kCoreColor, 
					0.5,
					6.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					1.0,	
					0.2,	 
					0.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					0,		
					0.1,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.IONTORP)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("IonTorpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Ion Burst")

def GetDamage():
	return 100.0

def GetGuidanceLifetime():
	return 1.0

def GetMaxAngularAccel():
	return 0.5

import FoundationTech
import ftb.Tech.IonProjectile
      
sYieldName = ''
sFireName = ''

oFire = ftb.Tech.IonProjectile.oIonWeapon
FoundationTech.dOnFires[__name__] = oFire
FoundationTech.dYields[__name__] = oFire
