import App
import GlobalPropertyTemplates
# Setting up local templates.
ParentPropertyScript = "ships.Hardpoints.MatanKeldon2"
if not ('g_bIsModelPropertyEditor' in dir(App)):
	ParentModule = __import__("ships.Hardpoints.MatanKeldon2", globals(), locals(), ['*'])
	reload(ParentModule)
#################################################
CloakingDevice = App.CloakingSubsystemProperty_Create("Cloak Generator")

CloakingDevice.SetMaxCondition(2000.000000)
CloakingDevice.SetCritical(0)
CloakingDevice.SetTargetable(1)
CloakingDevice.SetPrimary(1)
CloakingDevice.SetPosition(0.000000, -1.200000, 0.400000)
CloakingDevice.SetPosition2D(80.000000, 60.000000)
CloakingDevice.SetRepairComplexity(3.000000)
CloakingDevice.SetDisabledPercentage(0.750000)
CloakingDevice.SetRadius(0.300000)
CloakingDevice.SetNormalPowerPerSecond(10.000000)
CloakingDevice.SetCloakStrength(200.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CloakingDevice)
#################################################
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	if not ('g_bIsModelPropertyEditor' in dir(App)):
		ParentModule.LoadPropertySet(pObj)
	prop = App.g_kModelPropertyManager.FindByName("Cloak Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)