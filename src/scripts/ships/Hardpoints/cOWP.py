# C:\Documents and Settings\Owner.STARFLEETHQ\My Documents\KM 1.0 Changes (2)\scripts\ships\Hardpoints\cOWP.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ForwardTorpedo = App.TorpedoTubeProperty_Create("Forward Torpedo")

ForwardTorpedo.SetMaxCondition(1800.000000)
ForwardTorpedo.SetCritical(0)
ForwardTorpedo.SetTargetable(1)
ForwardTorpedo.SetPrimary(1)
ForwardTorpedo.SetPosition(1.022190, -0.715990, 0.513506)
ForwardTorpedo.SetPosition2D(60.000000, 30.000000)
ForwardTorpedo.SetRepairComplexity(3.000000)
ForwardTorpedo.SetDisabledPercentage(0.750000)
ForwardTorpedo.SetRadius(0.100000)
ForwardTorpedo.SetDumbfire(1)
ForwardTorpedo.SetWeaponID(1)
ForwardTorpedo.SetGroups(2)
ForwardTorpedo.SetDamageRadiusFactor(0.200000)
ForwardTorpedo.SetIconNum(370)
ForwardTorpedo.SetIconPositionX(78.000000)
ForwardTorpedo.SetIconPositionY(64.000000)
ForwardTorpedo.SetIconAboveShip(1)
ForwardTorpedo.SetImmediateDelay(0.100000)
ForwardTorpedo.SetReloadDelay(20.000000)
ForwardTorpedo.SetMaxReady(2)
ForwardTorpedoDirection = App.TGPoint3()
ForwardTorpedoDirection.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo.SetDirection(ForwardTorpedoDirection)
ForwardTorpedoRight = App.TGPoint3()
ForwardTorpedoRight.SetXYZ(1.000000, 0.000000, 0.000000)
ForwardTorpedo.SetRight(ForwardTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(10000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.686227, 0.251614, -0.404718)
Hull.SetPosition2D(51.000000, 49.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.800000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(5000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.015849, 0.164052, 0.022181)
ShieldGenerator.SetPosition2D(69.000000, 46.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.300000)
ShieldGenerator.SetNormalPowerPerSecond(200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.901961, 0.721569, 0.019608, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(3.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 13000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 13000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 13000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 13000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 13000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 13000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 25.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(5000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(-0.392227, 0.114379, -0.208831)
SensorArray.SetPosition2D(84.000000, 5.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.150000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(800.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(4000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(-0.004641, -0.261359, 0.036398)
WarpCore.SetPosition2D(41.000000, 48.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.470000)
WarpCore.SetMainBatteryLimit(140000.000000)
WarpCore.SetBackupBatteryLimit(50000.000000)
WarpCore.SetMainConduitCapacity(700.000000)
WarpCore.SetBackupConduitCapacity(100.000000)
WarpCore.SetPowerOutput(600.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(2800.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(-0.316628, -0.215091, 0.546203)
ImpulseEngines.SetPosition2D(54.000000, 35.000000)
ImpulseEngines.SetRepairComplexity(4.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.150000)
ImpulseEngines.SetNormalPowerPerSecond(70.000000)
ImpulseEngines.SetMaxAccel(0.000000)
ImpulseEngines.SetMaxAngularAccel(2.700000)
ImpulseEngines.SetMaxAngularVelocity(2.500000)
ImpulseEngines.SetMaxSpeed(0.000000)
ImpulseEngines.SetEngineSound("Cardassian Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(3600.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.579410, -0.219463, -0.029741)
Torpedoes.SetPosition2D(64.000000, 20.000000)
Torpedoes.SetRepairComplexity(3.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.120000)
Torpedoes.SetNormalPowerPerSecond(70.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 1000)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.cOWPTorpedo")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
RepairSubsystem = App.RepairSubsystemProperty_Create("Repair Subsystem")

RepairSubsystem.SetMaxCondition(1000.000000)
RepairSubsystem.SetCritical(0)
RepairSubsystem.SetTargetable(0)
RepairSubsystem.SetPrimary(1)
RepairSubsystem.SetPosition(0.060782, 0.164051, 0.024321)
RepairSubsystem.SetPosition2D(75.000000, 35.000000)
RepairSubsystem.SetRepairComplexity(4.000000)
RepairSubsystem.SetDisabledPercentage(0.100000)
RepairSubsystem.SetRadius(0.100000)
RepairSubsystem.SetNormalPowerPerSecond(1.000000)
RepairSubsystem.SetMaxRepairPoints(20.000000)
RepairSubsystem.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSubsystem)
#################################################
Compressors = App.WeaponSystemProperty_Create("Compressors")

Compressors.SetMaxCondition(1200.000000)
Compressors.SetCritical(0)
Compressors.SetTargetable(0)
Compressors.SetPrimary(1)
Compressors.SetPosition(1.724980, 1.201130, -0.996524)
Compressors.SetPosition2D(54.000000, 35.000000)
Compressors.SetRepairComplexity(7.000000)
Compressors.SetDisabledPercentage(0.750000)
Compressors.SetRadius(0.100000)
Compressors.SetNormalPowerPerSecond(200.000000)
Compressors.SetWeaponSystemType(Compressors.WST_PHASER)
Compressors.SetSingleFire(1)
Compressors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Compressors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Compressors)
#################################################
ForwardBeam = App.PhaserProperty_Create("Forward Beam")

ForwardBeam.SetMaxCondition(1600.000000)
ForwardBeam.SetCritical(0)
ForwardBeam.SetTargetable(1)
ForwardBeam.SetPrimary(1)
ForwardBeam.SetPosition(1.710450, 1.181870, -0.984388)
ForwardBeam.SetPosition2D(68.000000, 85.000000)
ForwardBeam.SetRepairComplexity(7.000000)
ForwardBeam.SetDisabledPercentage(0.750000)
ForwardBeam.SetRadius(0.100000)
ForwardBeam.SetDumbfire(0)
ForwardBeam.SetWeaponID(1)
ForwardBeam.SetGroups(0)
ForwardBeam.SetDamageRadiusFactor(0.150000)
ForwardBeam.SetIconNum(362)
ForwardBeam.SetIconPositionX(83.000000)
ForwardBeam.SetIconPositionY(95.000000)
ForwardBeam.SetIconAboveShip(1)
ForwardBeam.SetFireSound("CardBeam")
ForwardBeam.SetMaxCharge(2.100000)
ForwardBeam.SetMaxDamage(1200.000000)
ForwardBeam.SetMaxDamageDistance(30.000000)
ForwardBeam.SetMinFiringCharge(1.000000)
ForwardBeam.SetNormalDischargeRate(1.000000)
ForwardBeam.SetRechargeRate(1.000000)
ForwardBeam.SetIndicatorIconNum(509)
ForwardBeam.SetIndicatorIconPositionX(83.000000)
ForwardBeam.SetIndicatorIconPositionY(95.000000)
ForwardBeamForward = App.TGPoint3()
ForwardBeamForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardBeamUp = App.TGPoint3()
ForwardBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardBeam.SetOrientation(ForwardBeamForward, ForwardBeamUp)
ForwardBeam.SetWidth(0.001000)
ForwardBeam.SetLength(0.001000)
ForwardBeam.SetArcWidthAngles(-1.134464, 1.134464)
ForwardBeam.SetArcHeightAngles(-1.134464, 0.523599)
ForwardBeam.SetPhaserTextureStart(8)
ForwardBeam.SetPhaserTextureEnd(15)
ForwardBeam.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.501961, 0.000000, 1.000000)
ForwardBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.501961, 0.247059, 1.000000)
ForwardBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
ForwardBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
ForwardBeam.SetInnerCoreColor(kColor)
ForwardBeam.SetNumSides(6)
ForwardBeam.SetMainRadius(0.080000)
ForwardBeam.SetTaperRadius(0.010000)
ForwardBeam.SetCoreScale(0.500000)
ForwardBeam.SetTaperRatio(0.250000)
ForwardBeam.SetTaperMinLength(2.000000)
ForwardBeam.SetTaperMaxLength(10.000000)
ForwardBeam.SetLengthTextureTilePerUnit(0.500000)
ForwardBeam.SetPerimeterTile(1.000000)
ForwardBeam.SetTextureSpeed(2.500000)
ForwardBeam.SetTextureName("data/CACardassian.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardBeam)
#################################################
Engine1 = App.EngineProperty_Create("Engine 1")

Engine1.SetMaxCondition(400.000000)
Engine1.SetCritical(0)
Engine1.SetTargetable(1)
Engine1.SetPrimary(1)
Engine1.SetPosition(-0.547303, -0.272789, -0.260090)
Engine1.SetPosition2D(31.000000, 45.000000)
Engine1.SetRepairComplexity(4.000000)
Engine1.SetDisabledPercentage(0.500000)
Engine1.SetRadius(0.300000)
Engine1.SetEngineType(Engine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine1)
#################################################
Engine2 = App.EngineProperty_Create("Engine 2")

Engine2.SetMaxCondition(400.000000)
Engine2.SetCritical(0)
Engine2.SetTargetable(1)
Engine2.SetPrimary(1)
Engine2.SetPosition(0.524709, -0.273985, -0.263802)
Engine2.SetPosition2D(50.000000, 24.000000)
Engine2.SetRepairComplexity(4.000000)
Engine2.SetDisabledPercentage(0.500000)
Engine2.SetRadius(0.300000)
Engine2.SetEngineType(Engine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine2)
#################################################
Engine3 = App.EngineProperty_Create("Engine 3")

Engine3.SetMaxCondition(400.000000)
Engine3.SetCritical(0)
Engine3.SetTargetable(1)
Engine3.SetPrimary(1)
Engine3.SetPosition(-0.002912, -0.274733, 0.644230)
Engine3.SetPosition2D(30.000000, 65.000000)
Engine3.SetRepairComplexity(4.000000)
Engine3.SetDisabledPercentage(0.500000)
Engine3.SetRadius(0.250000)
Engine3.SetEngineType(Engine3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine3)
#################################################
Engine4 = App.EngineProperty_Create("Engine 4")

Engine4.SetMaxCondition(1400.000000)
Engine4.SetCritical(0)
Engine4.SetTargetable(1)
Engine4.SetPrimary(1)
Engine4.SetPosition(0.490000, -2.700000, 0.035016)
Engine4.SetPosition2D(84.000000, 120.000000)
Engine4.SetRepairComplexity(4.000000)
Engine4.SetDisabledPercentage(0.500000)
Engine4.SetRadius(0.250000)
Engine4.SetEngineType(Engine4.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine4)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(2000.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, 0.000000, -0.300000)
Tractors.SetPosition2D(49.000000, 60.000000)
Tractors.SetRepairComplexity(7.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.250000)
Tractors.SetNormalPowerPerSecond(400.000000)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
AftBeam = App.PhaserProperty_Create("Aft Beam")

AftBeam.SetMaxCondition(800.000000)
AftBeam.SetCritical(0)
AftBeam.SetTargetable(1)
AftBeam.SetPrimary(1)
AftBeam.SetPosition(-0.059847, -0.261360, 0.110050)
AftBeam.SetPosition2D(22.000000, 43.000000)
AftBeam.SetRepairComplexity(7.000000)
AftBeam.SetDisabledPercentage(0.750000)
AftBeam.SetRadius(0.200000)
AftBeam.SetDumbfire(0)
AftBeam.SetWeaponID(4)
AftBeam.SetGroups(0)
AftBeam.SetDamageRadiusFactor(0.100000)
AftBeam.SetIconNum(361)
AftBeam.SetIconPositionX(34.000000)
AftBeam.SetIconPositionY(55.000000)
AftBeam.SetIconAboveShip(1)
AftBeam.SetFireSound("Card Phaser")
AftBeam.SetMaxCharge(8.000000)
AftBeam.SetMaxDamage(200.000000)
AftBeam.SetMaxDamageDistance(40.000000)
AftBeam.SetMinFiringCharge(5.000000)
AftBeam.SetNormalDischargeRate(1.000000)
AftBeam.SetRechargeRate(0.100000)
AftBeam.SetIndicatorIconNum(508)
AftBeam.SetIndicatorIconPositionX(34.000000)
AftBeam.SetIndicatorIconPositionY(55.000000)
AftBeamForward = App.TGPoint3()
AftBeamForward.SetXYZ(0.000000, -1.000000, 0.000000)
AftBeamUp = App.TGPoint3()
AftBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
AftBeam.SetOrientation(AftBeamForward, AftBeamUp)
AftBeam.SetWidth(0.020000)
AftBeam.SetLength(0.020000)
AftBeam.SetArcWidthAngles(-0.698132, 0.698132)
AftBeam.SetArcHeightAngles(-0.610865, 0.610865)
AftBeam.SetPhaserTextureStart(8)
AftBeam.SetPhaserTextureEnd(15)
AftBeam.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.501961, 0.000000, 1.000000)
AftBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.501961, 0.247059, 1.000000)
AftBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
AftBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
AftBeam.SetInnerCoreColor(kColor)
AftBeam.SetNumSides(6)
AftBeam.SetMainRadius(0.150000)
AftBeam.SetTaperRadius(0.010000)
AftBeam.SetCoreScale(0.500000)
AftBeam.SetTaperRatio(0.250000)
AftBeam.SetTaperMinLength(5.000000)
AftBeam.SetTaperMaxLength(30.000000)
AftBeam.SetLengthTextureTilePerUnit(0.500000)
AftBeam.SetPerimeterTile(1.000000)
AftBeam.SetTextureSpeed(2.500000)
AftBeam.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftBeam)
#################################################
OWP = App.ShipProperty_Create("OWP")

OWP.SetGenus(1)
OWP.SetSpecies(207)
OWP.SetMass(80.000000)
OWP.SetRotationalInertia(8000.000000)
OWP.SetShipName("OWP")
OWP.SetModelFilename("data/Models/Ships/Keldon.nif")
OWP.SetDamageResolution(10.000000)
OWP.SetAffiliation(0)
OWP.SetStationary(0)
OWP.SetAIString("NonFedAttack")
OWP.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(OWP)
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
ViewscreenForwardPosition.SetXYZ(0.000612, 0.164052, 0.052868)
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
ViewscreenBackPosition.SetXYZ(0.000000, -3.100000, 0.100000)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 1.400000, 0.300000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 1.400000, 0.300000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 1.400000, 0.300000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 1.400000, 0.170000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 1.400000, 0.300000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
ForwardBeam2 = App.PhaserProperty_Create("Forward Beam 2")

ForwardBeam2.SetMaxCondition(1600.000000)
ForwardBeam2.SetCritical(0)
ForwardBeam2.SetTargetable(1)
ForwardBeam2.SetPrimary(1)
ForwardBeam2.SetPosition(0.016840, 1.140680, 2.074520)
ForwardBeam2.SetPosition2D(59.000000, 48.000000)
ForwardBeam2.SetRepairComplexity(7.000000)
ForwardBeam2.SetDisabledPercentage(0.750000)
ForwardBeam2.SetRadius(0.100000)
ForwardBeam2.SetDumbfire(0)
ForwardBeam2.SetWeaponID(1)
ForwardBeam2.SetGroups(0)
ForwardBeam2.SetDamageRadiusFactor(0.150000)
ForwardBeam2.SetIconNum(362)
ForwardBeam2.SetIconPositionX(97.000000)
ForwardBeam2.SetIconPositionY(53.000000)
ForwardBeam2.SetIconAboveShip(1)
ForwardBeam2.SetFireSound("CardBeam")
ForwardBeam2.SetMaxCharge(2.100000)
ForwardBeam2.SetMaxDamage(1200.000000)
ForwardBeam2.SetMaxDamageDistance(30.000000)
ForwardBeam2.SetMinFiringCharge(1.000000)
ForwardBeam2.SetNormalDischargeRate(1.000000)
ForwardBeam2.SetRechargeRate(1.000000)
ForwardBeam2.SetIndicatorIconNum(509)
ForwardBeam2.SetIndicatorIconPositionX(97.000000)
ForwardBeam2.SetIndicatorIconPositionY(53.000000)
ForwardBeam2Forward = App.TGPoint3()
ForwardBeam2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardBeam2Up = App.TGPoint3()
ForwardBeam2Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardBeam2.SetOrientation(ForwardBeam2Forward, ForwardBeam2Up)
ForwardBeam2.SetWidth(0.001000)
ForwardBeam2.SetLength(0.001000)
ForwardBeam2.SetArcWidthAngles(-1.134464, 1.134464)
ForwardBeam2.SetArcHeightAngles(1.134464, -0.523599)
ForwardBeam2.SetPhaserTextureStart(8)
ForwardBeam2.SetPhaserTextureEnd(15)
ForwardBeam2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.501961, 0.000000, 1.000000)
ForwardBeam2.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.501961, 0.247059, 1.000000)
ForwardBeam2.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
ForwardBeam2.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
ForwardBeam2.SetInnerCoreColor(kColor)
ForwardBeam2.SetNumSides(6)
ForwardBeam2.SetMainRadius(0.080000)
ForwardBeam2.SetTaperRadius(0.010000)
ForwardBeam2.SetCoreScale(0.500000)
ForwardBeam2.SetTaperRatio(0.250000)
ForwardBeam2.SetTaperMinLength(2.000000)
ForwardBeam2.SetTaperMaxLength(10.000000)
ForwardBeam2.SetLengthTextureTilePerUnit(0.500000)
ForwardBeam2.SetPerimeterTile(1.000000)
ForwardBeam2.SetTextureSpeed(2.500000)
ForwardBeam2.SetTextureName("data/CACardassian.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardBeam2)
#################################################
ForwardBeam3 = App.PhaserProperty_Create("Forward Beam 3")

ForwardBeam3.SetMaxCondition(1600.000000)
ForwardBeam3.SetCritical(0)
ForwardBeam3.SetTargetable(1)
ForwardBeam3.SetPrimary(1)
ForwardBeam3.SetPosition(-1.745170, 1.185780, -0.949134)
ForwardBeam3.SetPosition2D(83.000000, 42.000000)
ForwardBeam3.SetRepairComplexity(7.000000)
ForwardBeam3.SetDisabledPercentage(0.750000)
ForwardBeam3.SetRadius(0.100000)
ForwardBeam3.SetDumbfire(0)
ForwardBeam3.SetWeaponID(1)
ForwardBeam3.SetGroups(0)
ForwardBeam3.SetDamageRadiusFactor(0.150000)
ForwardBeam3.SetIconNum(362)
ForwardBeam3.SetIconPositionX(62.000000)
ForwardBeam3.SetIconPositionY(55.000000)
ForwardBeam3.SetIconAboveShip(1)
ForwardBeam3.SetFireSound("CardBeam")
ForwardBeam3.SetMaxCharge(2.100000)
ForwardBeam3.SetMaxDamage(1200.000000)
ForwardBeam3.SetMaxDamageDistance(30.000000)
ForwardBeam3.SetMinFiringCharge(1.000000)
ForwardBeam3.SetNormalDischargeRate(1.000000)
ForwardBeam3.SetRechargeRate(1.000000)
ForwardBeam3.SetIndicatorIconNum(509)
ForwardBeam3.SetIndicatorIconPositionX(62.000000)
ForwardBeam3.SetIndicatorIconPositionY(55.000000)
ForwardBeam3Forward = App.TGPoint3()
ForwardBeam3Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardBeam3Up = App.TGPoint3()
ForwardBeam3Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardBeam3.SetOrientation(ForwardBeam3Forward, ForwardBeam3Up)
ForwardBeam3.SetWidth(0.001000)
ForwardBeam3.SetLength(0.001000)
ForwardBeam3.SetArcWidthAngles(-1.134464, 1.134464)
ForwardBeam3.SetArcHeightAngles(1.134464, -0.523599)
ForwardBeam3.SetPhaserTextureStart(8)
ForwardBeam3.SetPhaserTextureEnd(15)
ForwardBeam3.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.501961, 0.000000, 1.000000)
ForwardBeam3.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.501961, 0.247059, 1.000000)
ForwardBeam3.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
ForwardBeam3.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
ForwardBeam3.SetInnerCoreColor(kColor)
ForwardBeam3.SetNumSides(6)
ForwardBeam3.SetMainRadius(0.080000)
ForwardBeam3.SetTaperRadius(0.010000)
ForwardBeam3.SetCoreScale(0.500000)
ForwardBeam3.SetTaperRatio(0.250000)
ForwardBeam3.SetTaperMinLength(2.000000)
ForwardBeam3.SetTaperMaxLength(10.000000)
ForwardBeam3.SetLengthTextureTilePerUnit(0.500000)
ForwardBeam3.SetPerimeterTile(1.000000)
ForwardBeam3.SetTextureSpeed(2.500000)
ForwardBeam3.SetTextureName("data/CACardassian.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardBeam3)
#################################################
ForwardTorpedo2 = App.TorpedoTubeProperty_Create("Forward Torpedo 2")

ForwardTorpedo2.SetMaxCondition(1800.000000)
ForwardTorpedo2.SetCritical(0)
ForwardTorpedo2.SetTargetable(1)
ForwardTorpedo2.SetPrimary(1)
ForwardTorpedo2.SetPosition(-0.914955, -0.711345, 0.718376)
ForwardTorpedo2.SetPosition2D(75.000000, 63.000000)
ForwardTorpedo2.SetRepairComplexity(3.000000)
ForwardTorpedo2.SetDisabledPercentage(0.750000)
ForwardTorpedo2.SetRadius(0.100000)
ForwardTorpedo2.SetDumbfire(1)
ForwardTorpedo2.SetWeaponID(1)
ForwardTorpedo2.SetGroups(2)
ForwardTorpedo2.SetDamageRadiusFactor(0.200000)
ForwardTorpedo2.SetIconNum(370)
ForwardTorpedo2.SetIconPositionX(85.000000)
ForwardTorpedo2.SetIconPositionY(87.000000)
ForwardTorpedo2.SetIconAboveShip(1)
ForwardTorpedo2.SetImmediateDelay(0.100000)
ForwardTorpedo2.SetReloadDelay(20.000000)
ForwardTorpedo2.SetMaxReady(2)
ForwardTorpedo2Direction = App.TGPoint3()
ForwardTorpedo2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo2.SetDirection(ForwardTorpedo2Direction)
ForwardTorpedo2Right = App.TGPoint3()
ForwardTorpedo2Right.SetXYZ(1.000000, 0.000000, 0.000000)
ForwardTorpedo2.SetRight(ForwardTorpedo2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo2)
#################################################
ForwardTorpedo3 = App.TorpedoTubeProperty_Create("Forward Torpedo 3")

ForwardTorpedo3.SetMaxCondition(1800.000000)
ForwardTorpedo3.SetCritical(0)
ForwardTorpedo3.SetTargetable(1)
ForwardTorpedo3.SetPrimary(1)
ForwardTorpedo3.SetPosition(-0.134290, -0.727319, -1.091890)
ForwardTorpedo3.SetPosition2D(52.000000, 67.000000)
ForwardTorpedo3.SetRepairComplexity(3.000000)
ForwardTorpedo3.SetDisabledPercentage(0.750000)
ForwardTorpedo3.SetRadius(0.100000)
ForwardTorpedo3.SetDumbfire(1)
ForwardTorpedo3.SetWeaponID(1)
ForwardTorpedo3.SetGroups(2)
ForwardTorpedo3.SetDamageRadiusFactor(0.200000)
ForwardTorpedo3.SetIconNum(370)
ForwardTorpedo3.SetIconPositionX(67.000000)
ForwardTorpedo3.SetIconPositionY(94.000000)
ForwardTorpedo3.SetIconAboveShip(1)
ForwardTorpedo3.SetImmediateDelay(0.100000)
ForwardTorpedo3.SetReloadDelay(20.000000)
ForwardTorpedo3.SetMaxReady(2)
ForwardTorpedo3Direction = App.TGPoint3()
ForwardTorpedo3Direction.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTorpedo3.SetDirection(ForwardTorpedo3Direction)
ForwardTorpedo3Right = App.TGPoint3()
ForwardTorpedo3Right.SetXYZ(1.000000, 0.000000, 0.000000)
ForwardTorpedo3.SetRight(ForwardTorpedo3Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTorpedo3)
#################################################
AftBeam2 = App.PhaserProperty_Create("Aft Beam 2")

AftBeam2.SetMaxCondition(800.000000)
AftBeam2.SetCritical(0)
AftBeam2.SetTargetable(1)
AftBeam2.SetPrimary(1)
AftBeam2.SetPosition(-0.788023, -0.759203, 0.459288)
AftBeam2.SetPosition2D(40.000000, 63.000000)
AftBeam2.SetRepairComplexity(7.000000)
AftBeam2.SetDisabledPercentage(0.750000)
AftBeam2.SetRadius(0.200000)
AftBeam2.SetDumbfire(0)
AftBeam2.SetWeaponID(4)
AftBeam2.SetGroups(0)
AftBeam2.SetDamageRadiusFactor(0.100000)
AftBeam2.SetIconNum(361)
AftBeam2.SetIconPositionX(47.000000)
AftBeam2.SetIconPositionY(19.000000)
AftBeam2.SetIconAboveShip(1)
AftBeam2.SetFireSound("Card Phaser")
AftBeam2.SetMaxCharge(8.000000)
AftBeam2.SetMaxDamage(200.000000)
AftBeam2.SetMaxDamageDistance(40.000000)
AftBeam2.SetMinFiringCharge(5.000000)
AftBeam2.SetNormalDischargeRate(1.000000)
AftBeam2.SetRechargeRate(0.100000)
AftBeam2.SetIndicatorIconNum(508)
AftBeam2.SetIndicatorIconPositionX(47.000000)
AftBeam2.SetIndicatorIconPositionY(19.000000)
AftBeam2Forward = App.TGPoint3()
AftBeam2Forward.SetXYZ(0.000000, -1.000000, 0.000000)
AftBeam2Up = App.TGPoint3()
AftBeam2Up.SetXYZ(0.000000, 0.000000, 1.000000)
AftBeam2.SetOrientation(AftBeam2Forward, AftBeam2Up)
AftBeam2.SetWidth(0.020000)
AftBeam2.SetLength(0.020000)
AftBeam2.SetArcWidthAngles(-0.698132, 0.698132)
AftBeam2.SetArcHeightAngles(-0.610865, 0.610865)
AftBeam2.SetPhaserTextureStart(8)
AftBeam2.SetPhaserTextureEnd(15)
AftBeam2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.501961, 0.000000, 1.000000)
AftBeam2.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.501961, 0.247059, 1.000000)
AftBeam2.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
AftBeam2.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
AftBeam2.SetInnerCoreColor(kColor)
AftBeam2.SetNumSides(6)
AftBeam2.SetMainRadius(0.150000)
AftBeam2.SetTaperRadius(0.010000)
AftBeam2.SetCoreScale(0.500000)
AftBeam2.SetTaperRatio(0.250000)
AftBeam2.SetTaperMinLength(5.000000)
AftBeam2.SetTaperMaxLength(30.000000)
AftBeam2.SetLengthTextureTilePerUnit(0.500000)
AftBeam2.SetPerimeterTile(1.000000)
AftBeam2.SetTextureSpeed(2.500000)
AftBeam2.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftBeam2)
#################################################
AftBeam3 = App.PhaserProperty_Create("Aft Beam 3")

AftBeam3.SetMaxCondition(800.000000)
AftBeam3.SetCritical(0)
AftBeam3.SetTargetable(1)
AftBeam3.SetPrimary(1)
AftBeam3.SetPosition(0.777058, -0.757907, 0.454432)
AftBeam3.SetPosition2D(47.000000, 36.000000)
AftBeam3.SetRepairComplexity(7.000000)
AftBeam3.SetDisabledPercentage(0.750000)
AftBeam3.SetRadius(0.200000)
AftBeam3.SetDumbfire(0)
AftBeam3.SetWeaponID(4)
AftBeam3.SetGroups(0)
AftBeam3.SetDamageRadiusFactor(0.100000)
AftBeam3.SetIconNum(361)
AftBeam3.SetIconPositionX(46.000000)
AftBeam3.SetIconPositionY(91.000000)
AftBeam3.SetIconAboveShip(1)
AftBeam3.SetFireSound("Card Phaser")
AftBeam3.SetMaxCharge(8.000000)
AftBeam3.SetMaxDamage(200.000000)
AftBeam3.SetMaxDamageDistance(40.000000)
AftBeam3.SetMinFiringCharge(5.000000)
AftBeam3.SetNormalDischargeRate(1.000000)
AftBeam3.SetRechargeRate(0.100000)
AftBeam3.SetIndicatorIconNum(508)
AftBeam3.SetIndicatorIconPositionX(46.000000)
AftBeam3.SetIndicatorIconPositionY(90.000000)
AftBeam3Forward = App.TGPoint3()
AftBeam3Forward.SetXYZ(0.000000, -1.000000, 0.000000)
AftBeam3Up = App.TGPoint3()
AftBeam3Up.SetXYZ(0.000000, 0.000000, 1.000000)
AftBeam3.SetOrientation(AftBeam3Forward, AftBeam3Up)
AftBeam3.SetWidth(0.020000)
AftBeam3.SetLength(0.020000)
AftBeam3.SetArcWidthAngles(-0.698132, 0.698132)
AftBeam3.SetArcHeightAngles(-0.610865, 0.610865)
AftBeam3.SetPhaserTextureStart(8)
AftBeam3.SetPhaserTextureEnd(15)
AftBeam3.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.501961, 0.000000, 1.000000)
AftBeam3.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.501961, 0.247059, 1.000000)
AftBeam3.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
AftBeam3.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
AftBeam3.SetInnerCoreColor(kColor)
AftBeam3.SetNumSides(6)
AftBeam3.SetMainRadius(0.150000)
AftBeam3.SetTaperRadius(0.010000)
AftBeam3.SetCoreScale(0.500000)
AftBeam3.SetTaperRatio(0.250000)
AftBeam3.SetTaperMinLength(5.000000)
AftBeam3.SetTaperMaxLength(30.000000)
AftBeam3.SetLengthTextureTilePerUnit(0.500000)
AftBeam3.SetPerimeterTile(1.000000)
AftBeam3.SetTextureSpeed(2.500000)
AftBeam3.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftBeam3)

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
	prop = App.g_kModelPropertyManager.FindByName("Compressors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair Subsystem", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("OWP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Forward Beam 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Beam 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Torpedo 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)