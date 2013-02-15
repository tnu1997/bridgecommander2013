# by USS Sovereign, DS9FXMine cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXMine'
iconName = 'DS9FXMine'
longName = 'DS9FXMine'
shipFile = 'DS9FXMine' 
species = App.SPECIES_GALAXY

# Credits                                                  
credits = {
	'modName': 'DS9FXMine',
	'author': 'BCS:TNG',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'This vessel should NOT appear in QB menus.'
}

# Ship foundation def
Foundation.ShipDef.DS9FXMine = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXMine.desc = 'DS9FXMine'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

