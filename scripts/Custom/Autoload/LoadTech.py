import App
import Foundation
import techfunc


mode = Foundation.MutatorDef("New Technology System")


App.ET_INPUT_CLEAR_SECONDARY_TARGETS = App.UtopiaModule_GetNextEventType()
App.ET_INPUT_TOGGLE_SECONDARY_TARGET = App.UtopiaModule_GetNextEventType()

class FTBTrigger(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)
		self.name = name
		self.eventKey = eventKey
		self.dict = dict

        def __call__(self, pObject, pEvent, dict = {}):
                techfunc.ImportTechs()

        def Deactivate(self):
                techfunc.pluginsLoaded = {}
		Foundation.TriggerDef.__init__(self, self.name, self.eventKey, self.dict)

FTBTrigger('FTB Trigger', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )

if hasattr(Foundation, "g_kKeyBucket"):
	Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("take secondary Target", "take secondary Target", App.ET_INPUT_TOGGLE_SECONDARY_TARGET, App.KeyboardBinding.GET_INT_EVENT, 1, "Ship", dict = {"modes": [mode]}))
	Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("clear sec Targets", "clear sec Targets", App.ET_INPUT_CLEAR_SECONDARY_TARGETS, App.KeyboardBinding.GET_INT_EVENT, 1, "Ship", dict = {"modes": [mode]}))
