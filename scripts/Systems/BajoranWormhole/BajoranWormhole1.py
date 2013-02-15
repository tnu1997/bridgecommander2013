# by USS Sovereign a system creation file

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pInsideWormholeBackgroundTexture = pModule.InsideWormholeBackgroundTexture


import App

def Initialize():
	# Create the set ("BajoranWormhole1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "BajoranWormhole1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.BajoranWormhole.BajoranWormhole1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("BajoranWormhole1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "BajoranWormhole1_S.py" file with an Initialize function that creates them.
	try:
		import BajoranWormhole1_S
		BajoranWormhole1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "BajoranWormhole1"

def GetSet():
	return App.g_kSetManager.GetSet("BajoranWormhole1")

def Terminate():
	App.g_kSetManager.DeleteSet("BajoranWormhole1")

def LoadPlacements(sSetName):
	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.1)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

        # Psycho sugested Directional Light Changes
        
	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-0.044018, 0.572347, 0.029146)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.076971, 0.995795, 0.049676)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.006766, -0.050345, 0.998709)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1, 0.7, 0.7, 1)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-3.792000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.417716, 0.620277, 0.663905)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.898685, 0.389602, 0.201435)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

        # Position "WormholeCone Position"
	kThis = App.Waypoint_Create("WormholeCone Position", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-3.792000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.417716, 0.620277, 0.663905)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.898685, 0.389602, 0.201435)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "WormholeCone Position"

	# Position "WormholeCone2 Position"
	kThis = App.Waypoint_Create("WormholeCone2 Position", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-3.792000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.417716, 0.620277, 0.663905)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.898685, 0.389602, 0.201435)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "WormholeCone2 Position"
	

import App

def LoadBackdrops(pSet):
        if pInsideWormholeBackgroundTexture == 1:

            #Draw order is implicit. First object gets drawn first

            # Star Sphere "Backdrop stars"
            kThis = App.StarSphere_Create()
            kThis.SetName("Backdrop stars")
            kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
            kForward = App.TGPoint3()
            kForward.SetXYZ(0.185766, 0.947862, -0.258937)
            kUp = App.TGPoint3()
            kUp.SetXYZ(0.049823, 0.254099, 0.965894)
            kThis.AlignToVectors(kForward, kUp)
            kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphics2.tga")
            kThis.SetTargetPolyCount(256)
            kThis.SetHorizontalSpan(300.000000)
            kThis.SetVerticalSpan(300.000000)
            kThis.SetSphereRadius(300.000000)
            kThis.SetTextureHTile(300.000000)
            kThis.SetTextureVTile(300.000000)
            kThis.Rebuild()
            pSet.AddBackdropToSet(kThis,"Backdrop stars")
            kThis.Update(0)
            kThis = None
            # End Backdrop Sphere "Backdrop stars"

        elif pInsideWormholeBackgroundTexture == 2:

            #Draw order is implicit. First object gets drawn first

            # Star Sphere "Backdrop stars"
            kThis = App.StarSphere_Create()
            kThis.SetName("Backdrop stars")
            kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
            kForward = App.TGPoint3()
            kForward.SetXYZ(0.185766, 0.947862, -0.258937)
            kUp = App.TGPoint3()
            kUp.SetXYZ(0.049823, 0.254099, 0.965894)
            kThis.AlignToVectors(kForward, kUp)
            kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphicsChrome.tga")
            kThis.SetTargetPolyCount(256)
            kThis.SetHorizontalSpan(300.000000)
            kThis.SetVerticalSpan(300.000000)
            kThis.SetSphereRadius(300.000000)
            kThis.SetTextureHTile(300.000000)
            kThis.SetTextureVTile(300.000000)
            kThis.Rebuild()
            pSet.AddBackdropToSet(kThis,"Backdrop stars")
            kThis.Update(0)
            kThis = None
            # End Backdrop Sphere "Backdrop stars"

        elif pInsideWormholeBackgroundTexture == 3:

            #Draw order is implicit. First object gets drawn first

            # Star Sphere "Backdrop stars"
            kThis = App.StarSphere_Create()
            kThis.SetName("Backdrop stars")
            kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
            kForward = App.TGPoint3()
            kForward.SetXYZ(0.185766, 0.947862, -0.258937)
            kUp = App.TGPoint3()
            kUp.SetXYZ(0.049823, 0.254099, 0.965894)
            kThis.AlignToVectors(kForward, kUp)
            kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphicsDarkBlue.tga")
            kThis.SetTargetPolyCount(256)
            kThis.SetHorizontalSpan(300.000000)
            kThis.SetVerticalSpan(300.000000)
            kThis.SetSphereRadius(300.000000)
            kThis.SetTextureHTile(300.000000)
            kThis.SetTextureVTile(300.000000)
            kThis.Rebuild()
            pSet.AddBackdropToSet(kThis,"Backdrop stars")
            kThis.Update(0)
            kThis = None
            # End Backdrop Sphere "Backdrop stars"


        elif pInsideWormholeBackgroundTexture == 4:

            #Draw order is implicit. First object gets drawn first

            # Star Sphere "Backdrop stars"
            kThis = App.StarSphere_Create()
            kThis.SetName("Backdrop stars")
            kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
            kForward = App.TGPoint3()
            kForward.SetXYZ(0.185766, 0.947862, -0.258937)
            kUp = App.TGPoint3()
            kUp.SetXYZ(0.049823, 0.254099, 0.965894)
            kThis.AlignToVectors(kForward, kUp)
            kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphicsWaterBlue.tga")
            kThis.SetTargetPolyCount(256)
            kThis.SetHorizontalSpan(300.000000)
            kThis.SetVerticalSpan(300.000000)
            kThis.SetSphereRadius(300.000000)
            kThis.SetTextureHTile(300.000000)
            kThis.SetTextureVTile(300.000000)
            kThis.Rebuild()
            pSet.AddBackdropToSet(kThis,"Backdrop stars")
            kThis.Update(0)
            kThis = None
            # End Backdrop Sphere "Backdrop stars"

        elif pInsideWormholeBackgroundTexture == 5:

            #Draw order is implicit. First object gets drawn first

            # Star Sphere "Backdrop stars"
            kThis = App.StarSphere_Create()
            kThis.SetName("Backdrop stars")
            kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
            kForward = App.TGPoint3()
            kForward.SetXYZ(0.185766, 0.947862, -0.258937)
            kUp = App.TGPoint3()
            kUp.SetXYZ(0.049823, 0.254099, 0.965894)
            kThis.AlignToVectors(kForward, kUp)
            kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphicsWierd.tga")
            kThis.SetTargetPolyCount(256)
            kThis.SetHorizontalSpan(300.000000)
            kThis.SetVerticalSpan(300.000000)
            kThis.SetSphereRadius(300.000000)
            kThis.SetTextureHTile(300.000000)
            kThis.SetTextureVTile(300.000000)
            kThis.Rebuild()
            pSet.AddBackdropToSet(kThis,"Backdrop stars")
            kThis.Update(0)
            kThis = None
            # End Backdrop Sphere "Backdrop stars"

        else:

            #Draw order is implicit. First object gets drawn first

            # Star Sphere "Backdrop stars"
            kThis = App.StarSphere_Create()
            kThis.SetName("Backdrop stars")
            kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
            kForward = App.TGPoint3()
            kForward.SetXYZ(0.185766, 0.947862, -0.258937)
            kUp = App.TGPoint3()
            kUp.SetXYZ(0.049823, 0.254099, 0.965894)
            kThis.AlignToVectors(kForward, kUp)
            kThis.SetTextureFileName("data/DS9FXInsideWormholeGraphics.tga")
            kThis.SetTargetPolyCount(256)
            kThis.SetHorizontalSpan(300.000000)
            kThis.SetVerticalSpan(300.000000)
            kThis.SetSphereRadius(300.000000)
            kThis.SetTextureHTile(300.000000)
            kThis.SetTextureVTile(300.000000)
            kThis.Rebuild()
            pSet.AddBackdropToSet(kThis,"Backdrop stars")
            kThis.Update(0)
            kThis = None
            # End Backdrop Sphere "Backdrop stars"
