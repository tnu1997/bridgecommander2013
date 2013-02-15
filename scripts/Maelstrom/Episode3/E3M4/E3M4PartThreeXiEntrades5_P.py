import App

def LoadPlacements(sSetName):
	# Position "Chairo"
	kThis = App.Waypoint_Create("Chairo", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(52.646473, 330.479980, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.679576, 0.000000, 0.733605)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Chairo"
	
	# Position "T'Awsun"
	kThis = App.Waypoint_Create("T'Awsun", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(95.214828, 326.085449, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.966905, 0.000000, -0.255136)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "T'Awsun"
	
	# Position "Generex"
	kThis = App.Waypoint_Create("Generex", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(68.214828, 225.085449, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.966905, 0.000000, -0.255136)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Generex"
	
	# Position "Dvorak"
	kThis = App.Waypoint_Create("Dvorak", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(34.214828, 380.085449, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.966905, 0.000000, -0.255136)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Dvorak"

	# Position "Galor 3"
	kThis = App.Waypoint_Create("Galor 3", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(74.121094, 362.706543, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.546690, -0.815563, -0.189705)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.149788, -0.318156, 0.936130)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor 3"

	# Position "Galor 2"
	kThis = App.Waypoint_Create("Galor 2", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(36.914055, 350.987793, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.214912, -0.931947, -0.292042)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.806941, 0.001000, 0.590632)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor 2"

	# Position "Galor 1"
	kThis = App.Waypoint_Create("Galor 1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(20.507811, 319.640137, 67.391998)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.929755, 0.136669, -0.341872)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.288859, 0.304972, 0.907498)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor 1"
	
	# Position "Galor 4"
	kThis = App.Waypoint_Create("Galor 4", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(15.507811, 301.640137, 59.391998)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.929755, 0.136669, -0.341872)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.288859, 0.304972, 0.907498)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor 4"
	
	# Position "Galor 5"
	kThis = App.Waypoint_Create("Galor 5", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(48.507811, 270.640137, 33.391998)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.929755, -0.136669, -0.341872)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.288859, 0.304972, 0.907498)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor 5"
	
	# Position "Galor 6"
	kThis = App.Waypoint_Create("Galor 6", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(0.507811, 340.640137, 12.391998)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.929755, -0.136669, -0.341872)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.288859, 0.304972, 0.907498)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Galor 6"

	# Position "Keldon 1"
	kThis = App.Waypoint_Create("Keldon 1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(77.636711, 280.089355, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.764617, -0.602100, -0.229862)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.365715, 0.111672, 0.924003)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Keldon 1"
	
	# Position "Keldon 2"
	kThis = App.Waypoint_Create("Keldon 2", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(44.636711, 320.089355, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.764617, -0.602100, 0.229862)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.365715, 0.111672, 0.924003)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Keldon 2"
	
	# Position "Keldon 3"
	kThis = App.Waypoint_Create("Keldon 3", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(99.636711, 200.089355, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.764617, 0.602100, -0.229862)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.365715, 0.111672, 0.924003)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Keldon 3"