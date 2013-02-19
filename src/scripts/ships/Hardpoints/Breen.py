# C:\Users\Owner\Documents\FinalHP_Changes_Breen\Breen.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(11000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.100000, -0.800000, 0.000000)
Hull.SetPosition2D(64.000000, 35.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(3.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(11000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.203468, -0.785321, -0.106787)
WarpCore.SetPosition2D(64.000000, 75.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.400000)
WarpCore.SetMainBatteryLimit(1800000.000000)
WarpCore.SetBackupBatteryLimit(220000.000000)
WarpCore.SetMainConduitCapacity(2500.000000)
WarpCore.SetBackupConduitCapacity(350.000000)
WarpCore.SetPowerOutput(2000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(1000.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(64.000000, 120.000000)
RepairSystem.SetRepairComplexity(20.000000)
RepairSystem.SetDisabledPercentage(0.100000)
RepairSystem.SetRadius(0.250000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(40.000000)
RepairSystem.SetNumRepairTeams(3)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(8000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.337998, -1.004150, 0.558417)
SensorArray.SetPosition2D(64.000000, 20.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.150000)
SensorArray.SetNormalPowerPerSecond(250.000000)
SensorArray.SetBaseSensorRange(2600.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(10000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.219434, -0.533810, -0.042953)
ShieldGenerator.SetPosition2D(64.000000, 35.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.100000)
ShieldGenerator.SetNormalPowerPerSecond(200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.247059, 0.501961, 0.501961, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 9000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 15.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(12000.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, -1.000000, 0.000000)
WarpEngines.SetPosition2D(64.000000, 85.333336)
WarpEngines.SetRepairComplexity(3.000000)
WarpEngines.SetDisabledPercentage(0.750000)
WarpEngines.SetRadius(0.500000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
DrainWeapon = App.TorpedoSystemProperty_Create("Drain Weapon")

DrainWeapon.SetMaxCondition(500.000000)
DrainWeapon.SetCritical(0)
DrainWeapon.SetTargetable(0)
DrainWeapon.SetPrimary(1)
DrainWeapon.SetPosition(-0.094554, 2.612510, 0.168833)
DrainWeapon.SetPosition2D(64.000000, 25.000000)
DrainWeapon.SetRepairComplexity(3.000000)
DrainWeapon.SetDisabledPercentage(0.750000)
DrainWeapon.SetRadius(0.300000)
DrainWeapon.SetNormalPowerPerSecond(200.000000)
DrainWeapon.SetWeaponSystemType(DrainWeapon.WST_TORPEDO)
DrainWeapon.SetSingleFire(1)
DrainWeapon.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
DrainWeapon.SetFiringChainString(kFiringChainString)
DrainWeapon.SetMaxTorpedoes(0, 5)
DrainWeapon.SetTorpedoScript(0, "Tactical.Projectiles.ZZ_BreenTorp")
DrainWeapon.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(DrainWeapon)
#################################################
MainWarp = App.EngineProperty_Create("Main Warp")

MainWarp.SetMaxCondition(6000.000000)
MainWarp.SetCritical(0)
MainWarp.SetTargetable(1)
MainWarp.SetPrimary(1)
MainWarp.SetPosition(-0.522987, -1.843570, -0.105041)
MainWarp.SetPosition2D(44.000000, 80.000000)
MainWarp.SetRepairComplexity(3.000000)
MainWarp.SetDisabledPercentage(0.500000)
MainWarp.SetRadius(0.400000)
MainWarp.SetEngineType(MainWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainWarp)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(500.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, -1.000000, 0.000000)
ImpulseEngines.SetPosition2D(74.000000, 64.000000)
ImpulseEngines.SetRepairComplexity(4.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.500000)
ImpulseEngines.SetNormalPowerPerSecond(750.000000)
ImpulseEngines.SetMaxAccel(2.500000)
ImpulseEngines.SetMaxAngularAccel(0.420000)
ImpulseEngines.SetMaxAngularVelocity(0.700000)
ImpulseEngines.SetMaxSpeed(11.000000)
ImpulseEngines.SetEngineSound("Cardassian Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
MainImpulse = App.EngineProperty_Create("Main Impulse")

MainImpulse.SetMaxCondition(5000.000000)
MainImpulse.SetCritical(0)
MainImpulse.SetTargetable(1)
MainImpulse.SetPrimary(1)
MainImpulse.SetPosition(0.294440, -1.518320, 0.473813)
MainImpulse.SetPosition2D(64.000000, 60.000000)
MainImpulse.SetRepairComplexity(4.000000)
MainImpulse.SetDisabledPercentage(0.500000)
MainImpulse.SetRadius(0.200000)
MainImpulse.SetEngineType(MainImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainImpulse)
#################################################
BreenFrigate = App.ShipProperty_Create("Breen Frigate")

BreenFrigate.SetGenus(1)
BreenFrigate.SetSpecies(717)
BreenFrigate.SetMass(200.000000)
BreenFrigate.SetRotationalInertia(10000.000000)
BreenFrigate.SetShipName("Breen Frigate")
BreenFrigate.SetModelFilename("data/Models/Ships/CardHybrid.nif")
BreenFrigate.SetDamageResolution(10.000000)
BreenFrigate.SetAffiliation(0)
BreenFrigate.SetStationary(0)
BreenFrigate.SetAIString("NonFedAttack")
BreenFrigate.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(BreenFrigate)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(1500.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, -0.700000, 0.000000)
Tractors.SetPosition2D(64.000000, 75.000000)
Tractors.SetRepairComplexity(7.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.250000)
Tractors.SetNormalPowerPerSecond(500.000000)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
Torpedoes = App.WeaponSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(2400.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(64.000000, 105.000000)
Torpedoes.SetRepairComplexity(8.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.250000)
Torpedoes.SetNormalPowerPerSecond(500.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_PULSE)
Torpedoes.SetSingleFire(1)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
ForwardTractor = App.TractorBeamProperty_Create("Forward Tractor")

ForwardTractor.SetMaxCondition(1500.000000)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(1)
ForwardTractor.SetPrimary(1)
ForwardTractor.SetPosition(-0.083260, 2.605980, 0.269712)
ForwardTractor.SetPosition2D(64.000000, 55.000000)
ForwardTractor.SetRepairComplexity(7.000000)
ForwardTractor.SetDisabledPercentage(0.750000)
ForwardTractor.SetRadius(0.300000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(1)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(0.300000)
ForwardTractor.SetIconNum(0)
ForwardTractor.SetIconPositionX(62.223785)
ForwardTractor.SetIconPositionY(8.405760)
ForwardTractor.SetIconAboveShip(1)
ForwardTractor.SetFireSound("Dominion Tractor")
ForwardTractor.SetMaxCharge(5.000000)
ForwardTractor.SetMaxDamage(500.000000)
ForwardTractor.SetMaxDamageDistance(240.000000)
ForwardTractor.SetMinFiringCharge(3.000000)
ForwardTractor.SetNormalDischargeRate(0.500000)
ForwardTractor.SetRechargeRate(0.300000)
ForwardTractor.SetIndicatorIconNum(0)
ForwardTractor.SetIndicatorIconPositionX(62.223785)
ForwardTractor.SetIndicatorIconPositionY(8.405760)
ForwardTractorForward = App.TGPoint3()
ForwardTractorForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractorUp = App.TGPoint3()
ForwardTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardTractor.SetOrientation(ForwardTractorForward, ForwardTractorUp)
ForwardTractor.SetArcWidthAngles(-0.523599, 0.523599)
ForwardTractor.SetArcHeightAngles(-0.523599, 0.087266)
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
AftTractor = App.TractorBeamProperty_Create("Aft Tractor")

AftTractor.SetMaxCondition(1500.000000)
AftTractor.SetCritical(0)
AftTractor.SetTargetable(1)
AftTractor.SetPrimary(1)
AftTractor.SetPosition(-0.057868, -3.324730, 0.303991)
AftTractor.SetPosition2D(64.000000, 60.000000)
AftTractor.SetRepairComplexity(7.000000)
AftTractor.SetDisabledPercentage(0.750000)
AftTractor.SetRadius(0.300000)
AftTractor.SetDumbfire(0)
AftTractor.SetWeaponID(1)
AftTractor.SetGroups(0)
AftTractor.SetDamageRadiusFactor(0.300000)
AftTractor.SetIconNum(0)
AftTractor.SetIconPositionX(62.765484)
AftTractor.SetIconPositionY(134.927567)
AftTractor.SetIconAboveShip(1)
AftTractor.SetFireSound("Dominion Tractor")
AftTractor.SetMaxCharge(5.000000)
AftTractor.SetMaxDamage(500.000000)
AftTractor.SetMaxDamageDistance(240.000000)
AftTractor.SetMinFiringCharge(3.000000)
AftTractor.SetNormalDischargeRate(0.500000)
AftTractor.SetRechargeRate(0.300000)
AftTractor.SetIndicatorIconNum(0)
AftTractor.SetIndicatorIconPositionX(62.765484)
AftTractor.SetIndicatorIconPositionY(134.927567)
AftTractorForward = App.TGPoint3()
AftTractorForward.SetXYZ(0.000000, 1.000000, 0.000000)
AftTractorUp = App.TGPoint3()
AftTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
AftTractor.SetOrientation(AftTractorForward, AftTractorUp)
AftTractor.SetArcWidthAngles(-0.523599, 0.523599)
AftTractor.SetArcHeightAngles(-2.967060, -2.268928)
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
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.000000, 2.400000, 0.450000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -4.900000, 0.400000)
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
ViewscreenLeftPosition.SetXYZ(-0.900000, 2.000000, 0.450000)
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
ViewscreenRightPosition.SetXYZ(0.900000, 2.000000, 0.450000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 2.000000, 0.450000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 2.000000, 0.200000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 2.000000, 0.450000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
TorpedoTube = App.PulseWeaponProperty_Create("Torpedo Tube")

TorpedoTube.SetMaxCondition(2800.000000)
TorpedoTube.SetCritical(0)
TorpedoTube.SetTargetable(1)
TorpedoTube.SetPrimary(1)
TorpedoTube.SetPosition(-0.212324, 1.009660, -0.121224)
TorpedoTube.SetPosition2D(94.000000, 35.000000)
TorpedoTube.SetRepairComplexity(8.000000)
TorpedoTube.SetDisabledPercentage(0.750000)
TorpedoTube.SetRadius(0.250000)
TorpedoTube.SetDumbfire(1)
TorpedoTube.SetWeaponID(1)
TorpedoTube.SetGroups(1)
TorpedoTube.SetDamageRadiusFactor(0.300000)
TorpedoTube.SetIconNum(370)
TorpedoTube.SetIconPositionX(94.000000)
TorpedoTube.SetIconPositionY(55.000000)
TorpedoTube.SetIconAboveShip(1)
TorpedoTube.SetFireSound("Quantum Torpedo")
TorpedoTube.SetMaxCharge(4.000000)
TorpedoTube.SetMaxDamage(1400.000000)
TorpedoTube.SetMaxDamageDistance(150.000000)
TorpedoTube.SetMinFiringCharge(1.000000)
TorpedoTube.SetNormalDischargeRate(1.000000)
TorpedoTube.SetRechargeRate(0.300000)
TorpedoTube.SetIndicatorIconNum(0)
TorpedoTube.SetIndicatorIconPositionX(59.470421)
TorpedoTube.SetIndicatorIconPositionY(42.460587)
TorpedoTubeForward = App.TGPoint3()
TorpedoTubeForward.SetXYZ(0.000000, 1.000000, 0.000000)
TorpedoTubeUp = App.TGPoint3()
TorpedoTubeUp.SetXYZ(0.000000, 0.000000, 1.000000)
TorpedoTube.SetOrientation(TorpedoTubeForward, TorpedoTubeUp)
TorpedoTube.SetArcWidthAngles(-0.523599, 0.523599)
TorpedoTube.SetArcHeightAngles(-0.349066, 0.349066)
TorpedoTube.SetCooldownTime(10.000000)
TorpedoTube.SetModuleName("Tactical.Projectiles.ZZ_RomTorpTNG")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoTube)
#################################################
MainTube = App.TorpedoTubeProperty_Create("Main Tube")

MainTube.SetMaxCondition(4000.000000)
MainTube.SetCritical(0)
MainTube.SetTargetable(1)
MainTube.SetPrimary(1)
MainTube.SetPosition(-0.099757, 2.610120, 0.166963)
MainTube.SetPosition2D(64.000000, 50.000000)
MainTube.SetRepairComplexity(9.000000)
MainTube.SetDisabledPercentage(0.500000)
MainTube.SetRadius(0.250000)
MainTube.SetDumbfire(1)
MainTube.SetWeaponID(0)
MainTube.SetGroups(0)
MainTube.SetDamageRadiusFactor(0.600000)
MainTube.SetIconNum(370)
MainTube.SetIconPositionX(64.000000)
MainTube.SetIconPositionY(50.000000)
MainTube.SetIconAboveShip(1)
MainTube.SetImmediateDelay(0.250000)
MainTube.SetReloadDelay(120.000000)
MainTube.SetMaxReady(1)
MainTubeDirection = App.TGPoint3()
MainTubeDirection.SetXYZ(0.000000, 1.000000, 0.000000)
MainTube.SetDirection(MainTubeDirection)
MainTubeRight = App.TGPoint3()
MainTubeRight.SetXYZ(1.000000, 0.000000, 0.000000)
MainTube.SetRight(MainTubeRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainTube)
#################################################
TorpedoTube1 = App.PulseWeaponProperty_Create("Torpedo Tube 1")

TorpedoTube1.SetMaxCondition(2800.000000)
TorpedoTube1.SetCritical(0)
TorpedoTube1.SetTargetable(1)
TorpedoTube1.SetPrimary(1)
TorpedoTube1.SetPosition(1.064930, 0.892413, 0.058190)
TorpedoTube1.SetPosition2D(86.718506, 44.961857)
TorpedoTube1.SetRepairComplexity(1.000000)
TorpedoTube1.SetDisabledPercentage(0.750000)
TorpedoTube1.SetRadius(0.250000)
TorpedoTube1.SetDumbfire(1)
TorpedoTube1.SetWeaponID(0)
TorpedoTube1.SetGroups(0)
TorpedoTube1.SetDamageRadiusFactor(0.300000)
TorpedoTube1.SetIconNum(366)
TorpedoTube1.SetIconPositionX(86.718506)
TorpedoTube1.SetIconPositionY(44.961857)
TorpedoTube1.SetIconAboveShip(1)
TorpedoTube1.SetFireSound("Quantum Torpedo")
TorpedoTube1.SetMaxCharge(4.000000)
TorpedoTube1.SetMaxDamage(25.000000)
TorpedoTube1.SetMaxDamageDistance(100.000000)
TorpedoTube1.SetMinFiringCharge(1.000000)
TorpedoTube1.SetNormalDischargeRate(1.000000)
TorpedoTube1.SetRechargeRate(0.300000)
TorpedoTube1.SetIndicatorIconNum(0)
TorpedoTube1.SetIndicatorIconPositionX(86.718506)
TorpedoTube1.SetIndicatorIconPositionY(44.961857)
TorpedoTube1Forward = App.TGPoint3()
TorpedoTube1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
TorpedoTube1Up = App.TGPoint3()
TorpedoTube1Up.SetXYZ(0.000000, 0.000000, 1.000000)
TorpedoTube1.SetOrientation(TorpedoTube1Forward, TorpedoTube1Up)
TorpedoTube1.SetArcWidthAngles(-0.523599, 0.523599)
TorpedoTube1.SetArcHeightAngles(-0.349066, 0.349066)
TorpedoTube1.SetCooldownTime(10.000000)
TorpedoTube1.SetModuleName("Tactical.Projectiles.ZZ_RomTorpTNG")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoTube1)
#################################################
TorpedoTube2 = App.PulseWeaponProperty_Create("Torpedo Tube 2")

TorpedoTube2.SetMaxCondition(2800.000000)
TorpedoTube2.SetCritical(0)
TorpedoTube2.SetTargetable(1)
TorpedoTube2.SetPrimary(1)
TorpedoTube2.SetPosition(-0.202650, 2.306510, 0.343258)
TorpedoTube2.SetPosition2D(59.676800, 14.794453)
TorpedoTube2.SetRepairComplexity(1.000000)
TorpedoTube2.SetDisabledPercentage(0.750000)
TorpedoTube2.SetRadius(0.250000)
TorpedoTube2.SetDumbfire(1)
TorpedoTube2.SetWeaponID(0)
TorpedoTube2.SetGroups(0)
TorpedoTube2.SetDamageRadiusFactor(0.300000)
TorpedoTube2.SetIconNum(366)
TorpedoTube2.SetIconPositionX(59.676800)
TorpedoTube2.SetIconPositionY(14.794453)
TorpedoTube2.SetIconAboveShip(1)
TorpedoTube2.SetFireSound("Quantum Torpedo")
TorpedoTube2.SetMaxCharge(4.000000)
TorpedoTube2.SetMaxDamage(25.000000)
TorpedoTube2.SetMaxDamageDistance(100.000000)
TorpedoTube2.SetMinFiringCharge(1.000000)
TorpedoTube2.SetNormalDischargeRate(1.000000)
TorpedoTube2.SetRechargeRate(0.300000)
TorpedoTube2.SetIndicatorIconNum(0)
TorpedoTube2.SetIndicatorIconPositionX(59.676800)
TorpedoTube2.SetIndicatorIconPositionY(14.794453)
TorpedoTube2Forward = App.TGPoint3()
TorpedoTube2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
TorpedoTube2Up = App.TGPoint3()
TorpedoTube2Up.SetXYZ(0.000000, 0.000000, 1.000000)
TorpedoTube2.SetOrientation(TorpedoTube2Forward, TorpedoTube2Up)
TorpedoTube2.SetArcWidthAngles(-0.523599, 0.523599)
TorpedoTube2.SetArcHeightAngles(-0.349066, 0.349066)
TorpedoTube2.SetCooldownTime(10.000000)
TorpedoTube2.SetModuleName("Tactical.Projectiles.ZZ_RomTorpTNG")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoTube2)
#################################################
TorpedoTube3 = App.PulseWeaponProperty_Create("Torpedo Tube 3")

TorpedoTube3.SetMaxCondition(2800.000000)
TorpedoTube3.SetCritical(0)
TorpedoTube3.SetTargetable(1)
TorpedoTube3.SetPrimary(1)
TorpedoTube3.SetPosition(-1.147480, 0.892414, 0.057447)
TorpedoTube3.SetPosition2D(39.520428, 44.961834)
TorpedoTube3.SetRepairComplexity(1.000000)
TorpedoTube3.SetDisabledPercentage(0.750000)
TorpedoTube3.SetRadius(0.250000)
TorpedoTube3.SetDumbfire(1)
TorpedoTube3.SetWeaponID(0)
TorpedoTube3.SetGroups(0)
TorpedoTube3.SetDamageRadiusFactor(0.300000)
TorpedoTube3.SetIconNum(366)
TorpedoTube3.SetIconPositionX(39.520428)
TorpedoTube3.SetIconPositionY(44.961834)
TorpedoTube3.SetIconAboveShip(1)
TorpedoTube3.SetFireSound("Quantum Torpedo")
TorpedoTube3.SetMaxCharge(4.000000)
TorpedoTube3.SetMaxDamage(25.000000)
TorpedoTube3.SetMaxDamageDistance(100.000000)
TorpedoTube3.SetMinFiringCharge(1.000000)
TorpedoTube3.SetNormalDischargeRate(1.000000)
TorpedoTube3.SetRechargeRate(0.300000)
TorpedoTube3.SetIndicatorIconNum(0)
TorpedoTube3.SetIndicatorIconPositionX(39.520428)
TorpedoTube3.SetIndicatorIconPositionY(44.961834)
TorpedoTube3Forward = App.TGPoint3()
TorpedoTube3Forward.SetXYZ(0.000000, 1.000000, 0.000000)
TorpedoTube3Up = App.TGPoint3()
TorpedoTube3Up.SetXYZ(0.000000, 0.000000, 1.000000)
TorpedoTube3.SetOrientation(TorpedoTube3Forward, TorpedoTube3Up)
TorpedoTube3.SetArcWidthAngles(-0.523599, 0.523599)
TorpedoTube3.SetArcHeightAngles(-0.349066, 0.349066)
TorpedoTube3.SetCooldownTime(10.000000)
TorpedoTube3.SetModuleName("Tactical.Projectiles.ZZ_RomTorpTNG")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoTube3)
#################################################
TorpedoTube4 = App.PulseWeaponProperty_Create("Torpedo Tube 4")

TorpedoTube4.SetMaxCondition(2800.000000)
TorpedoTube4.SetCritical(0)
TorpedoTube4.SetTargetable(1)
TorpedoTube4.SetPrimary(1)
TorpedoTube4.SetPosition(-0.988621, -1.855190, 0.067992)
TorpedoTube4.SetPosition2D(42.909420, 103.577385)
TorpedoTube4.SetRepairComplexity(1.000000)
TorpedoTube4.SetDisabledPercentage(0.750000)
TorpedoTube4.SetRadius(0.250000)
TorpedoTube4.SetDumbfire(1)
TorpedoTube4.SetWeaponID(0)
TorpedoTube4.SetGroups(0)
TorpedoTube4.SetDamageRadiusFactor(0.300000)
TorpedoTube4.SetIconNum(365)
TorpedoTube4.SetIconPositionX(42.909420)
TorpedoTube4.SetIconPositionY(103.577385)
TorpedoTube4.SetIconAboveShip(1)
TorpedoTube4.SetFireSound("Quantum Torpedo")
TorpedoTube4.SetMaxCharge(4.000000)
TorpedoTube4.SetMaxDamage(25.000000)
TorpedoTube4.SetMaxDamageDistance(100.000000)
TorpedoTube4.SetMinFiringCharge(1.000000)
TorpedoTube4.SetNormalDischargeRate(1.000000)
TorpedoTube4.SetRechargeRate(0.300000)
TorpedoTube4.SetIndicatorIconNum(0)
TorpedoTube4.SetIndicatorIconPositionX(42.909420)
TorpedoTube4.SetIndicatorIconPositionY(103.577385)
TorpedoTube4Forward = App.TGPoint3()
TorpedoTube4Forward.SetXYZ(-0.052336, -0.998021, 0.034852)
TorpedoTube4Up = App.TGPoint3()
TorpedoTube4Up.SetXYZ(0.000000, -0.034899, -0.999391)
TorpedoTube4.SetOrientation(TorpedoTube4Forward, TorpedoTube4Up)
TorpedoTube4.SetArcWidthAngles(-0.523599, 0.523599)
TorpedoTube4.SetArcHeightAngles(-0.349066, 0.349066)
TorpedoTube4.SetCooldownTime(7.000000)
TorpedoTube4.SetModuleName("Tactical.Projectiles.ZZ_RomTorpTNG")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoTube4)
#################################################
TorpedoTube5 = App.PulseWeaponProperty_Create("Torpedo Tube 5")

TorpedoTube5.SetMaxCondition(2800.000000)
TorpedoTube5.SetCritical(0)
TorpedoTube5.SetTargetable(1)
TorpedoTube5.SetPrimary(1)
TorpedoTube5.SetPosition(0.938570, -1.841280, 0.084432)
TorpedoTube5.SetPosition2D(84.022827, 103.280640)
TorpedoTube5.SetRepairComplexity(1.000000)
TorpedoTube5.SetDisabledPercentage(0.750000)
TorpedoTube5.SetRadius(0.250000)
TorpedoTube5.SetDumbfire(1)
TorpedoTube5.SetWeaponID(0)
TorpedoTube5.SetGroups(0)
TorpedoTube5.SetDamageRadiusFactor(0.300000)
TorpedoTube5.SetIconNum(365)
TorpedoTube5.SetIconPositionX(84.022827)
TorpedoTube5.SetIconPositionY(103.280640)
TorpedoTube5.SetIconAboveShip(1)
TorpedoTube5.SetFireSound("Quantum Torpedo")
TorpedoTube5.SetMaxCharge(4.000000)
TorpedoTube5.SetMaxDamage(25.000000)
TorpedoTube5.SetMaxDamageDistance(100.000000)
TorpedoTube5.SetMinFiringCharge(1.000000)
TorpedoTube5.SetNormalDischargeRate(1.000000)
TorpedoTube5.SetRechargeRate(0.300000)
TorpedoTube5.SetIndicatorIconNum(0)
TorpedoTube5.SetIndicatorIconPositionX(84.022827)
TorpedoTube5.SetIndicatorIconPositionY(103.280640)
TorpedoTube5Forward = App.TGPoint3()
TorpedoTube5Forward.SetXYZ(0.172821, -0.983626, 0.051110)
TorpedoTube5Up = App.TGPoint3()
TorpedoTube5Up.SetXYZ(-0.005944, -0.052931, -0.998581)
TorpedoTube5.SetOrientation(TorpedoTube5Forward, TorpedoTube5Up)
TorpedoTube5.SetArcWidthAngles(-0.523599, 0.523599)
TorpedoTube5.SetArcHeightAngles(-0.349066, 0.349066)
TorpedoTube5.SetCooldownTime(7.000000)
TorpedoTube5.SetModuleName("Tactical.Projectiles.ZZ_RomTorpTNG")
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoTube5)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Drain Weapon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Breen Frigate", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Main Tube", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tube", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tube 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tube 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tube 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tube 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tube 5", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
