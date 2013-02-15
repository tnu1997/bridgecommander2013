# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\ModifiedTelTak.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(900.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(67.000000, 47.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.100000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SublightEngines = App.ImpulseEngineProperty_Create("Sublight Engines")

SublightEngines.SetMaxCondition(2000.000000)
SublightEngines.SetCritical(0)
SublightEngines.SetTargetable(0)
SublightEngines.SetPrimary(1)
SublightEngines.SetPosition(0.000000, 0.000000, 0.000000)
SublightEngines.SetPosition2D(51.000000, 48.000000)
SublightEngines.SetRepairComplexity(1.000000)
SublightEngines.SetDisabledPercentage(0.500000)
SublightEngines.SetRadius(0.003000)
SublightEngines.SetNormalPowerPerSecond(20.000000)
SublightEngines.SetMaxAccel(4.200000)
SublightEngines.SetMaxAngularAccel(2.500000)
SublightEngines.SetMaxAngularVelocity(0.750000)
SublightEngines.SetMaxSpeed(6.500000)
SublightEngines.SetEngineSound("AlkeshEngine")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngines)
#################################################
ReactorModule = App.PowerProperty_Create("Reactor Module")

ReactorModule.SetMaxCondition(1500.000000)
ReactorModule.SetCritical(1)
ReactorModule.SetTargetable(1)
ReactorModule.SetPrimary(1)
ReactorModule.SetPosition(0.000000, -0.150000, 0.020000)
ReactorModule.SetPosition2D(65, 55)
ReactorModule.SetRepairComplexity(3.000000)
ReactorModule.SetDisabledPercentage(0.400000)
ReactorModule.SetRadius(0.025000)
ReactorModule.SetMainBatteryLimit(100000.000000)
ReactorModule.SetBackupBatteryLimit(20000.000000)
ReactorModule.SetMainConduitCapacity(200.000000)
ReactorModule.SetBackupConduitCapacity(100.000000)
ReactorModule.SetPowerOutput(200.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ReactorModule)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(800.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.190000, -0.030000)
SensorArray.SetPosition2D(65, 15)
SensorArray.SetRepairComplexity(2.000000)
SensorArray.SetDisabledPercentage(0.600000)
SensorArray.SetRadius(0.010000)
SensorArray.SetNormalPowerPerSecond(20.000000)
SensorArray.SetBaseSensorRange(2000.000000)
SensorArray.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(2000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, -0.050000)
ShieldGenerator.SetPosition2D(65, 41)
ShieldGenerator.SetRepairComplexity(3.500000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.020000)
ShieldGenerator.SetNormalPowerPerSecond(40.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 600.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 1.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 1.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 1.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 1.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 1.500000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 1.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
ModifiedTelTak = App.ShipProperty_Create("Modified TelTak")

ModifiedTelTak.SetGenus(1)
ModifiedTelTak.SetSpecies(793)
ModifiedTelTak.SetMass(10000.000000)
ModifiedTelTak.SetRotationalInertia(2000.000000)
ModifiedTelTak.SetShipName("ModifiedTelTak")
ModifiedTelTak.SetModelFilename("data/Models/Ships/TelTak/TelTak.nif")
ModifiedTelTak.SetDamageResolution(0.000100)
ModifiedTelTak.SetAffiliation(0)
ModifiedTelTak.SetStationary(0)
ModifiedTelTak.SetAIString("NonFedAttack")
ModifiedTelTak.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(ModifiedTelTak)
#################################################
SublightEngine = App.EngineProperty_Create("Sublight Engine")

SublightEngine.SetMaxCondition(1000.000000)
SublightEngine.SetCritical(0)
SublightEngine.SetTargetable(1)
SublightEngine.SetPrimary(1)
SublightEngine.SetPosition(0.000000, -0.200000, -0.025000)
SublightEngine.SetPosition2D(65, 93)
SublightEngine.SetRepairComplexity(2.000000)
SublightEngine.SetDisabledPercentage(0.500000)
SublightEngine.SetRadius(0.025000)
SublightEngine.SetEngineType(SublightEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngine)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.175000, 0.000000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 0.170000, 0.000000)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(0.000000, 0.170000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.185000, 0.000000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 0.072000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -0.025000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.320000, 0.030000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(2000.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(0.000000, 0.000000)
Engineering.SetRepairComplexity(1.000000)
Engineering.SetDisabledPercentage(0.500000)
Engineering.SetRadius(0.060000)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(5.000000)
Engineering.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
Peltak = App.HullProperty_Create("Peltak")

Peltak.SetMaxCondition(2000.000000)
Peltak.SetCritical(1)
Peltak.SetTargetable(1)
Peltak.SetPrimary(0)
Peltak.SetPosition(0.000000, 0.165000, -0.005000)
Peltak.SetPosition2D(65, 27)
Peltak.SetRepairComplexity(3.000000)
Peltak.SetDisabledPercentage(0.000000)
Peltak.SetRadius(0.010000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Peltak)
#################################################
Hyperdrive1 = App.HullProperty_Create("Hyperdrive 1")

Hyperdrive1.SetMaxCondition(1000.000000)
Hyperdrive1.SetCritical(0)
Hyperdrive1.SetTargetable(1)
Hyperdrive1.SetPrimary(0)
Hyperdrive1.SetPosition(0.000000, -0.150000, 0.000000)
Hyperdrive1.SetPosition2D(65, 79)
Hyperdrive1.SetRepairComplexity(1.000000)
Hyperdrive1.SetDisabledPercentage(0.000000)
Hyperdrive1.SetRadius(0.025000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hyperdrive1)
#################################################
EnergyBeam = App.WeaponSystemProperty_Create("Energy Beam")

EnergyBeam.SetMaxCondition(200.000000)
EnergyBeam.SetCritical(0)
EnergyBeam.SetTargetable(0)
EnergyBeam.SetPrimary(1)
EnergyBeam.SetPosition(0.000000, 0.000000, 0.000000)
EnergyBeam.SetPosition2D(0.000000, 0.000000)
EnergyBeam.SetRepairComplexity(1.000000)
EnergyBeam.SetDisabledPercentage(0.500000)
EnergyBeam.SetRadius(0.250000)
EnergyBeam.SetNormalPowerPerSecond(150.000000)
EnergyBeam.SetWeaponSystemType(EnergyBeam.WST_PHASER)
EnergyBeam.SetSingleFire(0)
EnergyBeam.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
EnergyBeam.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(EnergyBeam)
#################################################
EnergyWeapon = App.PhaserProperty_Create("Energy Weapon")

EnergyWeapon.SetMaxCondition(1000.000000)
EnergyWeapon.SetCritical(0)
EnergyWeapon.SetTargetable(1)
EnergyWeapon.SetPrimary(1)
EnergyWeapon.SetPosition(0.000000, -0.088000, -0.070000)
EnergyWeapon.SetPosition2D(65, 66)
EnergyWeapon.SetRepairComplexity(1.000000)
EnergyWeapon.SetDisabledPercentage(0.500000)
EnergyWeapon.SetRadius(0.025000)
EnergyWeapon.SetDumbfire(0)
EnergyWeapon.SetWeaponID(0)
EnergyWeapon.SetGroups(0)
EnergyWeapon.SetDamageRadiusFactor(0.250000)
EnergyWeapon.SetIconNum(365)
EnergyWeapon.SetIconPositionX(75)
EnergyWeapon.SetIconPositionY(79)
EnergyWeapon.SetIconAboveShip(1)
EnergyWeapon.SetFireSound("CargoBeam")
EnergyWeapon.SetMaxCharge(100.000000)
EnergyWeapon.SetMaxDamage(100.000000)
EnergyWeapon.SetMaxDamageDistance(100.000000)
EnergyWeapon.SetMinFiringCharge(50.750000)
EnergyWeapon.SetNormalDischargeRate(1.000000)
EnergyWeapon.SetRechargeRate(2.750000)
EnergyWeapon.SetIndicatorIconNum(0)
EnergyWeapon.SetIndicatorIconPositionX(15)
EnergyWeapon.SetIndicatorIconPositionY(15)
EnergyWeaponForward = App.TGPoint3()
EnergyWeaponForward.SetXYZ(0.000000, 0.000000, -1.000000)
EnergyWeaponUp = App.TGPoint3()
EnergyWeaponUp.SetXYZ(0.000000, 1.000000, 0.000000)
EnergyWeapon.SetOrientation(EnergyWeaponForward, EnergyWeaponUp)
EnergyWeapon.SetWidth(0.001000)
EnergyWeapon.SetLength(0.001000)
EnergyWeapon.SetArcWidthAngles(-0.174533, 0.174533)
EnergyWeapon.SetArcHeightAngles(-0.174533, 0.174533)
EnergyWeapon.SetPhaserTextureStart(0)
EnergyWeapon.SetPhaserTextureEnd(0)
EnergyWeapon.SetPhaserWidth(0.035000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.949020)
EnergyWeapon.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.949020)
EnergyWeapon.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.949020)
EnergyWeapon.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.984314)
EnergyWeapon.SetInnerCoreColor(kColor)
EnergyWeapon.SetNumSides(6)
EnergyWeapon.SetMainRadius(0.050000)
EnergyWeapon.SetTaperRadius(0.040000)
EnergyWeapon.SetCoreScale(0.500000)
EnergyWeapon.SetTaperRatio(0.250000)
EnergyWeapon.SetTaperMinLength(5.000000)
EnergyWeapon.SetTaperMaxLength(30.000000)
EnergyWeapon.SetLengthTextureTilePerUnit(0.500000)
EnergyWeapon.SetPerimeterTile(1.000000)
EnergyWeapon.SetTextureSpeed(2.500000)
EnergyWeapon.SetTextureName("data/textures/tactical/CAFerengi.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(EnergyWeapon)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Modified TelTak", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Reactor Module", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Peltak", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperdrive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Energy Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Energy Weapon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
