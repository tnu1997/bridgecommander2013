from bcdebug import debug
# Since BC won't acknowledge deductive scale settings we do it manually, it's a load of work but the only way I can think of to execute this

# by USS Sovereign

# Imports
import App
import DS9FXMenuLib
import MissionLib
from Custom.DS9FX.DS9FXmain import GlobalCutsceneEnding


# Call in the first function and begin series of timer based events to manually set scale of the wormhole model back to 0.01
def StartScaling():
        debug(__name__ + ", StartScaling")
        Scale1(None, None)


# Manual Scaling
def Scale1(pObject, pEvent):
        
	# Play the sound
        debug(__name__ + ", Scale1")
        pSound = App.TGSound_Create("sfx/Custom/DS9FX/WormholeClose.wav", "WormClose", 0)
        pSound.SetSFX(0) 
        pSound.SetInterface(1) 
        App.g_kSoundManager.PlaySound("WormClose")
        
        # Get the player
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.9)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale2", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)


# Manual Scaling
def Scale2(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale2")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.8)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale3", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)


# Manual Scaling
def Scale3(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale3")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.7)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale4", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

 
# Manual Scaling
def Scale4(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale4")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.6)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale5", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

 
# Manual Scaling
def Scale5(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale5")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.5)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale6", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

 
# Manual Scaling
def Scale6(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale6")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.4)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale7", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

# Manual Scaling
def Scale7(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale7")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.3)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale8", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

 
# Manual Scaling
def Scale8(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale8")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.2)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale9", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

# Manual Scaling
def Scale9(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale9")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.1)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale10", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale10(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale10")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(3.0)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale11", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale11(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale11")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.9)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale12", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale12(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale12")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.8)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale13", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
# Manual Scaling
def Scale13(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale13")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.7)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale14", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale14(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale14")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.6)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale15", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale15(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale15")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.5)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale16", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 


# Manual Scaling
def Scale16(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale16")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.4)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale17", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

# Manual Scaling
def Scale17(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale17")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.3)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale18", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 


# Manual Scaling
def Scale18(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale18")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.2)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale19", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale19(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale19")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.1)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale20", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale20(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale20")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(2.0)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale21", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale21(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale21")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.9)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale22", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale22(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale22")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.8)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale23", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale23(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale23")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.7)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale24", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale24(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale24")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.6)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale25", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)


# Manual Scaling
def Scale25(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale25")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.5)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale26", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

# Manual Scaling
def Scale26(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale26")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.4)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale27", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

# Manual Scaling
def Scale27(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale27")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.3)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale28", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
# Manual Scaling
def Scale28(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale28")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.2)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale29", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
# Manual Scaling
def Scale29(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale29")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.1)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale30", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)

 
 
# Manual Scaling
def Scale30(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale30")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(1.0)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale31", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
# Manual Scaling
def Scale31(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale31")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.9)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale32", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
 
# Manual Scaling
def Scale32(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale32")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.8)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale33", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale33(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale33")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.7)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale34", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale34(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale34")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.6)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale35", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
# Manual Scaling
def Scale35(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale35")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.5)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale36", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
# Manual Scaling
def Scale36(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale36")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.4)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale37", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
# Manual Scaling
def Scale37(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale37")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.3)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale38", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
 
# Manual Scaling
def Scale38(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale38")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.2)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale39", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 
# Manual Scaling
def Scale39(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale39")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.1)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale40", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)


# Manual Scaling
def Scale40(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale40")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
		
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.01)

        # Call the other function
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Scale41", App.g_kUtopiaModule.GetGameTime() + 0.01, 0, 0)
 

# Manual Scaling
def Scale41(pObject, pEvent):
        # Get the player
        debug(__name__ + ", Scale41")
        pPlayer = App.Game_GetCurrentPlayer()    	
        if not pPlayer:
		 return 0
            
        # Get the set
        pSet = pPlayer.GetContainingSet()

        # Get the Wormhole model              
        pDS9FXWormhole = MissionLib.GetShip("Bajoran Wormhole", pSet)
            
        # Scale the wormhole! Wormhole has to be there so no safety measures are needed          
        pDS9FXWormhole.SetScale(0.01)

        # Import the flash file and play it, nice addition to the mod
        from Custom.DS9FX.DS9FXWormholeFlash.DS9FXExitWormholeFlash import StartGFX, CreateGFX
                
        StartGFX()
        for i in range(1):
                CreateGFX(pDS9FXWormhole)

        # Get us back now to DS9FXmain.py file and let it take over
        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".GlobalCutsceneEnding", App.g_kUtopiaModule.GetGameTime() + 6, 0, 0)

