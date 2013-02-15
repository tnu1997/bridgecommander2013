from bcdebug import debug
# Code which removes ships from a set, it is called by DS9FX_mutator.py
# by USS Sovereign

# Imports
import App
import MissionLib

# Vars
sList = []
iCounter = 0
Timer = None
iWatcher = 1

# Start the code
def StartUp():
        debug(__name__ + ", StartUp")
        global Timer, iWatcher

        if iWatcher == 1:
        
                Timer = StartUpTimer()  

        else:
            
            print 'DS9FX: Prevented multiple timers...'
            
            return
        

# Remove dying ship & repeat the timer based event
class StartUpTimer:
        def __init__(self):
            # Only start the timer once!!!
            debug(__name__ + ", __init__")
            global iWatcher
            iWatcher = 0
            self.pTimer = None
            self.__Timing__()

        def __Timing__(self):
            debug(__name__ + ", __Timing__")
            if not self.pTimer:
                self.pTimer = App.PythonMethodProcess()
		self.pTimer.SetInstance(self)
		self.pTimer.SetFunction("__Update__")
		self.pTimer.SetDelay(1)
		self.pTimer.SetPriority(App.TimeSliceProcess.NORMAL)

        def __Update__(self, sTime):
            debug(__name__ + ", __Update__")
            global sList, iCounter

            iCounter = iCounter + 1

            # Every six minutes reset sList
            if iCounter >= 360:
                iCounter = None
                iCounter = 0
                sList = None
                sList = []
            
            # From QuickBattle.py
            pSets = App.g_kSetManager.GetAllSets()
                    
            for pSet in pSets:
                
                for kShip in pSet.GetClassObjectList(App.CT_DAMAGEABLE_OBJECT):

                        pShip = kShip.GetObjID()
			if not MissionLib.GetPlayer():
				break

                        pPlayer = MissionLib.GetPlayer().GetObjID()
                    
                        if not pShip == pPlayer:

                                if kShip.IsDead():

                                        if not pShip in sList:

                                                sList.append(pShip)

                                                kShip.SetDeleteMe(1)

                                                App.g_kLODModelManager.Purge() 
                                                    
