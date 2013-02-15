########################################################################
#	Filename:	RomD2.py				       #
#								       #
#	Description:	Creates a Romulan disruptor pulse globule      #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.172549, 1.000000, 0.172549, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 1.000000, 0.639216, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.8, 0.15) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("Romulan Disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Romulan Disruptor")

def GetDamage():
	return 300.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.00125

def GetLifetime():
	return 8.0