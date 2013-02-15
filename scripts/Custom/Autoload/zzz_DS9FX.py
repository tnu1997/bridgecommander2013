###########################################################################
#       zzz_DS9FX.py
#
#       Filename notes: Added zzz to make sure that DS9FX loads in last
#
#       It was a simple mutator that added our little systems and loaded
#       our menus at mission start. Now it's much, much more!
#
#       by USS Sovereign 19/10/2005
#
#       Last Modified by USS Sovereign 25/03/2007
###########################################################################


pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pDebugMode = pModule.DebugMode
pStabilizeBC = pModule.StabilizeBC

# Imports
import App
import Foundation
import Custom.DS9FX.DS9FXmain
import MissionLib
from Custom.DS9FX.DS9FXLib import StabilizationCode

# DS9FX Version
pDS9FXVer = __import__("Custom.DS9FX.DS9FXVersionSignature")
pVer = pDS9FXVer.DS9FXVersion

# DS9FX mutator, should be changed with each version
mode = Foundation.MutatorDef("DS9FX " + pVer)

# Vars
Timer = None

# Events
ET_EVENT = App.UtopiaModule_GetNextEventType()


# Our systems
Foundation.SystemDef("DeepSpace9", 1, dict = { "modes": [ mode ] } )
# Gamma quadrant should not be playable anymore
# Foundation.SystemDef("GammaQuadrant", 1, dict = { "modes": [ mode ] } )
# I guess I was wrong, BC doesn't need to register each system via autoload file. Oh well thanks JB for the idea and input
# Foundation.SystemDef("BajoranWormhole", 1, dict = { "modes": [ mode ] } )


# I really hate classes
class DS9FXLoadTrigger(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.DS9FX.DS9FXmain.init()
                

# 2nd Trigger which is called when a player ship is created
class DS9FXRestartTrigger(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Custom.DS9FX.DS9FXmain.RestartTrigger()
                MakeASystemMenu()



# Load trigger at mission start, P.S. our menu fix for QBR double menu buttons is located in
# DS9FXMain.py
DS9FXLoadTrigger('DS9FX Load Trigger', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )


# Restart trigger
DS9FXRestartTrigger('DS9FX Restart Trigger', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )


# We need a new seperate restart trigger since not is all well with current DS9FX restart trigger
class DS9FXRestart(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                Handler(None, None)



# Found another way to fix ET_ENTERED_SET Event, partially my fault
DS9FXRestart('DS9FX Restarting Trigger', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )



# A new handler which is badly needed
def Handler(pObject, pEvent):
        # Grab all values that we need
        pPlayer = App.Game_GetCurrentPlayer()
        if not pPlayer:
            return
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
        pPlayerGroup = pGame.GetPlayerGroup()

        
        if (pSet.GetName() == "DeepSpace91"):
            
            # Return don't proceed, a false alarm
            return
        
        elif (pSet.GetName() == "GammaQuadrant1"):
            
            # Return don't proceed, a false alarm
            return
        
        elif (pSet.GetName() == "BajoranWormhole1"):
            
            # Return don't proceed, a false alarm
            return

        else:
            # This apparently isn't a false alarm so call in the function we want
            ActivateRestartTrigger()


# Now just simply call the core DS9FX file
def ActivateRestartTrigger():
    
            Custom.DS9FX.DS9FXmain.EnterSetTrigger()

            # print "DS9FX: Calling Core File!"


# Again thanks to JB's input we fixed this issue
def MakeASystemMenu():
            	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

		if pMission.GetScript() == "QuickBattle.QuickBattle":

                        try:                                
                            import Systems.DeepSpace9.DeepSpace9
                            Systems.DeepSpace9.DeepSpace9.CreateMenus()

                        except:
                            pass


# A function which cleans up our mess when we quit the game                        
class DS9FXQuit(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                DS9FXEnd()



# Called when you quit the QB match or any other game... I think!
DS9FXQuit('DS9FX Ending', App.ET_QUIT, dict = { 'modes': [ mode ] } )


# Call in the core file
def DS9FXEnd():
        Custom.DS9FX.DS9FXmain.DS9FXExit()
        

if mode.IsEnabled:
    # Small print, all big mods have it :P
    print "DS9FX Initializing..."


# One button full console print out in a txt file. Thanks to Mleo for giving his permission long time ago to use his mod in DS9FX.
class DS9FXPrintOut(Foundation.TriggerDef):
        def __init__(self, dict = {}):
                Foundation.TriggerDef.__init__(self, "DS9FXPrintOut", ET_EVENT, dict = {})

        def __call__(self, pObject, pEvent):

                Int = pEvent.GetInt()

                # Compare values
                if (Int == 500):
                    ConsolePrintOut()
                
                return 0
            
           
DS9FXPrintOut(dict = {"modes": [mode]})

# Bind Shift + P Key so we ca automatically produce a txt version of a console report
App.g_kKeyboardBinding.BindKey(App.WC_CAPS_P, App.TGKeyboardEvent.KS_NORMAL, ET_EVENT, App.KeyboardBinding.GET_INT_EVENT, 500)


# Produce a console report
def ConsolePrintOut():
        if pDebugMode == 1:
            # Bring up the console
            App.TopWindow_GetTopWindow().ToggleConsole()

            # Add txt to the console so that it appears we've pressed enter
            pTopWindow = App.TopWindow_GetTopWindow()
            pConsole = pTopWindow.FindMainWindow(App.MWT_CONSOLE)
            pCon = App.TGConsole_Cast(pConsole.GetFirstChild())
            pCon.AddConsoleString("### Console Dump...")
            pCon.EvalString("### Saved!")

            # Produce a console report
            import Custom.DS9FX.DS9FXLib.PrintConsole

            Custom.DS9FX.DS9FXLib.PrintConsole.Print()

            # Close the console
            App.TopWindow_GetTopWindow().ToggleConsole()

        else:
            return


# Try to free up memory resources & if NanoFX is installed prevent game crashes 
class DS9FXExplodingCleanUp(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                StabilizeBC()


DS9FXExplodingCleanUp('DS9FX Explosion Cleaning Up Active', App.ET_OBJECT_DESTROYED, dict = { 'modes': [ mode ] } )


# Now we are going to use ET_WEAPON_HIT Event... I hope it'll be effective
class DS9FXWeaponHitCleanUp(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                StabilizeBC()


DS9FXWeaponHitCleanUp('DS9FX Weapon Hit Cleaning Up Active', App.ET_WEAPON_HIT, dict = { 'modes': [ mode ] } )


# At the start of a game, some models could be in the memory of the game. So delete them!
class DS9FXGameStartCleanUp(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                MissionStartStabilizeBC()


DS9FXGameStartCleanUp('DS9FX Game Start Cleaning Up Active', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )


# Purge LODModelManager
def StabilizeBC():
        if pStabilizeBC == 1:
            App.g_kLODModelManager.Purge()

        else:
            return


# After 5 seconds purge lod manager
def MissionStartStabilizeBC():
        MissionLib.CreateTimer(GetNextEventType(), __name__ + ".TimerStabilizeBC", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)


# LODModelManager Purge
def TimerStabilizeBC(pObject, pEvent):
        if pStabilizeBC == 1:
            App.g_kLODModelManager.Purge()

        else:
            return


# Let's remove dying ships from the game, it prevents game crashes
class DS9FXRemoveDyingShips(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                CallTimer()

# Changed to ET_MISSION_START. We made sure that we constantly run only 1 copy of the timer
DS9FXRemoveDyingShips('DS9FX Remove Dying Ships', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )


# Redirect function
def CallTimer():
        global Timer
        
        Timer = MissionLib.CreateTimer(GetNextEventType(), __name__ + ".InitiateTimer", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
        

# Event delayed for 1 second
def InitiateTimer(pObject, pEvent):
        if pStabilizeBC == 1:
            StabilizationCode.StartUp()

        else:
            return
        
# Return event type
def GetNextEventType():
    
        return App.Mission_GetNextEventType() + 333
