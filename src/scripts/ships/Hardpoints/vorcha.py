# D:\Spiele\Bridge Commander\scripts\ships\Hardpoints\vorcha.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(12000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.800000, 0.000000)
Hull.SetPosition2D(64.000000, 60.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(6000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(-0.707087, -0.116340, -0.100000)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(4.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.200000)
ImpulseEngines.SetNormalPowerPerSecond(100.000000)
ImpulseEngines.SetMaxAccel(2.300000)
ImpulseEngines.SetMaxAngularAccel(0.400000)
ImpulseEngines.SetMaxAngularVelocity(0.600000)
ImpulseEngines.SetMaxSpeed(7.600000)
ImpulseEngines.SetEngineSound("Klingon Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(7000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.100000, -0.070000)
WarpCore.SetPosition2D(64.000000, 75.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.300000)
WarpCore.SetMainBatteryLimit(100000.000000)
WarpCore.SetBackupBatteryLimit(100000.000000)
WarpCore.SetMainConduitCapacity(900.000000)
WarpCore.SetBackupConduitCapacity(200.000000)
WarpCore.SetPowerOutput(800.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(800.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(-0.364869, 0.325853, -0.050000)
RepairSystem.SetPosition2D(44.000000, 70.000000)
RepairSystem.SetRepairComplexity(10.000000)
RepairSystem.SetDisabledPercentage(0.100000)
RepairSystem.SetRadius(0.150000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(32.000000)
RepairSystem.SetNumRepairTeams(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(7000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 2.200000, 0.150000)
SensorArray.SetPosition2D(64.000000, 25.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.750000)
SensorArray.SetRadius(0.130000)
SensorArray.SetNormalPowerPerSecond(100.000000)
SensorArray.SetBaseSensorRange(1800.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(10000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 1.100000, -0.130000)
ShieldGenerator.SetPosition2D(64.000000, 60.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.180000)
ShieldGenerator.SetNormalPowerPerSecond(250.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.866667, 0.176471, 0.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 10000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 10000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 10000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 10000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 10000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 10000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 11.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 11.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 11.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 11.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 11.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 11.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(10000.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(-0.014205, 0.909630, 0.000000)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(3.000000)
WarpEngines.SetDisabledPercentage(0.750000)
WarpEngines.SetRadius(0.200000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(4400.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 2.514620, -0.030000)
Torpedoes.SetPosition2D(57.000000, 13.000000)
Torpedoes.SetRepairComplexity(3.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.100000)
Torpedoes.SetNormalPowerPerSecond(150.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(1)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 500)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.CAKlingonTorpedoRed")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
DisruptorCannons = App.WeaponSystemProperty_Create("Disruptor Cannons")

DisruptorCannons.SetMaxCondition(8200.000000)
DisruptorCannons.SetCritical(0)
DisruptorCannons.SetTargetable(0)
DisruptorCannons.SetPrimary(1)
DisruptorCannons.SetPosition(0.000000, -0.296443, 0.250000)
DisruptorCannons.SetPosition2D(17.000000, 76.000000)
DisruptorCannons.SetRepairComplexity(3.000000)
DisruptorCannons.SetDisabledPercentage(0.750000)
DisruptorCannons.SetRadius(0.100000)
DisruptorCannons.SetNormalPowerPerSecond(150.000000)
DisruptorCannons.SetWeaponSystemType(DisruptorCannons.WST_PULSE)
DisruptorCannons.SetSingleFire(0)
DisruptorCannons.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
DisruptorCannons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorCannons)
#################################################
CloakingDevice = App.CloakingSubsystemProperty_Create("Cloaking Device")

CloakingDevice.SetMaxCondition(2000.000000)
CloakingDevice.SetCritical(0)
CloakingDevice.SetTargetable(1)
CloakingDevice.SetPrimary(1)
CloakingDevice.SetPosition(0.000000, 2.000000, -0.070000)
CloakingDevice.SetPosition2D(64.000000, 45.000000)
CloakingDevice.SetRepairComplexity(6.000000)
CloakingDevice.SetDisabledPercentage(0.750000)
CloakingDevice.SetRadius(0.200000)
CloakingDevice.SetNormalPowerPerSecond(700.000000)
CloakingDevice.SetCloakStrength(95.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingDevice)
#################################################
FwdTorpedo1 = App.TorpedoTubeProperty_Create("Fwd Torpedo 1")

FwdTorpedo1.SetMaxCondition(2200.000000)
FwdTorpedo1.SetCritical(0)
FwdTorpedo1.SetTargetable(1)
FwdTorpedo1.SetPrimary(1)
FwdTorpedo1.SetPosition(-0.050000, 2.900000, -0.030000)
FwdTorpedo1.SetPosition2D(57.000000, 13.000000)
FwdTorpedo1.SetRepairComplexity(3.000000)
FwdTorpedo1.SetDisabledPercentage(0.750000)
FwdTorpedo1.SetRadius(0.100000)
FwdTorpedo1.SetDumbfire(1)
FwdTorpedo1.SetWeaponID(0)
FwdTorpedo1.SetGroups(1)
FwdTorpedo1.SetDamageRadiusFactor(0.200000)
FwdTorpedo1.SetIconNum(370)
FwdTorpedo1.SetIconPositionX(72.000000)
FwdTorpedo1.SetIconPositionY(35.000000)
FwdTorpedo1.SetIconAboveShip(1)
FwdTorpedo1.SetImmediateDelay(0.250000)
FwdTorpedo1.SetReloadDelay(40.000000)
FwdTorpedo1.SetMaxReady(2)
FwdTorpedo1Direction = App.TGPoint3()
FwdTorpedo1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
FwdTorpedo1.SetDirection(FwdTorpedo1Direction)
FwdTorpedo1Right = App.TGPoint3()
FwdTorpedo1Right.SetXYZ(1.000000, 0.000000, 0.000000)
FwdTorpedo1.SetRight(FwdTorpedo1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdTorpedo1)
#################################################
StarCannon = App.PulseWeaponProperty_Create("Star Cannon")

StarCannon.SetMaxCondition(8600.000000)
StarCannon.SetCritical(0)
StarCannon.SetTargetable(1)
StarCannon.SetPrimary(1)
StarCannon.SetPosition(1.550000, 0.200000, -0.250000)
StarCannon.SetPosition2D(111.000000, 76.000000)
StarCannon.SetRepairComplexity(5.000000)
StarCannon.SetDisabledPercentage(0.750000)
StarCannon.SetRadius(0.100000)
StarCannon.SetDumbfire(1)
StarCannon.SetWeaponID(3)
StarCannon.SetGroups(1)
StarCannon.SetDamageRadiusFactor(0.300000)
StarCannon.SetIconNum(365)
StarCannon.SetIconPositionX(107.000000)
StarCannon.SetIconPositionY(75.000000)
StarCannon.SetIconAboveShip(1)
StarCannon.SetFireSound("Klingon Disruptor")
StarCannon.SetMaxCharge(10.000000)
StarCannon.SetMaxDamage(400.000000)
StarCannon.SetMaxDamageDistance(100.000000)
StarCannon.SetMinFiringCharge(3.000000)
StarCannon.SetNormalDischargeRate(1.000000)
StarCannon.SetRechargeRate(0.500000)
StarCannon.SetIndicatorIconNum(512)
StarCannon.SetIndicatorIconPositionX(33.000000)
StarCannon.SetIndicatorIconPositionY(71.000000)
StarCannonForward = App.TGPoint3()
StarCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannonUp = App.TGPoint3()
StarCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon.SetOrientation(StarCannonForward, StarCannonUp)
StarCannon.SetArcWidthAngles(-0.349066, 0.349066)
StarCannon.SetArcHeightAngles(-0.349066, 0.349066)
StarCannon.SetCooldownTime(0.400000)
StarCannon.SetModuleName("Tactical.Projectiles.Disruptor")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon)
#################################################
FwdTorpedo2 = App.TorpedoTubeProperty_Create("Fwd Torpedo 2")

FwdTorpedo2.SetMaxCondition(2200.000000)
FwdTorpedo2.SetCritical(0)
FwdTorpedo2.SetTargetable(1)
FwdTorpedo2.SetPrimary(1)
FwdTorpedo2.SetPosition(0.050000, 2.900000, -0.030000)
FwdTorpedo2.SetPosition2D(71.000000, 13.000000)
FwdTorpedo2.SetRepairComplexity(3.000000)
FwdTorpedo2.SetDisabledPercentage(0.750000)
FwdTorpedo2.SetRadius(0.100000)
FwdTorpedo2.SetDumbfire(1)
FwdTorpedo2.SetWeaponID(1)
FwdTorpedo2.SetGroups(1)
FwdTorpedo2.SetDamageRadiusFactor(0.200000)
FwdTorpedo2.SetIconNum(370)
FwdTorpedo2.SetIconPositionX(79.000000)
FwdTorpedo2.SetIconPositionY(35.000000)
FwdTorpedo2.SetIconAboveShip(1)
FwdTorpedo2.SetImmediateDelay(0.250000)
FwdTorpedo2.SetReloadDelay(40.000000)
FwdTorpedo2.SetMaxReady(3)
FwdTorpedo2Direction = App.TGPoint3()
FwdTorpedo2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
FwdTorpedo2.SetDirection(FwdTorpedo2Direction)
FwdTorpedo2Right = App.TGPoint3()
FwdTorpedo2Right.SetXYZ(1.000000, 0.000000, 0.000000)
FwdTorpedo2.SetRight(FwdTorpedo2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdTorpedo2)
#################################################
PortCannon = App.PulseWeaponProperty_Create("Port Cannon")

PortCannon.SetMaxCondition(8600.000000)
PortCannon.SetCritical(0)
PortCannon.SetTargetable(1)
PortCannon.SetPrimary(1)
PortCannon.SetPosition(-1.550000, 0.200000, -0.250000)
PortCannon.SetPosition2D(17.000000, 76.000000)
PortCannon.SetRepairComplexity(5.000000)
PortCannon.SetDisabledPercentage(0.750000)
PortCannon.SetRadius(0.100000)
PortCannon.SetDumbfire(1)
PortCannon.SetWeaponID(2)
PortCannon.SetGroups(1)
PortCannon.SetDamageRadiusFactor(0.300000)
PortCannon.SetIconNum(365)
PortCannon.SetIconPositionX(45.000000)
PortCannon.SetIconPositionY(75.000000)
PortCannon.SetIconAboveShip(1)
PortCannon.SetFireSound("Klingon Disruptor")
PortCannon.SetMaxCharge(10.000000)
PortCannon.SetMaxDamage(400.000000)
PortCannon.SetMaxDamageDistance(100.000000)
PortCannon.SetMinFiringCharge(3.000000)
PortCannon.SetNormalDischargeRate(1.000000)
PortCannon.SetRechargeRate(0.500000)
PortCannon.SetIndicatorIconNum(513)
PortCannon.SetIndicatorIconPositionX(96.000000)
PortCannon.SetIndicatorIconPositionY(71.000000)
PortCannonForward = App.TGPoint3()
PortCannonForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannonUp = App.TGPoint3()
PortCannonUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon.SetOrientation(PortCannonForward, PortCannonUp)
PortCannon.SetArcWidthAngles(-0.349066, 0.349066)
PortCannon.SetArcHeightAngles(-0.349066, 0.349066)
PortCannon.SetCooldownTime(0.400000)
PortCannon.SetModuleName("Tactical.Projectiles.Disruptor")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(3000.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.820000, -0.420000, -0.050000)
PortImpulse.SetPosition2D(34.000000, 84.000000)
PortImpulse.SetRepairComplexity(3.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.250000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(3000.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.820000, -0.420000, -0.050000)
StarImpulse.SetPosition2D(92.000000, 84.000000)
StarImpulse.SetRepairComplexity(3.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.250000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(5000.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-1.900000, -0.550000, -0.600000)
PortWarp.SetPosition2D(7.000000, 100.000000)
PortWarp.SetRepairComplexity(3.000000)
PortWarp.SetDisabledPercentage(0.750000)
PortWarp.SetRadius(0.600000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(5000.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(1.900000, -0.550000, -0.600000)
StarWarp.SetPosition2D(121.000000, 100.000000)
StarWarp.SetRepairComplexity(3.000000)
StarWarp.SetDisabledPercentage(0.750000)
StarWarp.SetRadius(0.600000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
AftTorpedo = App.TorpedoTubeProperty_Create("Aft Torpedo")

AftTorpedo.SetMaxCondition(2200.000000)
AftTorpedo.SetCritical(0)
AftTorpedo.SetTargetable(1)
AftTorpedo.SetPrimary(1)
AftTorpedo.SetPosition(0.000000, -0.500000, -0.030000)
AftTorpedo.SetPosition2D(64.000000, 90.000000)
AftTorpedo.SetRepairComplexity(3.000000)
AftTorpedo.SetDisabledPercentage(0.750000)
AftTorpedo.SetRadius(0.200000)
AftTorpedo.SetDumbfire(1)
AftTorpedo.SetWeaponID(2)
AftTorpedo.SetGroups(2)
AftTorpedo.SetDamageRadiusFactor(0.200000)
AftTorpedo.SetIconNum(370)
AftTorpedo.SetIconPositionX(77.000000)
AftTorpedo.SetIconPositionY(116.000000)
AftTorpedo.SetIconAboveShip(1)
AftTorpedo.SetImmediateDelay(0.250000)
AftTorpedo.SetReloadDelay(40.000000)
AftTorpedo.SetMaxReady(3)
AftTorpedoDirection = App.TGPoint3()
AftTorpedoDirection.SetXYZ(0.000000, -1.000000, 0.000000)
AftTorpedo.SetDirection(AftTorpedoDirection)
AftTorpedoRight = App.TGPoint3()
AftTorpedoRight.SetXYZ(1.000000, 0.000000, 0.000000)
AftTorpedo.SetRight(AftTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTorpedo)
#################################################
DisruptorBeams = App.WeaponSystemProperty_Create("Disruptor Beams")

DisruptorBeams.SetMaxCondition(3600.000000)
DisruptorBeams.SetCritical(0)
DisruptorBeams.SetTargetable(0)
DisruptorBeams.SetPrimary(1)
DisruptorBeams.SetPosition(-0.020195, 1.796620, 0.000000)
DisruptorBeams.SetPosition2D(64.000000, 10.000000)
DisruptorBeams.SetRepairComplexity(7.000000)
DisruptorBeams.SetDisabledPercentage(0.750000)
DisruptorBeams.SetRadius(0.100000)
DisruptorBeams.SetNormalPowerPerSecond(50.000000)
DisruptorBeams.SetWeaponSystemType(DisruptorBeams.WST_PHASER)
DisruptorBeams.SetSingleFire(1)
DisruptorBeams.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
DisruptorBeams.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(DisruptorBeams)
#################################################
Disruptor = App.PhaserProperty_Create("Disruptor")

Disruptor.SetMaxCondition(8000.000000)
Disruptor.SetCritical(0)
Disruptor.SetTargetable(1)
Disruptor.SetPrimary(1)
Disruptor.SetPosition(0.004404, 2.000000, 0.050000)
Disruptor.SetPosition2D(64.000000, 10.000000)
Disruptor.SetRepairComplexity(2.000000)
Disruptor.SetDisabledPercentage(0.750000)
Disruptor.SetRadius(0.200000)
Disruptor.SetDumbfire(0)
Disruptor.SetWeaponID(1)
Disruptor.SetGroups(0)
Disruptor.SetDamageRadiusFactor(0.180000)
Disruptor.SetIconNum(364)
Disruptor.SetIconPositionX(63.000000)
Disruptor.SetIconPositionY(23.000000)
Disruptor.SetIconAboveShip(1)
Disruptor.SetFireSound("Klingon Beam")
Disruptor.SetMaxCharge(3.000000)
Disruptor.SetMaxDamage(2000.000000)
Disruptor.SetMaxDamageDistance(60.000000)
Disruptor.SetMinFiringCharge(1.000000)
Disruptor.SetNormalDischargeRate(1.000000)
Disruptor.SetRechargeRate(1.000000)
Disruptor.SetIndicatorIconNum(510)
Disruptor.SetIndicatorIconPositionX(57.000000)
Disruptor.SetIndicatorIconPositionY(18.000000)
DisruptorForward = App.TGPoint3()
DisruptorForward.SetXYZ(0.000000, 1.000000, 0.000000)
DisruptorUp = App.TGPoint3()
DisruptorUp.SetXYZ(0.000000, 0.000000, 1.000000)
Disruptor.SetOrientation(DisruptorForward, DisruptorUp)
Disruptor.SetWidth(0.001000)
Disruptor.SetLength(0.001000)
Disruptor.SetArcWidthAngles(-0.261799, 0.261799)
Disruptor.SetArcHeightAngles(-0.959931, 0.959931)
Disruptor.SetPhaserTextureStart(16)
Disruptor.SetPhaserTextureEnd(23)
Disruptor.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.501961, 0.247059, 1.000000)
Disruptor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.000000, 1.000000)
Disruptor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 0.686275, 0.000000, 1.000000)
Disruptor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
Disruptor.SetInnerCoreColor(kColor)
Disruptor.SetNumSides(6)
Disruptor.SetMainRadius(0.150000)
Disruptor.SetTaperRadius(0.010000)
Disruptor.SetCoreScale(0.500000)
Disruptor.SetTaperRatio(0.250000)
Disruptor.SetTaperMinLength(5.000000)
Disruptor.SetTaperMaxLength(30.000000)
Disruptor.SetLengthTextureTilePerUnit(0.500000)
Disruptor.SetPerimeterTile(1.000000)
Disruptor.SetTextureSpeed(2.000000)
Disruptor.SetTextureName("data/CAKlingon.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Disruptor)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(2400.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, 0.600000, -0.200000)
Tractors.SetPosition2D(39.000000, 72.000000)
Tractors.SetRepairComplexity(7.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.250000)
Tractors.SetNormalPowerPerSecond(700.000000)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
AftTractor = App.TractorBeamProperty_Create("Aft Tractor")

AftTractor.SetMaxCondition(1200.000000)
AftTractor.SetCritical(0)
AftTractor.SetTargetable(1)
AftTractor.SetPrimary(1)
AftTractor.SetPosition(0.000000, -0.500000, 0.200000)
AftTractor.SetPosition2D(39.000000, 72.000000)
AftTractor.SetRepairComplexity(7.000000)
AftTractor.SetDisabledPercentage(0.750000)
AftTractor.SetRadius(0.150000)
AftTractor.SetDumbfire(0)
AftTractor.SetWeaponID(7)
AftTractor.SetGroups(0)
AftTractor.SetDamageRadiusFactor(0.300000)
AftTractor.SetIconNum(0)
AftTractor.SetIconPositionX(0.000000)
AftTractor.SetIconPositionY(0.000000)
AftTractor.SetIconAboveShip(1)
AftTractor.SetFireSound("Klingon Tractor")
AftTractor.SetMaxCharge(5.000000)
AftTractor.SetMaxDamage(500.000000)
AftTractor.SetMaxDamageDistance(120.000000)
AftTractor.SetMinFiringCharge(3.000000)
AftTractor.SetNormalDischargeRate(1.000000)
AftTractor.SetRechargeRate(0.300000)
AftTractor.SetIndicatorIconNum(0)
AftTractor.SetIndicatorIconPositionX(0.000000)
AftTractor.SetIndicatorIconPositionY(0.000000)
AftTractorForward = App.TGPoint3()
AftTractorForward.SetXYZ(0.000000, -1.000000, 0.000000)
AftTractorUp = App.TGPoint3()
AftTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
AftTractor.SetOrientation(AftTractorForward, AftTractorUp)
AftTractor.SetArcWidthAngles(-0.523599, 0.523599)
AftTractor.SetArcHeightAngles(-0.523599, 0.523599)
AftTractor.SetTractorBeamWidth(0.300000)
AftTractor.SetTextureStart(0)
AftTractor.SetTextureEnd(0)
AftTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetInnerCoreColor(kColor)
AftTractor.SetNumSides(12)
AftTractor.SetMainRadius(0.075000)
AftTractor.SetTaperRadius(0.000000)
AftTractor.SetCoreScale(0.450000)
AftTractor.SetTaperRatio(0.200000)
AftTractor.SetTaperMinLength(1.000000)
AftTractor.SetTaperMaxLength(5.000000)
AftTractor.SetLengthTextureTilePerUnit(0.250000)
AftTractor.SetPerimeterTile(1.000000)
AftTractor.SetTextureSpeed(0.200000)
AftTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTractor)
#################################################
Vorcha = App.ShipProperty_Create("Vorcha")

Vorcha.SetGenus(1)
Vorcha.SetSpecies(402)
Vorcha.SetMass(150.000000)
Vorcha.SetRotationalInertia(15000.000000)
Vorcha.SetShipName("Vorcha")
Vorcha.SetModelFilename("data/Models/Ships/Vorcha.nif")
Vorcha.SetDamageResolution(10.000000)
Vorcha.SetAffiliation(10)
Vorcha.SetStationary(0)
Vorcha.SetAIString("NonFedAttack")
Vorcha.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Vorcha)
#################################################
ForwardTractor = App.TractorBeamProperty_Create("Forward Tractor")

ForwardTractor.SetMaxCondition(1200.000000)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(1)
ForwardTractor.SetPrimary(1)
ForwardTractor.SetPosition(0.000000, 1.500000, -0.180000)
ForwardTractor.SetPosition2D(90.000000, 72.000000)
ForwardTractor.SetRepairComplexity(7.000000)
ForwardTractor.SetDisabledPercentage(0.750000)
ForwardTractor.SetRadius(0.200000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(7)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(0.300000)
ForwardTractor.SetIconNum(0)
ForwardTractor.SetIconPositionX(0.000000)
ForwardTractor.SetIconPositionY(0.000000)
ForwardTractor.SetIconAboveShip(1)
ForwardTractor.SetFireSound("Klingon Tractor")
ForwardTractor.SetMaxCharge(5.000000)
ForwardTractor.SetMaxDamage(500.000000)
ForwardTractor.SetMaxDamageDistance(120.000000)
ForwardTractor.SetMinFiringCharge(3.000000)
ForwardTractor.SetNormalDischargeRate(1.000000)
ForwardTractor.SetRechargeRate(0.300000)
ForwardTractor.SetIndicatorIconNum(0)
ForwardTractor.SetIndicatorIconPositionX(0.000000)
ForwardTractor.SetIndicatorIconPositionY(0.000000)
ForwardTractorForward = App.TGPoint3()
ForwardTractorForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractorUp = App.TGPoint3()
ForwardTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardTractor.SetOrientation(ForwardTractorForward, ForwardTractorUp)
ForwardTractor.SetArcWidthAngles(-0.523599, 0.523599)
ForwardTractor.SetArcHeightAngles(-1.047198, 0.000000)
ForwardTractor.SetTractorBeamWidth(0.300000)
ForwardTractor.SetTextureStart(0)
ForwardTractor.SetTextureEnd(0)
ForwardTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetInnerCoreColor(kColor)
ForwardTractor.SetNumSides(12)
ForwardTractor.SetMainRadius(0.075000)
ForwardTractor.SetTaperRadius(0.000000)
ForwardTractor.SetCoreScale(0.450000)
ForwardTractor.SetTaperRatio(0.200000)
ForwardTractor.SetTaperMinLength(1.000000)
ForwardTractor.SetTaperMaxLength(5.000000)
ForwardTractor.SetLengthTextureTilePerUnit(0.250000)
ForwardTractor.SetPerimeterTile(1.000000)
ForwardTractor.SetTextureSpeed(0.200000)
ForwardTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTractor)
#################################################
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.000000, 3.000000, 0.100000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(0.000000, -0.700000, 0.100000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
#################################################
ViewscreenLeft = App.PositionOrientationProperty_Create("ViewscreenLeft")

ViewscreenLeftForward = App.TGPoint3()
ViewscreenLeftForward.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenLeftUp = App.TGPoint3()
ViewscreenLeftUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenLeftRight = App.TGPoint3()
ViewscreenLeftRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenLeft.SetOrientation(ViewscreenLeftForward, ViewscreenLeftUp, ViewscreenLeftRight)
ViewscreenLeftPosition = App.TGPoint3()
ViewscreenLeftPosition.SetXYZ(0.000000, 3.000000, 0.100000)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(0.000000, 3.000000, 0.100000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, 3.000000, 0.100000)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.000000, 3.000000, -0.100000)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
#################################################
FirstPersonCamera = App.PositionOrientationProperty_Create("FirstPersonCamera")

FirstPersonCameraForward = App.TGPoint3()
FirstPersonCameraForward.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPersonCameraUp = App.TGPoint3()
FirstPersonCameraUp.SetXYZ(0.000000, 0.000000, 1.000000)
FirstPersonCameraRight = App.TGPoint3()
FirstPersonCameraRight.SetXYZ(1.000000, 0.000000, 0.000000)
FirstPersonCamera.SetOrientation(FirstPersonCameraForward, FirstPersonCameraUp, FirstPersonCameraRight)
FirstPersonCameraPosition = App.TGPoint3()
FirstPersonCameraPosition.SetXYZ(0.000000, 3.000000, 0.100000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
ShuttleBayOEP = App.ObjectEmitterProperty_Create("Shuttle Bay OEP")

ShuttleBayOEPForward = App.TGPoint3()
ShuttleBayOEPForward.SetXYZ(0.107309, -0.467591, -0.877407)
ShuttleBayOEPUp = App.TGPoint3()
ShuttleBayOEPUp.SetXYZ(0.034512, -0.880218, 0.473312)
ShuttleBayOEPRight = App.TGPoint3()
ShuttleBayOEPRight.SetXYZ(-0.993627, -0.081072, -0.078318)
ShuttleBayOEP.SetOrientation(ShuttleBayOEPForward, ShuttleBayOEPUp, ShuttleBayOEPRight)
ShuttleBayOEPPosition = App.TGPoint3()
ShuttleBayOEPPosition.SetXYZ(0.000000, 0.000000, 0.000000)
ShuttleBayOEP.SetPosition(ShuttleBayOEPPosition)
ShuttleBayOEP.SetEmittedObjectType(ShuttleBayOEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBayOEP)
#################################################
ShuttleBay = App.HullProperty_Create("Shuttle Bay")

ShuttleBay.SetMaxCondition(2000.000000)
ShuttleBay.SetCritical(0)
ShuttleBay.SetTargetable(1)
ShuttleBay.SetPrimary(0)
ShuttleBay.SetPosition(0.000000, 0.000000, 0.000000)
ShuttleBay.SetPosition2D(0.000000, 0.000000)
ShuttleBay.SetRepairComplexity(5.000000)
ShuttleBay.SetDisabledPercentage(0.500000)
ShuttleBay.SetRadius(0.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Beams", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Disruptor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Disruptor Cannons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Torpedo 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Torpedo 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cloaking Device", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Vorcha", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenLeft", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenRight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenUp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenDown", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FirstPersonCamera", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
