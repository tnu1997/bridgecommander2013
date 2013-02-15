# by USS Sovereign - A completly rewritten DS9FXConfig.py! 


##### NOTICE: To maintain compatibility with old DS9FXConfig.py and to save me a lot of work this script will have a lot of bridges which will fill the gap between the two versions.

# Imports
import App
import string
import nt
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXUnsavedConfig
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Grab presaved configuration and later on allow the user to save his own default config
# Mostly still needed because all Files from DS9FX Call this file to get correct settings
ExcaliburSelection  = DS9FXSavedConfig.ExcaliburSelection
DefiantSelection = DS9FXSavedConfig.DefiantSelection
OregonSelection = DS9FXSavedConfig.OregonSelection
LakotaSelection = DS9FXSavedConfig.LakotaSelection
DS9Selection = DS9FXSavedConfig.DS9Selection
Bugship1Selection = DS9FXSavedConfig.Bugship1Selection
Bugship2Selection = DS9FXSavedConfig.Bugship2Selection
Bugship3Selection = DS9FXSavedConfig.Bugship3Selection
WormholeSelection = DS9FXSavedConfig.WormholeSelection
VideoSelection = DS9FXSavedConfig.VideoSelection
ModelPreloadingSelection = DS9FXSavedConfig.ModelPreloadingSelection
RandomEnemyFleetAttacks = DS9FXSavedConfig.RandomEnemyFleetAttacks
DomIS = DS9FXSavedConfig.DomIS
DS9Music = DS9FXSavedConfig.DS9Music
WormholeMusic = DS9FXSavedConfig.WormholeMusic 
GammaMusic = DS9FXSavedConfig.GammaMusic
RandomDomStrength = DS9FXSavedConfig.RandomDomStrength
FederationSide = DS9FXSavedConfig.FederationSide
DominionSide = DS9FXSavedConfig.DominionSide
CometSelection = DS9FXSavedConfig.CometSelection
DS9Planets = DS9FXSavedConfig.DS9Planets
DS9NanoFX = DS9FXSavedConfig.DS9NanoFX
GammaPlanets = DS9FXSavedConfig.GammaPlanets
GammaNanoFX = DS9FXSavedConfig.GammaNanoFX
DominionTimeSpan = DS9FXSavedConfig.DominionTimeSpan
CometAlphaTrail = DS9FXSavedConfig.CometAlphaTrail
CometAlphaTrailTexture = DS9FXSavedConfig.CometAlphaTrailTexture
DebugMode = DS9FXSavedConfig.DebugMode
DS9MapPlanetDetail = DS9FXSavedConfig.DS9MapPlanetDetail
GammaMapPlanetDetail = DS9FXSavedConfig.GammaMapPlanetDetail
InsideWormholeBackgroundTexture = DS9FXSavedConfig.InsideWormholeBackgroundTexture
InsideWormholeModel = DS9FXSavedConfig.InsideWormholeModel
StabilizeBC = DS9FXSavedConfig.StabilizeBC
IntroVid = DS9FXSavedConfig.IntroVid
CompletionVid = DS9FXSavedConfig.CompletionVid


# Path to the directory where the configurations should be saved
Path  = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\DS9FXSavedConfig.py"
UnsavedPath = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\DS9FXUnsavedConfig.py"

# Events
ET_STATE_BUTTON  = App.UtopiaModule_GetNextEventType()
ET_ONOFF_BUTTON  = App.UtopiaModule_GetNextEventType()


# UMM Name
def GetName():
                return "DS9FX"
            

# Create a menu
def CreateMenu(pOptionPane, pContentPanel, bGameEnded = 0):
                CorrectConfig(None, None)
                
                pTopWindow = App.TopWindow_GetTopWindow()
                pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
                
                pOptionsWindow.AddPythonFuncHandlerForInstance(ET_STATE_BUTTON,  __name__ + ".HandleStateButton")
                pOptionsWindow.AddPythonFuncHandlerForInstance(ET_ONOFF_BUTTON,  __name__ + ".HandleOnOffButton")                

                CreateSubmenu1(pOptionPane, pContentPanel)
                CreateSubmenu2(pOptionPane, pContentPanel)
                CreateSubmenu3(pOptionPane, pContentPanel)
                CreateSubmenu4(pOptionPane, pContentPanel)
                CreateSubmenu5(pOptionPane, pContentPanel)
                CreateSubmenu6(pOptionPane, pContentPanel)
                CreateSubmenu7(pOptionPane, pContentPanel)
                CreateSubmenu8(pOptionPane, pContentPanel)
                CreateSubmenu9(pOptionPane, pContentPanel)
                CreateSubmenu10(pOptionPane, pContentPanel)
                CreateSubmenu11(pOptionPane, pContentPanel)
                CreateSubmenu12(pOptionPane, pContentPanel)
                CreateSubmenu13(pOptionPane, pContentPanel)

                # Create a button to call our credits
                CreateButton("DS9FX Credits", pContentPanel, pOptionPane, pContentPanel, __name__ + ".DSFXCredits")

                return App.TGPane_Create(0,0)


def CreateSubmenu1(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("DS9FX Sides")
                pContentPanel.AddChild(pMainMenu)

                pMenu1 = CreateStateButton(App.TGString("Federation Ships: "), "FederationSide", [App.TGString("Enemy"), App.TGString("Friendly")], DS9FXUnsavedConfig.FederationSide)
                pMainMenu.AddChild(pMenu1)

                pMenu2 = CreateStateButton(App.TGString("Dominion Ships: "), "DominionSide", [App.TGString("Enemy"), App.TGString("Friendly")], DS9FXUnsavedConfig.DominionSide)
                pMainMenu.AddChild(pMenu2)

                return pMainMenu
            

def CreateSubmenu2(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("Planet Options")
                pContentPanel.AddChild(pMainMenu)

                pMenu1 = CreateStateButton(App.TGString("Planets in DS9 Map: "), "DS9Planets", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DS9Planets)
                pMainMenu.AddChild(pMenu1)

                pMenu2 = CreateStateButton(App.TGString("NanoFX Atm.-DS9 Map: "), "DS9NanoFX", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DS9NanoFX)
                pMainMenu.AddChild(pMenu2)
                
                pMenu3 = CreateStateButton(App.TGString("DS9-Planet Detail: "), "DS9MapPlanetDetail", [App.TGString("Low"), App.TGString("Standard"), App.TGString("High")], DS9FXUnsavedConfig.DS9MapPlanetDetail)
                pMainMenu.AddChild(pMenu3)

                pMenu4 = CreateStateButton(App.TGString("Planets in Gamma Map: "), "DS9Planets", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DS9Planets)
                pMainMenu.AddChild(pMenu4)

                pMenu5 = CreateStateButton(App.TGString("NanoFX Atm.-Gamma Map: "), "GammaNanoFX", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.GammaNanoFX)
                pMainMenu.AddChild(pMenu5)

                pMenu6 = CreateStateButton(App.TGString("Gamma-Planet Detail: "), "GammaMapPlanetDetail", [App.TGString("Low"), App.TGString("Standard"), App.TGString("High")], DS9FXUnsavedConfig.GammaMapPlanetDetail)
                pMainMenu.AddChild(pMenu6)

                return pMainMenu


def CreateSubmenu3(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("DS9 Map Ships")
                pContentPanel.AddChild(pMainMenu)

                pMenu1 = CreateStateButton(App.TGString("USS Excalibur: "), "ExcaliburSelection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.ExcaliburSelection)
                pMainMenu.AddChild(pMenu1)

                pMenu2 = CreateStateButton(App.TGString("USS Defiant: "), "DefiantSelection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DefiantSelection)
                pMainMenu.AddChild(pMenu2)

                pMenu3 = CreateStateButton(App.TGString("USS Oregon: "), "OregonSelection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.OregonSelection)
                pMainMenu.AddChild(pMenu3)

                pMenu4 = CreateStateButton(App.TGString("USS Lakota: "), "LakotaSelection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.LakotaSelection)
                pMainMenu.AddChild(pMenu4)
                
                return pMainMenu
            

def CreateSubmenu4(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("DS9 Map Stations\Objects")
                pContentPanel.AddChild(pMainMenu)

                pMenu1 = CreateStateButton(App.TGString("Deep Space 9: "), "DS9Selection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.DS9Selection)
                pMainMenu.AddChild(pMenu1)

                pMenu2 = CreateStateButton(App.TGString("Comet Alpha: "), "CometSelection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.CometSelection)
                pMainMenu.AddChild(pMenu2)

                return pMainMenu


def CreateSubmenu5(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("Gamma Quadrant Map Ships")
                pContentPanel.AddChild(pMainMenu)

                pMenu1 = CreateStateButton(App.TGString("Bugship 1: "), "Bugship1Selection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.Bugship1Selection)
                pMainMenu.AddChild(pMenu1)

                pMenu2 = CreateStateButton(App.TGString("Bugship 2: "), "Bugship2Selection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.Bugship2Selection)
                pMainMenu.AddChild(pMenu2)

                pMenu3 = CreateStateButton(App.TGString("Bugship 3: "), "Bugship3Selection", [App.TGString("No"), App.TGString("Yes")], DS9FXUnsavedConfig.Bugship3Selection)
                pMainMenu.AddChild(pMenu3)

                return pMainMenu


def CreateSubmenu6(pOptionPane, pContentPanel):
                global pModel 
                                
                pMainMenu = App.STCharacterMenu_Create("Wormhole Options")
                pContentPanel.AddChild(pMainMenu)

                pModel = CreateButton("Wormhole:  None", pMainMenu, pOptionPane, pContentPanel, __name__ + ".SelectModel", EventInt = 0)

                pMenu2 = CreateOnOffButton(App.TGString("Video Sequence: "), "VideoSelection", DS9FXUnsavedConfig.VideoSelection)
                pMainMenu.AddChild(pMenu2)

                
                if DS9FXUnsavedConfig.WormholeSelection == 1:
                        pModel.SetName(App.TGString("Wormhole:  Model 2"))
                                        
                elif DS9FXUnsavedConfig.WormholeSelection == 2:
                        pModel.SetName(App.TGString("Wormhole:  Model 3"))
                                        
                elif DS9FXUnsavedConfig.WormholeSelection == 3:
                        pModel.SetName(App.TGString("Wormhole:  Model 4"))
                                        
                elif DS9FXUnsavedConfig.WormholeSelection == 4:
                        pModel.SetName(App.TGString("Wormhole:  Model 5"))
                                        
                elif DS9FXUnsavedConfig.WormholeSelection == 5:
                        pModel.SetName(App.TGString("Wormhole:  Model 6"))
                        
                else:
                        pModel.SetName(App.TGString("Wormhole:  Model 1"))
                        

                return pMainMenu


def CreateSubmenu7(pOptionPane, pContentPanel):
                global pBack
                global pVariant
                
                pMainMenu = App.STCharacterMenu_Create("Inside Wormhole Options")
                pContentPanel.AddChild(pMainMenu)

                pBack = CreateButton("Backgrounds:  None", pMainMenu, pOptionPane, pContentPanel, __name__ + ".InsideWormholeBack", EventInt = 0)

                if DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 1:
                        pBack.SetName(App.TGString("Backgrounds:  Red"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 2:
                        pBack.SetName(App.TGString("Backgrounds:  Chrome"))

                elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 3:
                        pBack.SetName(App.TGString("Backgrounds:  Dark Blue"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 4:
                        pBack.SetName(App.TGString("Backgrounds:  Water Blue"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 5:
                        pBack.SetName(App.TGString("Backgrounds:  Weird"))

                else:
                        pBack.SetName(App.TGString("Backgrounds:  Blue"))


                pVariant = CreateButton("Model Variants:  None", pMainMenu, pOptionPane, pContentPanel, __name__ + ".InsideWormholeModels", EventInt = 0)

                if DS9FXUnsavedConfig.InsideWormholeModel == 1:
                        pVariant.SetName(App.TGString("Model Variants:  Yellow"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeModel == 2:
                        pVariant.SetName(App.TGString("Model Variants:  Red Dawn"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeModel == 3:
                        pVariant.SetName(App.TGString("Model Variants:  Slipstream"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeModel == 4:
                        pVariant.SetName(App.TGString("Model Variants:  Blackhole"))
                        
                else:
                        pVariant.SetName(App.TGString("Model Variants:  DS9 Series"))

                return pMainMenu
            

def CreateSubmenu8(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("Comet Alpha Options")
                pContentPanel.AddChild(pMainMenu)

                pMenu1 = CreateStateButton(App.TGString("Comet Trail Style: "), "CometAlphaTrail", [App.TGString("Plasma"), App.TGString("Comet")], DS9FXUnsavedConfig.CometAlphaTrail)
                pMainMenu.AddChild(pMenu1)

                pMenu2 = CreateStateButton(App.TGString("Comet Trail Color: "), "CometAlphaTrailTexture", [App.TGString("Blue"), App.TGString("White")], DS9FXUnsavedConfig.CometAlphaTrailTexture)
                pMainMenu.AddChild(pMenu2)

                return pMainMenu


def CreateSubmenu9(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("Misc Options")
                pContentPanel.AddChild(pMainMenu)

                pMenu1 = CreateOnOffButton(App.TGString("Debug Mode: "), "DebugMode", DS9FXUnsavedConfig.DebugMode)
                pMainMenu.AddChild(pMenu1) 

                pMenu2 = CreateOnOffButton(App.TGString("Stabilize BC: "), "StabilizeBC", DS9FXUnsavedConfig.StabilizeBC)
                pMainMenu.AddChild(pMenu2) 

                pMenu3 = CreateOnOffButton(App.TGString("Ship Model Preloading: "), "ModelPreloadingSelection", DS9FXUnsavedConfig.ModelPreloadingSelection)
                pMainMenu.AddChild(pMenu3) 

                pMenu4 = CreateStateButton(App.TGString("Random Attacks\Assists: "), "RandomEnemyFleetAttacks", [App.TGString("Off"), App.TGString("On")], DS9FXUnsavedConfig.RandomEnemyFleetAttacks)
                pMainMenu.AddChild(pMenu4)

                pMenu5 = CreateOnOffButton(App.TGString("Dom. Intensive Scan: "), "DomIS", DS9FXUnsavedConfig.DomIS)
                pMainMenu.AddChild(pMenu5) 

                pMenu6 = CreateStateButton(App.TGString("Random Fleet Strength: "), "RandomDomStrength", [App.TGString("Weak"), App.TGString("Medium"), App.TGString("Strong")], DS9FXUnsavedConfig.RandomDomStrength)
                pMainMenu.AddChild(pMenu6)

                pMenu7 = CreateStateButton(App.TGString("Random Fleet Timespan: "), "DominionTimeSpan", [App.TGString("2-4 mins"), App.TGString("4-6 mins"), App.TGString("6-8 mins")], DS9FXUnsavedConfig.DominionTimeSpan)
                pMainMenu.AddChild(pMenu7)

                pMenu8 = CreateOnOffButton(App.TGString("Mission Intro Vid: "), "IntroVid", DS9FXUnsavedConfig.IntroVid)
                pMainMenu.AddChild(pMenu8)

                pMenu9 = CreateOnOffButton(App.TGString("Campaign Completion Vid: "), "CompletionVid", DS9FXUnsavedConfig.CompletionVid)
                pMainMenu.AddChild(pMenu9)

                return pMainMenu


def CreateSubmenu10(pOptionPane, pContentPanel):
                global pMusicDS9
                
                pMainMenu = App.STCharacterMenu_Create("Music Options")
                pContentPanel.AddChild(pMainMenu)

		pMusicDS9 = CreateButton("DS9 Map Music: None", pMainMenu, pOptionPane, pContentPanel, __name__ + ".DS9MusicSelection", EventInt = 0)

                if DS9FXUnsavedConfig.DS9Music == 1:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Music 1"))
                        
                elif DS9FXUnsavedConfig.DS9Music == 2:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Music 2"))
                        
                elif DS9FXUnsavedConfig.DS9Music == 3:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Music 3"))
                        
                elif DS9FXUnsavedConfig.DS9Music == 4:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Random"))
                        
                else:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Off"))

                        
                pMenu2 = CreateStateButton(App.TGString("Bajoran Wormh. Music: "), "WormholeMusic", [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"), App.TGString("Random")], DS9FXUnsavedConfig.WormholeMusic)
                pMainMenu.AddChild(pMenu2)

                pMenu3 = CreateStateButton(App.TGString("Gamma Quad. Music: "), "GammaMusic", [App.TGString("Off"), App.TGString("Music 1"), App.TGString("Music 2"), App.TGString("Random")], DS9FXUnsavedConfig.GammaMusic)
                pMainMenu.AddChild(pMenu3)

                return pMainMenu


def CreateSubmenu11(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("Foundation Mutator Fix")
                pContentPanel.AddChild(pMainMenu)

                CreateButton("Save Foundation Settings", pMainMenu, pOptionPane, pContentPanel, __name__ + ".SaveFdntConfig", EventInt = 0)
                CreateButton("Restore Foundation Settings", pMainMenu, pOptionPane, pContentPanel, __name__ + ".RestoreFdtnConfig", EventInt = 0)

                return pMainMenu
            

def CreateSubmenu12(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("Extras")
                pContentPanel.AddChild(pMainMenu)

                CreateButton("Play Tutorial Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid4", EventInt = 0)
                CreateButton("Play Completion Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid1", EventInt = 0)
                CreateButton("Play Intro Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid2", EventInt = 0)
                CreateButton("Play Wormhole Video", pMainMenu, pOptionPane, pContentPanel, __name__ + ".ExtraVid3", EventInt = 0)

                return pMainMenu


def CreateSubmenu13(pOptionPane, pContentPanel):
                pMainMenu = App.STCharacterMenu_Create("DS9FX Configuration")
                pContentPanel.AddChild(pMainMenu)

                CreateButton("Apply New DS9FX Config", pMainMenu, pOptionPane, pContentPanel, __name__ + ".SaveConfig", EventInt = 0)
                CreateButton("Refresh DS9FX Config Settings", pMainMenu, pOptionPane, pContentPanel, __name__ + ".RefreshConfig", EventInt = 0)

                return pMainMenu
            


# Save foundation backup copy
def SaveFdntConfig(pObject, pEvent):
    
                PlayButtonClickedSound()
                
                from Custom.DS9FX.DS9FXLib import FoundationMutatorFix

                FoundationMutatorFix.SaveBackup()


# Restore backup foundation settings
def RestoreFdtnConfig(pObject, pEvent):
    
                PlayButtonClickedSound()
                
                from Custom.DS9FX.DS9FXLib import FoundationMutatorFix

                FoundationMutatorFix.RestoreFoundationSettings()

                # Make a hack, force UMM to reload all menus themselves again
                import MainMenu.mainmenu
                
                MainMenu.mainmenu.SwitchMiddlePane("Configure")
                
        
            
# Play extra vids. Some very close friends advised this to me, to add it lol
def ExtraVid1(pObject, pEvent):

                PlayButtonClickedSound()

                from Custom.DS9FX.DS9FXVids import DS9FXExtrasCompletionVid

                DS9FXExtrasCompletionVid.PlayMovieSeq(None, None)


                
# Play extra vids. Some very close friends advised this to me, to add it lol
def ExtraVid2(pObject, pEvent):

                PlayButtonClickedSound()
                
                from Custom.DS9FX.DS9FXVids import DS9FXExtrasIntroVid

                DS9FXExtrasIntroVid.PlayMovieSeq(None, None)

                

# Play extra vids. Some very close friends advised this to me, to add it lol
def ExtraVid3(pObject, pEvent):

                PlayButtonClickedSound()

                from Custom.DS9FX.DS9FXVids import DS9FXExtrasWormholeVid

                DS9FXExtrasWormholeVid.PlayMovieSeq(None, None)


# Play the tutorial video
def ExtraVid4(pObject, pEvent):

                PlayButtonClickedSound()

                from Custom.DS9FX.DS9FXVids import DS9FXExtrasTutorialVid

                DS9FXExtrasTutorialVid.PlayMovieSeq(None, None)



# Call in the file which plays our credits sequence
def DSFXCredits(pObject, pEvent):
    
                PlayCreditsButtonClickedSound()
                
                from Custom.DS9FX.DS9FXPrompts import DS9FXCreditsPrompt

                DS9FXCreditsPrompt.Prompt()
                

# Model Selection
def SelectModel(pObject, pEvent):                
                DS9FXUnsavedConfig.WormholeSelection = DS9FXUnsavedConfig.WormholeSelection + 1

                if DS9FXUnsavedConfig.WormholeSelection >= 6:
                    DS9FXUnsavedConfig.WormholeSelection = 0

                SetModelConfig()


def SetModelConfig():
                global pModel
                
                if DS9FXUnsavedConfig.WormholeSelection == 1:
                        pModel.SetName(App.TGString("Wormhole:  Model 2"))
                                        
                elif DS9FXUnsavedConfig.WormholeSelection == 2:
                        pModel.SetName(App.TGString("Wormhole:  Model 3"))
                                        
                elif DS9FXUnsavedConfig.WormholeSelection == 3:
                        pModel.SetName(App.TGString("Wormhole:  Model 4"))
                                        
                elif DS9FXUnsavedConfig.WormholeSelection == 4:
                        pModel.SetName(App.TGString("Wormhole:  Model 5"))
                                        
                elif DS9FXUnsavedConfig.WormholeSelection == 5:
                        pModel.SetName(App.TGString("Wormhole:  Model 6"))
                        
                else:
                        pModel.SetName(App.TGString("Wormhole:  Model 1"))
                                        
                SaveTempConfig()
                                

def InsideWormholeBack(pObject, pEvent):
                DS9FXUnsavedConfig.InsideWormholeBackgroundTexture = DS9FXUnsavedConfig.InsideWormholeBackgroundTexture + 1

                if DS9FXUnsavedConfig.InsideWormholeBackgroundTexture >= 6:
                    DS9FXUnsavedConfig.InsideWormholeBackgroundTexture = 0

                SetWormholeBackConfig()
                

def SetWormholeBackConfig():
                global pBack
                
                if DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 1:
                        pBack.SetName(App.TGString("Backgrounds:  Red"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 2:
                        pBack.SetName(App.TGString("Backgrounds:  Chrome"))

                elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 3:
                        pBack.SetName(App.TGString("Backgrounds:  Dark Blue"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 4:
                        pBack.SetName(App.TGString("Backgrounds:  Water Blue"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeBackgroundTexture == 5:
                        pBack.SetName(App.TGString("Backgrounds:  Weird"))

                else:
                        pBack.SetName(App.TGString("Backgrounds:  Blue"))

                SaveTempConfig()
                

def InsideWormholeModels(pObject, pEvent):
                DS9FXUnsavedConfig.InsideWormholeModel = DS9FXUnsavedConfig.InsideWormholeModel + 1

                if DS9FXUnsavedConfig.InsideWormholeModel >= 5:
                    DS9FXUnsavedConfig.InsideWormholeModel = 0

                SetWormholeModelConfig()


def SetWormholeModelConfig():
                global pVariant

                if DS9FXUnsavedConfig.InsideWormholeModel == 1:
                        pVariant.SetName(App.TGString("Model Variants:  Yellow"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeModel == 2:
                        pVariant.SetName(App.TGString("Model Variants:  Red Dawn"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeModel == 3:
                        pVariant.SetName(App.TGString("Model Variants:  Slipstream"))
                        
                elif DS9FXUnsavedConfig.InsideWormholeModel == 4:
                        pVariant.SetName(App.TGString("Model Variants:  Blackhole"))
                        
                else:
                        pVariant.SetName(App.TGString("Model Variants:  DS9 Series"))
                                        
                SaveTempConfig()


def DS9MusicSelection(pObject, pEvent):
                DS9FXUnsavedConfig.DS9Music = DS9FXUnsavedConfig.DS9Music + 1

                if DS9FXUnsavedConfig.DS9Music >= 5:
                    DS9FXUnsavedConfig.DS9Music = 0

                SetDS9MusicSelectionConfig()


def SetDS9MusicSelectionConfig():
                global pMusicDS9                

                if DS9FXUnsavedConfig.DS9Music == 1:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Music 1"))
                        
                elif DS9FXUnsavedConfig.DS9Music == 2:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Music 2"))
                        
                elif DS9FXUnsavedConfig.DS9Music == 3:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Music 3"))
                        
                elif DS9FXUnsavedConfig.DS9Music == 4:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Random"))
                        
                else:
                        pMusicDS9.SetName(App.TGString("DS9 Map Music:  Off"))

                SaveTempConfig()
                
                
# Handles state button
def HandleStateButton(pObject, pEvent):
                DS9FXUnsavedConfig.__dict__[pEvent.GetCString()] = App.STToggle_Cast(pEvent.GetSource()).GetState()
                App.g_kSoundManager.StopSound("Clicked")
                SaveTempConfig()
                pObject.CallNextHandler(pEvent)


# Handles on/off button
def HandleOnOffButton(pObject, pEvent):
                DS9FXUnsavedConfig.__dict__[pEvent.GetCString()] = App.STToggle_Cast(pEvent.GetSource()).GetState()
                App.g_kSoundManager.StopSound("Clicked")
                SaveTempConfig() 
                pObject.CallNextHandler(pEvent)


# Code by Mleo
def CreateStateButton(pName, sVar, lStates, iState):
                pTopWindow = App.TopWindow_GetTopWindow()
                pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

                kArgs = [pName, iState]
                kEvents=[]
                for kStateName in lStates:
                    pEvent = App.TGStringEvent_Create()
                    pEvent.SetEventType(ET_STATE_BUTTON)
                    pEvent.SetDestination(pOptionsWindow)
                    pEvent.SetString(sVar)

                    kArgs.append(kStateName)
                    kArgs.append(pEvent)
                    kEvents.append(pEvent)
                kMenuButton = apply(App.STToggle_CreateW, kArgs)
                for pEvent in kEvents:
                    pEvent.SetSource(kMenuButton)

                return kMenuButton


# Code by Mleo
def CreateOnOffButton(pName, sVar, iState):
                pTopWindow = App.TopWindow_GetTopWindow()
                pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

                pOffEvent = App.TGStringEvent_Create()
                pOnEvent  = App.TGStringEvent_Create()
                pOffEvent.SetString(sVar)
                pOnEvent.SetString(sVar)
                pOffEvent.SetEventType(ET_ONOFF_BUTTON)
                pOnEvent.SetEventType(ET_ONOFF_BUTTON)
                pOffEvent.SetDestination(pOptionsWindow)
                pOnEvent.SetDestination(pOptionsWindow)

                pMenuButton = App.STToggle_CreateW(pName, iState, App.TGString("Off"), pOnEvent, App.TGString("On"), pOffEvent)
                pOffEvent.SetSource(pMenuButton)
                pOnEvent.SetSource(pMenuButton)
                
                return pMenuButton


# Create a button def
def CreateButton(sButtonName, pMenu, pOptionPane, pContentPanel, sFunction, EventInt = 0):        
                ET_EVENT = App.UtopiaModule_GetNextEventType()

                pOptionPane.AddPythonFuncHandlerForInstance(ET_EVENT, sFunction)

                pEvent = App.TGStringEvent_Create()
                pEvent.SetEventType(ET_EVENT)
                pEvent.SetDestination(pOptionPane)
                pEvent.SetString(sButtonName)

                pButton = App.STButton_Create(sButtonName, pEvent)
                pButton.SetChosen(0)

                pEvent.SetSource(pButton)            
                pMenu.AddChild(pButton)

                return pButton


def PlayButtonClickedSound():
                 pSound = App.TGSound_Create("sfx/Custom/DS9FX/UMMMenuButtonClicked.wav", "Clicked", 0)
                 pSound.SetSFX(0) 
                 pSound.SetInterface(1) 
                 App.g_kSoundManager.PlaySound("Clicked")


def PlayConfigSavedSound():
                 pSound = App.TGSound_Create("sfx/Custom/DS9FX/UMMConfigSaved.wav", "Saved", 0)
                 pSound.SetSFX(0) 
                 pSound.SetInterface(1) 
                 App.g_kSoundManager.PlaySound("Saved")

def PlayCreditsButtonClickedSound():
                 pSound = App.TGSound_Create("sfx/Custom/DS9FX/UMMCreditsMenuButtonClicked.wav", "Clicked2", 0)
                 pSound.SetSFX(0) 
                 pSound.SetInterface(1) 
                 App.g_kSoundManager.PlaySound("Clicked2")


def SaveTempConfig():
                rExcaliburSelection  = DS9FXUnsavedConfig.ExcaliburSelection
                rDefiantSelection = DS9FXUnsavedConfig.DefiantSelection
                rOregonSelection = DS9FXUnsavedConfig.OregonSelection
                rLakotaSelection = DS9FXUnsavedConfig.LakotaSelection
                rDS9Selection = DS9FXUnsavedConfig.DS9Selection
                rBugship1Selection = DS9FXUnsavedConfig.Bugship1Selection
                rBugship2Selection = DS9FXUnsavedConfig.Bugship2Selection
                rBugship3Selection = DS9FXUnsavedConfig.Bugship3Selection
                rWormholeSelection = DS9FXUnsavedConfig.WormholeSelection
                rVideoSelection = DS9FXUnsavedConfig.VideoSelection
                rModelPreloadingSelection = DS9FXUnsavedConfig.ModelPreloadingSelection
                rRandomEnemyFleetAttacks = DS9FXUnsavedConfig.RandomEnemyFleetAttacks
                rDomIS = DS9FXUnsavedConfig.DomIS
                rDS9Music = DS9FXUnsavedConfig.DS9Music
                rWormholeMusic = DS9FXUnsavedConfig.WormholeMusic 
                rGammaMusic = DS9FXUnsavedConfig.GammaMusic
                rRandomDomStrength = DS9FXUnsavedConfig.RandomDomStrength
                rFederationSide = DS9FXUnsavedConfig.FederationSide
                rDominionSide = DS9FXUnsavedConfig.DominionSide
                rCometSelection = DS9FXUnsavedConfig.CometSelection
                rDS9Planets = DS9FXUnsavedConfig.DS9Planets
                rDS9NanoFX = DS9FXUnsavedConfig.DS9NanoFX
                rGammaPlanets = DS9FXUnsavedConfig.GammaPlanets
                rGammaNanoFX = DS9FXUnsavedConfig.GammaNanoFX
                rDominionTimeSpan = DS9FXUnsavedConfig.DominionTimeSpan
                rCometAlphaTrail = DS9FXUnsavedConfig.CometAlphaTrail
                rCometAlphaTrailTexture = DS9FXUnsavedConfig.CometAlphaTrailTexture
                rDebugMode = DS9FXUnsavedConfig.DebugMode
                rDS9MapPlanetDetail = DS9FXUnsavedConfig.DS9MapPlanetDetail
                rGammaMapPlanetDetail = DS9FXUnsavedConfig.GammaMapPlanetDetail
                rInsideWormholeBackgroundTexture = DS9FXUnsavedConfig.InsideWormholeBackgroundTexture
                rInsideWormholeModel = DS9FXUnsavedConfig.InsideWormholeModel
                rStabilizeBC = DS9FXUnsavedConfig.StabilizeBC
                rIntroVid = DS9FXUnsavedConfig.IntroVid
                rCompletionVid = DS9FXUnsavedConfig.CompletionVid

                file = nt.open(UnsavedPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
                nt.write(file, "ExcaliburSelection = " + str(rExcaliburSelection) +
                "\nDefiantSelection = " + str(rDefiantSelection) +
                "\nOregonSelection = " + str(rOregonSelection) +
                "\nLakotaSelection = " + str(rLakotaSelection) +
                "\nDS9Selection = " + str(rDS9Selection) +
                "\nBugship1Selection = " + str(rBugship1Selection) +
                "\nBugship2Selection = " + str(rBugship2Selection)+
                "\nBugship3Selection = " + str(rBugship3Selection) +
                "\nWormholeSelection = " + str(rWormholeSelection) +
                "\nVideoSelection = " + str(rVideoSelection) +
                "\nModelPreloadingSelection = " + str(rModelPreloadingSelection) +
                "\nRandomEnemyFleetAttacks = " + str(rRandomEnemyFleetAttacks) +
                "\nDomIS = " + str(rDomIS) +
                "\nDS9Music = " + str(rDS9Music) +
                "\nWormholeMusic = " + str(rWormholeMusic) +
                "\nGammaMusic = " + str(rGammaMusic) +
                "\nRandomDomStrength = " + str(rRandomDomStrength) +
                "\nFederationSide = " + str(rFederationSide) +
                "\nDominionSide = " + str(rDominionSide) +
                "\nCometSelection = " + str(rCometSelection) +
                "\nDS9Planets = " + str(rDS9Planets) +
                "\nDS9NanoFX = " + str(rDS9NanoFX) +
                "\nGammaPlanets = " + str(rGammaPlanets) +
                "\nGammaNanoFX = " + str(rGammaNanoFX) +
                "\nDominionTimeSpan = " + str(rDominionTimeSpan) +
                "\nCometAlphaTrail = " + str(rCometAlphaTrail) +
                "\nCometAlphaTrailTexture = " + str(rCometAlphaTrailTexture) +
                "\nDebugMode = " + str(rDebugMode) +
                "\nDS9MapPlanetDetail = " + str(rDS9MapPlanetDetail) +
                "\nGammaMapPlanetDetail = " + str(rGammaMapPlanetDetail) +
                "\nInsideWormholeBackgroundTexture = " + str(rInsideWormholeBackgroundTexture) +
                "\nInsideWormholeModel = " + str(rInsideWormholeModel) +
                "\nStabilizeBC = " + str(rStabilizeBC) +
                "\nIntroVid = " + str(rIntroVid) +
                "\nCompletionVid = " + str(rCompletionVid))
                nt.close(file)

                reload(DS9FXUnsavedConfig)

                PlayButtonClickedSound()
                

def RefreshConfig(pObject, pEvent):
                rExcaliburSelection  = DS9FXSavedConfig.ExcaliburSelection
                rDefiantSelection = DS9FXSavedConfig.DefiantSelection
                rOregonSelection = DS9FXSavedConfig.OregonSelection
                rLakotaSelection = DS9FXSavedConfig.LakotaSelection
                rDS9Selection = DS9FXSavedConfig.DS9Selection
                rBugship1Selection = DS9FXSavedConfig.Bugship1Selection
                rBugship2Selection = DS9FXSavedConfig.Bugship2Selection
                rBugship3Selection = DS9FXSavedConfig.Bugship3Selection
                rWormholeSelection = DS9FXSavedConfig.WormholeSelection
                rVideoSelection = DS9FXSavedConfig.VideoSelection
                rModelPreloadingSelection = DS9FXSavedConfig.ModelPreloadingSelection
                rRandomEnemyFleetAttacks = DS9FXSavedConfig.RandomEnemyFleetAttacks
                rDomIS = DS9FXSavedConfig.DomIS
                rDS9Music = DS9FXSavedConfig.DS9Music
                rWormholeMusic = DS9FXSavedConfig.WormholeMusic 
                rGammaMusic = DS9FXSavedConfig.GammaMusic
                rRandomDomStrength = DS9FXSavedConfig.RandomDomStrength
                rFederationSide = DS9FXSavedConfig.FederationSide
                rDominionSide = DS9FXSavedConfig.DominionSide
                rCometSelection = DS9FXSavedConfig.CometSelection
                rDS9Planets = DS9FXSavedConfig.DS9Planets
                rDS9NanoFX = DS9FXSavedConfig.DS9NanoFX
                rGammaPlanets = DS9FXSavedConfig.GammaPlanets
                rGammaNanoFX = DS9FXSavedConfig.GammaNanoFX
                rDominionTimeSpan = DS9FXSavedConfig.DominionTimeSpan
                rCometAlphaTrail = DS9FXSavedConfig.CometAlphaTrail
                rCometAlphaTrailTexture = DS9FXSavedConfig.CometAlphaTrailTexture
                rDebugMode = DS9FXSavedConfig.DebugMode
                rDS9MapPlanetDetail = DS9FXSavedConfig.DS9MapPlanetDetail
                rGammaMapPlanetDetail = DS9FXSavedConfig.GammaMapPlanetDetail
                rInsideWormholeBackgroundTexture = DS9FXSavedConfig.InsideWormholeBackgroundTexture
                rInsideWormholeModel = DS9FXSavedConfig.InsideWormholeModel
                rStabilizeBC = DS9FXSavedConfig.StabilizeBC
                rIntroVid = DS9FXSavedConfig.IntroVid
                rCompletionVid = DS9FXSavedConfig.CompletionVid

                file = nt.open(UnsavedPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
                nt.write(file, "ExcaliburSelection = " + str(rExcaliburSelection) +
                "\nDefiantSelection = " + str(rDefiantSelection) +
                "\nOregonSelection = " + str(rOregonSelection) +
                "\nLakotaSelection = " + str(rLakotaSelection) +
                "\nDS9Selection = " + str(rDS9Selection) +
                "\nBugship1Selection = " + str(rBugship1Selection) +
                "\nBugship2Selection = " + str(rBugship2Selection)+
                "\nBugship3Selection = " + str(rBugship3Selection) +
                "\nWormholeSelection = " + str(rWormholeSelection) +
                "\nVideoSelection = " + str(rVideoSelection) +
                "\nModelPreloadingSelection = " + str(rModelPreloadingSelection) +
                "\nRandomEnemyFleetAttacks = " + str(rRandomEnemyFleetAttacks) +
                "\nDomIS = " + str(rDomIS) +
                "\nDS9Music = " + str(rDS9Music) +
                "\nWormholeMusic = " + str(rWormholeMusic) +
                "\nGammaMusic = " + str(rGammaMusic) +
                "\nRandomDomStrength = " + str(rRandomDomStrength) +
                "\nFederationSide = " + str(rFederationSide) +
                "\nDominionSide = " + str(rDominionSide) +
                "\nCometSelection = " + str(rCometSelection) +
                "\nDS9Planets = " + str(rDS9Planets) +
                "\nDS9NanoFX = " + str(rDS9NanoFX) +
                "\nGammaPlanets = " + str(rGammaPlanets) +
                "\nGammaNanoFX = " + str(rGammaNanoFX) +
                "\nDominionTimeSpan = " + str(rDominionTimeSpan) +
                "\nCometAlphaTrail = " + str(rCometAlphaTrail) +
                "\nCometAlphaTrailTexture = " + str(rCometAlphaTrailTexture) +
                "\nDebugMode = " + str(rDebugMode) +
                "\nDS9MapPlanetDetail = " + str(rDS9MapPlanetDetail) +
                "\nGammaMapPlanetDetail = " + str(rGammaMapPlanetDetail) +
                "\nInsideWormholeBackgroundTexture = " + str(rInsideWormholeBackgroundTexture) +
                "\nInsideWormholeModel = " + str(rInsideWormholeModel) +
                "\nStabilizeBC = " + str(rStabilizeBC) +
                "\nIntroVid = " + str(rIntroVid) +
                "\nCompletionVid = " + str(rCompletionVid))
                nt.close(file)

                reload(DS9FXUnsavedConfig)

                PlayButtonClickedSound()
                
                # Make a hack, force UMM to reload all menus themselves again
                import MainMenu.mainmenu
                MainMenu.mainmenu.SwitchMiddlePane("Configure")
                

def SaveConfig(pObject, pEvent):                
                rExcaliburSelection  = DS9FXUnsavedConfig.ExcaliburSelection
                rDefiantSelection = DS9FXUnsavedConfig.DefiantSelection
                rOregonSelection = DS9FXUnsavedConfig.OregonSelection
                rLakotaSelection = DS9FXUnsavedConfig.LakotaSelection
                rDS9Selection = DS9FXUnsavedConfig.DS9Selection
                rBugship1Selection = DS9FXUnsavedConfig.Bugship1Selection
                rBugship2Selection = DS9FXUnsavedConfig.Bugship2Selection
                rBugship3Selection = DS9FXUnsavedConfig.Bugship3Selection
                rWormholeSelection = DS9FXUnsavedConfig.WormholeSelection
                rVideoSelection = DS9FXUnsavedConfig.VideoSelection
                rModelPreloadingSelection = DS9FXUnsavedConfig.ModelPreloadingSelection
                rRandomEnemyFleetAttacks = DS9FXUnsavedConfig.RandomEnemyFleetAttacks
                rDomIS = DS9FXUnsavedConfig.DomIS
                rDS9Music = DS9FXUnsavedConfig.DS9Music
                rWormholeMusic = DS9FXUnsavedConfig.WormholeMusic 
                rGammaMusic = DS9FXUnsavedConfig.GammaMusic
                rRandomDomStrength = DS9FXUnsavedConfig.RandomDomStrength
                rFederationSide = DS9FXUnsavedConfig.FederationSide
                rDominionSide = DS9FXUnsavedConfig.DominionSide
                rCometSelection = DS9FXUnsavedConfig.CometSelection
                rDS9Planets = DS9FXUnsavedConfig.DS9Planets
                rDS9NanoFX = DS9FXUnsavedConfig.DS9NanoFX
                rGammaPlanets = DS9FXUnsavedConfig.GammaPlanets
                rGammaNanoFX = DS9FXUnsavedConfig.GammaNanoFX
                rDominionTimeSpan = DS9FXUnsavedConfig.DominionTimeSpan
                rCometAlphaTrail = DS9FXUnsavedConfig.CometAlphaTrail
                rCometAlphaTrailTexture = DS9FXUnsavedConfig.CometAlphaTrailTexture
                rDebugMode = DS9FXUnsavedConfig.DebugMode
                rDS9MapPlanetDetail = DS9FXUnsavedConfig.DS9MapPlanetDetail
                rGammaMapPlanetDetail = DS9FXUnsavedConfig.GammaMapPlanetDetail
                rInsideWormholeBackgroundTexture = DS9FXUnsavedConfig.InsideWormholeBackgroundTexture
                rInsideWormholeModel = DS9FXUnsavedConfig.InsideWormholeModel
                rStabilizeBC = DS9FXUnsavedConfig.StabilizeBC
                rIntroVid = DS9FXUnsavedConfig.IntroVid
                rCompletionVid = DS9FXUnsavedConfig.CompletionVid

                file = nt.open(Path, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
                nt.write(file, "ExcaliburSelection = " + str(rExcaliburSelection) +
                "\nDefiantSelection = " + str(rDefiantSelection) +
                "\nOregonSelection = " + str(rOregonSelection) +
                "\nLakotaSelection = " + str(rLakotaSelection) +
                "\nDS9Selection = " + str(rDS9Selection) +
                "\nBugship1Selection = " + str(rBugship1Selection) +
                "\nBugship2Selection = " + str(rBugship2Selection)+
                "\nBugship3Selection = " + str(rBugship3Selection) +
                "\nWormholeSelection = " + str(rWormholeSelection) +
                "\nVideoSelection = " + str(rVideoSelection) +
                "\nModelPreloadingSelection = " + str(rModelPreloadingSelection) +
                "\nRandomEnemyFleetAttacks = " + str(rRandomEnemyFleetAttacks) +
                "\nDomIS = " + str(rDomIS) +
                "\nDS9Music = " + str(rDS9Music) +
                "\nWormholeMusic = " + str(rWormholeMusic) +
                "\nGammaMusic = " + str(rGammaMusic) +
                "\nRandomDomStrength = " + str(rRandomDomStrength) +
                "\nFederationSide = " + str(rFederationSide) +
                "\nDominionSide = " + str(rDominionSide) +
                "\nCometSelection = " + str(rCometSelection) +
                "\nDS9Planets = " + str(rDS9Planets) +
                "\nDS9NanoFX = " + str(rDS9NanoFX) +
                "\nGammaPlanets = " + str(rGammaPlanets) +
                "\nGammaNanoFX = " + str(rGammaNanoFX) +
                "\nDominionTimeSpan = " + str(rDominionTimeSpan) +
                "\nCometAlphaTrail = " + str(rCometAlphaTrail) +
                "\nCometAlphaTrailTexture = " + str(rCometAlphaTrailTexture) +
                "\nDebugMode = " + str(rDebugMode) +
                "\nDS9MapPlanetDetail = " + str(rDS9MapPlanetDetail) +
                "\nGammaMapPlanetDetail = " + str(rGammaMapPlanetDetail) +
                "\nInsideWormholeBackgroundTexture = " + str(rInsideWormholeBackgroundTexture) +
                "\nInsideWormholeModel = " + str(rInsideWormholeModel) +
                "\nStabilizeBC = " + str(rStabilizeBC) +
                "\nIntroVid = " + str(rIntroVid) +
                "\nCompletionVid = " + str(rCompletionVid))
                nt.close(file)

                reload(DS9FXSavedConfig)

                PlayConfigSavedSound()

                # Restart notice
                from Custom.DS9FX.DS9FXPrompts import DS9FXQuitPrompt

                DS9FXQuitPrompt.Prompt()


def CorrectConfig(pObject, pEvent):
                rExcaliburSelection  = DS9FXSavedConfig.ExcaliburSelection
                rDefiantSelection = DS9FXSavedConfig.DefiantSelection
                rOregonSelection = DS9FXSavedConfig.OregonSelection
                rLakotaSelection = DS9FXSavedConfig.LakotaSelection
                rDS9Selection = DS9FXSavedConfig.DS9Selection
                rBugship1Selection = DS9FXSavedConfig.Bugship1Selection
                rBugship2Selection = DS9FXSavedConfig.Bugship2Selection
                rBugship3Selection = DS9FXSavedConfig.Bugship3Selection
                rWormholeSelection = DS9FXSavedConfig.WormholeSelection
                rVideoSelection = DS9FXSavedConfig.VideoSelection
                rModelPreloadingSelection = DS9FXSavedConfig.ModelPreloadingSelection
                rRandomEnemyFleetAttacks = DS9FXSavedConfig.RandomEnemyFleetAttacks
                rDomIS = DS9FXSavedConfig.DomIS
                rDS9Music = DS9FXSavedConfig.DS9Music
                rWormholeMusic = DS9FXSavedConfig.WormholeMusic 
                rGammaMusic = DS9FXSavedConfig.GammaMusic
                rRandomDomStrength = DS9FXSavedConfig.RandomDomStrength
                rFederationSide = DS9FXSavedConfig.FederationSide
                rDominionSide = DS9FXSavedConfig.DominionSide
                rCometSelection = DS9FXSavedConfig.CometSelection
                rDS9Planets = DS9FXSavedConfig.DS9Planets
                rDS9NanoFX = DS9FXSavedConfig.DS9NanoFX
                rGammaPlanets = DS9FXSavedConfig.GammaPlanets
                rGammaNanoFX = DS9FXSavedConfig.GammaNanoFX
                rDominionTimeSpan = DS9FXSavedConfig.DominionTimeSpan
                rCometAlphaTrail = DS9FXSavedConfig.CometAlphaTrail
                rCometAlphaTrailTexture = DS9FXSavedConfig.CometAlphaTrailTexture
                rDebugMode = DS9FXSavedConfig.DebugMode
                rDS9MapPlanetDetail = DS9FXSavedConfig.DS9MapPlanetDetail
                rGammaMapPlanetDetail = DS9FXSavedConfig.GammaMapPlanetDetail
                rInsideWormholeBackgroundTexture = DS9FXSavedConfig.InsideWormholeBackgroundTexture
                rInsideWormholeModel = DS9FXSavedConfig.InsideWormholeModel
                rStabilizeBC = DS9FXSavedConfig.StabilizeBC
                rIntroVid = DS9FXSavedConfig.IntroVid
                rCompletionVid = DS9FXSavedConfig.CompletionVid

                file = nt.open(UnsavedPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
                nt.write(file, "ExcaliburSelection = " + str(rExcaliburSelection) +
                "\nDefiantSelection = " + str(rDefiantSelection) +
                "\nOregonSelection = " + str(rOregonSelection) +
                "\nLakotaSelection = " + str(rLakotaSelection) +
                "\nDS9Selection = " + str(rDS9Selection) +
                "\nBugship1Selection = " + str(rBugship1Selection) +
                "\nBugship2Selection = " + str(rBugship2Selection)+
                "\nBugship3Selection = " + str(rBugship3Selection) +
                "\nWormholeSelection = " + str(rWormholeSelection) +
                "\nVideoSelection = " + str(rVideoSelection) +
                "\nModelPreloadingSelection = " + str(rModelPreloadingSelection) +
                "\nRandomEnemyFleetAttacks = " + str(rRandomEnemyFleetAttacks) +
                "\nDomIS = " + str(rDomIS) +
                "\nDS9Music = " + str(rDS9Music) +
                "\nWormholeMusic = " + str(rWormholeMusic) +
                "\nGammaMusic = " + str(rGammaMusic) +
                "\nRandomDomStrength = " + str(rRandomDomStrength) +
                "\nFederationSide = " + str(rFederationSide) +
                "\nDominionSide = " + str(rDominionSide) +
                "\nCometSelection = " + str(rCometSelection) +
                "\nDS9Planets = " + str(rDS9Planets) +
                "\nDS9NanoFX = " + str(rDS9NanoFX) +
                "\nGammaPlanets = " + str(rGammaPlanets) +
                "\nGammaNanoFX = " + str(rGammaNanoFX) +
                "\nDominionTimeSpan = " + str(rDominionTimeSpan) +
                "\nCometAlphaTrail = " + str(rCometAlphaTrail) +
                "\nCometAlphaTrailTexture = " + str(rCometAlphaTrailTexture) +
                "\nDebugMode = " + str(rDebugMode) +
                "\nDS9MapPlanetDetail = " + str(rDS9MapPlanetDetail) +
                "\nGammaMapPlanetDetail = " + str(rGammaMapPlanetDetail) +
                "\nInsideWormholeBackgroundTexture = " + str(rInsideWormholeBackgroundTexture) +
                "\nInsideWormholeModel = " + str(rInsideWormholeModel) +
                "\nStabilizeBC = " + str(rStabilizeBC) +
                "\nIntroVid = " + str(rIntroVid) +
                "\nCompletionVid = " + str(rCompletionVid))
                nt.close(file)

                reload(DS9FXUnsavedConfig)
                
