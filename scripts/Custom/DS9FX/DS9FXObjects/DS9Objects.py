from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# Well sometimes we don't get objects to load, I don't know really why so we're gonna move everything else over here and define all
# objects. We do also get this problem when restarting QB battle but the problem should be fixed up in the main file easily.

# by USS Sovereign


# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pWormholeSelection = pModule.WormholeSelection
pCometSelection = pModule.CometSelection
pCometAlphaTrail = pModule.CometAlphaTrail


# Imports
import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXCometFX.DS9FXIntroCometFX import StartGFX, CreateGFX
                
                
# Just an object setup def
def DS9SetObjects():
        # Get the set directly from the set file
        debug(__name__ + ", DS9SetObjects")
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")   
        DS9Set = DS9.GetSet()
        import Custom.DS9FX.DS9FXShips

        if pCometSelection == 1:

                # Comet creation
                Comet = "Comet Alpha"
		import Custom.DS9FX.DS9FXShips
                pComet = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXComet, DS9Set, Comet, "Comet Location")
                        
                pDS9FXComet = MissionLib.GetShip("Comet Alpha", DS9Set)

                # You have 2 choices in Comet Settings
                
                if pCometAlphaTrail == 1:
                    from Custom.DS9FX.DS9FXCometFX.LibComet import CometTrail

                    CometTrail(pDS9FXComet)

                else:
                    
                    # Make me a pretty trail effect :P
                    StartGFX()
                    for i in range(1):
                        CreateGFX(pDS9FXComet)

                # Give the object movement effect
                import Custom.DS9FX.DS9FXAILib.DS9FXCometAI

                DS9FXComet = App.ShipClass_Cast(pDS9FXComet)

                DS9FXComet.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXCometAI.CreateAI(DS9FXComet))
                
                
                # I'll tell you what I'm gonna do, make this baby invincible. It's a pretty thing to be destroyed.
                pDS9FXComet.SetInvincible(1)
                pDS9FXComet.SetHurtable(0)


        else:
                pass


        if pWormholeSelection == 1:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole, DS9Set, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                # Well the Wormhole should be invincible we don't want to destroy it accidentaly
                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)

                # Wormhole scale is so very small
                pDS9FXWormhole.SetScale(0.01) 

        elif pWormholeSelection == 2:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole3, DS9Set, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                # Well the Wormhole should be invincible we don't want to destroy it accidentaly
                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)

                # Wormhole scale is so very small
                pDS9FXWormhole.SetScale(0.01) 

        elif pWormholeSelection == 3:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole4, DS9Set, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                # Well the Wormhole should be invincible we don't want to destroy it accidentaly
                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)

                # Wormhole scale is so very small
                pDS9FXWormhole.SetScale(0.01) 

        elif pWormholeSelection == 4:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole5, DS9Set, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                # Well the Wormhole should be invincible we don't want to destroy it accidentaly
                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)

                # Wormhole scale is so very small
                pDS9FXWormhole.SetScale(0.01)

        elif pWormholeSelection == 5:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole6, DS9Set, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                # Well the Wormhole should be invincible we don't want to destroy it accidentaly
                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)

                # Wormhole scale is so very small
                pDS9FXWormhole.SetScale(0.01)

        else:
                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole2, DS9Set, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", DS9Set) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                # Well the Wormhole should be invincible we don't want to destroy it accidentaly
                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)

                # Wormhole scale is so very small
                pDS9FXWormhole.SetScale(0.01) 


