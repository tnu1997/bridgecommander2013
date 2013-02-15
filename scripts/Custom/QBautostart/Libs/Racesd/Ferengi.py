from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

Races["Ferengi"] = RaceInfo("Ferengi")
Races["Ferengi"].SetPeaceValue(0.90)

Races["Ferengi"].AddShip("Marauder")

# give it initial ship
Races["Ferengi"].BuildShip("Marauder")

# Resources
Races["Ferengi"].AddResource("Latinum", 100000.00)
