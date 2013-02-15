from bcdebug import debug
# Made by Lost Jedi

# Adapted for UMM purposes by USS Sovereign

pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pCometAlphaTrailTexture = pModule.CometAlphaTrailTexture


import App

def ApplyTrailToPlayer():
    # this an example of how to add a comet trail to a ship
    debug(__name__ + ", ApplyTrailToPlayer")
    pPlayer = App.Game_GetCurrentGame().GetPlayer()
    CometTrail(pPlayer)

def CreateSingleAnimated(strFile = None,iNumXFrames = None,iNumYFrames = None):
    debug(__name__ + ", CreateSingleAnimated")
    fX = 0.0
    fY = 0.0
    pContainer = App.g_kTextureAnimManager.AddContainer(strFile)
    if not pContainer:
        raise RuntimeError, "DS9FX CometFX: Couldn't access texture file at: " + str(strFile)
    else:
        pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
        for index in range(iNumXFrames * iNumYFrames):
                pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                fX = fX + (1.0 / iNumXFrames)
                if (fX == 1.0):
                        fX = 0.0
                        fY = fY + (1.0 / iNumYFrames)
    return strFile


class CometTrail:

    if pCometAlphaTrailTexture == 1:
        ## This is declared as a shared public data item of the CometTrail Class so its only loaded once
        TrailTexture = CreateSingleAnimated("scripts/Custom/DS9FX/DS9FXCometFX/GFX/Trail0.tga",8,4)

    else:
        TrailTexture = CreateSingleAnimated("scripts/Custom/DS9FX/DS9FXCometFX/GFX/Comet0.tga",8,4)


    ## Set our ship
    def __init__(self,pCometShip):

        ## A few constructors
        debug(__name__ + ", __init__")
        self.pComet = pCometShip
        self.pSequence = None

        ## Create our trails
        self.CreateTrails()

    def GetSet(self):
        debug(__name__ + ", GetSet")
        if self.pComet:
            return self.pComet.GetContainingSet()

    def AbortTrails(self):
        debug(__name__ + ", AbortTrails")
        if self.pSequence:
            self.pSequence.Destroy()
            self.pSequence = None
    
    def CreateTrails(self):
        debug(__name__ + ", CreateTrails")
        pSet = self.GetSet()

        ## Trail
	pPlayer = self.pComet
	
        ## Some Data
        pController = App.AnimTSParticleController_Create()

        ## Brightness / R / G / B
        pController.AddColorKey(0.5,   1.0,		1.0,		1.0)
        pController.AddColorKey(0.1,   0.9,		0.9,		1.0)

        
        pController.AddAlphaKey(0.0, 1.0)
        pController.AddAlphaKey(0.8, 0.6)
        pController.AddAlphaKey(1.0, 0.0)

        ## Setup Size Stuff
        pController.AddSizeKey(0.0, 1.0 * pPlayer.GetRadius() * 0.7)
        pController.AddSizeKey(1.0, 1.0 * pPlayer.GetRadius()* 2)

        ## Animation Properties
        pController.SetEmitLife(5.0)
        pController.SetEmitFrequency(0.03)
        pController.SetEffectLifeTime(999*9999)
        pController.CreateTarget(CometTrail.TrailTexture)

        ## Physics Properties
        pController.SetEmitVelocity(0.1)
        pController.SetAngleVariance(150.0)
        pController.SetEmitRadius(1.25)

        ## Alpha Blend Mode
        pController.SetTargetAlphaBlendModes(0, 7)

        ## TG Object Properties	
        pController.SetEmitFromObject(App.TGModelUtils_CastNodeToAVObject(pPlayer.GetNode()))
        pController.SetEmitPositionAndDirection(App.NiPoint3(0, 0, 0), App.NiPoint3(0, 0, 0))
        pController.SetInheritsVelocity(0)
        pController.SetDetachEmitObject(0)
        pController.AttachEffect(pSet.GetEffectRoot())

        ## Compile Effect
        pEffect = App.EffectAction_Create(pController)

        if self.pSequence:
            self.pSequence.Destroy()
            
        self.pSequence = App.TGSequence_Create()
        self.pSequence.AddAction(pEffect)
        self.pSequence.Play()
