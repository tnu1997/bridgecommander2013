# C:\Users\Owner\Documents\FinalHP_Changes_Feds\pulsemine.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(6000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.007382, 0.025272, 0.073688)
Hull.SetPosition2D(50.000000, 50.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.400000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(2000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(1)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.007382, -0.024727, 0.073688)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(1.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.060000)
ImpulseEngines.SetNormalPowerPerSecond(1.000000)
ImpulseEngines.SetMaxAccel(0.000000)
ImpulseEngines.SetMaxAngularAccel(20.000000)
ImpulseEngines.SetMaxAngularVelocity(20.000000)
ImpulseEngines.SetMaxSpeed(0.000000)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(5000.000000)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.012276, 0.008244, 0.102987)
PowerPlant.SetPosition2D(65.000000, 65.000000)
PowerPlant.SetRepairComplexity(1.000000)
PowerPlant.SetDisabledPercentage(0.500000)
PowerPlant.SetRadius(0.200000)
PowerPlant.SetMainBatteryLimit(800000.000000)
PowerPlant.SetBackupBatteryLimit(400000.000000)
PowerPlant.SetMainConduitCapacity(4000.000000)
PowerPlant.SetBackupConduitCapacity(4000.000000)
PowerPlant.SetPowerOutput(1500.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(1500.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.007382, -0.024727, 0.073688)
SensorArray.SetPosition2D(35.000000, 40.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.022000)
SensorArray.SetNormalPowerPerSecond(1.000000)
SensorArray.SetBaseSensorRange(10000.000000)
SensorArray.SetMaxProbes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(120.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.013260, 0.017897, 0.091964)
ShieldGenerator.SetPosition2D(50.000000, 50.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.500000)
ShieldGenerator.SetNormalPowerPerSecond(1.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 1.000000, 1.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 5000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 12.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(2000.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.007382, -0.024727, 0.073688)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.050000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Warp = App.EngineProperty_Create("Warp")

Warp.SetMaxCondition(5000.000000)
Warp.SetCritical(0)
Warp.SetTargetable(0)
Warp.SetPrimary(1)
Warp.SetPosition(0.007382, -0.024727, 0.073688)
Warp.SetPosition2D(95.000000, 90.000000)
Warp.SetRepairComplexity(3.000000)
Warp.SetDisabledPercentage(0.750000)
Warp.SetRadius(0.025000)
Warp.SetEngineType(Warp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Warp)
#################################################
Impulse = App.EngineProperty_Create("Impulse")

Impulse.SetMaxCondition(50.000000)
Impulse.SetCritical(0)
Impulse.SetTargetable(1)
Impulse.SetPrimary(1)
Impulse.SetPosition(0.007382, -0.024727, 0.073688)
Impulse.SetPosition2D(80.000000, 75.000000)
Impulse.SetRepairComplexity(1.000000)
Impulse.SetDisabledPercentage(0.500000)
Impulse.SetRadius(0.020000)
Impulse.SetEngineType(Impulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse)
#################################################
PulseMine = App.ShipProperty_Create("PulseMine")

PulseMine.SetGenus(1)
PulseMine.SetSpecies(151)
PulseMine.SetMass(1000.000000)
PulseMine.SetRotationalInertia(900.000000)
PulseMine.SetShipName("PulseMine")
PulseMine.SetModelFilename("data/Models/Misc/asteroid.nif")
PulseMine.SetDamageResolution(10.000000)
PulseMine.SetAffiliation(0)
PulseMine.SetStationary(0)
PulseMine.SetAIString("NonFedAttack")
PulseMine.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(PulseMine)
#################################################
CLOAK = App.CloakingSubsystemProperty_Create("CLOAK")

CLOAK.SetMaxCondition(2000.000000)
CLOAK.SetCritical(0)
CLOAK.SetTargetable(1)
CLOAK.SetPrimary(1)
CLOAK.SetPosition(0.013043, 0.017089, 0.051230)
CLOAK.SetPosition2D(0.000000, 0.000000)
CLOAK.SetRepairComplexity(1.000000)
CLOAK.SetDisabledPercentage(0.500000)
CLOAK.SetRadius(0.010000)
CLOAK.SetNormalPowerPerSecond(1.000000)
CLOAK.SetCloakStrength(500.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CLOAK)
#################################################
pulseweapon = App.PulseWeaponProperty_Create("pulseweapon")

pulseweapon.SetMaxCondition(2000.000000)
pulseweapon.SetCritical(0)
pulseweapon.SetTargetable(1)
pulseweapon.SetPrimary(1)
pulseweapon.SetPosition(-0.484326, 0.367851, 0.011410)
pulseweapon.SetPosition2D(0.000000, 0.000000)
pulseweapon.SetRepairComplexity(1.000000)
pulseweapon.SetDisabledPercentage(0.500000)
pulseweapon.SetRadius(0.250000)
pulseweapon.SetDumbfire(1)
pulseweapon.SetWeaponID(0)
pulseweapon.SetGroups(0)
pulseweapon.SetDamageRadiusFactor(0.400000)
pulseweapon.SetIconNum(0)
pulseweapon.SetIconPositionX(0.000000)
pulseweapon.SetIconPositionY(0.000000)
pulseweapon.SetIconAboveShip(1)
pulseweapon.SetFireSound("pulsemine")
pulseweapon.SetMaxCharge(5.000000)
pulseweapon.SetMaxDamage(500.000000)
pulseweapon.SetMaxDamageDistance(300.000000)
pulseweapon.SetMinFiringCharge(3.000000)
pulseweapon.SetNormalDischargeRate(1.000000)
pulseweapon.SetRechargeRate(50.000000)
pulseweapon.SetIndicatorIconNum(0)
pulseweapon.SetIndicatorIconPositionX(0.000000)
pulseweapon.SetIndicatorIconPositionY(0.000000)
pulseweaponForward = App.TGPoint3()
pulseweaponForward.SetXYZ(-0.771370, 0.623373, 0.128046)
pulseweaponUp = App.TGPoint3()
pulseweaponUp.SetXYZ(-0.139858, 0.030234, -0.989710)
pulseweapon.SetOrientation(pulseweaponForward, pulseweaponUp)
pulseweapon.SetArcWidthAngles(-0.357190, 0.357190)
pulseweapon.SetArcHeightAngles(-0.357190, 0.357190)
pulseweapon.SetCooldownTime(0.000000)
pulseweapon.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(pulseweapon)
#################################################
pulsesystem = App.WeaponSystemProperty_Create("pulsesystem")

pulsesystem.SetMaxCondition(2000.000000)
pulsesystem.SetCritical(0)
pulsesystem.SetTargetable(1)
pulsesystem.SetPrimary(1)
pulsesystem.SetPosition(0.000000, 0.000000, 0.000000)
pulsesystem.SetPosition2D(0.000000, 0.000000)
pulsesystem.SetRepairComplexity(1.000000)
pulsesystem.SetDisabledPercentage(0.500000)
pulsesystem.SetRadius(0.250000)
pulsesystem.SetNormalPowerPerSecond(1.000000)
pulsesystem.SetWeaponSystemType(pulsesystem.WST_PULSE)
pulsesystem.SetSingleFire(1)
pulsesystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
pulsesystem.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(pulsesystem)
#################################################
p2 = App.PulseWeaponProperty_Create("p2")

p2.SetMaxCondition(200.000000)
p2.SetCritical(0)
p2.SetTargetable(1)
p2.SetPrimary(1)
p2.SetPosition(-0.605318, 0.056406, 0.006192)
p2.SetPosition2D(0.000000, 0.000000)
p2.SetRepairComplexity(1.000000)
p2.SetDisabledPercentage(0.500000)
p2.SetRadius(0.250000)
p2.SetDumbfire(1)
p2.SetWeaponID(0)
p2.SetGroups(0)
p2.SetDamageRadiusFactor(0.300000)
p2.SetIconNum(0)
p2.SetIconPositionX(0.000000)
p2.SetIconPositionY(0.000000)
p2.SetIconAboveShip(1)
p2.SetFireSound("pulsemine")
p2.SetMaxCharge(5.000000)
p2.SetMaxDamage(500.000000)
p2.SetMaxDamageDistance(300.000000)
p2.SetMinFiringCharge(3.000000)
p2.SetNormalDischargeRate(1.000000)
p2.SetRechargeRate(50.000000)
p2.SetIndicatorIconNum(0)
p2.SetIndicatorIconPositionX(0.000000)
p2.SetIndicatorIconPositionY(0.000000)
p2Forward = App.TGPoint3()
p2Forward.SetXYZ(-0.999808, -0.003464, 0.019271)
p2Up = App.TGPoint3()
p2Up.SetXYZ(-0.019371, 0.031364, -0.999320)
p2.SetOrientation(p2Forward, p2Up)
p2.SetArcWidthAngles(-0.357094, 0.357094)
p2.SetArcHeightAngles(-0.357094, 0.357094)
p2.SetCooldownTime(0.000000)
p2.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p2)
#################################################
p3 = App.PulseWeaponProperty_Create("p3")

p3.SetMaxCondition(200.000000)
p3.SetCritical(0)
p3.SetTargetable(1)
p3.SetPrimary(1)
p3.SetPosition(-0.318947, -0.482352, -0.007784)
p3.SetPosition2D(0.000000, 0.000000)
p3.SetRepairComplexity(1.000000)
p3.SetDisabledPercentage(0.500000)
p3.SetRadius(0.250000)
p3.SetDumbfire(1)
p3.SetWeaponID(0)
p3.SetGroups(0)
p3.SetDamageRadiusFactor(0.300000)
p3.SetIconNum(0)
p3.SetIconPositionX(0.000000)
p3.SetIconPositionY(0.000000)
p3.SetIconAboveShip(1)
p3.SetFireSound("pulsemine")
p3.SetMaxCharge(5.000000)
p3.SetMaxDamage(500.000000)
p3.SetMaxDamageDistance(300.000000)
p3.SetMinFiringCharge(3.000000)
p3.SetNormalDischargeRate(1.000000)
p3.SetRechargeRate(50.000000)
p3.SetIndicatorIconNum(0)
p3.SetIndicatorIconPositionX(0.000000)
p3.SetIndicatorIconPositionY(0.000000)
p3Forward = App.TGPoint3()
p3Forward.SetXYZ(-0.341298, -0.939934, 0.006269)
p3Up = App.TGPoint3()
p3Up.SetXYZ(-0.093002, 0.027131, -0.995296)
p3.SetOrientation(p3Forward, p3Up)
p3.SetArcWidthAngles(-0.357094, 0.357094)
p3.SetArcHeightAngles(-0.357094, 0.357094)
p3.SetCooldownTime(0.000000)
p3.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p3)
#################################################
p4 = App.PulseWeaponProperty_Create("p4")

p4.SetMaxCondition(200.000000)
p4.SetCritical(0)
p4.SetTargetable(1)
p4.SetPrimary(1)
p4.SetPosition(-0.030975, -0.572715, -0.001722)
p4.SetPosition2D(0.000000, 0.000000)
p4.SetRepairComplexity(1.000000)
p4.SetDisabledPercentage(0.500000)
p4.SetRadius(0.250000)
p4.SetDumbfire(1)
p4.SetWeaponID(0)
p4.SetGroups(0)
p4.SetDamageRadiusFactor(0.300000)
p4.SetIconNum(0)
p4.SetIconPositionX(0.000000)
p4.SetIconPositionY(0.000000)
p4.SetIconAboveShip(1)
p4.SetFireSound("pulsemine")
p4.SetMaxCharge(5.000000)
p4.SetMaxDamage(500.000000)
p4.SetMaxDamageDistance(300.000000)
p4.SetMinFiringCharge(3.000000)
p4.SetNormalDischargeRate(1.000000)
p4.SetRechargeRate(50.000000)
p4.SetIndicatorIconNum(0)
p4.SetIndicatorIconPositionX(0.000000)
p4.SetIndicatorIconPositionY(0.000000)
p4Forward = App.TGPoint3()
p4Forward.SetXYZ(0.295064, -0.953555, 0.060584)
p4Up = App.TGPoint3()
p4Up.SetXYZ(-0.172646, -0.115573, -0.978180)
p4.SetOrientation(p4Forward, p4Up)
p4.SetArcWidthAngles(-0.357094, 0.357094)
p4.SetArcHeightAngles(-0.357094, 0.357094)
p4.SetCooldownTime(0.000000)
p4.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p4)
#################################################
p5 = App.PulseWeaponProperty_Create("p5")

p5.SetMaxCondition(200.000000)
p5.SetCritical(0)
p5.SetTargetable(1)
p5.SetPrimary(1)
p5.SetPosition(0.241261, -0.514056, 0.000285)
p5.SetPosition2D(0.000000, 0.000000)
p5.SetRepairComplexity(1.000000)
p5.SetDisabledPercentage(0.500000)
p5.SetRadius(0.250000)
p5.SetDumbfire(1)
p5.SetWeaponID(0)
p5.SetGroups(0)
p5.SetDamageRadiusFactor(0.300000)
p5.SetIconNum(0)
p5.SetIconPositionX(0.000000)
p5.SetIconPositionY(0.000000)
p5.SetIconAboveShip(1)
p5.SetFireSound("pulsemine")
p5.SetMaxCharge(5.000000)
p5.SetMaxDamage(500.000000)
p5.SetMaxDamageDistance(300.000000)
p5.SetMinFiringCharge(3.000000)
p5.SetNormalDischargeRate(1.000000)
p5.SetRechargeRate(50.000000)
p5.SetIndicatorIconNum(0)
p5.SetIndicatorIconPositionX(0.000000)
p5.SetIndicatorIconPositionY(0.000000)
p5Forward = App.TGPoint3()
p5Forward.SetXYZ(0.663744, -0.741431, 0.098613)
p5Up = App.TGPoint3()
p5Up.SetXYZ(-0.148004, -0.259430, -0.954354)
p5.SetOrientation(p5Forward, p5Up)
p5.SetArcWidthAngles(-0.357094, 0.357094)
p5.SetArcHeightAngles(-0.357094, 0.357094)
p5.SetCooldownTime(0.000000)
p5.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p5)
#################################################
p6 = App.PulseWeaponProperty_Create("p6")

p6.SetMaxCondition(200.000000)
p6.SetCritical(0)
p6.SetTargetable(1)
p6.SetPrimary(1)
p6.SetPosition(0.434081, -0.365229, 0.005960)
p6.SetPosition2D(0.000000, 0.000000)
p6.SetRepairComplexity(1.000000)
p6.SetDisabledPercentage(0.500000)
p6.SetRadius(0.250000)
p6.SetDumbfire(1)
p6.SetWeaponID(0)
p6.SetGroups(0)
p6.SetDamageRadiusFactor(0.300000)
p6.SetIconNum(0)
p6.SetIconPositionX(0.000000)
p6.SetIconPositionY(0.000000)
p6.SetIconAboveShip(1)
p6.SetFireSound("pulsemine")
p6.SetMaxCharge(5.000000)
p6.SetMaxDamage(500.000000)
p6.SetMaxDamageDistance(300.000000)
p6.SetMinFiringCharge(3.000000)
p6.SetNormalDischargeRate(1.000000)
p6.SetRechargeRate(50.000000)
p6.SetIndicatorIconNum(0)
p6.SetIndicatorIconPositionX(0.000000)
p6.SetIndicatorIconPositionY(0.000000)
p6Forward = App.TGPoint3()
p6Forward.SetXYZ(0.756972, -0.650319, 0.063873)
p6Up = App.TGPoint3()
p6Up.SetXYZ(-0.084688, -0.194560, -0.977228)
p6.SetOrientation(p6Forward, p6Up)
p6.SetArcWidthAngles(-0.357094, 0.357094)
p6.SetArcHeightAngles(-0.357094, 0.357094)
p6.SetCooldownTime(0.000000)
p6.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p6)
#################################################
p7 = App.PulseWeaponProperty_Create("p7")

p7.SetMaxCondition(200.000000)
p7.SetCritical(0)
p7.SetTargetable(1)
p7.SetPrimary(1)
p7.SetPosition(0.571683, -0.057851, 0.001976)
p7.SetPosition2D(0.000000, 0.000000)
p7.SetRepairComplexity(1.000000)
p7.SetDisabledPercentage(0.500000)
p7.SetRadius(0.250000)
p7.SetDumbfire(1)
p7.SetWeaponID(0)
p7.SetGroups(0)
p7.SetDamageRadiusFactor(0.300000)
p7.SetIconNum(0)
p7.SetIconPositionX(0.000000)
p7.SetIconPositionY(0.000000)
p7.SetIconAboveShip(1)
p7.SetFireSound("pulsemine")
p7.SetMaxCharge(5.000000)
p7.SetMaxDamage(500.000000)
p7.SetMaxDamageDistance(300.000000)
p7.SetMinFiringCharge(3.000000)
p7.SetNormalDischargeRate(1.000000)
p7.SetRechargeRate(50.000000)
p7.SetIndicatorIconNum(0)
p7.SetIndicatorIconPositionX(0.000000)
p7.SetIndicatorIconPositionY(0.000000)
p7Forward = App.TGPoint3()
p7Forward.SetXYZ(0.976170, 0.211730, -0.047557)
p7Up = App.TGPoint3()
p7Up.SetXYZ(-0.058547, 0.045945, -0.997227)
p7.SetOrientation(p7Forward, p7Up)
p7.SetArcWidthAngles(-0.357094, 0.357094)
p7.SetArcHeightAngles(-0.357094, 0.357094)
p7.SetCooldownTime(0.000000)
p7.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p7)
#################################################
p8 = App.PulseWeaponProperty_Create("p8")

p8.SetMaxCondition(200.000000)
p8.SetCritical(0)
p8.SetTargetable(1)
p8.SetPrimary(1)
p8.SetPosition(0.540693, 0.223250, 0.002045)
p8.SetPosition2D(0.000000, 0.000000)
p8.SetRepairComplexity(1.000000)
p8.SetDisabledPercentage(0.500000)
p8.SetRadius(0.250000)
p8.SetDumbfire(1)
p8.SetWeaponID(0)
p8.SetGroups(0)
p8.SetDamageRadiusFactor(0.300000)
p8.SetIconNum(0)
p8.SetIconPositionX(0.000000)
p8.SetIconPositionY(0.000000)
p8.SetIconAboveShip(1)
p8.SetFireSound("pulsemine")
p8.SetMaxCharge(5.000000)
p8.SetMaxDamage(500.000000)
p8.SetMaxDamageDistance(300.000000)
p8.SetMinFiringCharge(3.000000)
p8.SetNormalDischargeRate(1.000000)
p8.SetRechargeRate(50.000000)
p8.SetIndicatorIconNum(0)
p8.SetIndicatorIconPositionX(0.000000)
p8.SetIndicatorIconPositionY(0.000000)
p8Forward = App.TGPoint3()
p8Forward.SetXYZ(0.905853, 0.423483, -0.009623)
p8Up = App.TGPoint3()
p8Up.SetXYZ(-0.044031, 0.071545, -0.996465)
p8.SetOrientation(p8Forward, p8Up)
p8.SetArcWidthAngles(-0.357094, 0.357094)
p8.SetArcHeightAngles(-0.357094, 0.357094)
p8.SetCooldownTime(0.000000)
p8.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p8)
#################################################
p9 = App.PulseWeaponProperty_Create("p9")

p9.SetMaxCondition(200.000000)
p9.SetCritical(0)
p9.SetTargetable(1)
p9.SetPrimary(1)
p9.SetPosition(0.323116, 0.501906, 0.006638)
p9.SetPosition2D(0.000000, 0.000000)
p9.SetRepairComplexity(1.000000)
p9.SetDisabledPercentage(0.500000)
p9.SetRadius(0.250000)
p9.SetDumbfire(1)
p9.SetWeaponID(0)
p9.SetGroups(0)
p9.SetDamageRadiusFactor(0.300000)
p9.SetIconNum(0)
p9.SetIconPositionX(0.000000)
p9.SetIconPositionY(0.000000)
p9.SetIconAboveShip(1)
p9.SetFireSound("pulsemine")
p9.SetMaxCharge(5.000000)
p9.SetMaxDamage(500.000000)
p9.SetMaxDamageDistance(300.000000)
p9.SetMinFiringCharge(3.000000)
p9.SetNormalDischargeRate(1.000000)
p9.SetRechargeRate(50.000000)
p9.SetIndicatorIconNum(0)
p9.SetIndicatorIconPositionX(0.000000)
p9.SetIndicatorIconPositionY(0.000000)
p9Forward = App.TGPoint3()
p9Forward.SetXYZ(0.499296, 0.863049, 0.076482)
p9Up = App.TGPoint3()
p9Up.SetXYZ(0.000294, 0.088105, -0.996111)
p9.SetOrientation(p9Forward, p9Up)
p9.SetArcWidthAngles(-0.357094, 0.357094)
p9.SetArcHeightAngles(-0.357094, 0.357094)
p9.SetCooldownTime(0.000000)
p9.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p9)
#################################################
p10 = App.PulseWeaponProperty_Create("p10")

p10.SetMaxCondition(200.000000)
p10.SetCritical(0)
p10.SetTargetable(1)
p10.SetPrimary(1)
p10.SetPosition(0.001941, 0.609949, 0.007541)
p10.SetPosition2D(0.000000, 0.000000)
p10.SetRepairComplexity(1.000000)
p10.SetDisabledPercentage(0.500000)
p10.SetRadius(0.250000)
p10.SetDumbfire(1)
p10.SetWeaponID(0)
p10.SetGroups(0)
p10.SetDamageRadiusFactor(0.300000)
p10.SetIconNum(0)
p10.SetIconPositionX(0.000000)
p10.SetIconPositionY(0.000000)
p10.SetIconAboveShip(1)
p10.SetFireSound("pulsemine")
p10.SetMaxCharge(5.000000)
p10.SetMaxDamage(500.000000)
p10.SetMaxDamageDistance(300.000000)
p10.SetMinFiringCharge(3.000000)
p10.SetNormalDischargeRate(1.000000)
p10.SetRechargeRate(50.000000)
p10.SetIndicatorIconNum(0)
p10.SetIndicatorIconPositionX(0.000000)
p10.SetIndicatorIconPositionY(0.000000)
p10Forward = App.TGPoint3()
p10Forward.SetXYZ(0.065470, 0.980130, 0.187239)
p10Up = App.TGPoint3()
p10Up.SetXYZ(-0.003516, 0.187868, -0.982188)
p10.SetOrientation(p10Forward, p10Up)
p10.SetArcWidthAngles(-0.357094, 0.357094)
p10.SetArcHeightAngles(-0.357094, 0.357094)
p10.SetCooldownTime(0.000000)
p10.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(p10)
#################################################
REPAIRSYSTEM = App.RepairSubsystemProperty_Create("REPAIR SYSTEM")

REPAIRSYSTEM.SetMaxCondition(200.000000)
REPAIRSYSTEM.SetCritical(0)
REPAIRSYSTEM.SetTargetable(1)
REPAIRSYSTEM.SetPrimary(1)
REPAIRSYSTEM.SetPosition(0.000000, 0.000000, 0.000000)
REPAIRSYSTEM.SetPosition2D(0.000000, 0.000000)
REPAIRSYSTEM.SetRepairComplexity(1.000000)
REPAIRSYSTEM.SetDisabledPercentage(0.500000)
REPAIRSYSTEM.SetRadius(0.250000)
REPAIRSYSTEM.SetNormalPowerPerSecond(1.000000)
REPAIRSYSTEM.SetMaxRepairPoints(100.000000)
REPAIRSYSTEM.SetNumRepairTeams(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(REPAIRSYSTEM)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("PulseMine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("pulseweapon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("pulsesystem", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p5", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p6", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p7", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p8", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p9", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("p10", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("REPAIR SYSTEM", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
