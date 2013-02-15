import Foundation
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

Races["Dominion"] = RaceInfo("Dominion")
Races["Dominion"].AddFriendly("Cardassian")
Races["Dominion"].AddFriendly("Breen")
Races["Dominion"].AddEnemy("Federation")
Races["Dominion"].AddEnemy("Klingon")
Races["Dominion"].AddEnemy("Borg")
Races["Dominion"].AddEnemy("Romulan")
Races["Dominion"].SetPeaceValue(0.05)

# Add Dom ships from the foundation
FdtnShips = Foundation.shipList
if FdtnShips:
	for Ship in FdtnShips:
		if not Ship.MenuGroup():
			continue
        	if (Ship.MenuGroup() == "Dominion Ships"):
			Races["Dominion"].AddShip(Ship.GetShipFile())
			# Bugs always come in group of 3:
			if Ship.GetShipFile() == "bug" or Ship.GetShipFile() == "bugship":
				Races["Dominion"].AddEscort(Ship.GetShipFile(), Ship.GetShipFile())
				Races["Dominion"].AddEscort(Ship.GetShipFile(), Ship.GetShipFile())

# give it initial shuttle
Races["Dominion"].BuildShip("bug")