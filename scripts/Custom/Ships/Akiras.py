import App
import Foundation



# NX Akira
abbrev = 'NXAkira'
iconName = 'Akira'
longName = 'USS Akira(NX)'
shipFile = 'NXAkira' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Akira(NX)',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.NXAkira = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.NXAkira.desc = 'USS Akira(NX-62497)'

if menuGroup:           Foundation.ShipDef.NXAkira.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.NXAkira.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Broadsword
abbrev = 'Broadsword'
iconName = 'Akira'
longName = 'USS Broadsword'
shipFile = 'Broadsword' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Broadsword',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Broadsword = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Broadsword.desc = 'USS Broadsword(NCC-70542)'

if menuGroup:           Foundation.ShipDef.Broadsword.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Broadsword.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BroadswordIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/BroadswordID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/BroadswordID_specular.tga"]]}
	return retval

Foundation.ShipDef.Broadsword.__dict__["SDT Entry"] = BroadswordIDSwap



# Charger
abbrev = 'Charger'
iconName = 'Akira'
longName = 'USS Charger'
shipFile = 'Charger' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Charger',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Charger = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Charger.desc = 'USS Charger(NCC-63646)'

if menuGroup:           Foundation.ShipDef.Charger.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Charger.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ChargerIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/ChargerID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/ChargerID_specular.tga"]]}
	return retval

Foundation.ShipDef.Charger.__dict__["SDT Entry"] = ChargerIDSwap



# Charon
abbrev = 'Charon'
iconName = 'Akira'
longName = 'USS Charon'
shipFile = 'Charon' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Charon',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Charon = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Charon.desc = 'USS Charon(NCC-63839)'

if menuGroup:           Foundation.ShipDef.Charon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Charon.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CharonIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/CharonID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/CharonID_specular.tga"]]}
	return retval

Foundation.ShipDef.Charon.__dict__["SDT Entry"] = CharonIDSwap



# Asimov
abbrev = 'Asimov'
iconName = 'Akira'
longName = 'USS Asimov'
shipFile = 'Asimov' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Asimov',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Asimov = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Asimov.desc = 'USS Asimov(NCC-63985)'

if menuGroup:           Foundation.ShipDef.Asimov.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Asimov.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AsimovIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/AsimovID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/AsimovID_specular.tga"]]}
	return retval

Foundation.ShipDef.Asimov.__dict__["SDT Entry"] = AsimovIDSwap



# Kobe
abbrev = 'Kobe'
iconName = 'Akira'
longName = 'USS Kobe'
shipFile = 'Kobe' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Kobe',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Kobe = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Kobe.desc = 'USS Kobe(NCC-65269)'

if menuGroup:           Foundation.ShipDef.Kobe.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Kobe.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def KobeIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/KobeID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/KobeID_specular.tga"]]}
	return retval

Foundation.ShipDef.Kobe.__dict__["SDT Entry"] = KobeIDSwap



# Gettysburg
abbrev = 'Gettysburg'
iconName = 'Akira'
longName = 'USS Gettysburg'
shipFile = 'Gettysburg' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Gettysburg',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Gettysburg = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Gettysburg.desc = 'USS Gettysburg(NCC-65612)'

if menuGroup:           Foundation.ShipDef.Gettysburg.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Gettysburg.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def GettysburgIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/GettysburgID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/GettysburgID_specular.tga"]]}
	return retval

Foundation.ShipDef.Gettysburg.__dict__["SDT Entry"] = GettysburgIDSwap



# Euphrosyne
abbrev = 'Euphrosyne'
iconName = 'Akira'
longName = 'USS Euphrosyne'
shipFile = 'Euphrosyne' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Euphrosyne',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Euphrosyne = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Euphrosyne.desc = 'USS Euphrosyne(NCC-65178)'

if menuGroup:           Foundation.ShipDef.Euphrosyne.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Euphrosyne.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def EuphrosyneIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/EuphrosyneID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/EuphrosyneID_specular.tga"]]}
	return retval

Foundation.ShipDef.Euphrosyne.__dict__["SDT Entry"] = EuphrosyneIDSwap



# Griffin
abbrev = 'Griffin'
iconName = 'Akira'
longName = 'USS Griffin'
shipFile = 'Griffin' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Griffin',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Griffin = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Griffin.desc = 'USS Griffin(NCC-81107)'

if menuGroup:           Foundation.ShipDef.Griffin.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Griffin.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def GriffinIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/GriffinID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/GriffinID_specular.tga"]]}
	return retval

Foundation.ShipDef.Griffin.__dict__["SDT Entry"] = GriffinIDSwap



# Raleigh
abbrev = 'Raleigh'
iconName = 'Akira'
longName = 'USS Raleigh'
shipFile = 'Raleigh' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Raleigh',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Raleigh = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Raleigh.desc = 'USS Raleigh(NCC-81152)'

if menuGroup:           Foundation.ShipDef.Raleigh.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Raleigh.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def RaleighIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/RaleighID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/RaleighID_specular.tga"]]}
	return retval

Foundation.ShipDef.Raleigh.__dict__["SDT Entry"] = RaleighIDSwap



# Scorpion
abbrev = 'Scorpion'
iconName = 'Akira'
longName = 'USS Scorpion'
shipFile = 'Scorpion' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Scorpion',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Scorpion = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Scorpion.desc = 'USS Scorpion(NCC-70383)'

if menuGroup:           Foundation.ShipDef.Scorpion.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Scorpion.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ScorpionIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/ScorpionID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/ScorpionID_specular.tga"]]}
	return retval

Foundation.ShipDef.Scorpion.__dict__["SDT Entry"] = ScorpionIDSwap



# Theseus
abbrev = 'Theseus'
iconName = 'Akira'
longName = 'USS Theseus'
shipFile = 'Theseus' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Theseus',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Theseus = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Theseus.desc = 'USS Theseus(NCC-69153)'

if menuGroup:           Foundation.ShipDef.Theseus.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Theseus.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def TheseusIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/TheseusID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/TheseusID_specular.tga"]]}
	return retval

Foundation.ShipDef.Theseus.__dict__["SDT Entry"] = TheseusIDSwap



# Charybdis
abbrev = 'Charybdis'
iconName = 'Akira'
longName = 'USS Charybdis'
shipFile = 'Charybdis' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Charybdis',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Charybdis = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Charybdis.desc = 'USS Charybdis(NCC-64921)'

if menuGroup:           Foundation.ShipDef.Charybdis.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Charybdis.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CharybdisIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/CharybdisID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/CharybdisID_specular.tga"]]}
	return retval

Foundation.ShipDef.Charybdis.__dict__["SDT Entry"] = CharybdisIDSwap



# Thunderchild
abbrev = 'Thunderchild'
iconName = 'Akira'
longName = 'USS Thunderchild'
shipFile = 'Thunderchild' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Thunderchild',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Thunderchild = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Thunderchild.desc = 'USS Thunderchild(NCC-63549)'

if menuGroup:           Foundation.ShipDef.Thunderchild.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Thunderchild.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ThunderchildIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/ThunderchildID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/ThunderchildID_specular.tga"]]}
	return retval

Foundation.ShipDef.Thunderchild.__dict__["SDT Entry"] = ThunderchildIDSwap



# Atlantis
abbrev = 'Atlantis'
iconName = 'Akira'
longName = 'USS Atlantis'
shipFile = 'Atlantis' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Atlantis',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Atlantis = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Atlantis.desc = 'USS Atlantis(NCC-67781)'

if menuGroup:           Foundation.ShipDef.Atlantis.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Atlantis.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AtlantisIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/AtlantisID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/AtlantisID_specular.tga"]]}
	return retval

Foundation.ShipDef.Atlantis.__dict__["SDT Entry"] = AtlantisIDSwap



# Tiger
abbrev = 'Tiger'
iconName = 'Akira'
longName = 'USS Tiger'
shipFile = 'Tiger' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Tiger',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Tiger = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Tiger.desc = 'USS Tiger(NCC-71759)'

if menuGroup:           Foundation.ShipDef.Tiger.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Tiger.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def TigerIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/TigerID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/TigerID_specular.tga"]]}
	return retval

Foundation.ShipDef.Tiger.__dict__["SDT Entry"] = TigerIDSwap



# Geronimo
abbrev = 'Geronimo'
iconName = 'Akira'
longName = 'USS Geronimo'
shipFile = 'Geronimo' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Geronimo',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Geronimo = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Geronimo.desc = 'USS Geronimo(NCC-69302)'

if menuGroup:           Foundation.ShipDef.Geronimo.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Geronimo.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def GeronimoIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/GeronimoID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/GeronimoID_specular.tga"]]}
	return retval

Foundation.ShipDef.Geronimo.__dict__["SDT Entry"] = GeronimoIDSwap



# Devore
abbrev = 'Devore'
iconName = 'Akira'
longName = 'USS Devore'
shipFile = 'Devore' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Akira"
species = App.SPECIES_AKIRA
credits = {
	'modName': 'USS Devore',
	'author': 'SNS/CR',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Devore = Foundation.AkiraDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Devore.desc = 'USS Devore(NCC-64088)'

if menuGroup:           Foundation.ShipDef.Devore.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Devore.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def DevoreIDSwap(self):
	retval = {"Textures": [
	["akID_glow", "Data/Models/SharedTextures/Akira/DevoreID_glow.tga"],
	["akID_specular", "Data/Models/SharedTextures/Akira/DevoreID_specular.tga"]]}
	return retval

Foundation.ShipDef.Devore.__dict__["SDT Entry"] = DevoreIDSwap