import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(1.0, 0.247059, 0.247059, 1.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(0.721568, 0.0, 0.0, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 4.2, 0.3)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.3)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.ROMPLASMAPULSE)
    return 0


def GetLaunchSpeed():
    return 36.0


def GetLaunchSound():
    return 'Romulan Pulse'


def GetPowerCost():
    return 60.0


def GetName():
    return 'Plasma Pulse'


def GetDamage():
    return 700.0


def GetGuidanceLifetime():
    return 6.0


def GetMaxAngularAccel():
    return 0.25
