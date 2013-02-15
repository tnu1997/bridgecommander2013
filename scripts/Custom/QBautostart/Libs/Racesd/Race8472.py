import Foundation
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

Races["8472"] = RaceInfo("8472")
Races["8472"].AddEnemy("Borg")
Races["8472"].SetPeaceValue(0.0)

# Add 8472 ships from the foundation
FdtnShips = Foundation.shipList
if FdtnShips:
	for Ship in FdtnShips:
		if not Ship.MenuGroup():
			continue
        	if (Ship.MenuGroup() == "8472 Ships"):
			Races["8472"].AddShip(Ship.GetShipFile())

mynameslist = (
"F4E23",
"F2B74",
"F5Y10",
"F7O98",
"F8G65",
"F5V63",
"F6R53",
"F1Q32",
"F6F54",
"F1M36",
"F1N76",
"F6D20",
"F9G98",
"F7N76",
"F9M94",
"F1F89",
"F5H18",
"F4M85",
"F2H44",
"F0S13",
"F0Y67",
"F8J54",
"F5KHY",
"F6G88",
"F4L09",
"F3P86",
"F4T65",
"F9M76",
"F1A87",
"F8Z36",
"F7F84",
"F9I81",
)
