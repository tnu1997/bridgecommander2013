import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(1, 1, 1, 0.95)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(0.9, 0.95, 1, 0.85)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(1, 1, 1, 1)

    pTorp.CreateTorpedoModel(
                                "data/Textures/Tactical/TorpedoCore.tga",
                                kCoreColor,
                                0.25,
                                1.2,
                                "data/Textures/Tactical/CRTorpCore.tga", 
                                kGlowColor,
                                1.0,
                                1.1,
                                1.3,
                                "data/Textures/Tactical/Dur_TorpedoFlares.tga",
                                kFlareColor,
                                24,
                                0.7,
                                0.8)
    pTorp.SetDamage(7000.0)
    pTorp.SetDamageRadiusFactor(0.40)
    pTorp.SetGuidanceLifetime(60.0)
    pTorp.SetMaxAngularAccel(0.6)
    
    # Multiplayer specific stuff.  Please, if you create a new torp
    # type. modify the SpeciesToTorp.py file to add the new type.
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    
    return (0)


def GetLaunchSpeed():
    return (75.0)

def GetLaunchSound():
    return ("Tricobalt Torpedo")

def GetPowerCost():
    return (10.0)

def GetName():
    return ("Tricobalt")