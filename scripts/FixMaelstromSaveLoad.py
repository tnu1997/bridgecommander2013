from bcdebug import debug
import FoundationTech


#BC can not save instances in dicts, so delete them.
def DoPreSaveGameStuff():
        debug(__name__ + ", DoPreSaveGameStuff")
        print("Doing Pre Save game stuff")
