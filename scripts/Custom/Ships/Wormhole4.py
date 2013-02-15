# by USS Sovereign, Wormhole cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'Wormhole4'
iconName = 'Wormhole4'
longName = 'Wormhole4'
shipFile = 'Wormhole4' 
species = App.SPECIES_GALAXY

# Credits                                                  
credits = {
	'modName': 'Wormhole',
	'author': 'BCS:TNG',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'This vessel should NOT appear in QB menus.'
}

# Ship foundation def
Foundation.ShipDef.Wormhole4 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.Wormhole4.desc = 'Bajoran Wormhole'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

