import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(25.0 / 255.0, 25.0 / 255.0, 50.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(50.0 / 255.0, 50.0 / 255.0, 100.0 / 255.0, 1.0)

    pTorp.CreateTorpedoModel(
                                "data/Textures/Tactical/TorpedoCore.tga",
                                kCoreColor,
                                0.2,
                                1.2,
                                "data/Textures/Tactical/TorpedoGlow.tga",
                                kGlowColor,
                                2.0,
                                1.4,
                                1.8,
                                "data/Textures/Tactical/TorpedoFlares.tga",
                                kFlareColor,
                                40,
                                0.7,
                                0.3)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.35)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime( GetLifetime() )

    # Multiplayer specific stuff.  Please, if you create a new torp
    # type. modify the SpeciesToTorp.py file to add the new type.
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    
    return (0)


def GetLaunchSpeed():
    return (45.0)

def GetLaunchSound():
    return ("Quantum Torpedo")

def GetPowerCost():
    return (10.0)

def GetName():
    return ("Quantum")

def GetDamage():
    return 1750.0

def GetGuidanceLifetime():
    return 45.0

def GetMaxAngularAccel():
    return 0.5

def GetLifetime():
	return 45.0

def GetFlashColor():
	return (25.0, 25.0, 50.0)