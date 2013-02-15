import App

def LoadPlacements(sSetName):
	# Position "Geronimo"
	kThis = App.Waypoint_Create("Geronimo", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-39.986458, 139.173599, 16.547358)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.990591, 0.136842, 0.002109)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.001166, -0.006970, 0.999975)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Geronimo"
	
	# Position "Prometheus"
	kThis = App.Waypoint_Create("Prometheus", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-48.986458, 145.173599, -32.547358)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.990591, 0.136842, 0.002109)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.001166, -0.006970, -0.999975)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Prometheus"

	# Position "Defiant"
	kThis = App.Waypoint_Create("Defiant", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-125.986458, 125.173599, 74.547358)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.990591, 0.136842, 0.002109)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.001166, 0.006970, 0.999975)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Defiant"
	
	# Position "Cochrane"
	kThis = App.Waypoint_Create("Cochrane", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(135.986458, 177.173599, 88.547358)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.990591, 0.136842, 0.002109)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.001166, -0.006970, 0.999975)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cochrane"


