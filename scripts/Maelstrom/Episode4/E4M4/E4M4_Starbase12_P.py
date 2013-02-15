import App

def LoadPlacements(sSetName):

	# Position "Nebula Start"
	kThis = App.Waypoint_Create("Nebula Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(76.748604, 19.185289, 25.896635)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.653262, 0.749229, -0.109103)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.034469, 0.114522, 0.992823)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nebula Start"

	# Position "Circling Intrepid"
	kThis = App.Waypoint_Create("Circling Intrepid", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-34.326130, -23.886063, 5.916601)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.867540, 0.488582, 0.093068)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.054240, -0.093068, 0.994181)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Circling Intrepid"
