import Foundation
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

Races["Breen"] = RaceInfo("Breen")
Races["Breen"].AddFriendly("Cardassian")
Races["Breen"].AddFriendly("Dominion")
Races["Breen"].AddEnemy("Federation")
Races["Breen"].AddEnemy("Klingon")
Races["Breen"].AddEnemy("Borg")
Races["Breen"].AddEnemy("Romulan")
Races["Breen"].SetPeaceValue(0.30)

# Add Dom ships from the foundation
FdtnShips = Foundation.shipList
if FdtnShips:
	for Ship in FdtnShips:
		if not Ship.MenuGroup():
			continue
        	if (Ship.MenuGroup() == "Breen Ships"):
			Races["Breen"].AddShip(Ship.GetShipFile())

# give it initial ship
Races["Breen"].BuildShip("Breen")
