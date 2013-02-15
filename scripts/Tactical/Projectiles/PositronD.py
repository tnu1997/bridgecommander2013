########################################################################
#	Filename:	PositronD.py				       #
#								       #
#	Description:	Creates a Kessok Positron pulse globule	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.172549, 0.172549, 1.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 0.639216, 1.000000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.2, 0.4) 	

	pTorp.SetDamage(1000.0)
	pTorp.SetDamageRadiusFactor(0.30)
	pTorp.SetGuidanceLifetime(0.0)
	pTorp.SetMaxAngularAccel(0.01)
	pTorp.SetLifetime(12.0)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KESSOKDISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("Positron Cannon")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Kessok Disruptor")