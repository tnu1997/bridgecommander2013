########################################################################
#	Filename:	CardD.py				       #
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
	kOuterShellColor.SetRGBA(0.900000, 0.900000, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 0.850000, 0.172549, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 5.6, 0.45) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.09)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.CARDASSIANDISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(95.0)

def GetLaunchSound():
	return("Klingon Disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Cardassian Disruptor")

def GetDamage():
	return 800.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.01

def GetLifetime():
	return 20.0