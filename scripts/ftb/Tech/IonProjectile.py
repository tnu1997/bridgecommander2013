import App
import FoundationTech
import MissionLib
from DisablerYields import *

class IonWeaponDef(MultipleDisableDef):

	def IsDrainYield(self):
		return 1

	def OnYield(self, pShip, pInstance, pEvent, pTorp):
                if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                        pImpulse = pShip.GetImpulseEngineSubsystem()
                        if pImpulse:
                                for i in range(pImpulse.GetNumChildSubsystems()):
                                        pEngine = pImpulse.GetChildSubsystem(i)
                                        fNewC = pEngine.GetMaxCondition() * pEngine.GetDisabledPercentage() / 1.8
                                        if fNewC < pEngine.GetCondition():
                                                pEngine.SetCondition(fNewC)


oIonWeapon = IonWeaponDef('Ion Weapon', {})
