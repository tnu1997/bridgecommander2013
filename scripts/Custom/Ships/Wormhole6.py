# by USS Sovereign, Wormhole cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'Wormhole6'
iconName = 'Wormhole6'
longName = 'Wormhole6'
shipFile = 'Wormhole6' 
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
Foundation.ShipDef.Wormhole6 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.Wormhole6.desc = 'Bajoran Wormhole'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

