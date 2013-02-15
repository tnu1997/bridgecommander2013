from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# Just like the DS9Objects.py this holds info about all objects that are located in the set

# by USS Sovereign


# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pWormholeSelection = pModule.WormholeSelection


# Imports
import App
import loadspacehelper
import MissionLib

# Just an object setup def
def GammsSetObjects():
        # Grab the system name from the set file
        debug(__name__ + ", GammsSetObjects")
        Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
        GammaSet = Gamma.GetSet()
        import Custom.DS9FX.DS9FXShips

        if pWormholeSelection == 1:

                # Wormhole creation line
                Wormhole = "Bajoran Wormhole"
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole, GammaSet, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
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
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole3, GammaSet, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
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
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole4, GammaSet, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
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
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole5, GammaSet, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
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
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole6, GammaSet, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
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
                pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.Wormhole2, GammaSet, Wormhole, "Wormhole Location")
                
                # Thanks LJ for this one but we need to rotate it on y axis not x :P        
                # And yet Mr. Wowbagger suggested that I use this and it actually works, thank you Wowy :)
                pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", GammaSet) 
                vCurVelocity = App.TGPoint3()
                vCurVelocity.SetXYZ(0, 0.2, 0)
                pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

                # Well the Wormhole should be invincible we don't want to destroy it accidentaly
                pDS9FXWormhole.SetInvincible(1)
                pDS9FXWormhole.SetHurtable(0)
                pDS9FXWormhole.SetHidden(1)

                # Wormhole scale is so very small
                pDS9FXWormhole.SetScale(0.01) 
