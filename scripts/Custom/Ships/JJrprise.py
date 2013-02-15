
import Foundation
import App

abbrev = 'JJrprise'
iconName = 'JJrprise'
longName = 'USS JJrprise'
shipFile = 'JJrprise' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY

credits = {
	'modName': 'JJrprise',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.JJrprise = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

Foundation.ShipDef.JJrprise.fMaxWarp = 8.8
Foundation.ShipDef.JJrprise.fCruiseWarp = 7.2
Foundation.ShipDef.JJrprise.desc = 'USS JJrprise'
Foundation.ShipDef.JJrprise.dTechs = {
	# Here comes the AdonisTMPWarmUp script config
	# The sequence describes the warm up, and it's reversed (timed correctly) on cool off
	# The numbers are moments in time
	# 2 requirements, the first moment is the normal texture, and the last moment
	# On the other hand, you can also use startTrack and stopTrack, with the same config, but you can time it differently, and use different textures (if you want)
	"AdonisTMPWarpStartUp": {
		"track": {
			"bussard_glow": {
				0.0: "data/Models/Ships/JJrprise/bussard_glow.tga", 
				1.0: "data/Models/Ships/JJrprise/bussardonline_glow.tga",
			}
		}
	}

}
if menuGroup:           Foundation.ShipDef.JJrprise.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JJrprise.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
