from bcdebug import debug
# by USS Sovereign, a basic Starbase Attack AI

import App
import MissionLib

def CreateAI(pShip):
        debug(__name__ + ", CreateAI")
        pMission = MissionLib.GetMission ()
	pEnemyGroup = MissionLib.GetFriendlyGroup ()
	#########################################
	# Creating CompoundAI DS9Attack at (278, 110)
	import AI.Compound.StarbaseAttack
	pDS9Attack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9Attack
	#########################################
	#########################################
	# Creating ConditionalAI ConditionTimePassed at (161, 197)
	## Conditions:
	#### Condition ConditionTimer
	pConditionTimer = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 6, 0)
	## Evaluation function:
	def EvalFunc(bConditionTimer):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bConditionTimer:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionTimePassed = App.ConditionalAI_Create(pShip, "ConditionTimePassed")
	pConditionTimePassed.SetInterruptable(1)
	pConditionTimePassed.SetContainedAI(pDS9Attack)
	pConditionTimePassed.AddCondition(pConditionTimer)
	pConditionTimePassed.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionTimePassed
	#########################################
	return pConditionTimePassed
