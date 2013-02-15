import App
import Foundation



# NX Galaxy
abbrev = 'NXGalaxy'
iconName = 'NXGalaxy'
longName = 'USS Galaxy(NX)'
shipFile = 'NXGalaxy' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Prototype"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Galaxy(NX)',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.NXGalaxy = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.NXGalaxy.desc = 'USS Galaxy(Nx-70637)'

if menuGroup:           Foundation.ShipDef.NXGalaxy.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NXGalaxy.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Magellan
abbrev = 'Magellan'
iconName = 'Galaxy'
longName = 'USS Magellan'
shipFile = 'Magellan' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Magellan',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Magellan = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Magellan.desc = 'USS Magellan(NCC-71962)'

if menuGroup:           Foundation.ShipDef.Magellan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Magellan.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def MagellanIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/MagellanID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/MagellanID_spec.tga"]]}
	return retval

Foundation.ShipDef.Magellan.__dict__["SDT Entry"] = MagellanIDSwap



# Archimedes
abbrev = 'Archimedes'
iconName = 'WarGalaxy'
longName = 'USS Archimedes'
shipFile = 'Archimedes' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "War"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Archimedes',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Archimedes = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Archimedes.desc = 'USS Archimedes(NCC-78116)'

if menuGroup:           Foundation.ShipDef.Archimedes.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Archimedes.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ArchimedesIDSwap(self):
	retval = {"Textures": [["wardefaultID_glow", "Data/Models/SharedTextures/Galaxy/ArchimedesID_glow.tga"], ["wardefaultID_spec", "Data/Models/SharedTextures/Galaxy/ArchimedesID_spec.tga"]]}
	return retval

Foundation.ShipDef.Archimedes.__dict__["SDT Entry"] = ArchimedesIDSwap



# Vantage
abbrev = 'Vantage'
iconName = 'Galaxy'
longName = 'USS Vantage'
shipFile = 'Vantage' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Vantage',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Vantage = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Vantage.desc = 'USS Vantage(NCC-71883)'

if menuGroup:           Foundation.ShipDef.Vantage.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Vantage.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def VantageIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/VantageID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/VantageID_spec.tga"]]}
	return retval

Foundation.ShipDef.Vantage.__dict__["SDT Entry"] = VantageIDSwap



# Pangaea
abbrev = 'Pangaea'
iconName = 'Galaxy'
longName = 'USS Pangaea'
shipFile = 'Pangaea' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Pangaea',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Pangaea = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Pangaea.desc = 'USS Pangaea(NCC-71883)'

if menuGroup:           Foundation.ShipDef.Pangaea.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Pangaea.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def PangaeaIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/PangaeaID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/PangaeaID_spec.tga"]]}
	return retval

Foundation.ShipDef.Pangaea.__dict__["SDT Entry"] = PangaeaIDSwap



# Excelsior-A
abbrev = 'ExcelsiorA'
iconName = 'GalaxyRefitI'
longName = 'USS Excelsior-A'
shipFile = 'ExcelsiorA' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit I"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Excelsior-A',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.ExcelsiorA = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.ExcelsiorA.desc = 'USS Excelsior(NCC-2000-A)'

if menuGroup:           Foundation.ShipDef.ExcelsiorA.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ExcelsiorA.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ExcelsiorAIDSwap(self):
	retval = {"Textures": [["refitdefaultID_glow", "Data/Models/SharedTextures/Galaxy/ExcelsiorID_glow.tga"], ["refitdefaultID_spec", "Data/Models/SharedTextures/Galaxy/ExcelsiorID_spec.tga"]]}
	return retval

Foundation.ShipDef.ExcelsiorA.__dict__["SDT Entry"] = ExcelsiorAIDSwap



# Buccaneer
abbrev = 'Buccaneer'
iconName = 'Galaxy'
longName = 'USS Buccaneer'
shipFile = 'Buccaneer' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Buccaneer',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Buccaneer = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Buccaneer.desc = 'USS Buccaneer(NCC-74187)'

if menuGroup:           Foundation.ShipDef.Buccaneer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Buccaneer.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BuccaneerIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/BuccaneerID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/BuccaneerID_spec.tga"]]}
	return retval

Foundation.ShipDef.Buccaneer.__dict__["SDT Entry"] = BuccaneerIDSwap



# Satie
abbrev = 'Satie'
iconName = 'GalaxyRefitI'
longName = 'USS Satie'
shipFile = 'Satie' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit I"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Satie',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Satie = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Satie.desc = 'USS Satie(NCC-74214)'

if menuGroup:           Foundation.ShipDef.Satie.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Satie.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SatieIDSwap(self):
	retval = {"Textures": [["refitdefaultID_glow", "Data/Models/SharedTextures/Galaxy/SatieID_glow.tga"], ["refitdefaultID_spec", "Data/Models/SharedTextures/Galaxy/SatieID_spec.tga"]]}
	return retval

Foundation.ShipDef.Satie.__dict__["SDT Entry"] = SatieIDSwap



# Valkyrie
abbrev = 'Valkyrie'
iconName = 'GalaxyRefitI'
longName = 'USS Valkyrie'
shipFile = 'Valkyrie' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit I"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Valkyrie',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Valkyrie = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Valkyrie.desc = 'USS Valkyrie(NCC-79556)'

if menuGroup:           Foundation.ShipDef.Valkyrie.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Valkyrie.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ValkyrieIDSwap(self):
	retval = {"Textures": [["refitdefaultID_glow", "Data/Models/SharedTextures/Galaxy/ValkyrieID_glow.tga"], ["refitdefaultID_spec", "Data/Models/SharedTextures/Galaxy/ValkyrieID_spec.tga"]]}
	return retval

Foundation.ShipDef.Valkyrie.__dict__["SDT Entry"] = ValkyrieIDSwap




# Chenkov
abbrev = 'Chenkov'
iconName = 'GalaxyRefitI'
longName = 'USS Chenkov'
shipFile = 'Chenkov' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit I"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Chenkov',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Chenkov = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Chenkov.desc = 'USS Chenkov(NCC-73009)'

if menuGroup:           Foundation.ShipDef.Chenkov.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Chenkov.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ChenkovIDSwap(self):
	retval = {"Textures": [["refitdefaultID_glow", "Data/Models/SharedTextures/Galaxy/ChenkovID_glow.tga"], ["refitdefaultID_spec", "Data/Models/SharedTextures/Galaxy/ChenkovID_spec.tga"]]}
	return retval

Foundation.ShipDef.Chenkov.__dict__["SDT Entry"] = ChenkovIDSwap




# Discovery
abbrev = 'Discovery'
iconName = 'Galaxy'
longName = 'USS Discovery'
shipFile = 'Discovery' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Discovery',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Discovery = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Discovery.desc = 'USS Discovery(NCC-71804)'

if menuGroup:           Foundation.ShipDef.Discovery.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Discovery.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def DiscoveryIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/DiscoveryID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/DiscoveryID_spec.tga"]]}
	return retval

Foundation.ShipDef.Discovery.__dict__["SDT Entry"] = DiscoveryIDSwap




# Enterprise-D
abbrev = 'EnterpriseD'
iconName = 'Galaxy'
longName = 'USS Enterprise-D'
shipFile = 'EnterpriseD' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Enterprise-D',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.EnterpriseD = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.EnterpriseD.desc = 'USS Enterprise(NCC-1701-D)'

if menuGroup:           Foundation.ShipDef.EnterpriseD.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseD.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def EnterpriseDIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/EnterpriseID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/EnterpriseID_spec.tga"]]}
	return retval

Foundation.ShipDef.EnterpriseD.__dict__["SDT Entry"] = EnterpriseDIDSwap



# Trinculo
abbrev = 'Trinculo'
iconName = 'WarGalaxy'
longName = 'USS Trinculo'
shipFile = 'Trinculo' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "War"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Trinculo',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Trinculo = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Trinculo.desc = 'USS Trinculo(NCC-71867)'

if menuGroup:           Foundation.ShipDef.Trinculo.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Trinculo.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def TrinculoIDSwap(self):
	retval = {"Textures": [["wardefaultID_glow", "Data/Models/SharedTextures/Galaxy/TrinculoID_glow.tga"], ["wardefaultID_spec", "Data/Models/SharedTextures/Galaxy/TrinculoID_spec.tga"]]}
	return retval

Foundation.ShipDef.Trinculo.__dict__["SDT Entry"] = TrinculoIDSwap



# Galaxy
abbrev = 'SNSGalaxy'
iconName = 'Galaxy'
longName = 'USS Galaxy'
shipFile = 'SNSGalaxy' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Galaxy',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.SNSGalaxy = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.SNSGalaxy.desc = 'USS Galaxy(NCC-70637)'

if menuGroup:           Foundation.ShipDef.SNSGalaxy.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SNSGalaxy.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SNSGalaxyIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/GalaxyID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/GalaxyID_spec.tga"]]}
	return retval

Foundation.ShipDef.SNSGalaxy.__dict__["SDT Entry"] = SNSGalaxyIDSwap



# Dauntless
abbrev = 'Dauntless'
iconName = 'Galaxy'
longName = 'USS Dauntless'
shipFile = 'Dauntless' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Dauntless',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Dauntless = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Dauntless.desc = 'USS Dauntless(NCC-71879)'

if menuGroup:           Foundation.ShipDef.Dauntless.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Dauntless.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def DauntlessIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/DauntlessID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/DauntlessID_spec.tga"]]}
	return retval

Foundation.ShipDef.Dauntless.__dict__["SDT Entry"] = DauntlessIDSwap



# Odyssey
abbrev = 'Odyssey'
iconName = 'Galaxy'
longName = 'USS Odyssey'
shipFile = 'Odyssey' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Odyssey',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Odyssey = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Odyssey.desc = 'USS Odyssey(NCC-71832)'

if menuGroup:           Foundation.ShipDef.Odyssey.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Odyssey.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def OdysseyIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/OdysseyID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/OdysseyID_spec.tga"]]}
	return retval

Foundation.ShipDef.Odyssey.__dict__["SDT Entry"] = OdysseyIDSwap



# Challenger
abbrev = 'Challenger'
iconName = 'Galaxy'
longName = 'USS Challenger'
shipFile = 'Challenger' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Challenger',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Challenger = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Challenger.desc = 'USS Challenger(NCC-71099)'

if menuGroup:           Foundation.ShipDef.Challenger.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Challenger.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ChallengerIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/ChallengerID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/ChallengerID_spec.tga"]]}
	return retval

Foundation.ShipDef.Challenger.__dict__["SDT Entry"] = ChallengerIDSwap



# San Francisco
abbrev = 'SanFrancisco'
iconName = 'WarGalaxy'
longName = 'USS San Francisco'
shipFile = 'SanFrancisco' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "War"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS San Francisco',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.SanFrancisco = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.SanFrancisco.desc = 'USS San Francisco(NCC-69480)'

if menuGroup:           Foundation.ShipDef.SanFrancisco.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.SanFrancisco.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SanFranciscoIDSwap(self):
	retval = {"Textures": [["wardefaultID_glow", "Data/Models/SharedTextures/Galaxy/SanFranciscoID_glow.tga"], ["wardefaultID_spec", "Data/Models/SharedTextures/Galaxy/SanFranciscoID_spec.tga"]]}
	return retval

Foundation.ShipDef.SanFrancisco.__dict__["SDT Entry"] = SanFranciscoIDSwap



# Yamato
abbrev = 'Yamato'
iconName = 'Galaxy'
longName = 'USS Yamato'
shipFile = 'Yamato' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Yamato',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Yamato = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Yamato.desc = 'USS Yamato(NCC-71807)'

if menuGroup:           Foundation.ShipDef.Yamato.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Yamato.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def YamatoIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/YamatoID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/YamatoID_spec.tga"]]}
	return retval

Foundation.ShipDef.Yamato.__dict__["SDT Entry"] = YamatoIDSwap



# Venture
abbrev = 'Venture'
iconName = 'GalaxyRefitI'
longName = 'USS Venture'
shipFile = 'Venture' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit I"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Venture',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Venture = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Venture.desc = 'USS Venture(NCC-71854)'

if menuGroup:           Foundation.ShipDef.Venture.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Venture.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def VentureIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/VentureID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/VentureID_spec.tga"]]}
	return retval

Foundation.ShipDef.Venture.__dict__["SDT Entry"] = VentureIDSwap



# Cortez
abbrev = 'Cortez'
iconName = 'GalaxyRefitI'
longName = 'USS Cortez'
shipFile = 'Cortez' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit I"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Cortez',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Cortez = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Cortez.desc = 'USS Cortez(NCC-71825)'

if menuGroup:           Foundation.ShipDef.Cortez.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Cortez.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CortezIDSwap(self):
	retval = {"Textures": [["refitdefaultID_glow", "Data/Models/SharedTextures/Galaxy/CortezID_glow.tga"], ["refitdefaultID_spec", "Data/Models/SharedTextures/Galaxy/CortezID_spec.tga"]]}
	return retval

Foundation.ShipDef.Cortez.__dict__["SDT Entry"] = CortezIDSwap



# Constitution
abbrev = 'Constitution'
iconName = 'Galaxy'
longName = 'USS Constitution'
shipFile = 'Constitution' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Standard"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Constitution',
	'author': 'CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Constitution = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Constitution.desc = 'USS Constitution(NCC-1700-B)'

if menuGroup:           Foundation.ShipDef.Constitution.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Constitution.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ConstitutionIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Galaxy/ConstitutionID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Galaxy/ConstitutionID_spec.tga"]]}
	return retval

Foundation.ShipDef.Constitution.__dict__["SDT Entry"] = ConstitutionIDSwap




# Europa
abbrev = 'CREuropa'
iconName = 'Europa'
longName = 'USS Europa'
shipFile = 'CREuropa' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Europa"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Europa',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.CREuropa = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.CREuropa.desc = 'USS Europa(NCC-81327)'

if menuGroup:           Foundation.ShipDef.CREuropa.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CREuropa.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CREuropaIDSwap(self):
	retval = {"Textures": [["europadefaultID_glow", "Data/Models/SharedTextures/Europa/EuropaID_glow.tga"], ["europadefaultID_spec", "Data/Models/SharedTextures/Europa/EuropaID_spec.tga"]]}
	return retval

Foundation.ShipDef.CREuropa.__dict__["SDT Entry"] = CREuropaIDSwap



# NX Europa
abbrev = 'NXEuropa'
iconName = 'Europa'
longName = 'USS Europa(NX)'
shipFile = 'NXEuropa' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Europa"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Europa(NX)',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.NXEuropa = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.NXEuropa.desc = 'USS Europa(NX-71745)'

if menuGroup:           Foundation.ShipDef.NXEuropa.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NXEuropa.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def NXEuropaIDSwap(self):
	retval = {"Textures": [["europadefaultID_glow", "Data/Models/SharedTextures/Europa/NXEuropaID_glow.tga"], ["europadefaultID_spec", "Data/Models/SharedTextures/Europa/NXEuropaID_spec.tga"]]}
	return retval

Foundation.ShipDef.NXEuropa.__dict__["SDT Entry"] = NXEuropaIDSwap



# Aharonov
abbrev = 'Aharonov'
iconName = 'Europa'
longName = 'USS Aharonov'
shipFile = 'Aharonov' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Europa"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Aharonov',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Aharonov = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Aharonov.desc = 'USS Aharonov(NCC-84272)'

if menuGroup:           Foundation.ShipDef.Aharonov.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Aharonov.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AharonovIDSwap(self):
	retval = {"Textures": [["europadefaultID_glow", "Data/Models/SharedTextures/Europa/AharonovID_glow.tga"], ["europadefaultID_spec", "Data/Models/SharedTextures/Europa/AharonovID_spec.tga"]]}
	return retval

Foundation.ShipDef.Aharonov.__dict__["SDT Entry"] = AharonovIDSwap



# Bonaventure
abbrev = 'Bonaventure'
iconName = 'Europa'
longName = 'USS Bonaventure'
shipFile = 'Bonaventure' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Europa"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Bonaventure',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Bonaventure = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Bonaventure.desc = 'USS Bonaventure(NCC-85423)'

if menuGroup:           Foundation.ShipDef.Bonaventure.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Bonaventure.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BonaventureIDSwap(self):
	retval = {"Textures": [["europadefaultID_glow", "Data/Models/SharedTextures/Europa/BonaventureID_glow.tga"], ["europadefaultID_spec", "Data/Models/SharedTextures/Europa/BonaventureID_spec.tga"]]}
	return retval

Foundation.ShipDef.Bonaventure.__dict__["SDT Entry"] = BonaventureIDSwap



# Saratoga
abbrev = 'Saratoga'
iconName = 'Europa'
longName = 'USS Saratoga'
shipFile = 'Saratoga' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Europa"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Saratoga',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Saratoga = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Saratoga.desc = 'USS Saratoga(NCC-83759)'

if menuGroup:           Foundation.ShipDef.Saratoga.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Saratoga.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SaratogaIDSwap(self):
	retval = {"Textures": [["europadefaultID_glow", "Data/Models/SharedTextures/Europa/SaratogaID_glow.tga"], ["europadefaultID_spec", "Data/Models/SharedTextures/Europa/SaratogaID_spec.tga"]]}
	return retval

Foundation.ShipDef.Saratoga.__dict__["SDT Entry"] = SaratogaIDSwap



# Vladivostok
abbrev = 'Vladivostok'
iconName = 'Europa'
longName = 'USS Vladivostok'
shipFile = 'Vladivostok' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Europa"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Vladivostok',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Vladivostok = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Vladivostok.desc = 'USS Vladivostok(NCC-81994)'

if menuGroup:           Foundation.ShipDef.Vladivostok.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Vladivostok.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def VladivostokIDSwap(self):
	retval = {"Textures": [["europadefaultID_glow", "Data/Models/SharedTextures/Europa/VladivostokID_glow.tga"], ["europadefaultID_spec", "Data/Models/SharedTextures/Europa/VladivostokID_spec.tga"]]}
	return retval

Foundation.ShipDef.Vladivostok.__dict__["SDT Entry"] = VladivostokIDSwap



# Pegasus
abbrev = 'Pegasus'
iconName = 'GalaxyDreadnought'
longName = 'USS Pegasus'
shipFile = 'Pegasus' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Dreadnought"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Pegasus',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Pegasus = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Pegasus.desc = 'USS Pegasus(NCC-53847-A)'

if menuGroup:           Foundation.ShipDef.Pegasus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Pegasus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def PegasusIDSwap(self):
	retval = {"Textures": [["gddefaultID_glow", "Data/Models/SharedTextures/GalaxyDreadnought/PegasusID_glow.tga"], ["gddefaultID_spec", "Data/Models/SharedTextures/GalaxyDreadnought/PegasusID_spec.tga"]]}
	return retval

Foundation.ShipDef.Pegasus.__dict__["SDT Entry"] = PegasusIDSwap



# Olympus
abbrev = 'Olympus'
iconName = 'GalaxyDreadnought'
longName = 'USS Olympus'
shipFile = 'Olympus' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Dreadnought"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Olympus',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Olympus = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Olympus.desc = 'USS Olympus(NCC-1803-B)'

if menuGroup:           Foundation.ShipDef.Olympus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Olympus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def OlympusIDSwap(self):
	retval = {"Textures": [["gddefaultID_glow", "Data/Models/SharedTextures/GalaxyDreadnought/OlympusID_glow.tga"], ["gddefaultID_spec", "Data/Models/SharedTextures/GalaxyDreadnought/OlympusID_spec.tga"]]}
	return retval

Foundation.ShipDef.Olympus.__dict__["SDT Entry"] = OlympusIDSwap



# Challenger Refit
abbrev = 'ChallengerR'
iconName = 'GalaxyDreadnought'
longName = 'USS Challenger(R)'
shipFile = 'ChallengerR' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Dreadnought"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Challenger(R)',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.ChallengerR = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.ChallengerR.desc = 'USS Challenger(NCC-71099)'

if menuGroup:           Foundation.ShipDef.ChallengerR.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ChallengerR.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ChallengerRIDSwap(self):
	retval = {"Textures": [["gddefaultID_glow", "Data/Models/SharedTextures/GalaxyDreadnought/ChallengerRID_glow.tga"], ["gddefaultID_spec", "Data/Models/SharedTextures/GalaxyDreadnought/ChallengerRID_spec.tga"]]}
	return retval

Foundation.ShipDef.ChallengerR.__dict__["SDT Entry"] = ChallengerRIDSwap



# Leyte Gulf
abbrev = 'LeyteGulf'
iconName = 'GalaxyRefitII'
longName = 'USS Leyte Gulf'
shipFile = 'LeyteGulf' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit II"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Leyte Gulf',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.LeyteGulf = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.LeyteGulf.desc = 'USS Leyte Gulf(NCC-74840)'

if menuGroup:           Foundation.ShipDef.LeyteGulf.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.LeyteGulf.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def LeyteGulfIDSwap(self):
	retval = {"Textures": [["lgdefaultID_glow", "Data/Models/SharedTextures/GalaxyRefitII/LeyteGulfID_glow.tga"], ["lgdefaultID_spec", "Data/Models/SharedTextures/GalaxyRefitII/LeyteGulfID_spec.tga"]]}
	return retval

Foundation.ShipDef.LeyteGulf.__dict__["SDT Entry"] = LeyteGulfIDSwap



# Hornady
abbrev = 'Hornady'
iconName = 'GalaxyRefitII'
longName = 'USS Hornady'
shipFile = 'Hornady' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit II"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Hornady',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Hornady = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Hornady.desc = 'USS Hornady(NCC-79813)'

if menuGroup:           Foundation.ShipDef.Hornady.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Hornady.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def HornadyIDSwap(self):
	retval = {"Textures": [["lgdefaultID_glow", "Data/Models/SharedTextures/GalaxyRefitII/HornadyID_glow.tga"], ["lgdefaultID_spec", "Data/Models/SharedTextures/GalaxyRefitII/HornadyID_spec.tga"]]}
	return retval

Foundation.ShipDef.Hornady.__dict__["SDT Entry"] = HornadyIDSwap



# Sagan
abbrev = 'Sagan'
iconName = 'GalaxyRefitII'
longName = 'USS Sagan'
shipFile = 'Sagan' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Galaxy"
SubSubMenu = "Refit II"
species = App.SPECIES_GALAXY
credits = {
	'modName': 'USS Sagan',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Sagan = Foundation.GalaxyDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Sagan.desc = 'USS Sagan(NCC-79221)'

if menuGroup:           Foundation.ShipDef.Sagan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Sagan.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SaganIDSwap(self):
	retval = {"Textures": [["lgdefaultID_glow", "Data/Models/SharedTextures/GalaxyRefitII/SaganID_glow.tga"], ["lgdefaultID_spec", "Data/Models/SharedTextures/GalaxyRefitII/SaganID_spec.tga"]]}
	return retval

Foundation.ShipDef.Sagan.__dict__["SDT Entry"] = SaganIDSwap