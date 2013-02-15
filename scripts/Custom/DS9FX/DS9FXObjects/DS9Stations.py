from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# Over here we'll save the locations of stations which we'll load when we enter DS9 Map

# by USS Sovereign

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pDS9Selection = pModule.DS9Selection
pFederationSide = pModule.FederationSide

# Imports
import App
import loadspacehelper
import MissionLib

# Define stations in DS9 Map
def DS9SetStations():

        # Grab the system's name directly from the set file
        debug(__name__ + ", DS9SetStations")
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        import Custom.DS9FX.DS9FXShips

        if pFederationSide == 1:

                if pDS9Selection == 1:

                        # Create the station
                        DS9Name = "Deep_Space_9"
                        import Custom.DS9FX.DS9FXShips
                        pDS9 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDeepSpace9, DS9Set, DS9Name, "DS9 Location")

                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetFriendlyGroup().AddName(DS9Name)

                        # Assign the AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXDS9AI

                        DeepSpace9 = MissionLib.GetShip("Deep_Space_9", DS9Set)

                        pDeepSpace9 = App.ShipClass_Cast(DeepSpace9)

                        pDeepSpace9.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXDS9AI.CreateAI(pDeepSpace9))

        else:
                if pDS9Selection == 1:

                        # Create the station
                        DS9Name = "Deep_Space_9"
                        pDS9 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDeepSpace9, DS9Set, DS9Name, "DS9 Location")

                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetEnemyGroup().AddName(DS9Name)

                        # Assign the AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyDS9AI

                        DeepSpace9 = MissionLib.GetShip("Deep_Space_9", DS9Set)

                        pDeepSpace9 = App.ShipClass_Cast(DeepSpace9)

                        pDeepSpace9.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyDS9AI.CreateAI(pDeepSpace9))

        
# Force BC to Assign an AI
def CreateAI(pShip):
	debug(__name__ + ", CreateAI")
	pPlayer = MissionLib.GetPlayer()

        Random = lambda fMin, fMax : App.g_kSystemWrapper.GetRandomNumber((fMax - fMin) * 1000.0) / 1000.0 - fMin
        # Range values used in the AI.
        fInRange = 150.0 + Random(-25, 20)

	#########################################
	# Creating PlainAI Intercept at (279, 253)
	pIntercept = App.PlainAI_Create(pShip, "Intercept")
	pIntercept.SetScriptModule("Intercept")
	pIntercept.SetInterruptable(1)
	pScript = pIntercept.GetScriptInstance()
	pScript.SetTargetObjectName(pPlayer.GetName())
	# Done creating PlainAI Intercept
	#########################################
	#########################################
	# Creating ConditionalAI ConditionIntercept at (148, 273)
	## Conditions:
	#### Condition HaveToIntercept
	pHaveToIntercept = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fInRange, pPlayer.GetName(), pShip.GetName())
	## Evaluation function:
	def EvalFunc(bHaveToIntercept):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bHaveToIntercept:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionIntercept = App.ConditionalAI_Create(pShip, "ConditionIntercept")
	pConditionIntercept.SetInterruptable(1)
	pConditionIntercept.SetContainedAI(pIntercept)
	pConditionIntercept.AddCondition(pHaveToIntercept)
	pConditionIntercept.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionIntercept
	#########################################
	#########################################
	# Creating PlainAI Follow at (280, 181)
	pFollow = App.PlainAI_Create(pShip, "Follow")
	pFollow.SetScriptModule("FollowObject")
	pFollow.SetInterruptable(1)
	pScript = pFollow.GetScriptInstance()
	pScript.SetFollowObjectName(pPlayer.GetName())
	pScript.SetRoughDistances(10,20,30)
	# Done creating PlainAI Follow
	#########################################
	#########################################
	# Creating ConditionalAI PlayerInSameSet at (164, 201)
	## Conditions:
	#### Condition InSet
	pInSet = App.ConditionScript_Create("Conditions.ConditionAllInSameSet", "ConditionAllInSameSet", pShip.GetName(), pPlayer.GetName())
	## Evaluation function:
	def EvalFunc(bInSet):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInSet:
			# Player is in the same set as we are.
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pPlayerInSameSet = App.ConditionalAI_Create(pShip, "PlayerInSameSet")
	pPlayerInSameSet.SetInterruptable(1)
	pPlayerInSameSet.SetContainedAI(pFollow)
	pPlayerInSameSet.AddCondition(pInSet)
	pPlayerInSameSet.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI PlayerInSameSet
	#########################################
	#########################################
	# Creating CompoundAI FollowWarp at (281, 125)
	import AI.Compound.FollowThroughWarp
	pFollowWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName())
	# Done creating CompoundAI FollowWarp
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (47, 125)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (139, 132)
	pPriorityList.AddAI(pConditionIntercept, 1)
	pPriorityList.AddAI(pPlayerInSameSet, 2)
	pPriorityList.AddAI(pFollowWarp, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (6, 188)
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
