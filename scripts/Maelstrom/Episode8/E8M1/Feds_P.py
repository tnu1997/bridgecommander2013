import App

def LoadPlacements(sSetName):
	# Position "Galaxy Start"
	kThis = App.Waypoint_Create("Galaxy Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-75.400000, 68.914978, 75.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.040128, -0.996885, 0.067897)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.029710, 0.069112, 0.997166)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galaxy Start"