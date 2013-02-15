########################################################################
#	Filename:	FedPulse2.py				       #
#								       #
#	Description:	Creates a Federation pulse phaser globule      #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.275000, 0.003922, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.2, 0.13) 	
	pTorp.SetDamage(600.0)
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime(0.0)
	pTorp.SetMaxAngularAccel(0.005)
	pTorp.SetLifetime(30.0)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Pulse Phaser")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Pulse Phaser")