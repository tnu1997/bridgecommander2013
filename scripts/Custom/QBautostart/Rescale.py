import App
import MissionLib

MODINFO = { "needBridge": 0 }

# use the ShipName of the Hardpoint file as key here
g_dShipScales = {
        "USS Lakota": 0.4,
}


def ObjectCreatedHandler(pObject, pEvent):
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if pShip:
                sShipProbName = pShip.GetShipProperty().GetShipName()
                for sCurName in g_dShipScales.keys():
                        if sCurName == sShipProbName:
                                pShip.SetScale(g_dShipScales[sCurName])
        
        pObject.CallNextHandler(pEvent)


def init():
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, MissionLib.GetMission(), __name__ + ".ObjectCreatedHandler")
