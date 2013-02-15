import App
import GlobalPropertyTemplates

ParentPropertyScript = "ships.Hardpoints.Akira"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.Akira", globals(), locals(), ['*'])
	reload(ParentModule)

# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(22000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.500000, 0.000000)
Hull.SetPosition2D(64.000000, 50.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(10000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 1.000000, -0.250000)
ShieldGenerator.SetPosition2D(64.000000, 50.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.180000)
ShieldGenerator.SetNormalPowerPerSecond(200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 15076.923077)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 15076.923077)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 15076.923077)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 15076.923077)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 15076.923077)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 15076.923077)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 25.128206)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 25.128206)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 25.128206)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 25.128206)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 25.128206)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 25.128206)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(12000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(-0.450000, 0.700000, 0.000000)
WarpCore.SetPosition2D(64.000000, 30.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.200000)
WarpCore.SetMainBatteryLimit(150000.000000)
WarpCore.SetBackupBatteryLimit(50000.000000)
WarpCore.SetMainConduitCapacity(900.000000)
WarpCore.SetBackupConduitCapacity(100.000000)
WarpCore.SetPowerOutput(800.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(22000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 1.000000, 0.000000)
ImpulseEngines.SetPosition2D(120.000000, 120.000000)
ImpulseEngines.SetRepairComplexity(3.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.250000)
ImpulseEngines.SetNormalPowerPerSecond(75.000000)
ImpulseEngines.SetMaxAccel(27.427615)
ImpulseEngines.SetMaxAngularAccel(0.600000)
ImpulseEngines.SetMaxAngularVelocity(0.600000)
ImpulseEngines.SetMaxSpeed(13.713808)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedo Tubes")

Torpedoes.SetMaxCondition(22000.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.640000, 0.000000)
Torpedoes.SetPosition2D(82.000000, 64.000000)
Torpedoes.SetRepairComplexity(3.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.300000)
Torpedoes.SetNormalPowerPerSecond(100.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("0;Single;1234;Burst")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 400)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.FedQuantum")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
def LoadPropertySet(pObj):
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tubes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)