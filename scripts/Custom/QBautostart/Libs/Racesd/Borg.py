import Foundation
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

Races["Borg"] = RaceInfo("Borg")
Races["Borg"].AddEnemy("Klingon")
Races["Borg"].AddEnemy("Cardassian")
Races["Borg"].AddEnemy("Dominion")
Races["Borg"].AddEnemy("Breen")
Races["Borg"].AddEnemy("Borg")
Races["Borg"].AddEnemy("Romulan")
Races["Borg"].AddEnemy("Federation")
Races["Borg"].AddEnemy("8472")
Races["Borg"].SetPeaceValue(0.00)

# Add Borg ships from the foundation
FdtnShips = Foundation.shipList
if FdtnShips:
	for Ship in FdtnShips:
		if not Ship.MenuGroup():
			continue
        	if (Ship.MenuGroup() == "Borg Ships"):
			Races["Borg"].AddShip(Ship.GetShipFile())

mynameslist = (
"A923-02324",
"A923-98746",
"L923-64456",
"C923-02555",
"A923-15345",
"A923-02133",
"A923-19275",
"A923-16554",
"D923-98744",
"A923-53985",
"A923-98743",
"U923-15485",
"A923-02335",
"A923-02335",
"R923-32366",
"A923-02555",
"A923-98445",
"A923-08267",
"F923-98765",
"A923-75656",
"S923-18479",
"A923-55649",
"U923-11523",
"A923-63545",
"I472-18644",
"I472-48746",
"I472-16471",
"I472-05641",
"A472-68464",
"I472-12844",
"I472-78416",
"S472-16841",
"I472-48541",
"I472-85104",
"V472-56160",
"I472-63155",
"I472-04645",
"I472-45614",
"I472-05646",
"I472-78911",
"O472-46844",
"I472-78916",
"I472-16104",
"I472-96461",
"L472-75161",
"I472-91464",
"K472-48941",
"I472-46514",
)

for name in mynameslist:
	Races["Borg"].AddName(name)
