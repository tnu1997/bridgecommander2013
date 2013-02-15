# by USS Sovereign, Wormhole Cone cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'WormholeConeVar2_2'
iconName = 'WormholeConeVar2_2'
longName = 'WormholeConeVar2_2'
shipFile = 'WormholeConeVar2_2' 
species = App.SPECIES_GALAXY

# Credits                                                  
credits = {
	'modName': 'WormholeConeVar2_2',
	'author': 'BCS:TNG',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'This vessel should NOT appear in QB menus.'
}

# Ship foundation def
Foundation.ShipDef.WormholeConeVar2_2 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.WormholeConeVar2_2.desc = 'Bajoran Wormhole'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
