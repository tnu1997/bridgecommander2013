import App
import Foundation



# Intimidator
abbrev = 'CRIntimidator'
iconName = 'Intimidator'
longName = 'USS Intimidator'
shipFile = 'CRIntimidator'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intimidator"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Intimidator',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.CRIntimidator = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.CRIntimidator.desc = 'USS Intimidator(NCC-81889)'

if menuGroup:           Foundation.ShipDef.CRIntimidator.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CRIntimidator.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CRIntimidatorIDSwap(self):
	retval = {"Textures": [["SovereignID_glow.tga", "data/Models/SharedTextures/Intimidator/IntimidatorID_glow.tga"], ["SovereignID_specular.tga", "data/Models/SharedTextures/Intimidator/IntimidatorID_specular.tga"]]}
	return retval

Foundation.ShipDef.CRIntimidator.__dict__["SDT Entry"] = CRIntimidatorIDSwap



# NX Intimidator
abbrev = 'NXIntimidator'
iconName = 'NXIntimidator'
longName = 'USS Intimidator(NX)'
shipFile = 'NXIntimidator'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intimidator"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Intimidator(NX)',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.NXIntimidator = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.NXIntimidator.desc = 'USS Intimidator(NX-81889)'

if menuGroup:           Foundation.ShipDef.NXIntimidator.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NXIntimidator.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Adjudicator
abbrev = 'Adjudicator'
iconName = 'Intimidator'
longName = 'USS Adjudicator'
shipFile = 'Adjudicator'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intimidator"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Adjudicator',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Adjudicator = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Adjudicator.desc = 'USS Adjudicator(NCC-84174)'

if menuGroup:           Foundation.ShipDef.Adjudicator.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Adjudicator.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AdjudicatorIDSwap(self):
	retval = {"Textures": [["SovereignID_glow.tga", "data/Models/SharedTextures/Intimidator/AdjudicatorID_glow.tga"], ["SovereignID_specular.tga", "data/Models/SharedTextures/Intimidator/AdjudicatorID_specular.tga"]]}
	return retval

Foundation.ShipDef.Adjudicator.__dict__["SDT Entry"] = AdjudicatorIDSwap



# Weinberg
abbrev = 'Weinberg'
iconName = 'Intimidator'
longName = 'USS Weinberg'
shipFile = 'Weinberg'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intimidator"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Weinberg',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Weinberg = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Weinberg.desc = 'USS Weinberg(NCC-84923)'

if menuGroup:           Foundation.ShipDef.Weinberg.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Weinberg.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def WeinbergIDSwap(self):
	retval = {"Textures": [["SovereignID_glow.tga", "data/Models/SharedTextures/Intimidator/WeinbergID_glow.tga"], ["SovereignID_specular.tga", "data/Models/SharedTextures/Intimidator/WeinbergID_specular.tga"]]}
	return retval

Foundation.ShipDef.Weinberg.__dict__["SDT Entry"] = WeinbergIDSwap



# Enterprise-F
abbrev = 'EnterpriseF'
iconName = 'Intimidator'
longName = 'USS Enterprise-F'
shipFile = 'EnterpriseF'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intimidator"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Enterprise-F',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.EnterpriseF = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.EnterpriseF.desc = 'USS Enterprise(NCC-1701-F)'

if menuGroup:           Foundation.ShipDef.EnterpriseF.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseF.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def EnterpriseFIDSwap(self):
	retval = {"Textures": [["SovereignID_glow.tga", "data/Models/SharedTextures/Intimidator/EnterpriseID_glow.tga"], ["SovereignID_specular.tga", "data/Models/SharedTextures/Intimidator/EnterpriseID_specular.tga"]]}
	return retval

Foundation.ShipDef.EnterpriseF.__dict__["SDT Entry"] = EnterpriseFIDSwap



# Schwarzchild
abbrev = 'Schwarzchild'
iconName = 'WarIntimidator'
longName = 'USS Schwarzchild'
shipFile = 'Schwarzchild'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Intimidator"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Schwarzchild',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Schwarzchild = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Schwarzchild.desc = 'USS Schwarzchild(NCC-82776)'

if menuGroup:           Foundation.ShipDef.Schwarzchild.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Schwarzchild.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SchwarzchildIDSwap(self):
	retval = {"Textures": [["warintID_glow.tga", "data/Models/SharedTextures/Intimidator/SchwarzchildID_glow.tga"], ["warintID_specular.tga", "data/Models/SharedTextures/Intimidator/SchwarzchildID_specular.tga"]]}
	return retval

Foundation.ShipDef.Schwarzchild.__dict__["SDT Entry"] = SchwarzchildIDSwap