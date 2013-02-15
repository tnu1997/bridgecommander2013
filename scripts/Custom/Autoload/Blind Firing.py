import App
import Foundation
import techfunc
import Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu

mode = Foundation.MutatorDef("Blind Firing")


class TechExpansion(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
		Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu.LoadMenu()

TechExpansion('TechExpansion', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )

Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu.CreateKeys(mode)
