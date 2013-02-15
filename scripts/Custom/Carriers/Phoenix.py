# Carrier file Phoenix.py autogenerated by http://defiant.homedns.org/~erik/STBC/carrier/

Carrier = __import__("ftb.Carrier")
class Phoenix(Carrier.Carrier):
    def __init__(self, pShip):
        Carrier.Carrier.__init__(self, pShip)
        LauncherGroup = __import__("ftb.LauncherGroup")
        group = LauncherGroup.LauncherGroup()

        LauncherManager = __import__("ftb.LauncherManager")

	launcher1 = LauncherManager.GetLauncher("Shuttle Bay", pShip)
	group.AddLauncher("Shuttle Bay", launcher1)

	launcher2 = LauncherManager.GetLauncher("Shuttle Bay 2", pShip)
	group.AddLauncher("Shuttle Bay 2", launcher2)

	launcher1.AddLaunchable("Shuttle", "ftb.friendlyAI", 8)

	launcher2.AddLaunchable("type9", "ftb.friendlyAI", 2)

	self.AddLauncher("Group 1", group)

ShipManager = __import__("ftb.ShipManager")
ShipManager.RegisterShipClass("Phoenix", Phoenix)