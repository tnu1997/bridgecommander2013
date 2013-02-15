import Foundation
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

Races["Romulan"] = RaceInfo("Romulan")
Races["Romulan"].AddEnemy("Cardassian")
Races["Romulan"].AddEnemy("Federation")
Races["Romulan"].AddEnemy("Dominion")
Races["Romulan"].AddEnemy("Breen")
Races["Romulan"].AddEnemy("Borg")
Races["Romulan"].AddEnemy("Romulan")
Races["Romulan"].SetPeaceValue(0.4)

# Add Romulan ships from the foundation
FdtnShips = Foundation.shipList
if FdtnShips:
	for Ship in FdtnShips:
		if not Ship.MenuGroup():
			continue
        	if (Ship.MenuGroup() == "Romulan Ships"):
			Races["Romulan"].AddShip(Ship.GetShipFile())

# Ship names from http://armada.filefront.com/file.info?ID=20882
# used a few unix commands (sed, tr, awk) to get the > "USS Shipname", < Format.
mynameslist = (
"Adrodius",
"Anturunia",
"Avarek",
"Avenius"
"Bandis",
"Celleius",
"Copidius",
"Dejerek",
"D'lassus",
"D'oras",
"D'pas",
"D'relan",
"D'thal",
"D'yl",
"Equitus",
"Flardius",
"Grocus",
"Imderia",
"Infini",
"Inydar",
"Irixidon",
"Kellem",
"Kerata",
"Kessar",
"Lemal",
"Lirilius",
"Lossal",
"Lukan",
"Marrus",
"Meret",
"Metollis",
"Nucarrus",
"Pespedius",
"Quarius",
"Rumaal",
"Seres",
"Suratak",
"S'alpal",
"S'pala",
"S'paut",
"Theron",
"Toralan",
"T'ala",
"T'anis",
"T'endadar",
"T'lasadon",
"T'mera",
"T'nar",
"T'onara",
"T'ossan",
"T'rarn",
"T'rassis",
"T'salin",
"T'san",
"T'sassan",
"T'varian",
"Vastar",
"Vestela",
"V'ashnu",
"V'eshan",
"V'laneth",
"V'lrath",
"V'tar",
"V'terex",
)

for name in mynameslist:
	Races["Romulan"].AddName(name)

# give it initial shuttle
Races["Romulan"].BuildShip("romulanshuttle")
