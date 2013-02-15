import App
import Foundation



# NX Nebula
abbrev = 'NXNebula'
iconName = 'NXNebula'
longName = 'USS Nebula(NX)'
shipFile = 'NXNebula' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Prototype"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Nebula(NX)',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.NXNebula = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.NXNebula.desc = 'USS Nebula(NX-60572)'

if menuGroup:           Foundation.ShipDef.NXNebula.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NXNebula.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Nebula
abbrev = 'CRNebula'
iconName = 'NebulaVar1_A'
longName = 'USS Nebula'
shipFile = 'CRNebula' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Nebula',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.CRNebula = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.CRNebula.desc = 'USS Nebula(NCC-60572)'

if menuGroup:           Foundation.ShipDef.CRNebula.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CRNebula.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CRNebulaIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/NebulaID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/NebulaID_spec.tga"]]}
	return retval

Foundation.ShipDef.CRNebula.__dict__["SDT Entry"] = CRNebulaIDSwap



# Horizon
abbrev = 'Horizon'
iconName = 'NebulaVar1_B'
longName = 'USS Horizon'
shipFile = 'Horizon' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Horizon',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Horizon = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Horizon.desc = 'USS Horizon(NCC-60831)'

if menuGroup:           Foundation.ShipDef.Horizon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Horizon.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def HorizonIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/HorizonID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/HorizonID_spec.tga"]]}
	return retval

Foundation.ShipDef.Horizon.__dict__["SDT Entry"] = HorizonIDSwap



# Beregovoy
abbrev = 'Beregovoy'
iconName = 'NebulaVar1_A'
longName = 'USS Beregovoy'
shipFile = 'Beregovoy' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1 Refit"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Beregovoy',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Beregovoy = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Beregovoy.desc = 'USS Beregovoy(NCC-79273)'

if menuGroup:           Foundation.ShipDef.Beregovoy.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Beregovoy.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BeregovoyIDSwap(self):
	retval = {"Textures": [["refitdefaultID_glow", "Data/Models/SharedTextures/Nebula/BeregovoyID_glow.tga"], ["refitdefaultID_spec", "Data/Models/SharedTextures/Nebula/BeregovoyID_spec.tga"]]}
	return retval

Foundation.ShipDef.Beregovoy.__dict__["SDT Entry"] = BeregovoyIDSwap



# Bonchune
abbrev = 'Bonchune'
iconName = 'NebulaVar1_B'
longName = 'USS Bonchune'
shipFile = 'Bonchune' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Bonchune',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Bonchune = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Bonchune.desc = 'USS Bonchune(NCC-70915)'

if menuGroup:           Foundation.ShipDef.Bonchune.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Bonchune.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BonchuneIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/BonchuneID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/BonchuneID_spec.tga"]]}
	return retval

Foundation.ShipDef.Bonchune.__dict__["SDT Entry"] = BonchuneIDSwap



# Vera Cruz
abbrev = 'VeraCruz'
iconName = 'NebulaVar1_A'
longName = 'USS Vera Cruz'
shipFile = 'VeraCruz' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Vera Cruz',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.VeraCruz = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.VeraCruz.desc = 'USS Vera Cruz(NCC-64118)'

if menuGroup:           Foundation.ShipDef.VeraCruz.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VeraCruz.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def VeraCruzIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/VeraCruzID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/VeraCruzID_spec.tga"]]}
	return retval

Foundation.ShipDef.VeraCruz.__dict__["SDT Entry"] = VeraCruzIDSwap



# Hera
abbrev = 'Hera'
iconName = 'NebulaVar1_A'
longName = 'USS Hera'
shipFile = 'Hera' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Hera',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Hera = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Hera.desc = 'USS Hera(NCC-62006)'

if menuGroup:           Foundation.ShipDef.Hera.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Hera.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def HeraIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/HeraID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/HeraID_spec.tga"]]}
	return retval

Foundation.ShipDef.Hera.__dict__["SDT Entry"] = HeraIDSwap



# Tereshkova
abbrev = 'Tereshkova'
iconName = 'NebulaVar1_A'
longName = 'USS Tereshkova'
shipFile = 'Tereshkova' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Tereshkova',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Tereshkova = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Tereshkova.desc = 'USS Tereshkova(NCC-68913)'

if menuGroup:           Foundation.ShipDef.Tereshkova.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Tereshkova.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def TereshkovaIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/TereshkovaID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/TereshkovaID_spec.tga"]]}
	return retval

Foundation.ShipDef.Tereshkova.__dict__["SDT Entry"] = TereshkovaIDSwap



# Minotaur
abbrev = 'Minotaur'
iconName = 'NebulaVar1_A'
longName = 'USS Minotaur'
shipFile = 'Minotaur' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1 Refit II"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Minotaur',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Minotaur = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Minotaur.desc = 'USS Minotaur(NCC-79993)'

if menuGroup:           Foundation.ShipDef.Minotaur.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Minotaur.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def MinotaurIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/MinotaurID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/MinotaurID_spec.tga"]]}
	return retval

Foundation.ShipDef.Minotaur.__dict__["SDT Entry"] = MinotaurIDSwap



# Endeavour
abbrev = 'Endeavour'
iconName = 'NebulaVar1_A'
longName = 'USS Endeavour'
shipFile = 'Endeavour' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Endeavour',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Endeavour = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Endeavour.desc = 'USS Endeavour(NCC-71805)'

if menuGroup:           Foundation.ShipDef.Endeavour.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Endeavour.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def EndeavourIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/EndeavourID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/EndeavourID_spec.tga"]]}
	return retval

Foundation.ShipDef.Endeavour.__dict__["SDT Entry"] = EndeavourIDSwap



# Dionysus
abbrev = 'Dionysus'
iconName = 'NebulaVar1_A'
longName = 'USS Dionysus'
shipFile = 'Dionysus' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1 Refit"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Dionysus',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Dionysus = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Dionysus.desc = 'USS Dionysus(NCC-71420)'

if menuGroup:           Foundation.ShipDef.Dionysus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Dionysus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def DionysusIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/DionysusID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/DionysusID_spec.tga"]]}
	return retval

Foundation.ShipDef.Dionysus.__dict__["SDT Entry"] = DionysusIDSwap



# Proxima
abbrev = 'Proxima'
iconName = 'NebulaVar2'
longName = 'USS Proxima'
shipFile = 'Proxima' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 2"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Proxima',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Proxima = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Proxima.desc = 'USS Proxima(NCC-61952)'

if menuGroup:           Foundation.ShipDef.Proxima.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Proxima.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ProximaIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/ProximaID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/ProximaID_spec.tga"]]}
	return retval

Foundation.ShipDef.Proxima.__dict__["SDT Entry"] = ProximaIDSwap



# Proteus
abbrev = 'Proteus'
iconName = 'NebulaVar1_B'
longName = 'USS Proteus'
shipFile = 'Proteus' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Proteus',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Proteus = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Proteus.desc = 'USS Proteus(NCC-71201)'

if menuGroup:           Foundation.ShipDef.Proteus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Proteus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ProteusIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/ProteusID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/ProteusID_spec.tga"]]}
	return retval

Foundation.ShipDef.Proteus.__dict__["SDT Entry"] = ProteusIDSwap



# Indri
abbrev = 'Indri'
iconName = 'NebulaVar1_B'
longName = 'USS Indri'
shipFile = 'Indri' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Indri',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Indri = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Indri.desc = 'USS Indri(NCC-69803)'

if menuGroup:           Foundation.ShipDef.Indri.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Indri.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def IndriIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/IndriID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/IndriID_spec.tga"]]}
	return retval

Foundation.ShipDef.Indri.__dict__["SDT Entry"] = IndriIDSwap



# Monitor
abbrev = 'Monitor'
iconName = 'NebulaVar1_A'
longName = 'USS Monitor'
shipFile = 'Monitor' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Monitor',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Monitor = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Monitor.desc = 'USS Monitor(NCC-61826)'

if menuGroup:           Foundation.ShipDef.Monitor.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Monitor.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def MonitorIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/MonitorID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/MonitorID_spec.tga"]]}
	return retval

Foundation.ShipDef.Monitor.__dict__["SDT Entry"] = MonitorIDSwap



# Merrimack
abbrev = 'Merrimack'
iconName = 'NebulaVar1_A'
longName = 'USS Merrimack'
shipFile = 'Merrimack' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Merrimack',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Merrimack = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Merrimack.desc = 'USS Merrimack(NCC-61827)'

if menuGroup:           Foundation.ShipDef.Merrimack.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Merrimack.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def MerrimackIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/MerrimackID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/MerrimackID_spec.tga"]]}
	return retval

Foundation.ShipDef.Merrimack.__dict__["SDT Entry"] = MerrimackIDSwap



# Vulcan
abbrev = 'Vulcan'
iconName = 'NebulaVar1_A'
longName = 'USS Vulcan'
shipFile = 'Vulcan' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1 Refit II"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Vulcan',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Vulcan = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Vulcan.desc = 'USS Vulcan(NCC-80040)'

if menuGroup:           Foundation.ShipDef.Vulcan.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Vulcan.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def VulcanIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/VulcanID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/VulcanID_spec.tga"]]}
	return retval

Foundation.ShipDef.Vulcan.__dict__["SDT Entry"] = VulcanIDSwap



# New England
abbrev = 'NewEngland'
iconName = 'NebulaVar1_A'
longName = 'USS New England'
shipFile = 'NewEngland' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1 Refit"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS New England',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.NewEngland = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.NewEngland.desc = 'USS New England(NCC-79366)'

if menuGroup:           Foundation.ShipDef.NewEngland.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NewEngland.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def NewEnglandIDSwap(self):
	retval = {"Textures": [["refitdefaultID_glow", "Data/Models/SharedTextures/Nebula/NewEnglandID_glow.tga"], ["refitdefaultID_spec", "Data/Models/SharedTextures/Nebula/NewEnglandID_spec.tga"]]}
	return retval

Foundation.ShipDef.NewEngland.__dict__["SDT Entry"] = NewEnglandIDSwap



# Sojourner
abbrev = 'Sojourner'
iconName = 'NebulaVar3'
longName = 'USS Sojourner'
shipFile = 'Sojourner' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 3"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Sojourner',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Sojourner = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Sojourner.desc = 'USS Sojourner(NCC-79711)'

if menuGroup:           Foundation.ShipDef.Sojourner.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Sojourner.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SojournerIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/SojournerID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/SojournerID_spec.tga"]]}
	return retval

Foundation.ShipDef.Sojourner.__dict__["SDT Entry"] = SojournerIDSwap



# Ulysses
abbrev = 'Ulysses'
iconName = 'NebulaVar1_A'
longName = 'USS Ulysses'
shipFile = 'Ulysses' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Ulysses',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Ulysses = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Ulysses.desc = 'USS Ulysses(NCC-66808)'

if menuGroup:           Foundation.ShipDef.Ulysses.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Ulysses.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def UlyssesIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/UlyssesID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/UlyssesID_spec.tga"]]}
	return retval

Foundation.ShipDef.Ulysses.__dict__["SDT Entry"] = UlyssesIDSwap



# Honshu
abbrev = 'Honshu'
iconName = 'NebulaVar1_A'
longName = 'USS Honshu'
shipFile = 'Honshu' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Honshu',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Honshu = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Honshu.desc = 'USS Honshu(NCC-71454)'

if menuGroup:           Foundation.ShipDef.Honshu.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Honshu.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def HonshuIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/HonshuID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/HonshuID_spec.tga"]]}
	return retval

Foundation.ShipDef.Honshu.__dict__["SDT Entry"] = HonshuIDSwap



# Bristol
abbrev = 'Bristol'
iconName = 'NebulaVar1_A'
longName = 'USS Bristol'
shipFile = 'Bristol' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Bristol',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Bristol = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Bristol.desc = 'USS Bristol(NCC-68807)'

if menuGroup:           Foundation.ShipDef.Bristol.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Bristol.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BristolIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/BristolID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/BristolID_spec.tga"]]}
	return retval

Foundation.ShipDef.Bristol.__dict__["SDT Entry"] = BristolIDSwap



# Lexington
abbrev = 'Lexington'
iconName = 'NebulaVar1_A'
longName = 'USS Lexington'
shipFile = 'Lexington' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Lexington',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Lexington = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Lexington.desc = 'USS Lexington(NCC-61832)'

if menuGroup:           Foundation.ShipDef.Lexington.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Lexington.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def LexingtonIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/LexingtonID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/LexingtonID_spec.tga"]]}
	return retval

Foundation.ShipDef.Lexington.__dict__["SDT Entry"] = LexingtonIDSwap



# Sutherland
abbrev = 'Sutherland'
iconName = 'NebulaVar1_A'
longName = 'USS Sutherland'
shipFile = 'Sutherland' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Sutherland',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Sutherland = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Sutherland.desc = 'USS Sutherland(NCC-70215)'

if menuGroup:           Foundation.ShipDef.Sutherland.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Sutherland.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def SutherlandIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/SutherlandID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/SutherlandID_spec.tga"]]}
	return retval

Foundation.ShipDef.Sutherland.__dict__["SDT Entry"] = SutherlandIDSwap



# Farragut
abbrev = 'Farragut'
iconName = 'NebulaVar1_A'
longName = 'USS Farragut'
shipFile = 'Farragut' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Farragut',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Farragut = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Farragut.desc = 'USS Farragut(NCC-60591)'

if menuGroup:           Foundation.ShipDef.Farragut.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Farragut.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def FarragutIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/FarragutID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/FarragutID_spec.tga"]]}
	return retval

Foundation.ShipDef.Farragut.__dict__["SDT Entry"] = FarragutIDSwap




# Khitomer
abbrev = 'Khitomer'
iconName = 'NebulaVar1_A'
longName = 'USS Khitomer'
shipFile = 'Khitomer' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Khitomer',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Khitomer = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Khitomer.desc = 'USS Khitomer(NCC-71906)'

if menuGroup:           Foundation.ShipDef.Khitomer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Khitomer.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def KhitomerIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/KhitomerID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/KhitomerID_spec.tga"]]}
	return retval

Foundation.ShipDef.Khitomer.__dict__["SDT Entry"] = KhitomerIDSwap




# Melbourne
abbrev = 'Melbourne'
iconName = 'NebulaVar3'
longName = 'USS Melbourne'
shipFile = 'Melbourne' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 3"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Melbourne',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Melbourne = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Melbourne.desc = 'USS Melbourne(NCC-62043)'

if menuGroup:           Foundation.ShipDef.Melbourne.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Melbourne.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def MelbourneIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/MelbourneID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/MelbourneID_spec.tga"]]}
	return retval

Foundation.ShipDef.Melbourne.__dict__["SDT Entry"] = MelbourneIDSwap



# Berkeley
abbrev = 'Berkeley'
iconName = 'NebulaVar2'
longName = 'USS Berkeley'
shipFile = 'Berkeley' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 2"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Berkeley',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Berkeley = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Berkeley.desc = 'USS Berkeley(NCC-64720)'

if menuGroup:           Foundation.ShipDef.Berkeley.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Berkeley.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BerkeleyIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/BerkeleyID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/BerkeleyID_spec.tga"]]}
	return retval

Foundation.ShipDef.Berkeley.__dict__["SDT Entry"] = BerkeleyIDSwap



# Phoenix
abbrev = 'Phoenix'
iconName = 'NebulaVar2'
longName = 'USS Phoenix'
shipFile = 'Phoenix' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 2"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Phoenix',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Phoenix = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Phoenix.desc = 'USS Phoenix(NCC-65420)'

if menuGroup:           Foundation.ShipDef.Phoenix.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Phoenix.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def PhoenixIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/PhoenixID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/PhoenixID_spec.tga"]]}
	return retval

Foundation.ShipDef.Phoenix.__dict__["SDT Entry"] = PhoenixIDSwap



# Nightingale
abbrev = 'Nightingale'
iconName = 'NebulaVar4'
longName = 'USS Nightingale'
shipFile = 'Nightingale' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 4"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Nightingale',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Nightingale = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Nightingale.desc = 'USS Nightingale(NCC-60805)'

if menuGroup:           Foundation.ShipDef.Nightingale.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Nightingale.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def NightingaleIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/NightingaleID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/NightingaleID_spec.tga"]]}
	return retval

Foundation.ShipDef.Nightingale.__dict__["SDT Entry"] = NightingaleIDSwap



# Shogun
abbrev = 'Shogun'
iconName = 'NebulaVar3'
longName = 'USS Shogun'
shipFile = 'Shogun' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 3"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Shogun',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Shogun = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Shogun.desc = 'USS Shogun(NCC-70056)'

if menuGroup:           Foundation.ShipDef.Shogun.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Shogun.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ShogunIDSwap(self):
	retval = {"Textures": [["defaultID_glow", "Data/Models/SharedTextures/Nebula/ShogunID_glow.tga"], ["defaultID_spec", "Data/Models/SharedTextures/Nebula/ShogunID_spec.tga"]]}
	return retval

Foundation.ShipDef.Shogun.__dict__["SDT Entry"] = ShogunIDSwap



# Stockholm
abbrev = 'Stockholm'
iconName = 'NebulaVar1_A'
longName = 'USS Stockholm'
shipFile = 'Stockholm' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Nebula"
SubSubMenu = "Variant 1 Refit"
species = App.SPECIES_NEBULA
credits = {
	'modName': 'USS Stockholm',
	'author': 'CaptainRussell',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Stockholm = Foundation.NebulaDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Stockholm.desc = 'USS Stockholm(NCC-79145)'

if menuGroup:           Foundation.ShipDef.Stockholm.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Stockholm.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def StockholmIDSwap(self):
	retval = {"Textures": [["refitdefaultID_glow", "Data/Models/SharedTextures/Nebula/StockholmID_glow.tga"], ["refitdefaultID_spec", "Data/Models/SharedTextures/Nebula/StockholmID_spec.tga"]]}
	return retval

Foundation.ShipDef.Stockholm.__dict__["SDT Entry"] = StockholmIDSwap