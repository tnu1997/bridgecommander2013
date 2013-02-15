from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# We'll preload needed ship models to prevent any problems :) well speed up game loading

# by USS Sovereign


# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pModelPreloadingSelection = pModule.ModelPreloadingSelection


# Imports
import loadspacehelper

# Preloaded models
def PreLoadEverything(pMission):

        debug(__name__ + ", PreLoadEverything")
        import Custom.DS9FX.DS9FXShips
        if pModelPreloadingSelection == 1:
                    
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.Wormhole, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXExcalibur, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXDeepSpace9, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXDefiant, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXMiranda, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, 3)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.WormholeCone, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.WormholeCone2, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.Wormhole2, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXLakota, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXDummy, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.DS9FXComet, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.Wormhole3, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.Wormhole4, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.Wormhole5, 1)
                loadspacehelper.PreloadShip(Custom.DS9FX.DS9FXShips.Wormhole6, 1)
                           
        
        else:
                return
