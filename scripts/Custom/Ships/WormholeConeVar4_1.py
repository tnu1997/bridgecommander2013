# by USS Sovereign, Wormhole Cone cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'WormholeConeVar4_1'
iconName = 'WormholeConeVar4_1'
longName = 'WormholeConeVar4_1'
shipFile = 'WormholeConeVar4_1' 
species = App.SPECIES_GALAXY

# Credits                                                  
credits = {
	'modName': 'WormholeConeVar4_1',
	'author': 'BCS:TNG',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'This vessel should NOT appear in QB menus.'
}

# Ship foundation def
Foundation.ShipDef.WormholeConeVar4_1 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.WormholeConeVar4_1.desc = 'Bajoran Wormhole'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

