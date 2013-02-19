# C:\unzipped\DS9FX\DS9FX\scripts\ships\Hardpoints\DS9FXDummy.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(8000000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(65.000000, 60.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.120000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(1000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(52.000000, 59.000000)
ImpulseEngines.SetRepairComplexity(2.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.003000)
ImpulseEngines.SetNormalPowerPerSecond(10.000000)
ImpulseEngines.SetMaxAccel(2.500000)
ImpulseEngines.SetMaxAngularAccel(0.600000)
ImpulseEngines.SetMaxAngularVelocity(0.800000)
ImpulseEngines.SetMaxSpeed(4.000000)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(800000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.060000, -0.030000)
WarpCore.SetPosition2D(65.000000, 80.000000)
WarpCore.SetRepairComplexity(1.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.040000)
WarpCore.SetMainBatteryLimit(20000.000000)
WarpCore.SetBackupBatteryLimit(10000.000000)
WarpCore.SetMainConduitCapacity(140.000000)
WarpCore.SetBackupConduitCapacity(40.000000)
WarpCore.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(200.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(1)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(0.000000, 0.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.250000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(15.000000)
RepairSystem.SetNumRepairTeams(3)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(1400.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.040000, -0.014000)
SensorArray.SetPosition2D(65.000000, 40.000000)
SensorArray.SetRepairComplexity(0.400000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.030000)
SensorArray.SetNormalPowerPerSecond(20.000000)
SensorArray.SetBaseSensorRange(3000.000000)
SensorArray.SetMaxProbes(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(2600.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.040000, 0.040000)
ShieldGenerator.SetPosition2D(65.000000, 60.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.040000)
ShieldGenerator.SetNormalPowerPerSecond(30.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 2400.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 800.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 800.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 800.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 800.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 800.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 12.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 12.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")

Phasers.SetMaxCondition(800.000000)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(0.000175, 0.015236, -0.000475)
Phasers.SetPosition2D(79.000000, 59.000000)
Phasers.SetRepairComplexity(3.000000)
Phasers.SetDisabledPercentage(0.750000)
Phasers.SetRadius(0.002500)
Phasers.SetNormalPowerPerSecond(70.000000)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(1)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
Phaser = App.PhaserProperty_Create("Phaser")

Phaser.SetMaxCondition(800.000000)
Phaser.SetCritical(0)
Phaser.SetTargetable(0)
Phaser.SetPrimary(1)
Phaser.SetPosition(0.000000, 0.110000, -0.013000)
Phaser.SetPosition2D(65.000000, 26.000000)
Phaser.SetRepairComplexity(3.000000)
Phaser.SetDisabledPercentage(0.750000)
Phaser.SetRadius(0.034000)
Phaser.SetDumbfire(0)
Phaser.SetWeaponID(1)
Phaser.SetGroups(1)
Phaser.SetDamageRadiusFactor(0.100000)
Phaser.SetIconNum(364)
Phaser.SetIconPositionX(62.000000)
Phaser.SetIconPositionY(25.000000)
Phaser.SetIconAboveShip(1)
Phaser.SetFireSound("Akira Phaser")
Phaser.SetMaxCharge(4.000000)
Phaser.SetMaxDamage(300.000000)
Phaser.SetMaxDamageDistance(45.000000)
Phaser.SetMinFiringCharge(2.000000)
Phaser.SetNormalDischargeRate(1.000000)
Phaser.SetRechargeRate(0.800000)
Phaser.SetIndicatorIconNum(510)
Phaser.SetIndicatorIconPositionX(56.000000)
Phaser.SetIndicatorIconPositionY(21.000000)
PhaserForward = App.TGPoint3()
PhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
PhaserUp = App.TGPoint3()
PhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
Phaser.SetOrientation(PhaserForward, PhaserUp)
Phaser.SetWidth(0.001000)
Phaser.SetLength(0.001000)
Phaser.SetArcWidthAngles(-0.959931, 0.959931)
Phaser.SetArcHeightAngles(-1.047198, 0.610865)
Phaser.SetPhaserTextureStart(0)
Phaser.SetPhaserTextureEnd(7)
Phaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
Phaser.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
Phaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
Phaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)
Phaser.SetInnerCoreColor(kColor)
Phaser.SetNumSides(6)
Phaser.SetMainRadius(0.020000)
Phaser.SetTaperRadius(0.010000)
Phaser.SetCoreScale(0.500000)
Phaser.SetTaperRatio(0.250000)
Phaser.SetTaperMinLength(5.000000)
Phaser.SetTaperMaxLength(30.000000)
Phaser.SetLengthTextureTilePerUnit(0.500000)
Phaser.SetPerimeterTile(1.000000)
Phaser.SetTextureSpeed(2.500000)
Phaser.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Phaser)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(1100.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.050000, -0.080000, 0.034000)
PortImpulse.SetPosition2D(51.000000, 82.000000)
PortImpulse.SetRepairComplexity(1.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.030000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(1100.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.050000, -0.080000, 0.034000)
StarImpulse.SetPosition2D(79.000000, 82.000000)
StarImpulse.SetRepairComplexity(1.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.030000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
Shuttle = App.ShipProperty_Create("Shuttle")

Shuttle.SetGenus(1)
Shuttle.SetSpecies(106)
Shuttle.SetMass(15.000000)
Shuttle.SetRotationalInertia(2000.000000)
Shuttle.SetShipName("Shuttle")
Shuttle.SetModelFilename("data/Models/Ships/shuttle.nif")
Shuttle.SetDamageResolution(6.000000)
Shuttle.SetAffiliation(0)
Shuttle.SetStationary(0)
Shuttle.SetAIString("FedAttack")
Shuttle.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Shuttle)
#################################################
Repair = App.RepairSubsystemProperty_Create("Repair")

Repair.SetMaxCondition(200.000000)
Repair.SetCritical(0)
Repair.SetTargetable(0)
Repair.SetPrimary(1)
Repair.SetPosition(0.000000, 0.030000, 0.000000)
Repair.SetPosition2D(52.000000, 59.000000)
Repair.SetRepairComplexity(4.000000)
Repair.SetDisabledPercentage(0.100000)
Repair.SetRadius(0.030000)
Repair.SetNormalPowerPerSecond(1.000000)
Repair.SetMaxRepairPoints(2.000000)
Repair.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Repair)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(1600.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, -0.020000)
WarpEngines.SetPosition2D(79.000000, 59.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.010000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(800.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.072000, -0.040000, -0.034000)
PortWarp.SetPosition2D(41.000000, 68.000000)
PortWarp.SetRepairComplexity(1.000000)
PortWarp.SetDisabledPercentage(0.500000)
PortWarp.SetRadius(0.030000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(800.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.072000, -0.040000, -0.034000)
StarWarp.SetPosition2D(90.000000, 68.000000)
StarWarp.SetRepairComplexity(1.000000)
StarWarp.SetDisabledPercentage(0.500000)
StarWarp.SetRadius(0.030000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.110000, 0.020000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.120000, 0.020000)
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
ViewscreenLeftPosition.SetXYZ(-0.060000, 0.060000, 0.020000)
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
ViewscreenRightPosition.SetXYZ(0.060000, 0.060000, 0.020000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.080000, 0.040000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.080000, -0.030000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.110000, 0.020000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(400.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, -0.050000, -0.010000)
Tractors.SetPosition2D(52.000000, 59.000000)
Tractors.SetRepairComplexity(4.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.050000)
Tractors.SetNormalPowerPerSecond(120.000000)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
ForwardTractor = App.TractorBeamProperty_Create("Forward Tractor")

ForwardTractor.SetMaxCondition(400.000000)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(0)
ForwardTractor.SetPrimary(1)
ForwardTractor.SetPosition(0.000000, 0.120000, -0.010000)
ForwardTractor.SetPosition2D(52.000000, 59.000000)
ForwardTractor.SetRepairComplexity(4.000000)
ForwardTractor.SetDisabledPercentage(0.750000)
ForwardTractor.SetRadius(0.040000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(0)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(0.300000)
ForwardTractor.SetIconNum(0)
ForwardTractor.SetIconPositionX(0.000000)
ForwardTractor.SetIconPositionY(0.000000)
ForwardTractor.SetIconAboveShip(1)
ForwardTractor.SetFireSound("Tractor Beam")
ForwardTractor.SetMaxCharge(5.000000)
ForwardTractor.SetMaxDamage(20.000000)
ForwardTractor.SetMaxDamageDistance(100.000000)
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
ForwardTractor.SetArcWidthAngles(-0.698132, 0.698132)
ForwardTractor.SetArcHeightAngles(-0.698132, 0.349066)
ForwardTractor.SetTractorBeamWidth(0.100000)
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
ForwardTractor.SetMainRadius(0.030000)
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

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
