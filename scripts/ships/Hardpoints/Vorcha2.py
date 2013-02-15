#################################################
#	Makes JonKa use only Polaron torpedoes 	#
#################################################

import App
import GlobalPropertyTemplates
	# The line below is needed by the editor to restore
	# the name of the parent script.
ParentPropertyScript = "ships.Hardpoints.Vorcha"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.Vorcha", globals(), locals(), ['*'])
	reload(ParentModule)
# Setting up local templates.
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedo Tubes")

Torpedoes.SetMaxCondition(18000.000000)
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
kFiringChainString.SetString("0;Single;12;Burst")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 400)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.KPolaron")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo Tubes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)