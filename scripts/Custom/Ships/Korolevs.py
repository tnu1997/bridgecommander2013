import App
import Foundation



# Korolev
abbrev = 'CRKorolev'
iconName = 'Korolev'
longName = 'USS Korolev'
shipFile = 'CRKorolev' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Korolev"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Korolev',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.CRKorolev = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu})

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.CRKorolev.desc = 'USS Korolev(NCC-58986)'

if menuGroup:           Foundation.ShipDef.CRKorolev.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CRKorolev.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CRKorolevIDSwap(self):
	retval = {"Textures": [["korolevdefaultID_glow", "Data/Models/SharedTextures/Korolev/KorolevID_glow.tga"], ["korolevdefaultID_spec", "Data/Models/SharedTextures/Korolev/KorolevID_spec.tga"]]}
	return retval

Foundation.ShipDef.CRKorolev.__dict__["SDT Entry"] = CRKorolevIDSwap




# Haarland
abbrev = 'Haarland'
iconName = 'Korolev'
longName = 'USS Haarland'
shipFile = 'Haarland' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Korolev"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Haarland',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Haarland = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu})

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Haarland.desc = 'USS Haarland(NCC-59312)'

if menuGroup:           Foundation.ShipDef.Haarland.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Haarland.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def HaarlandIDSwap(self):
	retval = {"Textures": [["korolevdefaultID_glow", "Data/Models/SharedTextures/Korolev/HaarlandID_glow.tga"], ["korolevdefaultID_spec", "Data/Models/SharedTextures/Korolev/HaarlandID_spec.tga"]]}
	return retval

Foundation.ShipDef.Haarland.__dict__["SDT Entry"] = HaarlandIDSwap




# Goddard
abbrev = 'Goddard'
iconName = 'Korolev'
longName = 'USS Goddard'
shipFile = 'Goddard' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Korolev"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Goddard',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Goddard = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu})

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Goddard.desc = 'USS Goddard(NCC-59621)'

if menuGroup:           Foundation.ShipDef.Goddard.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Goddard.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def GoddardIDSwap(self):
	retval = {"Textures": [["korolevdefaultID_glow", "Data/Models/SharedTextures/Korolev/GoddardID_glow.tga"], ["korolevdefaultID_spec", "Data/Models/SharedTextures/Korolev/GoddardID_spec.tga"]]}
	return retval

Foundation.ShipDef.Goddard.__dict__["SDT Entry"] = GoddardIDSwap




# Gadarene
abbrev = 'Gadarene'
iconName = 'Korolev'
longName = 'USS Gadarene'
shipFile = 'Gadarene' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Korolev"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Gadarene',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Gadarene = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu})

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Gadarene.desc = 'USS Gadarene(NCC-59682)'

if menuGroup:           Foundation.ShipDef.Gadarene.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Gadarene.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def GadareneIDSwap(self):
	retval = {"Textures": [["korolevdefaultID_glow", "Data/Models/SharedTextures/Korolev/GadareneID_glow.tga"], ["korolevdefaultID_spec", "Data/Models/SharedTextures/Korolev/GadareneID_spec.tga"]]}
	return retval

Foundation.ShipDef.Gadarene.__dict__["SDT Entry"] = GadareneIDSwap