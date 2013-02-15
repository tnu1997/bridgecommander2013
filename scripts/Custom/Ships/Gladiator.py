#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Gladiator"
iconName = "Gladiator"
longName = "Enterprise J Refit"
shipFile = "Gladiator"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.Gladiator = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Gladiator.desc = "In one possible future timeline, the USS Enterprise (NCC-1701-J) was a Federation starship of unspecified class in operation some time during the 26th century.\n\nThe Enterprise-J participated in the pivotal Battle of Procyon V, in which the forces of the Federation (at that point in history included the Klingons and Ithenites) defeated the invasion of the Sphere Builders; transdimensional beings who worked to colonize the galaxy by reconfiguring space. The temporal agent Daniels brought Jonathan Archer from the 22nd century aboard the Enterprise-J to witness the battle; so that he might convince Archer of the need to make peace between the Xindi and the Humans of the 22nd century. The crew of Enterprise-J included several Xindi, one of which owned a medal that Archer used to help convince Degra that he wanted peace.\n\nWeapons : \n10 Antipolaron Arrays \n8 Fwd Torpedo Tubes / 4 Aft Torpedo Tubes (Complement 1000 Quantum, 200 Advanced Quantum, 60 Chroniton)\n2 Fwd Quantum Singularity Torpedo Tubes / 1 Aft Quantum Singularity Torpedo Tube\n4 Pulse Cannons\n\nShield Rating : Heavy Shield Generator\nF: 50000\nA: 50000\nT: 50000\nB: 50000\nL: 50000\nR: 50000 \n\nHull Rating: Regenerative Armor Plating 45000\n\n\n"
Foundation.ShipDef.Gladiator.CloakingSFX = ""
Foundation.ShipDef.Gladiator.DeCloakingSFX = ""
Foundation.ShipDef.Gladiator.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.Gladiator.fCruiseWarp = 9.95 + 0.0001


if menuGroup:           Foundation.ShipDef.Gladiator.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Gladiator.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
