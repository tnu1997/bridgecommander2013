# ShipListSubMenu Addition V2.
# This modification of the Foundation allows you to get a submenu in the race list (ie Federation Ships -> Galaxy Class)
# This modification is by MLeoDaalder

import App
import Foundation

if int(Foundation.version[0:8]) < 20040611:
	import FoundationMenu

	class ShipMenuBuilderDef(FoundationMenu.MenuBuilderDef):
		def __init__(self, tglDatabase):
			FoundationMenu.MenuBuilderDef.__init__(self, tglDatabase)

		def __call__(self, raceShipList, menu, buttonType, uiHandler, fWidth = 0.0, fHeight = 0.0):
			foundShips = {}
			for race in raceShipList.keys():
				for ship in raceShipList[race][0]:
					foundShips[race] = 1
					break

			raceList = foundShips.keys()
			raceList.sort()

			for race in raceList:
				self.textButton(race)
				pRaceButton = self.textButton.MakeSubMenu()
				menu.AddChild(pRaceButton)

				shipList = raceShipList[race][1].keys()
				shipList.sort()

				for key in shipList:
					ship = raceShipList[race][1][key]
					self.textButton(ship.name)
					if(ship.__dict__.has_key("SubMenu")):
						if(ship.SubMenu != None and str(ship.SubMenu) != ""):
							if(str(ship.SubMenu)[0] == "[" and str(ship.SubMenu)[len(str(ship.SubMenu)) - 1] == "]" and len(ship.SubMenu) > 0):
								pMenu = pRaceButton
								for name in ship.SubMenu:
									pSubMenu = pMenu.GetSubmenuW(App.TGString(name))
									if(pSubMenu == None):
										pSubMenu = App.STCharacterMenu_Create(name)
										pMenu.AddChild(pSubMenu)
										pMenu.ForceUpdate(0)
									pMenu = pSubMenu
							else:
								pSubMenu = pRaceButton.GetSubmenuW(App.TGString(ship.SubMenu))
								if(pSubMenu == None):
									pSubMenu = App.STCharacterMenu_Create(ship.SubMenu)
									pRaceButton.AddChild(pSubMenu)
									pRaceButton.ForceUpdate(0)
							if(ship.__dict__.has_key("SubSubMenu")):
								if pSubMenu == None:
									pSubMenu = pRaceButton
								if(ship.SubSubMenu != None and str(ship.SubSubMenu) != ""):
									if(str(ship.SubSubMenu)[0] == "[" and str(ship.SubSubMenu)[len(str(ship.SubSubMenu)) - 1] == "]" and len(ship.SubMenu) > 0):
										for name in ship.SubSubMenu:
											pSubSubMenu = pSubMenu.GetSubmenuW(App.TGString(name))
											if(pSubSubMenu == None):
												pSubSubMenu = App.STCharacterMenu_Create(name)
												pSubMenu.AddChild(pSubSubMenu)
												pSubMenu.ForceUpdate(0)
											pSubMenu = pSubSubMenu
									else:
										pSubSubMenu = pSubMenu.GetSubmenuW(App.TGString(ship.SubSubMenu))
										if(pSubSubMenu == None):
											pSubSubMenu = App.STCharacterMenu_Create(ship.SubSubMenu)
											pSubMenu.AddChild(pSubSubMenu)
											pSubMenu.ForceUpdate(0)
										pSubMenu = pSubSubMenu
							pSubMenu.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))
							pSubMenu.ForceUpdate(0)
					elif(ship.__dict__.has_key("SubSubMenu")):
						pSubMenu = pRaceButton
						if(ship.SubSubMenu != None and str(ship.SubSubMenu) != ""):
							if(str(ship.SubSubMenu)[0] == "[" and str(ship.SubSubMenu)[len(str(ship.SubSubMenu)) - 1] == "]" and len(ship.SubSubMenu) > 0):
								for name in ship.SubSubMenu:
									pSubSubMenu = pSubMenu.GetSubmenuW(App.TGString(name))
									if(pSubSubMenu == None):
										pSubSubMenu = App.STCharacterMenu_Create(name)
										pSubMenu.AddChild(pSubSubMenu)
										pSubMenu.ForceUpdate(0)
									pSubMenu = pSubSubMenu
							else:
								pSubSubMenu = pSubMenu.GetSubmenuW(App.TGString(ship.SubSubMenu))
								if(pSubSubMenu == None):
									pSubSubMenu = App.STCharacterMenu_Create(ship.SubSubMenu)
									pSubMenu.AddChild(pSubSubMenu)
									pSubMenu.ForceUpdate(0)
								pSubMenu = pSubSubMenu
						pSubMenu.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))
						pSubMenu.ForceUpdate(0)
					else:
						pRaceButton.AddChild(self.textButton.MakeIntButton(buttonType, ship.num, uiHandler, fWidth, fHeight))

				pRaceButton.ForceUpdate(0)

	FoundationMenu.ShipMenuBuilderDef = ShipMenuBuilderDef
	Foundation.version = "20040611"
	print "Updating FoundationMenu.ShipMenuBuilderDef V2"
