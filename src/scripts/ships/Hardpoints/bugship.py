# C:\Users\Owner\Documents\FinalHP_Changes_Jem'Hadar\bugship.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(5000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.000000, 60.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(4000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(-0.004454, -0.460570, 0.027654)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(4.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.060000)
ImpulseEngines.SetNormalPowerPerSecond(100.000000)
ImpulseEngines.SetMaxAccel(6.000000)
ImpulseEngines.SetMaxAngularAccel(0.800000)
ImpulseEngines.SetMaxAngularVelocity(0.800000)
ImpulseEngines.SetMaxSpeed(11.000000)
ImpulseEngines.SetEngineSound("Klingon Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(3000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000393, -0.384610, 0.080335)
WarpCore.SetPosition2D(64.000000, 75.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.040000)
WarpCore.SetMainBatteryLimit(100000.000000)
WarpCore.SetBackupBatteryLimit(100000.000000)
WarpCore.SetMainConduitCapacity(1000.000000)
WarpCore.SetBackupConduitCapacity(500.000000)
WarpCore.SetPowerOutput(1000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(800.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, -0.054646, 0.110000)
RepairSystem.SetPosition2D(44.000000, 70.000000)
RepairSystem.SetRepairComplexity(10.000000)
RepairSystem.SetDisabledPercentage(0.100000)
RepairSystem.SetRadius(0.060000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(30.000000)
RepairSystem.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(4000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.001533, 0.325334, -0.010000)
SensorArray.SetPosition2D(64.000000, 25.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.750000)
SensorArray.SetRadius(0.100000)
SensorArray.SetNormalPowerPerSecond(100.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(3000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(-0.001717, 0.071949, 0.171682)
ShieldGenerator.SetPosition2D(64.000000, 60.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.050000)
ShieldGenerator.SetNormalPowerPerSecond(250.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(1.000000, 0.000000, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 6000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 1000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 3000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 6000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 6000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 6000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 12.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(5000.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, -0.262486, 0.059276)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(3.000000)
WarpEngines.SetDisabledPercentage(0.750000)
WarpEngines.SetRadius(0.060000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(4400.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.001533, 0.325334, -0.010000)
Torpedoes.SetPosition2D(57.000000, 13.000000)
Torpedoes.SetRepairComplexity(3.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.100000)
Torpedoes.SetNormalPowerPerSecond(150.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("0;Single;1;Dual")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 60)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.PoleronJLH")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
ForwardTorpedo1 = App.TorpedoTubeProperty_Create("Forward Torpedo 1")

ForwardTorpedo1.SetMaxCondition(1000.000000)
ForwardTorpedo1.SetCritical(0)
ForwardTorpedo1.SetTargetable(1)
ForwardTorpedo1.SetPrimary(1)
ForwardTorpedo1.SetPosition(-0.026748, 0.487110, -0.011673)
ForwardTorpedo1.SetPosition2D(57.000000, 13.000000)
ForwardTorpedo1.SetRepairComplexity(5.000000)
ForwardTorpedo1.SetDisabledPercentage(0.750000)
ForwardTorpedo1.SetRadius(0.010000)
ForwardTorpedo1.SetDumbfire(1)
ForwardTorpedo1.SetWeaponID(1)
ForwardTorpedo1.SetGroups(1)
ForwardTorpedo1.SetDamageRadiusFactor(0.500000)
ForwardTorpedo1.SetIconNum(370)
ForwardTorpedo1.SetIconPositionX(72.000000)
ForwardTorpedo1.SetIconPositionY(35.000000)
ForwardTorpedo1.SetIconAboveShip(1)
ForwardTorpedo1.SetImmediateDelay(0.220000)
ForwardTorpedo1.SetReloadDelay(35.000000)
ForwardTorpedo1.SetMaxReady(2)
ForwardTorpedo1Direction = App.TGPoint3()
ForwardTorpedo1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo1.SetDirection(ForwardTorpedo1Direction)
ForwardTorpedo1Right = App.TGPoint3()
ForwardTorpedo1Right.SetXYZ(1.000000, 0.000000, 0.000000)
ForwardTorpedo1.SetRight(ForwardTorpedo1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo1)
#################################################
FwdTorpedo2 = App.TorpedoTubeProperty_Create("Fwd Torpedo 2")

FwdTorpedo2.SetMaxCondition(1000.000000)
FwdTorpedo2.SetCritical(0)
FwdTorpedo2.SetTargetable(1)
FwdTorpedo2.SetPrimary(1)
FwdTorpedo2.SetPosition(0.025974, 0.485535, -0.014004)
FwdTorpedo2.SetPosition2D(71.000000, 13.000000)
FwdTorpedo2.SetRepairComplexity(5.000000)
FwdTorpedo2.SetDisabledPercentage(0.750000)
FwdTorpedo2.SetRadius(0.010000)
FwdTorpedo2.SetDumbfire(1)
FwdTorpedo2.SetWeaponID(2)
FwdTorpedo2.SetGroups(1)
FwdTorpedo2.SetDamageRadiusFactor(0.500000)
FwdTorpedo2.SetIconNum(370)
FwdTorpedo2.SetIconPositionX(79.000000)
FwdTorpedo2.SetIconPositionY(35.000000)
FwdTorpedo2.SetIconAboveShip(1)
FwdTorpedo2.SetImmediateDelay(0.220000)
FwdTorpedo2.SetReloadDelay(35.000000)
FwdTorpedo2.SetMaxReady(2)
FwdTorpedo2Direction = App.TGPoint3()
FwdTorpedo2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
FwdTorpedo2.SetDirection(FwdTorpedo2Direction)
FwdTorpedo2Right = App.TGPoint3()
FwdTorpedo2Right.SetXYZ(-1.000000, 0.000000, 0.000000)
FwdTorpedo2.SetRight(FwdTorpedo2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdTorpedo2)
#################################################
CenterImpulse = App.EngineProperty_Create("Center Impulse")

CenterImpulse.SetMaxCondition(1500.000000)
CenterImpulse.SetCritical(0)
CenterImpulse.SetTargetable(1)
CenterImpulse.SetPrimary(1)
CenterImpulse.SetPosition(-0.005796, -0.460297, 0.028460)
CenterImpulse.SetPosition2D(92.000000, 84.000000)
CenterImpulse.SetRepairComplexity(3.000000)
CenterImpulse.SetDisabledPercentage(0.500000)
CenterImpulse.SetRadius(0.050000)
CenterImpulse.SetEngineType(CenterImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(CenterImpulse)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(3000.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.800000, 0.200000, -0.070000)
PortWarp.SetPosition2D(7.000000, 100.000000)
PortWarp.SetRepairComplexity(3.000000)
PortWarp.SetDisabledPercentage(0.750000)
PortWarp.SetRadius(0.570000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(3000.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.800000, 0.200000, -0.070000)
StarWarp.SetPosition2D(121.000000, 100.000000)
StarWarp.SetRepairComplexity(3.000000)
StarWarp.SetDisabledPercentage(0.750000)
StarWarp.SetRadius(0.570000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
PoleronBeams = App.WeaponSystemProperty_Create("Poleron Beams")

PoleronBeams.SetMaxCondition(1700.000000)
PoleronBeams.SetCritical(0)
PoleronBeams.SetTargetable(0)
PoleronBeams.SetPrimary(1)
PoleronBeams.SetPosition(0.000000, 0.324363, 0.061000)
PoleronBeams.SetPosition2D(64.000000, 10.000000)
PoleronBeams.SetRepairComplexity(7.000000)
PoleronBeams.SetDisabledPercentage(0.750000)
PoleronBeams.SetRadius(0.100000)
PoleronBeams.SetNormalPowerPerSecond(100.000000)
PoleronBeams.SetWeaponSystemType(PoleronBeams.WST_PHASER)
PoleronBeams.SetSingleFire(1)
PoleronBeams.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
PoleronBeams.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(PoleronBeams)
#################################################
PhasedPoleronBeam = App.PhaserProperty_Create("Phased Poleron Beam")

PhasedPoleronBeam.SetMaxCondition(800.000000)
PhasedPoleronBeam.SetCritical(0)
PhasedPoleronBeam.SetTargetable(1)
PhasedPoleronBeam.SetPrimary(1)
PhasedPoleronBeam.SetPosition(0.000000, 0.489746, -0.009602)
PhasedPoleronBeam.SetPosition2D(64.000000, 10.000000)
PhasedPoleronBeam.SetRepairComplexity(5.000000)
PhasedPoleronBeam.SetDisabledPercentage(0.750000)
PhasedPoleronBeam.SetRadius(0.200000)
PhasedPoleronBeam.SetDumbfire(0)
PhasedPoleronBeam.SetWeaponID(1)
PhasedPoleronBeam.SetGroups(0)
PhasedPoleronBeam.SetDamageRadiusFactor(0.180000)
PhasedPoleronBeam.SetIconNum(364)
PhasedPoleronBeam.SetIconPositionX(63.000000)
PhasedPoleronBeam.SetIconPositionY(23.000000)
PhasedPoleronBeam.SetIconAboveShip(1)
PhasedPoleronBeam.SetFireSound("Polaron Beam")
PhasedPoleronBeam.SetMaxCharge(1.000000)
PhasedPoleronBeam.SetMaxDamage(1600.000000)
PhasedPoleronBeam.SetMaxDamageDistance(100.000000)
PhasedPoleronBeam.SetMinFiringCharge(1.000000)
PhasedPoleronBeam.SetNormalDischargeRate(1.000000)
PhasedPoleronBeam.SetRechargeRate(1.000000)
PhasedPoleronBeam.SetIndicatorIconNum(510)
PhasedPoleronBeam.SetIndicatorIconPositionX(57.000000)
PhasedPoleronBeam.SetIndicatorIconPositionY(18.000000)
PhasedPoleronBeamForward = App.TGPoint3()
PhasedPoleronBeamForward.SetXYZ(0.000000, 1.000000, 0.000000)
PhasedPoleronBeamUp = App.TGPoint3()
PhasedPoleronBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
PhasedPoleronBeam.SetOrientation(PhasedPoleronBeamForward, PhasedPoleronBeamUp)
PhasedPoleronBeam.SetWidth(0.010000)
PhasedPoleronBeam.SetLength(0.010000)
PhasedPoleronBeam.SetArcWidthAngles(-0.523599, 0.523599)
PhasedPoleronBeam.SetArcHeightAngles(-0.523599, 0.523599)
PhasedPoleronBeam.SetPhaserTextureStart(16)
PhasedPoleronBeam.SetPhaserTextureEnd(23)
PhasedPoleronBeam.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.749020, 1.000000)
PhasedPoleronBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(0.309804, 0.309804, 1.000000, 0.803922)
PhasedPoleronBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 1.000000, 1.000000)
PhasedPoleronBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.392157, 0.392157, 1.000000, 0.603922)
PhasedPoleronBeam.SetInnerCoreColor(kColor)
PhasedPoleronBeam.SetNumSides(12)
PhasedPoleronBeam.SetMainRadius(0.100000)
PhasedPoleronBeam.SetTaperRadius(0.020000)
PhasedPoleronBeam.SetCoreScale(0.600000)
PhasedPoleronBeam.SetTaperRatio(0.250000)
PhasedPoleronBeam.SetTaperMinLength(5.000000)
PhasedPoleronBeam.SetTaperMaxLength(30.000000)
PhasedPoleronBeam.SetLengthTextureTilePerUnit(0.500000)
PhasedPoleronBeam.SetPerimeterTile(1.000000)
PhasedPoleronBeam.SetTextureSpeed(2.000000)
PhasedPoleronBeam.SetTextureName("data/CADominion.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(PhasedPoleronBeam)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(1400.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.002647, 0.300915, 0.000000)
Tractors.SetPosition2D(39.000000, 72.000000)
Tractors.SetRepairComplexity(7.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.100000)
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

AftTractor.SetMaxCondition(800.000000)
AftTractor.SetCritical(0)
AftTractor.SetTargetable(1)
AftTractor.SetPrimary(1)
AftTractor.SetPosition(0.002379, -0.217019, -0.017219)
AftTractor.SetPosition2D(39.000000, 72.000000)
AftTractor.SetRepairComplexity(7.000000)
AftTractor.SetDisabledPercentage(0.750000)
AftTractor.SetRadius(0.010000)
AftTractor.SetDumbfire(0)
AftTractor.SetWeaponID(7)
AftTractor.SetGroups(0)
AftTractor.SetDamageRadiusFactor(0.300000)
AftTractor.SetIconNum(0)
AftTractor.SetIconPositionX(0.000000)
AftTractor.SetIconPositionY(0.000000)
AftTractor.SetIconAboveShip(1)
AftTractor.SetFireSound("Tractor Beam")
AftTractor.SetMaxCharge(5.000000)
AftTractor.SetMaxDamage(70.000000)
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
AftTractor.SetArcWidthAngles(-0.785398, 0.785398)
AftTractor.SetArcHeightAngles(-0.785398, 0.087266)
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
ForwardTractor = App.TractorBeamProperty_Create("Forward Tractor")

ForwardTractor.SetMaxCondition(800.000000)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(1)
ForwardTractor.SetPrimary(1)
ForwardTractor.SetPosition(0.002557, 0.556863, -0.031086)
ForwardTractor.SetPosition2D(90.000000, 72.000000)
ForwardTractor.SetRepairComplexity(7.000000)
ForwardTractor.SetDisabledPercentage(0.750000)
ForwardTractor.SetRadius(0.010000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(7)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(0.300000)
ForwardTractor.SetIconNum(0)
ForwardTractor.SetIconPositionX(0.000000)
ForwardTractor.SetIconPositionY(0.000000)
ForwardTractor.SetIconAboveShip(1)
ForwardTractor.SetFireSound("Dominion Tractor")
ForwardTractor.SetMaxCharge(5.000000)
ForwardTractor.SetMaxDamage(200.000000)
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
ForwardTractor.SetArcWidthAngles(-0.785398, 0.785398)
ForwardTractor.SetArcHeightAngles(-1.047198, 0.017453)
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
bugship = App.ShipProperty_Create("bugship")

bugship.SetGenus(1)
bugship.SetSpecies(923)
bugship.SetMass(500.000000)
bugship.SetRotationalInertia(200.000000)
bugship.SetShipName("bugship")
bugship.SetModelFilename("data/Models/Ships/bug/Bug.NIF")
bugship.SetDamageResolution(5.000000)
bugship.SetAffiliation(0)
bugship.SetStationary(0)
bugship.SetAIString("DomRamAI")
bugship.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(bugship)
#################################################
RearTorpedo1 = App.TorpedoTubeProperty_Create("Rear Torpedo 1")

RearTorpedo1.SetMaxCondition(1200.000000)
RearTorpedo1.SetCritical(0)
RearTorpedo1.SetTargetable(1)
RearTorpedo1.SetPrimary(1)
RearTorpedo1.SetPosition(0.000000, -0.330000, 0.022178)
RearTorpedo1.SetPosition2D(75.000000, 100.000000)
RearTorpedo1.SetRepairComplexity(1.000000)
RearTorpedo1.SetDisabledPercentage(0.500000)
RearTorpedo1.SetRadius(0.250000)
RearTorpedo1.SetDumbfire(1)
RearTorpedo1.SetWeaponID(0)
RearTorpedo1.SetGroups(0)
RearTorpedo1.SetDamageRadiusFactor(0.600000)
RearTorpedo1.SetIconNum(370)
RearTorpedo1.SetIconPositionX(75.000000)
RearTorpedo1.SetIconPositionY(100.000000)
RearTorpedo1.SetIconAboveShip(1)
RearTorpedo1.SetImmediateDelay(0.250000)
RearTorpedo1.SetReloadDelay(5.000000)
RearTorpedo1.SetMaxReady(3)
RearTorpedo1Direction = App.TGPoint3()
RearTorpedo1Direction.SetXYZ(0.000000, -1.000000, 0.000000)
RearTorpedo1.SetDirection(RearTorpedo1Direction)
RearTorpedo1Right = App.TGPoint3()
RearTorpedo1Right.SetXYZ(1.000000, 0.000000, 0.000000)
RearTorpedo1.SetRight(RearTorpedo1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(RearTorpedo1)
#################################################
RearBeam1 = App.PhaserProperty_Create("Rear Beam 1")

RearBeam1.SetMaxCondition(1200.000000)
RearBeam1.SetCritical(0)
RearBeam1.SetTargetable(1)
RearBeam1.SetPrimary(1)
RearBeam1.SetPosition(-0.259495, -0.290586, 0.137106)
RearBeam1.SetPosition2D(0.000000, 0.000000)
RearBeam1.SetRepairComplexity(1.000000)
RearBeam1.SetDisabledPercentage(0.750000)
RearBeam1.SetRadius(0.250000)
RearBeam1.SetDumbfire(0)
RearBeam1.SetWeaponID(0)
RearBeam1.SetGroups(0)
RearBeam1.SetDamageRadiusFactor(0.250000)
RearBeam1.SetIconNum(0)
RearBeam1.SetIconPositionX(0.000000)
RearBeam1.SetIconPositionY(0.000000)
RearBeam1.SetIconAboveShip(1)
RearBeam1.SetFireSound("Polaron Beam")
RearBeam1.SetMaxCharge(2.000000)
RearBeam1.SetMaxDamage(800.000000)
RearBeam1.SetMaxDamageDistance(100.000000)
RearBeam1.SetMinFiringCharge(1.000000)
RearBeam1.SetNormalDischargeRate(1.000000)
RearBeam1.SetRechargeRate(1.000000)
RearBeam1.SetIndicatorIconNum(0)
RearBeam1.SetIndicatorIconPositionX(0.000000)
RearBeam1.SetIndicatorIconPositionY(0.000000)
RearBeam1Forward = App.TGPoint3()
RearBeam1Forward.SetXYZ(-0.008026, -0.939383, 0.342775)
RearBeam1Up = App.TGPoint3()
RearBeam1Up.SetXYZ(0.111787, -0.341480, -0.933218)
RearBeam1.SetOrientation(RearBeam1Forward, RearBeam1Up)
RearBeam1.SetWidth(0.001000)
RearBeam1.SetLength(0.001000)
RearBeam1.SetArcWidthAngles(-0.349066, 0.349066)
RearBeam1.SetArcHeightAngles(-0.349066, 0.349066)
RearBeam1.SetPhaserTextureStart(16)
RearBeam1.SetPhaserTextureEnd(23)
RearBeam1.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.749020, 1.000000)
RearBeam1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.309804, 0.309804, 1.000000, 1.000000)
RearBeam1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 1.000000, 1.000000)
RearBeam1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.392157, 0.392157, 1.000000, 1.000000)
RearBeam1.SetInnerCoreColor(kColor)
RearBeam1.SetNumSides(12)
RearBeam1.SetMainRadius(0.100000)
RearBeam1.SetTaperRadius(0.020000)
RearBeam1.SetCoreScale(0.600000)
RearBeam1.SetTaperRatio(0.250000)
RearBeam1.SetTaperMinLength(5.000000)
RearBeam1.SetTaperMaxLength(30.000000)
RearBeam1.SetLengthTextureTilePerUnit(0.500000)
RearBeam1.SetPerimeterTile(1.000000)
RearBeam1.SetTextureSpeed(2.000000)
RearBeam1.SetTextureName("data/CADominion.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(RearBeam1)
#################################################
RearBeam2 = App.PhaserProperty_Create("Rear Beam 2")

RearBeam2.SetMaxCondition(1200.000000)
RearBeam2.SetCritical(0)
RearBeam2.SetTargetable(1)
RearBeam2.SetPrimary(1)
RearBeam2.SetPosition(0.256283, -0.281085, 0.139286)
RearBeam2.SetPosition2D(0.000000, 0.000000)
RearBeam2.SetRepairComplexity(1.000000)
RearBeam2.SetDisabledPercentage(0.750000)
RearBeam2.SetRadius(0.250000)
RearBeam2.SetDumbfire(0)
RearBeam2.SetWeaponID(0)
RearBeam2.SetGroups(0)
RearBeam2.SetDamageRadiusFactor(0.250000)
RearBeam2.SetIconNum(0)
RearBeam2.SetIconPositionX(0.000000)
RearBeam2.SetIconPositionY(0.000000)
RearBeam2.SetIconAboveShip(1)
RearBeam2.SetFireSound("Polaron Beam")
RearBeam2.SetMaxCharge(2.000000)
RearBeam2.SetMaxDamage(800.000000)
RearBeam2.SetMaxDamageDistance(100.000000)
RearBeam2.SetMinFiringCharge(1.000000)
RearBeam2.SetNormalDischargeRate(1.000000)
RearBeam2.SetRechargeRate(1.000000)
RearBeam2.SetIndicatorIconNum(0)
RearBeam2.SetIndicatorIconPositionX(0.000000)
RearBeam2.SetIndicatorIconPositionY(0.000000)
RearBeam2Forward = App.TGPoint3()
RearBeam2Forward.SetXYZ(-0.092574, -0.904687, 0.415899)
RearBeam2Up = App.TGPoint3()
RearBeam2Up.SetXYZ(0.119040, -0.424753, -0.897449)
RearBeam2.SetOrientation(RearBeam2Forward, RearBeam2Up)
RearBeam2.SetWidth(0.001000)
RearBeam2.SetLength(0.001000)
RearBeam2.SetArcWidthAngles(-0.349066, 0.349066)
RearBeam2.SetArcHeightAngles(-0.349066, 0.349066)
RearBeam2.SetPhaserTextureStart(16)
RearBeam2.SetPhaserTextureEnd(23)
RearBeam2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.749020, 1.000000)
RearBeam2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.309804, 0.309804, 1.000000, 1.000000)
RearBeam2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 1.000000, 1.000000)
RearBeam2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.392157, 0.392157, 1.000000, 1.000000)
RearBeam2.SetInnerCoreColor(kColor)
RearBeam2.SetNumSides(12)
RearBeam2.SetMainRadius(0.100000)
RearBeam2.SetTaperRadius(0.010000)
RearBeam2.SetCoreScale(0.600000)
RearBeam2.SetTaperRatio(0.250000)
RearBeam2.SetTaperMinLength(5.000000)
RearBeam2.SetTaperMaxLength(30.000000)
RearBeam2.SetLengthTextureTilePerUnit(0.500000)
RearBeam2.SetPerimeterTile(1.000000)
RearBeam2.SetTextureSpeed(2.000000)
RearBeam2.SetTextureName("data/CADominion.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(RearBeam2)

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
	prop = App.g_kModelPropertyManager.FindByName("Poleron Beams", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phased Poleron Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("bugship", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Center Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Torpedo 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Rear Beam 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Rear Beam 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
