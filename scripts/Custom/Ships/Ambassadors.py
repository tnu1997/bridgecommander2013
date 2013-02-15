import App
import Foundation



# Ambassador
abbrev = 'LCAmbassador'
iconName = 'Ambassador'
longName = 'USS Ambassador'
shipFile = 'LCAmbassador' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Ambassador',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.LCAmbassador = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.LCAmbassador.desc = 'USS Ambassador(NCC-10521)'

if menuGroup:           Foundation.ShipDef.LCAmbassador.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.LCAmbassador.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Zhukov
abbrev = 'Zhukov'
iconName = 'Ambassador'
longName = 'USS Zhukov'
shipFile = 'Zhukov' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Zhukov',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Zhukov = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Zhukov.desc = 'USS Zhukov(NCC-26136)'

if menuGroup:           Foundation.ShipDef.Zhukov.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Zhukov.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Adelphi
abbrev = 'Adelphi'
iconName = 'Ambassador'
longName = 'USS Adelphi'
shipFile = 'Adelphi' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Adelphi',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Adelphi = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Adelphi.desc = 'USS Adelphi(NCC-26849)'

if menuGroup:           Foundation.ShipDef.Adelphi.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Adelphi.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Excalibur
abbrev = 'Excalibur'
iconName = 'Ambassador'
longName = 'USS Excalibur'
shipFile = 'Excalibur' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Excalibur',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Excalibur = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Excalibur.desc = 'USS Excalibur(NCC-26517)'

if menuGroup:           Foundation.ShipDef.Excalibur.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Excalibur.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Exeter
abbrev = 'Exeter'
iconName = 'Ambassador'
longName = 'USS Exeter'
shipFile = 'Exeter' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Exeter',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Exeter = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Exeter.desc = 'USS Exeter(NCC-26531)'

if menuGroup:           Foundation.ShipDef.Exeter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Exeter.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Gandhi
abbrev = 'Gandhi'
iconName = 'Ambassador'
longName = 'USS Gandhi'
shipFile = 'Gandhi' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Gandhi',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Gandhi = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Gandhi.desc = 'USS Gandhi(NCC-26632)'

if menuGroup:           Foundation.ShipDef.Gandhi.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Gandhi.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Horatio
abbrev = 'Horatio'
iconName = 'Ambassador'
longName = 'USS Horatio'
shipFile = 'Horatio' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Horatio',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Horatio = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Horatio.desc = 'USS Horatio(NCC-10532)'

if menuGroup:           Foundation.ShipDef.Horatio.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Horatio.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Valdemar
abbrev = 'Valdemar'
iconName = 'Ambassador'
longName = 'USS Valdemar'
shipFile = 'Valdemar' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Valdemar',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Valdemar = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Valdemar.desc = 'USS Valdemar(NCC-26198)'

if menuGroup:           Foundation.ShipDef.Valdemar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Valdemar.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]



# Yamaguchi
abbrev = 'Yamaguchi'
iconName = 'Ambassador'
longName = 'USS Yamaguchi'
shipFile = 'Yamaguchi' 
menuGroup = 'Named Ships'
playerMenuGroup = 'Named Ships'
SubMenu = "Ambassador"
species = App.SPECIES_AMBASSADOR
credits = {
	'modName': 'USS Yamaguchi',
	'author': 'LC Amaral',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Yamaguchi = Foundation.AmbassadorDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })

# Scotchy, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Yamaguchi.desc = 'USS Yamaguchi(NCC-26510)'

if menuGroup:           Foundation.ShipDef.Yamaguchi.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Yamaguchi.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]