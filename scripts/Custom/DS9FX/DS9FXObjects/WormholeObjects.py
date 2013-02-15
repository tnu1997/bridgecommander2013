from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# Over here we'll make a wormhole cone and rotate it slowly to simulate inside wormhole graphics

# by USS Sovereign


# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pInsideWormholeModel = pModule.InsideWormholeModel


# Imports
import App
import loadspacehelper
import MissionLib

# Variable
scale = 1000

# Just an object setup def
def WormholeSetObjects():
        debug(__name__ + ", WormholeSetObjects")
        global scale
        import Custom.DS9FX.DS9FXShips

        if pInsideWormholeModel == 1:
            # Get the set directly from the set file
            Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
            WormholeSet = Worm.GetSet()

            # Wormhole creation line
            Wormhole = "Bajoran Wormhole Outer"
            import Custom.DS9FX.DS9FXShips
            pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeConeVar1_1, WormholeSet, Wormhole, "WormholeCone Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, 0.2, 0)
            pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole.SetInvincible(1)
            pDS9FXWormhole.SetHurtable(0)
            pDS9FXWormhole.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole.SetScale(scale) 

            # Wormhole creation line
            Wormhole2 = "Bajoran Wormhole Inner"
            pWormhole2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeConeVar1_2, WormholeSet, Wormhole2, "WormholeCone2 Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
            # Disable collisions with the 2 models
            pDS9FXWormhole2.EnableCollisionsWith(pDS9FXWormhole, 0)
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, -0.2, 0)
            pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole2.SetInvincible(1)
            pDS9FXWormhole2.SetHurtable(0)
            pDS9FXWormhole2.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole2.SetScale(scale) 


        elif pInsideWormholeModel == 2:
            # Get the set directly from the set file
            Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
            WormholeSet = Worm.GetSet()

            # Wormhole creation line
            Wormhole = "Bajoran Wormhole Outer"
            pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeConeVar4_1, WormholeSet, Wormhole, "WormholeCone Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, 0.2, 0)
            pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole.SetInvincible(1)
            pDS9FXWormhole.SetHurtable(0)
            pDS9FXWormhole.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole.SetScale(scale) 

            # Wormhole creation line
            Wormhole2 = "Bajoran Wormhole Inner"
            pWormhole2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeConeVar4_2, WormholeSet, Wormhole2, "WormholeCone2 Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
            # Disable collisions with the 2 models
            pDS9FXWormhole2.EnableCollisionsWith(pDS9FXWormhole, 0)
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, -0.2, 0)
            pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole2.SetInvincible(1)
            pDS9FXWormhole2.SetHurtable(0)
            pDS9FXWormhole2.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole2.SetScale(scale) 


        elif pInsideWormholeModel == 3:
            # Get the set directly from the set file
            Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
            WormholeSet = Worm.GetSet()

            # Wormhole creation line
            Wormhole = "Bajoran Wormhole Outer"
            pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeConeVar3_1, WormholeSet, Wormhole, "WormholeCone Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, 0.2, 0)
            pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole.SetInvincible(1)
            pDS9FXWormhole.SetHurtable(0)
            pDS9FXWormhole.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole.SetScale(scale) 

            # Wormhole creation line
            Wormhole2 = "Bajoran Wormhole Inner"
            pWormhole2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeConeVar3_2, WormholeSet, Wormhole2, "WormholeCone2 Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
            # Disable collisions with the 2 models
            pDS9FXWormhole2.EnableCollisionsWith(pDS9FXWormhole, 0)
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, -0.2, 0)
            pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole2.SetInvincible(1)
            pDS9FXWormhole2.SetHurtable(0)
            pDS9FXWormhole2.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole2.SetScale(scale) 


        elif pInsideWormholeModel == 4:
            # Get the set directly from the set file
            Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
            WormholeSet = Worm.GetSet()

            # Wormhole creation line
            Wormhole = "Bajoran Wormhole Outer"
            pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeConeVar2_1, WormholeSet, Wormhole, "WormholeCone Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, 0.2, 0)
            pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole.SetInvincible(1)
            pDS9FXWormhole.SetHurtable(0)
            pDS9FXWormhole.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole.SetScale(scale) 

            # Wormhole creation line
            Wormhole2 = "Bajoran Wormhole Inner"
            pWormhole2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeConeVar2_2, WormholeSet, Wormhole2, "WormholeCone2 Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
            # Disable collisions with the 2 models
            pDS9FXWormhole2.EnableCollisionsWith(pDS9FXWormhole, 0)
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, -0.2, 0)
            pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole2.SetInvincible(1)
            pDS9FXWormhole2.SetHurtable(0)
            pDS9FXWormhole2.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole2.SetScale(scale) 
            

        else:
            
            # Get the set directly from the set file
            Worm = __import__("Systems.BajoranWormhole.BajoranWormhole1")   
            WormholeSet = Worm.GetSet()

            # Wormhole creation line
            Wormhole = "Bajoran Wormhole Outer"
            pWormhole = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeCone, WormholeSet, Wormhole, "WormholeCone Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole Outer", WormholeSet) 
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, 0.2, 0)
            pDS9FXWormhole.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole.SetInvincible(1)
            pDS9FXWormhole.SetHurtable(0)
            pDS9FXWormhole.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole.SetScale(scale) 

            # Wormhole creation line
            Wormhole2 = "Bajoran Wormhole Inner"
            pWormhole2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.WormholeCone2, WormholeSet, Wormhole2, "WormholeCone2 Position")
       
            # Get the ship and rotate it like the Bajoran Wormhole in DS9Set
            pDS9FXWormhole2 = MissionLib.GetShip("Bajoran Wormhole Inner", WormholeSet)
            # Disable collisions with the 2 models
            pDS9FXWormhole2.EnableCollisionsWith(pDS9FXWormhole, 0)
            vCurVelocity = App.TGPoint3()
            vCurVelocity.SetXYZ(0, -0.2, 0)
            pDS9FXWormhole2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

            # Well the Wormhole should be invincible we don't want to destroy it accidentaly
            pDS9FXWormhole2.SetInvincible(1)
            pDS9FXWormhole2.SetHurtable(0)
            pDS9FXWormhole2.SetTargetable(0)

            # Wormhole scale is very big. Very large ;)
            pDS9FXWormhole2.SetScale(scale) 

