import App
import Foundation



# Sovereign
abbrev = 'CGSovereign'
iconName = 'Sovereign'
longName = 'USS Sovereign'
shipFile = 'CGSovereign'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Sovereign"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS CGSovereign',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.CGSovereign = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.CGSovereign.desc = 'USS Sovereign(NCC-73811)'

if menuGroup:           Foundation.ShipDef.CGSovereign.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CGSovereign.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CGSovereignIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Sovereign/SovereignID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Sovereign/SovereignID_specular.tga"]]}
	return retval

Foundation.ShipDef.CGSovereign.__dict__["SDT Entry"] = CGSovereignIDSwap



# NX Sovereign
abbrev = 'NXSovereign'
iconName = 'NXSovereign'
longName = 'USS Sovereign(NX)'
shipFile = 'NXSovereign'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Sovereign"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Sovereign(NX)',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.NXSovereign = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.NXSovereign.desc = 'USS Sovereign(NX-73811)'

if menuGroup:           Foundation.ShipDef.NXSovereign.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NXSovereign.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Enterprise
abbrev = 'EnterpriseE'
iconName = 'Sovereign'
longName = 'USS Enterprise-E'
shipFile = 'EnterpriseE'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Sovereign"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS EnterpriseE-E',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.EnterpriseE = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.EnterpriseE.desc = 'USS Enterprise(NCC-1701-E)'

if menuGroup:           Foundation.ShipDef.EnterpriseE.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseE.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def EnterpriseEIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Sovereign/EnterpriseID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Sovereign/EnterpriseID_specular.tga"]]}
	return retval

Foundation.ShipDef.EnterpriseE.__dict__["SDT Entry"] = EnterpriseEIDSwap



# Regal
abbrev = 'Regal'
iconName = 'Sovereign'
longName = 'USS Regal'
shipFile = 'Regal'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Sovereign"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Regal',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Regal = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Regal.desc = 'USS Regal(NCC-74295)'

if menuGroup:           Foundation.ShipDef.Regal.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Regal.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def RegalIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Sovereign/RegalID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Sovereign/RegalID_specular.tga"]]}
	return retval

Foundation.ShipDef.Regal.__dict__["SDT Entry"] = RegalIDSwap



# Excelsior-B
abbrev = 'ExcelsiorB'
iconName = 'Sovereign'
longName = 'USS Excelsior-B'
shipFile = 'ExcelsiorB'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Sovereign"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Excelsior-B',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.ExcelsiorB = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.ExcelsiorB.desc = 'USS Excelsior(NCC-2000-B)'

if menuGroup:           Foundation.ShipDef.ExcelsiorB.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ExcelsiorB.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ExcelsiorBIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Sovereign/ExcelsiorID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Sovereign/ExcelsiorID_specular.tga"]]}
	return retval

Foundation.ShipDef.ExcelsiorB.__dict__["SDT Entry"] = ExcelsiorBIDSwap



# Sultan
abbrev = 'Sultan'
iconName = 'Sovereign'
longName = 'USS Sultan'
shipFile = 'Sultan'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Sovereign"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Sultan',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Sultan = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Sultan.desc = 'USS Sultan(NCC-75952)'

if menuGroup:           Foundation.ShipDef.Sultan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Sultan.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SultanIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Sovereign/SultanID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Sovereign/SultanID_specular.tga"]]}
	return retval

Foundation.ShipDef.Sultan.__dict__["SDT Entry"] = SultanIDSwap



# Pharaoh
abbrev = 'Pharaoh'
iconName = 'Sovereign'
longName = 'USS Pharaoh'
shipFile = 'Pharaoh'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Sovereign"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Pharaoh',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Pharaoh = Foundation.SovereignDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Pharaoh.desc = 'USS Pharaoh(NCC-75120)'

if menuGroup:           Foundation.ShipDef.Pharaoh.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Pharaoh.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def PharaohIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Sovereign/PharaohID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Sovereign/PharaohID_specular.tga"]]}
	return retval

Foundation.ShipDef.Pharaoh.__dict__["SDT Entry"] = PharaohIDSwap