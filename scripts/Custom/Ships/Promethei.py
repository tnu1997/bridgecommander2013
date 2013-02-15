import App
import Foundation



# Ariel
abbrev = 'Ariel'
iconName = 'Prometheus'
longName = 'USS Ariel'
shipFile = 'Ariel' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Prometheus"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Ariel',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Ariel = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Ariel.desc = 'USS Ariel(NCC-75776)'

if menuGroup:           Foundation.ShipDef.Ariel.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Ariel.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ArielIDSwap(self):
	retval = {"Textures": [["1_glow", "Data/Models/SharedTextures/Prometheus/ArielID_glow.tga"], ["1_spec", "Data/Models/SharedTextures/Prometheus/ArielID_spec.tga"]]}
	return retval

Foundation.ShipDef.Ariel.__dict__["SDT Entry"] = ArielIDSwap



# Nirvana
abbrev = 'Nirvana'
iconName = 'Prometheus'
longName = 'USS Nirvana'
shipFile = 'Nirvana' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Prometheus"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Nirvana',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Nirvana = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Nirvana.desc = 'USS Nirvana(NCC-75913)'

if menuGroup:           Foundation.ShipDef.Nirvana.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Nirvana.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def NirvanaIDSwap(self):
	retval = {"Textures": [["1_glow", "Data/Models/SharedTextures/Prometheus/NirvanaID_glow.tga"], ["1_spec", "Data/Models/SharedTextures/Prometheus/NirvanaID_spec.tga"]]}
	return retval

Foundation.ShipDef.Nirvana.__dict__["SDT Entry"] = NirvanaIDSwap



# Prometheus
abbrev = 'RPrometheus'
iconName = 'Prometheus'
longName = 'USS Prometheus'
shipFile = 'RPrometheus' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Prometheus"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Prometheus',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.RPrometheus = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.RPrometheus.desc = 'USS Prometheus(NCC-74913)'

if menuGroup:           Foundation.ShipDef.RPrometheus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.RPrometheus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def RPrometheusIDSwap(self):
	retval = {"Textures": [["1_glow", "Data/Models/SharedTextures/Prometheus/PrometheusID_glow.tga"], ["1_spec", "Data/Models/SharedTextures/Prometheus/PrometheusID_spec.tga"]]}
	return retval

Foundation.ShipDef.RPrometheus.__dict__["SDT Entry"] = RPrometheusIDSwap