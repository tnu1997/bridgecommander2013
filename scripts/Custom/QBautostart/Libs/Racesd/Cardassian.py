import Foundation
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

Races["Cardassian"] = RaceInfo("Cardassian")
Races["Cardassian"].AddFriendly("Dominion")
Races["Cardassian"].AddFriendly("Breen")
Races["Cardassian"].AddEnemy("Federation")
Races["Cardassian"].AddEnemy("Borg")
Races["Cardassian"].AddEnemy("Romulan")
Races["Cardassian"].AddEnemy("Klingon")
Races["Cardassian"].SetPeaceValue(0.20)

# Add cardassian ships from the foundation
FdtnShips = Foundation.shipList
if FdtnShips:
	for Ship in FdtnShips:
		if not Ship.MenuGroup():
			continue
        	if (Ship.MenuGroup() == "Card Ships"):
			Races["Cardassian"].AddShip(Ship.GetShipFile())
			
mynameslist = (
"Tanud",
"Duran",
"Gur",
"Gilam",
"Saereid",
"Hjading",
"Allaug",
"Hliring",
"Galandar",
"Nazirbakkhu",
"Sindurag",
"Khuled",
"Aenmi",
"Ostbi",
"Hjal",
"Steir",
"Indur",
"Hrulmgar",
"Hottild",
"Groki",
"Thungvi",
"Hroi",
"Larvard",
"Akar",
"Hugdin",
"Hifgrir",
"Beiti",
"Solmir",
"Bara",
"Grelni",
"Herkja",
"Rodi",
"Arod",
"Borgeiti",
"Otrolf",
"Ver",
"Neri",
"Isgegrid",
"Knadmid",
"Hrolreid",
"Hraetar",
"Skirkjar",
"Golpreid",
"Draring",
"Thogun",
"Hjodrglod",
"Hrundi",
"Thulgar",
"Stilod",
"Frik",
"Talfding",
"Hrirghild",
"Gwydre",
"Hirgyr",
"Gwynllon",
"Fariant",
"Heinmund",
"Silling",
"Hrolmar",
"Samod",
"Selian",
"Lugan",
"Cralas",
"Hirfyl",
"Gorkmod",
"Eigar",
"Swadlod",
"Baldir",
"Sunddydyw",
"Cinbert",
"Peurys",
"Hiwydd",
"Kardar",
"Lenawg",
"Gwunyr",
"Olfei",
"Llallbannon",
"Gwadydd",
"Haneid",
"Glydno",
"Fflyn",
"Teinnawg",
"Aneuawg",
"Efrei",
"Cawg",
"Nudeilig",
"Nwyfre",
"Myrgan",
"Uni",
"Halig",
"Maerch",
"Cilig",
"Arwm",
"Camwri",
"Gwalwn",
"Brawydd",
)

for name in mynameslist:
	Races["Cardassian"].AddName(name)


# give it initial ship
Races["Cardassian"].BuildShip("Hideki")
