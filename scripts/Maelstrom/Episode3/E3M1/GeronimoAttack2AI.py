import App
def CreateAI(pShip):
	#########################################
	# Creating PlainAI Scripted at (107, 298)
	pScripted = App.PlainAI_Create(pShip, "Scripted")
	pScripted.SetScriptModule("RunScript")
	pScripted.SetInterruptable(1)
	pScript = pScripted.GetScriptInstance()
	pScript.SetScriptModule("Maelstrom.Episode3.E3M1.E3M1")
	pScript.SetFunction("MacCrayDestroyed")
	# Done creating PlainAI Scripted
	#########################################
	#########################################
	# Creating PlainAI Stay at (217, 299)
	pStay = App.PlainAI_Create(pShip, "Stay")
	pStay.SetScriptModule("Stay")
	pStay.SetInterruptable(1)
	# Done creating PlainAI Stay
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (163, 224)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (185, 255)
	pSequence.AddAI(pScripted)
	pSequence.AddAI(pStay)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating ConditionalAI IfDamaged at (163, 179)
	## Conditions:
	#### Condition HullLow
	pHullLow = App.ConditionScript_Create("Conditions.ConditionSystemBelow", "ConditionSystemBelow", pShip.GetName (),App.CT_HULL_SUBSYSTEM,.5)
	#### Condition PowerSystemLow
	pPowerSystemLow = App.ConditionScript_Create("Conditions.ConditionSystemBelow", "ConditionSystemBelow", pShip.GetName (), App.CT_POWER_SUBSYSTEM, .5)
	#### Condition WarpDamaged
	pWarpDamaged = App.ConditionScript_Create("Conditions.ConditionSystemBelow", "ConditionSystemBelow", pShip.GetName (), App.CT_WARP_ENGINE_SUBSYSTEM, .5)
	## Evaluation function:
	def EvalFunc(bHullLow, bPowerSystemLow, bWarpDamaged):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bHullLow or bPowerSystemLow or bWarpDamaged:
			return ACTIVE
		else:
			return DORMANT
	## The ConditionalAI:
	pIfDamaged = App.ConditionalAI_Create(pShip, "IfDamaged")
	pIfDamaged.SetInterruptable(1)
	pIfDamaged.SetContainedAI(pSequence)
	pIfDamaged.AddCondition(pHullLow)
	pIfDamaged.AddCondition(pPowerSystemLow)
	pIfDamaged.AddCondition(pWarpDamaged)
	pIfDamaged.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI IfDamaged
	#########################################
	#########################################
	# Creating CompoundAI Attack at (292, 179)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, "player", ChooseSubsystemTargets = 0)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (220, 81)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (244, 112)
	pPriorityList.AddAI(pIfDamaged, 1)
	pPriorityList.AddAI(pAttack, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (224, 32)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles