# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\WarGalaxy2.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.Galaxy"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.Galaxy", globals(), locals(), ['*'])
	reload(ParentModule)
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(18000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.000000, 40.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(4.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(9000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.940000, -0.225000)
ShieldGenerator.SetPosition2D(64.000000, 40.000000)
ShieldGenerator.SetRepairComplexity(3.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.100000)
ShieldGenerator.SetNormalPowerPerSecond(1200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 10769.230469)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 8615.384766)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 10769.230469)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 10769.230469)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 8615.384766)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 8615.384766)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 17.948717)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 14.358975)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 17.948717)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 17.948717)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 14.358975)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 14.358975)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(18000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(60.000000, 60.000000)
ImpulseEngines.SetRepairComplexity(3.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.250000)
ImpulseEngines.SetNormalPowerPerSecond(1000.000000)
ImpulseEngines.SetMaxAccel(22.576542)
ImpulseEngines.SetMaxAngularAccel(0.600000)
ImpulseEngines.SetMaxAngularVelocity(0.600000)
ImpulseEngines.SetMaxSpeed(11.288271)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
TorpedoTubes = App.TorpedoSystemProperty_Create("Torpedo Tubes")

TorpedoTubes.SetMaxCondition(18000.000000)
TorpedoTubes.SetCritical(0)
TorpedoTubes.SetTargetable(0)
TorpedoTubes.SetPrimary(1)
TorpedoTubes.SetPosition(0.000000, 0.000000, 0.000000)
TorpedoTubes.SetPosition2D(64.000000, 60.000000)
TorpedoTubes.SetRepairComplexity(3.000000)
TorpedoTubes.SetDisabledPercentage(0.750000)
TorpedoTubes.SetRadius(0.200000)
TorpedoTubes.SetNormalPowerPerSecond(400.000000)
TorpedoTubes.SetWeaponSystemType(TorpedoTubes.WST_TORPEDO)
TorpedoTubes.SetSingleFire(0)
TorpedoTubes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("0;Single;5;Full")
TorpedoTubes.SetFiringChainString(kFiringChainString)
TorpedoTubes.SetMaxTorpedoes(0, 500)
TorpedoTubes.SetTorpedoScript(0, "Tactical.Projectiles.FedQuantum")
TorpedoTubes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoTubes)
#################################################
TurretF = App.TorpedoTubeProperty_Create("Turret F")

TurretF.SetMaxCondition(3500.000000)
TurretF.SetCritical(0)
TurretF.SetTargetable(1)
TurretF.SetPrimary(1)
TurretF.SetPosition(0.000000, 0.500000, -0.029000)
TurretF.SetPosition2D(49.000000, 55.000000)
TurretF.SetRepairComplexity(3.000000)
TurretF.SetDisabledPercentage(0.750000)
TurretF.SetRadius(0.050000)
TurretF.SetDumbfire(1)
TurretF.SetWeaponID(0)
TurretF.SetGroups(16)
TurretF.SetDamageRadiusFactor(0.200000)
TurretF.SetIconNum(370)
TurretF.SetIconPositionX(76.000000)
TurretF.SetIconPositionY(16)
TurretF.SetIconAboveShip(1)
TurretF.SetImmediateDelay(0.000001)
TurretF.SetReloadDelay(30.000000)
TurretF.SetMaxReady(8)
TurretFDirection = App.TGPoint3()
TurretFDirection.SetXYZ(0.000000, 1.000000, 0.000000)
TurretF.SetDirection(TurretFDirection)
TurretFRight = App.TGPoint3()
TurretFRight.SetXYZ(0.000000, 0.000000, 1.000000)
TurretF.SetRight(TurretFRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(TurretF)
#################################################
Galaxy = App.ShipProperty_Create("Galaxy")

Galaxy.SetGenus(1)
Galaxy.SetSpecies(101)
Galaxy.SetMass(325000.000000)
Galaxy.SetRotationalInertia(4875000217600.000000)
Galaxy.SetShipName("Dauntless")
Galaxy.SetModelFilename("")
Galaxy.SetDamageResolution(10.000000)
Galaxy.SetAffiliation(0)
Galaxy.SetStationary(0)
Galaxy.SetAIString("FedAttack")
Galaxy.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Galaxy)
#################################################
# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tubes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Turret F", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Galaxy", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)