########################################################################
#	Filename:	RemD2.py				       #
#								       #
#	Description:	Creates a Reman high-powered disruptor globule #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.0064, 0.800000, 0.400000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.1, 0.400000, 0.900000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 3.0, 0.6) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Big Reman Disruptor")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Large Reman Disruptor")

def GetDamage():
	return 1500.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0

def GetLifetime():
	return 30.0