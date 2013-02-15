import App
import GlobalPropertyTemplates

ParentPropertyScript = "ships.Hardpoints.Sovereign"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.Sovereign", globals(), locals(), ['*'])
	reload(ParentModule)

# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(28000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, -0.200000)
Hull.SetPosition2D(64.000000, 39.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.260000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(18000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.320000, 0.060000)
ShieldGenerator.SetPosition2D(9.000000, 7.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.100000)
ShieldGenerator.SetNormalPowerPerSecond(600.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 15076.923077)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 11846.153847)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 15076.923077)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 15076.923077)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 11846.153847)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 11846.153847)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 50.256411)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 39.487180)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 50.256411)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 50.256411)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 39.487180)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 39.487180)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(28000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, -0.060000, 0.010000)
ImpulseEngines.SetPosition2D(64.000000, 72.000000)
ImpulseEngines.SetRepairComplexity(3.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.100000)
ImpulseEngines.SetNormalPowerPerSecond(200.000000)
ImpulseEngines.SetMaxAccel(25.116371)
ImpulseEngines.SetMaxAngularAccel(0.600000)
ImpulseEngines.SetMaxAngularVelocity(0.600000)
ImpulseEngines.SetMaxSpeed(12.558186)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedo Tubes")

Torpedoes.SetMaxCondition(28000.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.640000, 0.000000)
Torpedoes.SetPosition2D(82.000000, 64.000000)
Torpedoes.SetRepairComplexity(3.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.300000)
Torpedoes.SetNormalPowerPerSecond(300.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("0;Single;5;Full")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 400)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.FedQuantum")
Torpedoes.SetMaxTorpedoes(1, 40)
Torpedoes.SetTorpedoScript(1, "Tactical.Projectiles.FedPhasedPlasma")
Torpedoes.SetNumAmmoTypes(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
def LoadPropertySet(pObj):
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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