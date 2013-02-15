from bcdebug import debug
# by USS Sovereign we introduce for the first time in BC the famous Comet Alpha

pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pCometAlphaTrailTexture = pModule.CometAlphaTrailTexture

# Imports
import App
import Foundation


# Path to the GFX folder
GFX = 'scripts/Custom/DS9FX/DS9FXCometFX/GFX/'
GFX2 = 'scripts/Custom/DS9FX/DS9FXCometFX/GFX/'

# Load the GFX
def StartGFX():
                # We need LoadGfx functions for each option
                debug(__name__ + ", StartGFX")
                LoadGfx(8,4,GFX)
                LoadGfx2(8,4,GFX2)

# Create these textures on the ship
def CreateGFX(pShip):
                # First basic stuff we define where where from we'll emmit those textures etc.
		debug(__name__ + ", CreateGFX")
		pAttachTo = pShip.GetNode()
		fSize     = 1
		pSequence = App.TGSequence_Create()	
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

		# Emiting direction and position
		vEmitDir = pShip.GetWorldUpTG()
                vEmitPos = pShip.GetHull().GetPosition()

                # Setup some needed values
                # Choose the proper Texture
                if pCometAlphaTrailTexture == 1:
                    sFile = ChooseRandomTexture2()

                else:
                    sFile = ChooseRandomTexture()
                    
                fLifeTime = 999*9999 # simulating endless effect, nobody plays BC that long LOL
                fRed = 255.0
                fGreen = 255.0
                fBlue = 255.0
                fBrightness = 0.8
                fSpeed = 1
                fVelocity = 0.2
                    
                # We start creating the effect, also very similar to the code from effects.py                
                pEffect = App.AnimTSParticleController_Create()
                pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
                pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
                pEffect.AddAlphaKey(0.0, 1.0)
                pEffect.AddAlphaKey(1.0, 1.0)
                pEffect.AddSizeKey(0.0, fSize)
                pEffect.AddSizeKey(1.0, fSize)

                pEffect.SetEmitVelocity(fVelocity)
                pEffect.SetAngleVariance(1.0)
                pEffect.SetEmitRadius(10)
                pEffect.SetEmitLife(fSpeed)
                pEffect.SetEmitFrequency(0.03)
                pEffect.SetInheritsVelocity(0)
                pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
                pEffect.CreateTarget(sFile)
                pEffect.SetEmitFromObject(pEmitFrom)
                pEffect.SetEmitPositionAndDirection(vEmitPos, vEmitDir)
                pEffect.SetDetachEmitObject(0)
                pEffect.AttachEffect(pAttachTo)    
                pEffect.SetTargetAlphaBlendModes(0, 7)                                
                                
                Effect1 = App.EffectAction_Create(pEffect)
                Effect2 = App.EffectAction_Create(pEffect) 
                pSequence.AddAction(Effect1)
                pSequence.AddAction(Effect2)  
                pSequence.Play ()
                    
                return

# Support for multiple textures, thanks LJ ;)
def ChooseRandomTexture():
                debug(__name__ + ", ChooseRandomTexture")
                iRandom = App.g_kSystemWrapper.GetRandomNumber(len(Foundation.GetFileNames(GFX, 'tga')))
                strFile = GFX + "Comet" + str(iRandom) + ".tga"
                
                return strFile

# Support for multiple textures, thanks LJ ;)
def ChooseRandomTexture2():
                debug(__name__ + ", ChooseRandomTexture2")
                iRandom = App.g_kSystemWrapper.GetRandomNumber(len(Foundation.GetFileNames(GFX2, 'tga')))
                strFile = GFX2 + "Trail" + str(iRandom) + ".tga"
                
                return strFile
            

# Load textures
def LoadGfx(iNumXFrames, iNumYFrames, Folder):
                debug(__name__ + ", LoadGfx")
                FileNames = Foundation.GetFileNames(Folder, 'tga')       

                for loadIndex in FileNames:
                        strFile = Folder + str(loadIndex)
                        fX = 0.0
                        fY = 0.0

                        pContainer = App.g_kTextureAnimManager.AddContainer(strFile)   
                        pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
                        for index in range(iNumXFrames * iNumYFrames):
                                pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                                fX = fX + (1.0 / iNumXFrames)

                                if (fX == 1.0):
                                        fX = 0.0
                                        fY = fY + (1.0 / iNumYFrames)

# Load textures
def LoadGfx2(iNumXFrames, iNumYFrames, Folder):
                debug(__name__ + ", LoadGfx2")
                FileNames = Foundation.GetFileNames(Folder, 'tga')       

                for loadIndex in FileNames:
                        strFile = Folder + str(loadIndex)
                        fX = 0.0
                        fY = 0.0

                        pContainer = App.g_kTextureAnimManager.AddContainer(strFile)   
                        pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
                        for index in range(iNumXFrames * iNumYFrames):
                                pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                                fX = fX + (1.0 / iNumXFrames)

                                if (fX == 1.0):
                                        fX = 0.0
                                        fY = fY + (1.0 / iNumYFrames)
  
