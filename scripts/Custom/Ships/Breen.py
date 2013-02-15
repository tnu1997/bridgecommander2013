import Foundation
import App

#
#Foundation.ShipDef.breen.hasTGLName = 1
#Foundation.ShipDef.breen.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.breen.desc = 'oundation
import App

# Usually, you need only edit these seven lines
abbrev = 'Breen'				# Short name, no spaces, used as a preface for descriptions
iconName = 'Breen'				# Name of icon .tga file
longName = 'Breen Frigate'				# Long name with spaces
shipFile = 'Breen'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Breen Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Breen Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_SOVEREIGN		# I'm not sure how important this is.

Foundation.ShipDef.Breen = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.Breen.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.Breen.fMaxWarp = 9.3
Foundation.SoundDef("sfx/Weapons/Breen1.wav", "Breen1", 1.0)
Foundation.SoundDef("sfx/Weapons/Breen2.wav", "Breen2", 1.0)

if menuGroup:			Foundation.ShipDef.Breen.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.Breen.RegisterQBPlayerShipMenu(playerMenuGroup)
