import App

def LoadPlacements(sSetName):
	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(0.064856, -9.354877, 2.359643)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.063956, 0.997314, 0.035700)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.001987, -0.035646, 0.999363)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Station Start"
	kThis = App.Waypoint_Create("Station Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-2.324634, 118.480637, 4.922688)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.053900, -0.998519, 0.007391)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.025848, 0.008794, 0.999627)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Station Start"

	# Position "Warbird Start"
	kThis = App.Waypoint_Create("Warbird Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-8.102109, 27.515141, 3.456827)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.308164, -0.951198, -0.016038)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.102882, -0.050081, 0.993432)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warbird Start"

	# Position "Vorcha Start"
	kThis = App.Waypoint_Create("Vorcha Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(10.760961, 26.932966, 3.618836)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.324774, -0.944920, -0.040596)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.023314, -0.050908, 0.998431)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Vorcha Start"

	# Position "Enemy1 Start"
	kThis = App.Waypoint_Create("Enemy1 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(37.428940, 627.953125, 16.793289)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy1 Start"

	# Position "Enemy2 Start"
	kThis = App.Waypoint_Create("Enemy2 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-8.598532, 642.195068, 17.140966)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy2 Start"

	# Position "Enemy3 Start"
	kThis = App.Waypoint_Create("Enemy3 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(95.369865, 625.624329, 16.739197)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy3 Start"
	
	# Position "Enemy11 Start"
	kThis = App.Waypoint_Create("Enemy11 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(37.428940, 607.953125, 6.793289)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy11 Start"

	# Position "Enemy12 Start"
	kThis = App.Waypoint_Create("Enemy12 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-2.598532, 642.195068, 37.140966)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy12 Start"

	# Position "Enemy13 Start"
	kThis = App.Waypoint_Create("Enemy13 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(98.369865, 645.624329, 16.739197)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy13 Start"
	
	# Position "Enemy22 Start"
	kThis = App.Waypoint_Create("Enemy22 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(47.428940, 600.953125, 56.793289)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy22 Start"

	# Position "Enemy23 Start"
	kThis = App.Waypoint_Create("Enemy23 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-18.598532, 612.195068, 47.140966)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy23 Start"

	# Position "Enemy32 Start"
	kThis = App.Waypoint_Create("Enemy32 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(75.369865, 650.624329, 22.739197)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy32 Start"
	
	# Position "Enemy33 Start"
	kThis = App.Waypoint_Create("Enemy33 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-37.428940, 617.953125, 10.793289)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy33 Start"

	# Position "Enemy42 Start"
	kThis = App.Waypoint_Create("Enemy42 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-7.598532, 622.195068, 17.140966)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy42 Start"

	# Position "Enemy43 Start"
	kThis = App.Waypoint_Create("Enemy43 Start", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(118.369865, 660.624329, 35.739197)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy43 Start"
	
	# Position "Enemy1 Way1"
	kThis = App.Waypoint_Create("Enemy1 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(6.537314, 417.509094, 12.991589)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy1 Way1"

	# Position "Enemy2 Way1"
	kThis = App.Waypoint_Create("Enemy2 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-42.390896, 445.594208, 13.678986)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy2 Way1"

	# Position "Enemy3 Way1"
	kThis = App.Waypoint_Create("Enemy3 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(60.282509, 419.255280, 13.036491)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy3 Way1"
	
	# Position "Enemy4 Way1"
	kThis = App.Waypoint_Create("Enemy4 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(6.537314, 407.509094, 22.991589)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy4 Way1"

	# Position "Enemy5 Way1"
	kThis = App.Waypoint_Create("Enemy5 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-42.390896, 485.594208, 34.678986)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy5 Way1"

	# Position "Enemy6 Way1"
	kThis = App.Waypoint_Create("Enemy6 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(50.282509, 409.255280, 43.036491)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy6 Way1"
	
	# Position "Enemy7 Way1"
	kThis = App.Waypoint_Create("Enemy7 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(12.537314, 445.509094, 32.991589)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy7 Way1"

	# Position "Enemy8 Way1"
	kThis = App.Waypoint_Create("Enemy8 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-22.390896, 425.594208, 14.678986)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy8 Way1"

	# Position "Enemy9 Way1"
	kThis = App.Waypoint_Create("Enemy9 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(30.282509, 475.255280, 23.036491)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy9 Way1"
	
	# Position "Enemy10 Way1"
	kThis = App.Waypoint_Create("Enemy10 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(44.537314, 410.509094, 22.991589)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy10 Way1"

	# Position "Enemy11 Way1"
	kThis = App.Waypoint_Create("Enemy11 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-32.390896, 390.594208, 37.678986)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy11 Way1"

	# Position "Enemy12 Way1"
	kThis = App.Waypoint_Create("Enemy12 Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(20.282509, 500.255280, 10.036491)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.124944, -0.991865, -0.024347)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000005, 0.024540, 0.999699)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(4.000000)
	kThis.Update(0)
	kThis = None
	# End position "Enemy12 Way1"

	# Position "Warbird Way1"
	kThis = App.Waypoint_Create("Warbird Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(-50.498444, -158.705612, 11.605355)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.096745, -0.991582, 0.086056)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.017495, 0.084754, 0.996248)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(5.000000)
	kThis.Update(0)
	kThis = None
	# End position "Warbird Way1"

	# Position "Vorcha Way1"
	kThis = App.Waypoint_Create("Vorcha Way1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetTranslateXYZ(47.340023, -161.550491, 8.280628)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.149605, -0.988724, 0.006562)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.007394, 0.005518, 0.999957)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(5.000000)
	kThis.Update(0)
	kThis = None
	# End position "Vorcha Way1"

	# Position "CloakCamera1"
	kThis = App.Waypoint_Create("CloakCamera1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-2.106918, 16.872555, 74.665810)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000242, -0.074694, -0.997206)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000260, 0.997206, -0.074694)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "CloakCamera1"

	# Position "CloakCamera2"
	kThis = App.Waypoint_Create("CloakCamera2", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1.871003, -8.766197, 3.784423)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.019546, 0.992283, -0.122443)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.006425, 0.122339, 0.992468)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "CloakCamera2"

	# Attaching object "CloakCamera1" after "CloakCamera1"...
	kThis = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "CloakCamera1") )
	kPrevious = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "CloakCamera1") )
	kThis.InsertAfterObj( kPrevious )
	kThis = kPrevious = None
	# Attaching object "CloakCamera2" after "CloakCamera2"...
	kThis = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "CloakCamera2") )
	kPrevious = App.Waypoint_Cast( App.PlacementObject_GetObjectBySetName(sSetName, "CloakCamera2") )
	kThis.InsertAfterObj( kPrevious )
	kThis = kPrevious = None
