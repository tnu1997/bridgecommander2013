# Custom Warp script

import App
import MissionLib
import Lib.LibEngineering
import AI.Player.InterceptTarget

sWarpButtonName = "In-System warp"
sNavPointNameAppend = "InSystemWarpNavPoint_"
fDist = 1e10

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.5",
                "Description": "Custom Warp",
                "needBridge": 0
            }


def GetInterceptNavPoint(pShip):
	if not pShip:
		return None
	
	pSet = pShip.GetContainingSet()
	
	if not pSet:
		return None
	
	pNav = App.Waypoint_Cast(App.ObjectClass_GetObject(pSet, sNavPointNameAppend + pShip.GetName()))
	if not pNav:
		pNav = App.Waypoint_Create(sNavPointNameAppend + pShip.GetName(), pSet.GetName(), None)
		pNav.SetNavPoint(1)
	pNav.SetTranslateXYZ(pShip.GetWorldLocation().GetX() + pShip.GetWorldForwardTG().GetX() * fDist, pShip.GetWorldLocation().GetY() + pShip.GetWorldForwardTG().GetY() * fDist, pShip.GetWorldLocation().GetZ() + pShip.GetWorldForwardTG().GetZ() * fDist)
	
	return pNav


def CustomWarp(pObject, pEvent):	
	pPlayer = MissionLib.GetPlayer()
	
	if pPlayer and not pPlayer.IsDoingInSystemWarp():
		pHull = pPlayer.GetHull()
		pImpulse = pPlayer.GetImpulseEngineSubsystem()
		pWarp = pPlayer.GetWarpEngineSubsystem()
		
		if pHull and pHull.GetConditionPercentage > 0.25 and pWarp and not pWarp.IsDisabled() and pImpulse and not pImpulse.IsDisabled():
			pNav = GetInterceptNavPoint(pPlayer)
			
			if pNav:
				MissionLib.SetPlayerAI("Helm", AI.Player.InterceptTarget.CreateAI(pPlayer, pNav))
				AppendOnSound(None, pPlayer, 20)
			else:
				MissionLib.SetPlayerAI("Helm", None)
		else:
			MissionLib.SetPlayerAI("Helm", None)
	else:
		MissionLib.SetPlayerAI("Helm", None)
		App.g_kSoundManager.PlaySound("OFF_Sound") 


def AppendOnSound(pAction, pShip, i):
	if pShip.IsDoingInSystemWarp():
		App.g_kSoundManager.PlaySound("ON_Sound")
		return 0
	
	if i > 0:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AppendOnSound", pShip, i-1), 0.5)
		pSeq.Play()
	
	return 0


def init():
	pButton = Lib.LibEngineering.CreateMenuButton(sWarpButtonName, "Helm", __name__ + ".CustomWarp")

	pSound = App.TGSound_Create("sfx/enter warp.wav", "ON_Sound", 0) 
	pSound.SetSFX(0) 
	pSound.SetInterface(1)
	pSound = App.TGSound_Create("sfx/exit warp.wav", "OFF_Sound", 0) 
	pSound.SetSFX(0)
	pSound.SetInterface(1)
