import App
import Foundation



# Intrepid
abbrev = 'Intrepid'
iconName = 'Intrepid'
longName = 'USS Intrepid'
shipFile = 'Intrepid'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intrepid"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Intrepid',
	'author': 'LC',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Intrepid = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Intrepid.desc = 'USS Intrepid(NCC-74600)'

if menuGroup:           Foundation.ShipDef.Intrepid.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Intrepid.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]




# Bellerophon
abbrev = 'Bellerophon'
iconName = 'Intrepid'
longName = 'USS Bellerophon'
shipFile = 'Bellerophon'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intrepid"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Bellerophon',
	'author': 'LC',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Bellerophon = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Bellerophon.desc = 'USS Bellerophon(NCC-74705)'

if menuGroup:           Foundation.ShipDef.Bellerophon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Bellerophon.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BellerophonIDSwap(self):
	retval = {"Textures": [["intrepid04_glow.tga", "data/Models/SharedTextures/Intrepid/Bellerophon04_glow.tga"], ["intrepid04_specular.tga", "data/Models/SharedTextures/Intrepid/Bellerophon04_specular.tga"]]}
	return retval

Foundation.ShipDef.Bellerophon.__dict__["SDT Entry"] = BellerophonIDSwap




# Fitzgerald
abbrev = 'Fitzgerald'
iconName = 'Intrepid'
longName = 'USS Fitzgerald'
shipFile = 'Fitzgerald'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intrepid"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Fitzgerald',
	'author': 'LC',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Fitzgerald = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Fitzgerald.desc = 'USS Fitzgerald(NCC-75771)'

if menuGroup:           Foundation.ShipDef.Fitzgerald.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Fitzgerald.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def FitzgeraldIDSwap(self):
	retval = {"Textures": [["intrepid04_glow.tga", "data/Models/SharedTextures/Intrepid/Fitzgerald04_glow.tga"], ["intrepid04_specular.tga", "data/Models/SharedTextures/Intrepid/Fitzgerald04_specular.tga"]]}
	return retval

Foundation.ShipDef.Fitzgerald.__dict__["SDT Entry"] = FitzgeraldIDSwap




# Voyager
abbrev = 'Voyager'
iconName = 'Intrepid'
longName = 'USS Voyager'
shipFile = 'Voyager'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intrepid"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Voyager',
	'author': 'LC',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Voyager = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Voyager.desc = 'USS Voyager(NCC-74656)'

if menuGroup:           Foundation.ShipDef.Voyager.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Voyager.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def VoyagerIDSwap(self):
	retval = {"Textures": [["intrepid04_glow.tga", "data/Models/SharedTextures/Intrepid/Voyager04_glow.tga"], ["intrepid04_specular.tga", "data/Models/SharedTextures/Intrepid/Voyager04_specular.tga"]]}
	return retval

Foundation.ShipDef.Voyager.__dict__["SDT Entry"] = VoyagerIDSwap