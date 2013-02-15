import App
import FoundationTech
import loadspacehelper

dTorpShips = {}

class Rocket(FoundationTech.TechDef):
	def __init__(self, name, dict = None):
		FoundationTech.TechDef.__init__(self, name, dict)
		self.__dict__.update(dict)
	def OnFire(self, pEvent, pTorp):
		print 'SolidTorpedoTorpedo.OnFire'

		pTorpID = pTorp.GetObjID()

		try:
			#print "Creating ship:", self.sModel, pTorp.GetContainingSet(), "SolidTorpedo"+str(pTorpID)
			pTorpShip = loadspacehelper.CreateShip(self.sModel, pTorp.GetContainingSet(), "SolidTorpedo" + str(pTorpID), "")
			pTorpShip.SetCollisionFlags(0)
			global dTorpShips
			dTorpShips[pTorpID] = pTorpShip
			pTorp.AttachObject(pTorpShip)
			pTorp.AddPythonFuncHandlerForInstance(App.ET_WEAPON_HIT, __name__ + ".TorpedoHit")
		except:
			print "Creating ship failed somehow..."
	def OnYield(self, pEvent, pTorp):
		pass # Handled by TorpedoHit

def TorpedoHit(pObject, pEvent):
	pTorp = None
	pTorp = App.TorpedoClass_Cast(pObject)
	if not pTorp:
		pObject.CallNextHandler(pEvent)
		return

	global dTorpShips
	pTorpID = pTorp.GetObjID()
	if not dTorpShips.has_key(pTorpID):
		pObject.CallNextHandler(pEvent)
		return
	if not dTorpShips[pTorpID]:
		pObject.CallNextHandler(pEvent)
		return
	pSet = pTorp.GetContainingSet()
	if not pSet:
		pObject.CallNextHandler(pEvent)
		return
	pSet.DeleteObjectFromSet(dTorpShips[pTorpID].GetName())
	pObject.CallNextHandler(pEvent)
