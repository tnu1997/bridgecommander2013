from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

Races["Sona"] = RaceInfo("Sona")

Races["Sona"].AddShip("SonaB")

# give it initial ship
Races["Sona"].BuildShip("SonaB")
