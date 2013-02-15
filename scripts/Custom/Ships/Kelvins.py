import App
import Foundation



# Kelvin
abbrev = 'CRKelvin'
iconName = 'Kelvin'
longName = 'USS Kelvin'
shipFile = 'CRKelvin'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Kelvin"
SubSubMenu = "Standard"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Kelvin',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.CRKelvin = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.CRKelvin.desc = 'USS Kelvin(NCC-74042)'

if menuGroup:           Foundation.ShipDef.CRKelvin.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CRKelvin.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CRKelvinIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Kelvin/KelvinID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Kelvin/KelvinID_specular.tga"]]}
	return retval

Foundation.ShipDef.CRKelvin.__dict__["SDT Entry"] = CRKelvinIDSwap



# France
abbrev = 'France'
iconName = 'Kelvin'
longName = 'USS France'
shipFile = 'France'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Kelvin"
SubSubMenu = "Standard"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS France',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.France = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.France.desc = 'USS France(NCC-74123)'

if menuGroup:           Foundation.ShipDef.France.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.France.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def FranceIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Kelvin/FranceID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Kelvin/FranceID_specular.tga"]]}
	return retval

Foundation.ShipDef.France.__dict__["SDT Entry"] = FranceIDSwap



# Minneapolis
abbrev = 'Minneapolis'
iconName = 'Kelvin'
longName = 'USS Minneapolis'
shipFile = 'Minneapolis'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Kelvin"
SubSubMenu = "Standard"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Minneapolis',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Minneapolis = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Minneapolis.desc = 'USS Minneapolis(NCC-75674)'

if menuGroup:           Foundation.ShipDef.Minneapolis.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Minneapolis.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def MinneapolisIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Kelvin/MinneapolisID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Kelvin/MinneapolisID_specular.tga"]]}
	return retval

Foundation.ShipDef.Minneapolis.__dict__["SDT Entry"] = MinneapolisIDSwap



# Minneapolis-A
abbrev = 'MinneapolisA'
iconName = 'KelvinRefit'
longName = 'USS Minneapolis-A'
shipFile = 'MinneapolisA'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Kelvin"
SubSubMenu = "Refit"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Minneapolis-A',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.MinneapolisA = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.MinneapolisA.desc = 'USS Minneapolis(NCC-75674-A)'

if menuGroup:           Foundation.ShipDef.MinneapolisA.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MinneapolisA.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def MinneapolisAIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Kelvin/MinneapolisAID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Kelvin/MinneapolisAID_specular.tga"]]}
	return retval

Foundation.ShipDef.MinneapolisA.__dict__["SDT Entry"] = MinneapolisAIDSwap



# Boltzmann
abbrev = 'Boltzmann'
iconName = 'KelvinRefit'
longName = 'USS Boltzmann'
shipFile = 'Boltzmann'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Kelvin"
SubSubMenu = "Refit"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Boltzmann',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Boltzmann = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Boltzmann.desc = 'USS Boltzmann(NCC-78549)'

if menuGroup:           Foundation.ShipDef.Boltzmann.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Boltzmann.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BoltzmannIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Kelvin/BoltzmannID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Kelvin/BoltzmannID_specular.tga"]]}
	return retval

Foundation.ShipDef.Boltzmann.__dict__["SDT Entry"] = BoltzmannIDSwap



# Feynman
abbrev = 'Feynman'
iconName = 'KelvinRefit'
longName = 'USS Feynman'
shipFile = 'Feynman'
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Kelvin"
SubSubMenu = "Refit"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'USS Feynman',
	'author': 'CG/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Feynman = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Feynman.desc = 'USS Feynman(NCC-79130)'

if menuGroup:           Foundation.ShipDef.Feynman.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Feynman.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def FeynmanIDSwap(self):
	retval = {"Textures": [["defaultID_glow.tga", "data/Models/SharedTextures/Kelvin/FeynmanID_glow.tga"], ["defaultID_specular.tga", "data/Models/SharedTextures/Kelvin/FeynmanID_specular.tga"]]}
	return retval

Foundation.ShipDef.Feynman.__dict__["SDT Entry"] = FeynmanIDSwap