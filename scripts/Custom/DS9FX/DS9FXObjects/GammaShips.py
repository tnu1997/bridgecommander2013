from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# Over here we'll save locations of Gamma Quadrant ships, the file is triggered when we enter Gamma Quadrant map

# by USS Sovereign

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pBugship1Selection = pModule.Bugship1Selection
pBugship2Selection  = pModule.Bugship2Selection 
pBugship3Selection = pModule.Bugship3Selection
pDominionSide = pModule.DominionSide

# Imports
import App
import loadspacehelper
import MissionLib

# Gamma Quadrant ship def
def GammaSetShips():
        # Grab the system name from the set file
        debug(__name__ + ", GammaSetShips")
        Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
        GammaSet = Gamma.GetSet()
        import Custom.DS9FX.DS9FXShips

        if pDominionSide == 1:

                if pBugship1Selection == 1:
                        # Create the Bugship 1
                        Bug1 = "Bugship 1"
                        pBug1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug1, "Bugship1 Location")

                        # Add it to a enemy group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetFriendlyGroup().AddName(Bug1)

                        # Assign it's AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBughsipAI

                        Bugship1 = MissionLib.GetShip("Bugship 1", GammaSet) 

                        pBugship1 = App.ShipClass_Cast(Bugship1)

                        pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBughsipAI.CreateAI(pBugship1))


                if pBugship2Selection == 1:
                        # Create the Bugship 2
                        Bug2 = "Bugship 2"
                        pBug2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug2, "Bugship2 Location")

                        # Add it to a enemy group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetFriendlyGroup().AddName(Bug2)

                        # Assign it's AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBugshipAI2

                        Bugship2 = MissionLib.GetShip("Bugship 2", GammaSet) 

                        pBugship2 = App.ShipClass_Cast(Bugship2)

                        pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBugshipAI2.CreateAI(pBugship2))


                if pBugship3Selection == 1:

                        # Create the Bugship 3
                        Bug3 = "Bugship 3"
                        pBug3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug3, "Bugship3 Location")

                        # Add it to a enemy group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetFriendlyGroup().AddName(Bug3)

                        # Assign it's AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBugshipAI3

                        Bugship3 = MissionLib.GetShip("Bugship 3", GammaSet) 

                        pBugship3 = App.ShipClass_Cast(Bugship3)

                        pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBugshipAI3.CreateAI(pBugship3))


        else:
            
                if pBugship1Selection == 1:
                        # Create the Bugship 1
                        Bug1 = "Bugship 1"
			import Custom.DS9FX.DS9FXShips
                        pBug1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug1, "Bugship1 Location")

                        # Add it to a enemy group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetEnemyGroup().AddName(Bug1)

                        # Assign it's AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI

                        Bugship1 = MissionLib.GetShip("Bugship 1", GammaSet) 

                        pBugship1 = App.ShipClass_Cast(Bugship1)

                        pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship1))


                if pBugship2Selection == 1:
                        # Create the Bugship 2
                        Bug2 = "Bugship 2"
                        pBug2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug2, "Bugship2 Location")

                        # Add it to a enemy group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetEnemyGroup().AddName(Bug2)

                        # Assign it's AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXBugshipAI2

                        Bugship2 = MissionLib.GetShip("Bugship 2", GammaSet) 

                        pBugship2 = App.ShipClass_Cast(Bugship2)

                        pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBugshipAI2.CreateAI(pBugship2))


                if pBugship3Selection == 1:

                        # Create the Bugship 3
                        Bug3 = "Bugship 3"
                        pBug3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, GammaSet, Bug3, "Bugship3 Location")

                        # Add it to a enemy group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetEnemyGroup().AddName(Bug3)

                        # Assign it's AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXBugshipAI3

                        Bugship3 = MissionLib.GetShip("Bugship 3", GammaSet) 

                        pBugship3 = App.ShipClass_Cast(Bugship3)

                        pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBugshipAI3.CreateAI(pBugship3))




# Force BC to assign an AI
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
