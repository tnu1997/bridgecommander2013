###############################################################################
#	Filename:	GammaQuadrant_S.py
#	
#	
#	Creates DeepSpaceFive 1 static objects.  Called by GammaQuadrant.py when 
#	region is created
#	
#	Created: 5.10.2005  by USS Sovereign
#       Modified: 14/6/2006
###############################################################################
import App
import Tactical.LensFlares

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pGammaPlanets = pModule.GammaPlanets
pGammaNanoFX = pModule.GammaNanoFX
pGammaMapPlanetDetail = pModule.GammaMapPlanetDetail


def Initialize(pSet):
    if pGammaMapPlanetDetail == 2:
        
            if pGammaPlanets == 1:
        
                    # And God said let there be light...
                    pSun = App.Sun_Create(400, 400, 400, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun, "Idran A")

                    # Place the sun
                    pSun.PlaceObjectByName( "Sun" )
                    pSun.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun)

                    # And God said let there be light...
                    pSun2 = App.Sun_Create(200, 200, 200, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun2, "Idran B")

                    # Place the sun
                    pSun2.PlaceObjectByName( "Sun2" )
                    pSun2.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun2)


                    # And God said let there be light...
                    pSun3 = App.Sun_Create(200, 200, 200, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun3, "Idran C")

                    # Place the sun
                    pSun3.PlaceObjectByName( "Sun3" )
                    pSun3.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun3)

                    # Model and placement
                    pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Idran")

                    # Place the object at the specified location.
                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if pGammaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif", "Class-M")

                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"


            else:
                return


    elif pGammaMapPlanetDetail == 1:
        
            if pGammaPlanets == 1:
        
                    # And God said let there be light...
                    pSun = App.Sun_Create(400, 400, 400, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun, "Idran A")

                    # Place the sun
                    pSun.PlaceObjectByName( "Sun" )
                    pSun.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun)

                    # And God said let there be light...
                    pSun2 = App.Sun_Create(200, 200, 200, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun2, "Idran B")

                    # Place the sun
                    pSun2.PlaceObjectByName( "Sun2" )
                    pSun2.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun2)


                    # And God said let there be light...
                    pSun3 = App.Sun_Create(200, 200, 200, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun3, "Idran C")

                    # Place the sun
                    pSun3.PlaceObjectByName( "Sun3" )
                    pSun3.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun3)

                    # Model and placement
                    pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Idran")

                    # Place the object at the specified location.
                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if pGammaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif", "Class-M")

                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"


            else:
                return


    else:
        
            if pGammaPlanets == 1:
        
                    # And God said let there be light...
                    pSun = App.Sun_Create(400, 400, 400, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun, "Idran A")

                    # Place the sun
                    pSun.PlaceObjectByName( "Sun" )
                    pSun.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun)

                    # And God said let there be light...
                    pSun2 = App.Sun_Create(200, 200, 200, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun2, "Idran B")

                    # Place the sun
                    pSun2.PlaceObjectByName( "Sun2" )
                    pSun2.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun2)


                    # And God said let there be light...
                    pSun3 = App.Sun_Create(200, 200, 200, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
                    pSet.AddObjectToSet(pSun3, "Idran C")

                    # Place the sun
                    pSun3.PlaceObjectByName( "Sun3" )
                    pSun3.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.WhiteLensFlare(pSet, pSun3)

                    # Model and placement
                    pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Idran")

                    # Place the object at the specified location.
                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if pGammaNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif", "Class-M")

                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"


            else:
                return

