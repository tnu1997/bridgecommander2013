########################################################################
#	Filename:	FerePlasma.py				       #
#								       #
#	Description:	Creates a Ferengi plasma bolt globule	       #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		5/28/2005				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.380392, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 0.870588, 0.662745, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.8, 0.30) 	

	pTorp.SetDamage(700.0)
	pTorp.SetDamageRadiusFactor(0.08)
	pTorp.SetGuidanceLifetime(1.0)
	pTorp.SetMaxAngularAccel(0.0075)
	pTorp.SetLifetime(8.0)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.FUSIONBOLT)

	return(0)

def GetLaunchSpeed():
	return(46.0)

def GetLaunchSound():
	return("Klingon Disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Fusion Bolt")