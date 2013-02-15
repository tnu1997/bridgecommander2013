from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# Over here we'll save the locations of ships which we'll load when we enter DS9 Map

# by USS Sovereign

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pExcaliburSelection = pModule.ExcaliburSelection
pDefiantSelection = pModule.DefiantSelection
pOregonSelection = pModule.OregonSelection
pLakotaSelection = pModule.LakotaSelection
pFederationSide = pModule.FederationSide

# Imports
import App
import loadspacehelper
import MissionLib

# Ship detail def
def DS9SetShips():
        # Grab the system name from the set file
        debug(__name__ + ", DS9SetShips")
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        import Custom.DS9FX.DS9FXShips

        if pFederationSide == 1:

                if pExcaliburSelection == 1:
                        # Create the Excalibur
                        Excal = "USS Excalibur"
                        import Custom.DS9FX.DS9FXShips
                        pExcal = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXExcalibur, DS9Set, Excal, "Excal Location")

                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetFriendlyGroup().AddName(Excal)

                        # Assign Excalibur AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXExcalAI

                        Excalibur = MissionLib.GetShip("USS Excalibur", DS9Set) 

                        pExcalibur = App.ShipClass_Cast(Excalibur)

                        pExcalibur.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXExcalAI.CreateAI(pExcalibur))

                if pDefiantSelection == 1:
                        # Create the Defiant
                        Def = "USS Defiant"
                        pDef = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDefiant, DS9Set, Def, "Defiant Location")

                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetFriendlyGroup().AddName(Def)

                        # Assign Defiant's AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXDefiantAI

                        Defiant = MissionLib.GetShip("USS Defiant", DS9Set)

                        pDefiant = App.ShipClass_Cast(Defiant)

                        pDefiant.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXDefiantAI.CreateAI(pDefiant))

                if pOregonSelection == 1:

                        # Create the Oregon
                        Oreg = "USS Oregon"
                        pOreg = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXMiranda, DS9Set, Oreg, "Oregon Location")
                        
                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetFriendlyGroup().AddName(Oreg)

                        # Assign Oregon AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXOregonAI

                        Oregon = MissionLib.GetShip("USS Oregon", DS9Set)

                        pOregon = App.ShipClass_Cast(Oregon)

                        pOregon.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXOregonAI.CreateAI(pOregon))

                if pLakotaSelection == 1:
                        # Create the Lakota
                        Lak = "USS_Lakota"
                        pLak = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXLakota, DS9Set, Lak, "Lakota Location")
                        
                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetFriendlyGroup().AddName(Lak)

                        # Assign Lakota AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXLakotaAI

                        Lakota = MissionLib.GetShip("USS_Lakota", DS9Set)

                        pLakota = App.ShipClass_Cast(Lakota)

                        pLakota.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXLakotaAI.CreateAI(pLakota))

        else:
            
                if pExcaliburSelection == 1:
                        # Create the Excalibur
                        Excal = "USS Excalibur"
                        pExcal = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXExcalibur, DS9Set, Excal, "Excal Location")

                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetEnemyGroup().AddName(Excal)

                        # Assign Excalibur AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyExcalAI

                        Excalibur = MissionLib.GetShip("USS Excalibur", DS9Set) 

                        pExcalibur = App.ShipClass_Cast(Excalibur)

                        pExcalibur.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyExcalAI.CreateAI(pExcalibur))

                if pDefiantSelection == 1:
                        # Create the Defiant
                        Def = "USS Defiant"
                        pDef = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDefiant, DS9Set, Def, "Defiant Location")

                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetEnemyGroup().AddName(Def)

                        # Assign Defiant's AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyDefiantAI

                        Defiant = MissionLib.GetShip("USS Defiant", DS9Set)

                        pDefiant = App.ShipClass_Cast(Defiant)

                        pDefiant.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyDefiantAI.CreateAI(pDefiant))

                if pOregonSelection == 1:

                        # Create the Oregon
                        Oreg = "USS Oregon"
                        pOreg = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXMiranda, DS9Set, Oreg, "Oregon Location")
                        
                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetEnemyGroup().AddName(Oreg)

                        # Assign Oregon AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyOregonAI

                        Oregon = MissionLib.GetShip("USS Oregon", DS9Set)

                        pOregon = App.ShipClass_Cast(Oregon)

                        pOregon.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyOregonAI.CreateAI(pOregon))

                if pLakotaSelection == 1:
                        # Create the Lakota
                        Lak = "USS_Lakota"
                        pLak = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXLakota, DS9Set, Lak, "Lakota Location")
                        
                        # Add it to a friendly group
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        pMission.GetEnemyGroup().AddName(Lak)

                        # Assign Lakota AI
                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyLakotaAI

                        Lakota = MissionLib.GetShip("USS_Lakota", DS9Set)

                        pLakota = App.ShipClass_Cast(Lakota)

                        pLakota.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyLakotaAI.CreateAI(pLakota))



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
