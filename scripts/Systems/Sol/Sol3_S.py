###############################################################################
#       Filename:       Sol3.py
#
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#
#       Starbase 12 region. Also contains Starbase 12 control room character set.
#
#       Created:        1/5/01 -        Alberto Fonseca
# NanoFx2 effects added: 2/20/04 - Chris Jones
###############################################################################

import App
import Bridge.BridgeUtils
import MissionLib
import Bridge.Characters.Graff
import Bridge.HelmMenuHandlers
import Tactical.LensFlares
import loadspacehelper

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " module...")

g_idDockAI = None

###############################################################################
#       Initialize()
#
#       Initialize the Starbase 12 set.
#
#       Args:   pSet    - The Starbase 12 set.
#
#       Return: none
###############################################################################
def Initialize(pSet):
        SetupEventHandlers(pSet)

        # 149.6 million km from the sun

        # Add a sun, far far away
        pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

        ######
        # Create the Planet - 12,756 km diameter
        pEarth = App.Planet_Create(728.91, "data/models/environment/earth.nif")
        pSet.AddObjectToSet(pEarth, "Earth")

        # Place the object at the specified location.
        pEarth.PlaceObjectByName( "Earth" )
        pEarth.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pEarth, "data/models/environment/Earth.nif", "Class-M")    


        ######
        # Create the Planet - 3,475 km diameter
        pMoon = App.Planet_Create(198.57, "data/models/environment/moon.nif")
        pSet.AddObjectToSet(pMoon, "Moon")

        # Place the object at the specified location.
        pMoon.PlaceObjectByName( "Moon" )
        pMoon.UpdateNodeOnly()
        pMoon.SetAtmosphereRadius(0.01)

        import Custom.QBautostart.Libs.LibPlanet
        global pEarthRotation, pMoonRotation
        pEarthRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pEarth, 8.62e4, 3.16e7, pSun)
        pMoonRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pMoon, 2360622, 2360622, pEarth)

###############################################################################
#       SetupEventHandlers()
#
#       Set up event handlers used by the Starbase 12 set.
#
#       Args:   pSet    - The Starbase 12 set.
#
#       Return: none
###############################################################################
def SetupEventHandlers(pSet):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()

        # Ship entrance event
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pSet,
                                                                                                                __name__ + ".EnterSet")
        # Ship exit event
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXITED_SET, pSet,
                                                                                                                __name__ + ".ExitSet")

###############################################################################
#       EnterSet(pObject, pEvent)
#
#       Event handler for player's ship entering this set.
#       Create the Starbase 12 Control Room Set when the player enters.
#
#       Args:
#
#       Return:
###############################################################################
def EnterSet(pObject, pEvent):
        try:
                # Get ship entering set.
                pShip = App.ShipClass_Cast(pEvent.GetDestination())

                # Get player.
                pPlayer = App.Game_GetCurrentPlayer()

                if pShip.GetObjID() != pPlayer.GetObjID():
                        # This ship isn't the player's ship.  We're done.
                        return
        except AttributeError:
                # Ship or Player is None.  Nothing to do here.
                return

        # The player is entering a set.  If they're entering the Starbase 12
        # set, setup the SB12 Control Room.
        if pShip.GetContainingSet().GetName() == "Sol3":
                SetupGraffSet()

###############################################################################
#       SetupGraffSet()
#
#       Setup the Starbase 12 Control Room set, so Graff can say something
#       if the player chooses to dock.  If the set already exists, this
#       does nothing.
#
#       Args:   None
#
#       Return: None
###############################################################################
def SetupGraffSet():
        pSB12Set = App.g_kSetManager.GetSet("FedOutpostSet_Graff")
        pBridge = App.g_kSetManager.GetSet("bridge")
        if not pSB12Set and pBridge:
                pSB12Set = MissionLib.SetupBridgeSet("FedOutpostSet_Graff", "data/Models/Sets/FedOutpost/fedoutpost.nif", -30, 65, -1.55)
        if not App.CharacterClass_GetObject(pSB12Set, "Graff") and pBridge:
                MissionLib.SetupCharacter("Bridge.Characters.Graff", "FedOutpostSet_Graff")

        # Enable dock button.
        pButton = Bridge.BridgeUtils.GetDockButton()
        if(pButton):
                pButton.SetEnabled()


###############################################################################
#       ExitSet(pObject, pEvent)
#
#       Event handler for player's ship exiting this set.
#       Delete the Starbase 12 Control Room Set when the player enters.
#
#       Args:
#
#       Return:
###############################################################################
def ExitSet(pObject, pEvent):
        try:
                # Get ship exiting set.
                pShip = App.ShipClass_Cast(pEvent.GetDestination())

                # Get player.
                pPlayer = App.Game_GetCurrentPlayer()

                if pShip.GetObjID() != pPlayer.GetObjID():
                        # This ship isn't the player's ship.  We're done.
                        return
        except AttributeError:
                # Ship or Player is None.  Nothing to do here.
                return

        # The player's ship is exiting a set.  Check if it's exiting
        # the Starbase 12 set...
        if pEvent.GetCString() == "Sol3":
                # Delete the Starbase 12 Control Room Set.
                pStarbaseControlSet = App.g_kSetManager.GetSet("FedOutpostSet_Graff")
                if pStarbaseControlSet:
                        App.g_kSetManager.DeleteSet("FedOutpostSet_Graff")

                Bridge.Characters.Graff.RemoveEventHandlers()

                # Disable dock button.
                pButton = Bridge.BridgeUtils.GetDockButton()
                if(pButton):
                        pButton.SetDisabled()


###############################################################################
#       DockStarbase():
#
#       Make Player's ship dock/undock with Starbase 12.
#
#       Args:   none
#
#       Return: none
###############################################################################
def DockStarbase():
        # Get Player.
        pPlayer = MissionLib.GetPlayer()
        if(pPlayer is None):
                return

        # Get Starbase 12 Set.
        pSol3Set = App.g_kSetManager.GetSet("Starbase12")
        if(pSol3Set is None):
#               debug("DockStarbase() unable to get Starbase 12 set.")
                return

        # Get Starbase 12.
        pSol3 = pSol3Set.GetObject("Starbase 12")
        if(pSol3 is None):
#               debug("DockStarbase() unable to get Starbase 12.")
                return

        # Check if there's a special action for Graff when the
        # player docks with the starbase.
        global g_idGraffAction
        try:
                pGraffAction = App.TGAction_Cast( App.TGObject_GetTGObjectPtr( g_idGraffAction ) )
        except NameError:
                pGraffAction = None

        try:
                bFadeEnd = g_bFadeGraffEnd
        except NameError:
                bFadeEnd = 1

        # Set AI for docking/undocking.
        import AI.Compound.DockWithStarbase
        MissionLib.SetPlayerAI("Helm", AI.Compound.DockWithStarbase.CreateAI(pPlayer, pSol3, pGraffAction, NoRepair = not g_bRepairsEnabled, FadeEnd = bFadeEnd))

###############################################################################
#       StarbaseRepairsEnabled
#
#       When a ship docks with the starbase, this sets whether or not
#       that ship is repaired.
#
#       Args:   bRepairsEnabled - 0 for no repairs, 1 to allow repairs.
#
#       Return: None
###############################################################################
g_bRepairsEnabled = 1
def StarbaseRepairsEnabled(bRepairsEnabled):
        global g_bRepairsEnabled
        g_bRepairsEnabled = bRepairsEnabled

###############################################################################
#       SetGraffDockingAction
#
#       Set a special TGAction to replace Commander Graff's normal
#       response when the player docks with Starbase 12.
#
#       Args:   pAction - The replacement action.  If this is None,
#                                         Graff's normal behavior is restored.
#                       bFadeEnd- True if the camera should fade to black after
#                                         Graff's cutscene finishes, as the camera switches
#                                         to the Sovereign flying out of the starbase.
#
#       Return: None
###############################################################################
def SetGraffDockingAction(pAction = None, bFadeEnd = 1):
        global g_idGraffAction
        global g_bFadeGraffEnd
        g_bFadeGraffEnd = bFadeEnd
        # If there was a replacement action before, make sure it's cleaned up.
        try:
                pGraffAction = App.TGAction_Cast( App.TGObject_GetTGObjectPtr( g_idGraffAction ) )
                if pGraffAction:
                        pGraffAction.Completed()
        except NameError: pass

        if pAction:
                g_idGraffAction = pAction.GetObjID()
        else:
                g_idGraffAction = App.NULL_ID


def SetupDefaultShips():
        return [ "FedStarbase", "Starbase 12", "Starfleet Command" ]
