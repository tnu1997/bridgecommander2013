#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 6/28/2006                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CRTacticalCube'
iconName = 'CRTacticalCube'
longName = 'CRTacticalCube'
shipFile = 'CRTacticalCube' 
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'CRTacticalCube',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.CRTacticalCube = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
Foundation.ShipDef.CRTacticalCube.hasTGLName = 1
Foundation.ShipDef.CRTacticalCube.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.CRTacticalCube.desc = 'No Description Available'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.CRTacticalCube.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CRTacticalCube.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
