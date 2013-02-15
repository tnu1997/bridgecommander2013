# by USS Sovereign, DS9FXDummy cannot be registered or playable

# Imports
import Foundation
import App

# Ship details
abbrev = 'DS9FXDummy'
iconName = 'DS9FXDummy'
longName = 'DS9FXDummy'
shipFile = 'DS9FXDummy' 
species = App.SPECIES_GALAXY

# Credits                                                  
credits = {
	'modName': 'DS9FXDummy',
	'author': 'BCS:TNG',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': 'This vessel should NOT appear in QB menus.'
}

# Ship foundation def
Foundation.ShipDef.DS9FXDummy = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Description, but it's not used
Foundation.ShipDef.DS9FXDummy.desc = 'DS9FXDummy'
if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

