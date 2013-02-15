from bcdebug import debug
# by USS Sovereign, create a nice flash effect from DS9 Series

# Imports
import App
import Foundation


# Path to the GFX folder
GFX = 'scripts/Custom/DS9FX/DS9FXWormholeFlash/GFX/'

# Load the GFX
def StartGFX():
                debug(__name__ + ", StartGFX")
                LoadGfx(4,4,GFX)

# Create these textures on the ship
def CreateGFX(pShip):
                # First basic stuff we define where where from we'll emmit those textures etc.
		debug(__name__ + ", CreateGFX")
		pAttachTo = pShip.GetNode()
		fSize     = 700
		pSequence = App.TGSequence_Create()	
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

                # Setup some needed values
                sFile = ChooseRandomTexture()
                fLifeTime = 1
                fRed = 255.0
                fGreen = 255.0
                fBlue = 255.0
                fBrightness = 0.8
                fSpeed = 1

                # We start creating the effect, also very similar to the code from effects.py                
		pEffect = App.AnimTSParticleController_Create()
		pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddAlphaKey(0.0, 1.0)
		pEffect.AddAlphaKey(1.0, 1.0)
		pEffect.AddSizeKey(0.0, fSize)
		pEffect.AddSizeKey(1.0, fSize)
		
                pEffect.SetEmitLife(fSpeed)
                pEffect.SetEmitFrequency(1)
                pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
                pEffect.SetInheritsVelocity(0)
                pEffect.SetDetachEmitObject(0)
                pEffect.CreateTarget(sFile)
                pEffect.SetTargetAlphaBlendModes(0, 7)
                pEffect.SetEmitFromObject(pEmitFrom)
                pEffect.AttachEffect(pAttachTo)                
                Effect = App.EffectAction_Create(pEffect)
                pSequence.AddAction(Effect)
                pSequence.Play ()
                
                return

# Support for multiple textures, thanks LJ ;)
def ChooseRandomTexture():
                debug(__name__ + ", ChooseRandomTexture")
                iRandom = App.g_kSystemWrapper.GetRandomNumber(len(Foundation.GetFileNames(GFX, 'tga')))
                strFile = GFX + "Flash" + str(iRandom) + ".tga"
                
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

                
