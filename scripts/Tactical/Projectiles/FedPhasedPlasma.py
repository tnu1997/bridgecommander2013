import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(240.0 / 255.0, 0.0 / 255.0, 15.0 / 255.0, 1.000000)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(100.0 / 255.0, 40.0 / 255.0, 40.0 / 255.0, 1.000000)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(80.0 / 255.0, 60.0 / 255.0, 70.0 / 255.0, 1.000000)

    pTorp.CreateTorpedoModel(
                                "data/Textures/Tactical/TorpedoCore.tga",
                                kCoreColor,
                                0.2,
                                1.2,
                                "data/Textures/Tactical/TorpedoGlow.tga",
                                kGlowColor,
                                4.0,
                                1.3,
                                1.6,
                                "data/Textures/Tactical/TorpedoFlares.tga",
                                kFlareColor,
                                18,
                                0.9,
                                0.6)
    pTorp.SetDamage(3200.0)
    pTorp.SetDamageRadiusFactor(0.5)
    pTorp.SetGuidanceLifetime(75.0)
    pTorp.SetMaxAngularAccel(0.15)
    
    # Multiplayer specific stuff.  Please, if you create a new torp
    # type. modify the SpeciesToTorp.py file to add the new type.
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    
    return (0)


def GetLaunchSpeed():
    return (60.0)

def GetLaunchSound():
    return ("Phased-Plasma Torpedo")

def GetPowerCost():
    return (10.0)

def GetName():
    return ("Phased-Plasma")