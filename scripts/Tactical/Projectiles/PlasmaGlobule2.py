########################################################################
#	Filename:	PlasmaGlobule2.py			       #
#								       #
#	Description:	Creates a giant Borg Plasma Cannon projectile  #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		8/18/2005				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.007843, 1.000000, 0.007843, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.239216, 1.000000, 0.239216, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 4.4, 2.2) 	
	pTorp.SetDamage(6000.0)
	pTorp.SetDamageRadiusFactor(0.6)
	pTorp.SetGuidanceLifetime(0.0)
	pTorp.SetMaxAngularAccel(0.015)
	pTorp.SetLifetime(120.0)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Borg Super Disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Borg Super Disruptor")