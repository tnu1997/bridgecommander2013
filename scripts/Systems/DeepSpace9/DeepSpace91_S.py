###############################################################################
#	Filename:	DeepSpace91_S.py
#	
#	
#	Creates DeepSpace91 static objects.  Called by DeepSpace9.py when region 
#	is created
#	
#	Created: 5.10.2005 by USS Sovereign
#       Modified: 13/6/2006
###############################################################################
import App
import Tactical.LensFlares

# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pDS9Planets = pModule.DS9Planets
pDS9NanoFX = pModule.DS9NanoFX
pDS9MapPlanetDetail = pModule.DS9MapPlanetDetail


def Initialize(pSet):

        if pDS9MapPlanetDetail == 2:

            if pDS9Planets == 1:
                
                    # Let's start with a sun, name is B'hava'el, I didn't know that but OK... Cannon is cannon, although I love to improvise a lot
                    pSun = App.Sun_Create(300, 300, 300, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
                    pSet.AddObjectToSet(pSun, "B'hava'el")

                    # Place the sun
                    pSun.PlaceObjectByName( "Sun" )
                    pSun.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)


                    # Model and placement
                    # 1st planet seems to be small so we're gonna make it a red planet
                    # First ones to do are the high textures, with higher poly models, finally
                    # And now we no longer need the stock red planet texture, for those who havent got the unreleased CA enhancement pack
                    pPlanet = App.Planet_Create(50.0, "data/Models/Environment/DS9FX/HighRes/Bajor1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Bajor 1")

                    # Place the object at the specified location.
                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()



                    # Model and placement
                    # 2nd is the same as the first one but a bit bigger
                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/HighRes/Bajor2High.nif")
                    pSet.AddObjectToSet(pPlanet2, "Bajor 2")

                    # Place the object at the specified location.
                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()



                    # Model and placement
                    # 3rd is a bit different, let's make is habitable. I'm improvising, having no clue how bajoran system really looks like lol
                    # Good idea with the habitable, bajor 3 is THE bajor, where the bajorans mainly live
                    pPlanet3 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor3High.nif")
                    pSet.AddObjectToSet(pPlanet3, "Bajor 3")

                    # Place the object at the specified location.
                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly() 



                    # Model and placement
                    # 4th is pretty much the same only a bit larger as it seems on the map... a picture I have on bajoran system
                    pPlanet4 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/HighRes/Bajor4High.nif")
                    pSet.AddObjectToSet(pPlanet4, "Bajor 4")

                    # Place the object at the specified location.
                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()  



                    # Model and placement
                    # 5th is a bit smaller... What did I get myself into...........
                    pPlanet5 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor5High.nif")
                    pSet.AddObjectToSet(pPlanet5, "Bajor 5")

                    # Place the object at the specified location.
                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()  



                    # Model and placement
                    # 6th you know the drill... I ran out of comments anyway....
                    pPlanet6 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor6High.nif")
                    pSet.AddObjectToSet(pPlanet6, "Bajor 6")

                    # Place the object at the specified location.
                    pPlanet6.PlaceObjectByName("Planet6")
                    pPlanet6.UpdateNodeOnly()   



                    # Model and placement 
                    # Time for a few more m class planets, always nice to look at
                    pPlanet7 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor7High.nif")
                    pSet.AddObjectToSet(pPlanet7, "Bajor 7")

                    # Place the object at the specified location.
                    pPlanet7.PlaceObjectByName("Planet7")
                    pPlanet7.UpdateNodeOnly()    



                    # Model and placement 
                    pPlanet8 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/HighRes/Bajor8High.nif")
                    pSet.AddObjectToSet(pPlanet8, "Bajor 8")

                    # Place the object at the specified location.
                    pPlanet8.PlaceObjectByName("Planet8")
                    pPlanet8.UpdateNodeOnly()    



                    # Model and placement 
                    # The texture ive done for 9 is for a gas giant, im saving that for the next one, but because im lazy
                    pPlanet9 = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/HighRes/Bajor11High.nif")
                    pSet.AddObjectToSet(pPlanet9, "Bajor 9")

                    # Place the object at the specified location.
                    pPlanet9.PlaceObjectByName("Planet9")
                    pPlanet9.UpdateNodeOnly()    



                    # Model and placement 
                    # 2 gas giants
                    pPlanet10 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/HighRes/Bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet10, "Bajor 10")

                    # Place the object at the specified location.
                    pPlanet10.PlaceObjectByName("Planet10")
                    pPlanet10.UpdateNodeOnly()   



                    # Model and placement 
                    pPlanet11 = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/HighRes/Bajor10High.nif")
                    pSet.AddObjectToSet(pPlanet11, "Bajor 11")

                    # Place the object at the specified location.
                    pPlanet11.PlaceObjectByName("Planet11")
                    pPlanet11.UpdateNodeOnly()     



                    # Model and placement 
                    # And a massive lump of rock
                    pPlanet12 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/HighRes/Bajor12High.nif")
                    pSet.AddObjectToSet(pPlanet12, "Bajor 12")

                    # Place the object at the specified location.
                    pPlanet12.PlaceObjectByName("Planet12")
                    pPlanet12.UpdateNodeOnly()     



                    # Model and placement 
                    # Havent dont enough planets cos i cant count, noone will notice a reuse tho
                    pPlanet13 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/HighRes/Bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet13, "Bajor 13")

                    # Place the object at the specified location.
                    pPlanet13.PlaceObjectByName("Planet13")
                    pPlanet13.UpdateNodeOnly()     



                    # Model and placement
                    # Damn finally the last planet. If someone says this isn't good... Oh man... You don't wanna know what I'll do to that person!
                    # Oh, yes we do. Last one, another lump of rock
                    pPlanet14 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor13High.nif")
                    pSet.AddObjectToSet(pPlanet14, "Bajor 14")

                    # Place the object at the specified location.
                    pPlanet14.PlaceObjectByName("Planet14")
                    pPlanet14.UpdateNodeOnly()

                    # For low end computers this is a life saver, saves memory like crazy. If problems still exist just turn off the planets
                    if pDS9NanoFX == 1:
                        # We'll try to use NanoFX 2.0 Beta atmospheres, but if it's not installed... well shame on you!
                        # Those horrible clouds? Well, i'd better change this part, too. Also, you don't want clouds on a gas giant as they cover the whole texture with a low res one, much better leaving that one...i hope you can just miss the last part out
                        try:
                            
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Bajor1High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Bajor2High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Bajor3High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/HighRes/Bajor4High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/HighRes/Bajor5High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet6, "data/Models/Environment/DS9FX/HighRes/Bajor6High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet7, "data/Models/Environment/DS9FX/HighRes/Bajor7High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet8, "data/Models/Environment/DS9FX/HighRes/Bajor8High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet9, "data/Models/Environment/DS9FX/HighRes/Bajor11High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet10, "data/Models/Environment/DS9FX/HighRes/Bajor9High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet11, "data/Models/Environment/DS9FX/HighRes/Bajor10High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet12, "data/Models/Environment/DS9FX/HighRes/Bajor12High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet13, "data/Models/Environment/DS9FX/HighRes/Bajor9High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet14, "data/Models/Environment/DS9FX/HighRes/Bajor13High.nif", "Class-K")


                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

                    else:
                        pass


            else:
                return

        elif pDS9MapPlanetDetail == 1:

            if pDS9Planets == 1:
                
                    # Let's start with a sun, name is B'hava'el, I didn't know that but OK... Cannon is cannon, although I love to improvise a lot
                    pSun = App.Sun_Create(300, 300, 300, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
                    pSet.AddObjectToSet(pSun, "B'hava'el")

                    # Place the sun
                    pSun.PlaceObjectByName( "Sun" )
                    pSun.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)


                    # Model and placement
                    # 1st planet seems to be small so we're gonna make it a red planet
                    # First ones to do are the high textures, with higher poly models, finally
                    # And now we no longer need the stock red planet texture, for those who havent got the unreleased CA enhancement pack
                    pPlanet = App.Planet_Create(50.0, "data/Models/Environment/DS9FX/StandardRes/Bajor1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Bajor 1")

                    # Place the object at the specified location.
                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()



                    # Model and placement
                    # 2nd is the same as the first one but a bit bigger
                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/StandardRes/Bajor2High.nif")
                    pSet.AddObjectToSet(pPlanet2, "Bajor 2")

                    # Place the object at the specified location.
                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()



                    # Model and placement
                    # 3rd is a bit different, let's make is habitable. I'm improvising, having no clue how bajoran system really looks like lol
                    # Good idea with the habitable, bajor 3 is THE bajor, where the bajorans mainly live
                    pPlanet3 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor3High.nif")
                    pSet.AddObjectToSet(pPlanet3, "Bajor 3")

                    # Place the object at the specified location.
                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly() 



                    # Model and placement
                    # 4th is pretty much the same only a bit larger as it seems on the map... a picture I have on bajoran system
                    pPlanet4 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/StandardRes/Bajor4High.nif")
                    pSet.AddObjectToSet(pPlanet4, "Bajor 4")

                    # Place the object at the specified location.
                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()  



                    # Model and placement
                    # 5th is a bit smaller... What did I get myself into...........
                    pPlanet5 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor5High.nif")
                    pSet.AddObjectToSet(pPlanet5, "Bajor 5")

                    # Place the object at the specified location.
                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()  



                    # Model and placement
                    # 6th you know the drill... I ran out of comments anyway....
                    pPlanet6 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor6High.nif")
                    pSet.AddObjectToSet(pPlanet6, "Bajor 6")

                    # Place the object at the specified location.
                    pPlanet6.PlaceObjectByName("Planet6")
                    pPlanet6.UpdateNodeOnly()   



                    # Model and placement 
                    # Time for a few more m class planets, always nice to look at
                    pPlanet7 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor7High.nif")
                    pSet.AddObjectToSet(pPlanet7, "Bajor 7")

                    # Place the object at the specified location.
                    pPlanet7.PlaceObjectByName("Planet7")
                    pPlanet7.UpdateNodeOnly()    



                    # Model and placement 
                    pPlanet8 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/StandardRes/Bajor8High.nif")
                    pSet.AddObjectToSet(pPlanet8, "Bajor 8")

                    # Place the object at the specified location.
                    pPlanet8.PlaceObjectByName("Planet8")
                    pPlanet8.UpdateNodeOnly()    



                    # Model and placement 
                    # The texture ive done for 9 is for a gas giant, im saving that for the next one, but because im lazy
                    pPlanet9 = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/StandardRes/Bajor11High.nif")
                    pSet.AddObjectToSet(pPlanet9, "Bajor 9")

                    # Place the object at the specified location.
                    pPlanet9.PlaceObjectByName("Planet9")
                    pPlanet9.UpdateNodeOnly()    



                    # Model and placement 
                    # 2 gas giants
                    pPlanet10 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/StandardRes/Bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet10, "Bajor 10")

                    # Place the object at the specified location.
                    pPlanet10.PlaceObjectByName("Planet10")
                    pPlanet10.UpdateNodeOnly()   



                    # Model and placement 
                    pPlanet11 = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/StandardRes/Bajor10High.nif")
                    pSet.AddObjectToSet(pPlanet11, "Bajor 11")

                    # Place the object at the specified location.
                    pPlanet11.PlaceObjectByName("Planet11")
                    pPlanet11.UpdateNodeOnly()     



                    # Model and placement 
                    # And a massive lump of rock
                    pPlanet12 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/StandardRes/Bajor12High.nif")
                    pSet.AddObjectToSet(pPlanet12, "Bajor 12")

                    # Place the object at the specified location.
                    pPlanet12.PlaceObjectByName("Planet12")
                    pPlanet12.UpdateNodeOnly()     



                    # Model and placement 
                    # Havent dont enough planets cos i cant count, noone will notice a reuse tho
                    pPlanet13 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/StandardRes/Bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet13, "Bajor 13")

                    # Place the object at the specified location.
                    pPlanet13.PlaceObjectByName("Planet13")
                    pPlanet13.UpdateNodeOnly()     



                    # Model and placement
                    # Damn finally the last planet. If someone says this isn't good... Oh man... You don't wanna know what I'll do to that person!
                    # Oh, yes we do. Last one, another lump of rock
                    pPlanet14 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor13High.nif")
                    pSet.AddObjectToSet(pPlanet14, "Bajor 14")

                    # Place the object at the specified location.
                    pPlanet14.PlaceObjectByName("Planet14")
                    pPlanet14.UpdateNodeOnly()

                    # For low end computers this is a life saver, saves memory like crazy. If problems still exist just turn off the planets
                    if pDS9NanoFX == 1:
                        # We'll try to use NanoFX 2.0 Beta atmospheres, but if it's not installed... well shame on you!
                        # Those horrible clouds? Well, i'd better change this part, too. Also, you don't want clouds on a gas giant as they cover the whole texture with a low res one, much better leaving that one...i hope you can just miss the last part out
                        try:
                            
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Bajor1High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Bajor2High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Bajor3High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/StandardRes/Bajor4High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/StandardRes/Bajor5High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet6, "data/Models/Environment/DS9FX/StandardRes/Bajor6High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet7, "data/Models/Environment/DS9FX/StandardRes/Bajor7High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet8, "data/Models/Environment/DS9FX/StandardRes/Bajor8High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet9, "data/Models/Environment/DS9FX/StandardRes/Bajor11High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet10, "data/Models/Environment/DS9FX/StandardRes/Bajor9High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet11, "data/Models/Environment/DS9FX/StandardRes/Bajor10High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet12, "data/Models/Environment/DS9FX/StandardRes/Bajor12High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet13, "data/Models/Environment/DS9FX/StandardRes/Bajor9High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet14, "data/Models/Environment/DS9FX/StandardRes/Bajor13High.nif", "Class-K")


                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

                    else:
                        pass


            else:
                return


        else:

            if pDS9Planets == 1:
                
                    # Let's start with a sun, name is B'hava'el, I didn't know that but OK... Cannon is cannon, although I love to improvise a lot
                    pSun = App.Sun_Create(300, 300, 300, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
                    pSet.AddObjectToSet(pSun, "B'hava'el")

                    # Place the sun
                    pSun.PlaceObjectByName( "Sun" )
                    pSun.UpdateNodeOnly()

                    # Build flares
                    Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)


                    # Model and placement
                    # 1st planet seems to be small so we're gonna make it a red planet
                    # First ones to do are the high textures, with higher poly models, finally
                    # And now we no longer need the stock red planet texture, for those who havent got the unreleased CA enhancement pack
                    pPlanet = App.Planet_Create(50.0, "data/Models/Environment/DS9FX/LowRes/Bajor1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Bajor 1")

                    # Place the object at the specified location.
                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()



                    # Model and placement
                    # 2nd is the same as the first one but a bit bigger
                    pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/LowRes/Bajor2High.nif")
                    pSet.AddObjectToSet(pPlanet2, "Bajor 2")

                    # Place the object at the specified location.
                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()



                    # Model and placement
                    # 3rd is a bit different, let's make is habitable. I'm improvising, having no clue how bajoran system really looks like lol
                    # Good idea with the habitable, bajor 3 is THE bajor, where the bajorans mainly live
                    pPlanet3 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor3High.nif")
                    pSet.AddObjectToSet(pPlanet3, "Bajor 3")

                    # Place the object at the specified location.
                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly() 



                    # Model and placement
                    # 4th is pretty much the same only a bit larger as it seems on the map... a picture I have on bajoran system
                    pPlanet4 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/LowRes/Bajor4High.nif")
                    pSet.AddObjectToSet(pPlanet4, "Bajor 4")

                    # Place the object at the specified location.
                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()  



                    # Model and placement
                    # 5th is a bit smaller... What did I get myself into...........
                    pPlanet5 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor5High.nif")
                    pSet.AddObjectToSet(pPlanet5, "Bajor 5")

                    # Place the object at the specified location.
                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()  



                    # Model and placement
                    # 6th you know the drill... I ran out of comments anyway....
                    pPlanet6 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor6High.nif")
                    pSet.AddObjectToSet(pPlanet6, "Bajor 6")

                    # Place the object at the specified location.
                    pPlanet6.PlaceObjectByName("Planet6")
                    pPlanet6.UpdateNodeOnly()   



                    # Model and placement 
                    # Time for a few more m class planets, always nice to look at
                    pPlanet7 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor7High.nif")
                    pSet.AddObjectToSet(pPlanet7, "Bajor 7")

                    # Place the object at the specified location.
                    pPlanet7.PlaceObjectByName("Planet7")
                    pPlanet7.UpdateNodeOnly()    



                    # Model and placement 
                    pPlanet8 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/LowRes/Bajor8High.nif")
                    pSet.AddObjectToSet(pPlanet8, "Bajor 8")

                    # Place the object at the specified location.
                    pPlanet8.PlaceObjectByName("Planet8")
                    pPlanet8.UpdateNodeOnly()    



                    # Model and placement 
                    # The texture ive done for 9 is for a gas giant, im saving that for the next one, but because im lazy
                    pPlanet9 = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/LowRes/Bajor11High.nif")
                    pSet.AddObjectToSet(pPlanet9, "Bajor 9")

                    # Place the object at the specified location.
                    pPlanet9.PlaceObjectByName("Planet9")
                    pPlanet9.UpdateNodeOnly()    



                    # Model and placement 
                    # 2 gas giants
                    pPlanet10 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowRes/Bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet10, "Bajor 10")

                    # Place the object at the specified location.
                    pPlanet10.PlaceObjectByName("Planet10")
                    pPlanet10.UpdateNodeOnly()   



                    # Model and placement 
                    pPlanet11 = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/LowRes/Bajor10High.nif")
                    pSet.AddObjectToSet(pPlanet11, "Bajor 11")

                    # Place the object at the specified location.
                    pPlanet11.PlaceObjectByName("Planet11")
                    pPlanet11.UpdateNodeOnly()     



                    # Model and placement 
                    # And a massive lump of rock
                    pPlanet12 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowRes/Bajor12High.nif")
                    pSet.AddObjectToSet(pPlanet12, "Bajor 12")

                    # Place the object at the specified location.
                    pPlanet12.PlaceObjectByName("Planet12")
                    pPlanet12.UpdateNodeOnly()     



                    # Model and placement 
                    # Havent dont enough planets cos i cant count, noone will notice a reuse tho
                    pPlanet13 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/LowRes/Bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet13, "Bajor 13")

                    # Place the object at the specified location.
                    pPlanet13.PlaceObjectByName("Planet13")
                    pPlanet13.UpdateNodeOnly()     



                    # Model and placement
                    # Damn finally the last planet. If someone says this isn't good... Oh man... You don't wanna know what I'll do to that person!
                    # Oh, yes we do. Last one, another lump of rock
                    pPlanet14 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor13High.nif")
                    pSet.AddObjectToSet(pPlanet14, "Bajor 14")

                    # Place the object at the specified location.
                    pPlanet14.PlaceObjectByName("Planet14")
                    pPlanet14.UpdateNodeOnly()

                    # For low end computers this is a life saver, saves memory like crazy. If problems still exist just turn off the planets
                    if pDS9NanoFX == 1:
                        # We'll try to use NanoFX 2.0 Beta atmospheres, but if it's not installed... well shame on you!
                        # Those horrible clouds? Well, i'd better change this part, too. Also, you don't want clouds on a gas giant as they cover the whole texture with a low res one, much better leaving that one...i hope you can just miss the last part out
                        try:
                            
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Bajor1High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Bajor2High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Bajor3High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowRes/Bajor4High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowRes/Bajor5High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet6, "data/Models/Environment/DS9FX/LowRes/Bajor6High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet7, "data/Models/Environment/DS9FX/LowRes/Bajor7High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet8, "data/Models/Environment/DS9FX/LowRes/Bajor8High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet9, "data/Models/Environment/DS9FX/LowRes/Bajor11High.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet10, "data/Models/Environment/DS9FX/LowRes/Bajor9High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet11, "data/Models/Environment/DS9FX/LowRes/Bajor10High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet12, "data/Models/Environment/DS9FX/LowRes/Bajor12High.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet13, "data/Models/Environment/DS9FX/LowRes/Bajor9High.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet14, "data/Models/Environment/DS9FX/LowRes/Bajor13High.nif", "Class-K")


                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

                    else:
                        pass


            else:
                return

