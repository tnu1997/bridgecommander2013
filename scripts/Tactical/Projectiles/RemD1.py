########################################################################
#	Filename:	RemD1.py				       #
#								       #
#	Description:	Creates a Reman disruptor globule	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.007843, 0.800000, 0.400000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 0.400000, 0.700000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.0, 0.35) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("Reman Disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Reman Disruptor")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0

def GetLifetime():
	return 15.0