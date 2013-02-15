from bcdebug import debug
# by USS Sovereign, Comet has to be a ship in order so that we may have that TrailFX....

import App

def CreateAI(pShip):
	#########################################
	# Creating PlainAI Way1 at (174, 130)
	debug(__name__ + ", CreateAI")
	pWay1 = App.PlainAI_Create(pShip, "Way1")
	pWay1.SetScriptModule("FollowWaypoints")
	pWay1.SetInterruptable(1)
	pScript = pWay1.GetScriptInstance()
	pScript.SetTargetWaypointName("Way1")
	# Done creating PlainAI Way1
	#########################################
	#########################################
	# Creating PlainAI Way2 at (265, 97)
	pWay2 = App.PlainAI_Create(pShip, "Way2")
	pWay2.SetScriptModule("FollowWaypoints")
	pWay2.SetInterruptable(1)
	pScript = pWay2.GetScriptInstance()
	pScript.SetTargetWaypointName("Way2")
	# Done creating PlainAI Way2
	#########################################
	#########################################
	# Creating PlainAI Way3 at (375, 93)
	pWay3 = App.PlainAI_Create(pShip, "Way3")
	pWay3.SetScriptModule("FollowWaypoints")
	pWay3.SetInterruptable(1)
	pScript = pWay3.GetScriptInstance()
	pScript.SetTargetWaypointName("Way3")
	# Done creating PlainAI Way3
	#########################################
	#########################################
	# Creating PlainAI Way4 at (477, 127)
	pWay4 = App.PlainAI_Create(pShip, "Way4")
	pWay4.SetScriptModule("FollowWaypoints")
	pWay4.SetInterruptable(1)
	pScript = pWay4.GetScriptInstance()
	pScript.SetTargetWaypointName("Way4")
	# Done creating PlainAI Way4
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (214, 284)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(0)
	# SeqBlock is at (348, 194)
	pPriorityList.AddAI(pWay1, 1)
	pPriorityList.AddAI(pWay2, 2)
	pPriorityList.AddAI(pWay3, 3)
	pPriorityList.AddAI(pWay4, 4)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (214, 360)
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
