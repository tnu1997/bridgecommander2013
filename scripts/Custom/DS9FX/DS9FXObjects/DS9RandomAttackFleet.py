from bcdebug import debug
import Custom.DS9FX.DS9FXShips
# Over here we'll precreate a random enemy attack fleet which will show up on your doorstep, so you better defend the Federation teritory

# by USS Sovereign


# UMM Customization
pModule = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.DS9FXConfig")

pRandomDomStrength = pModule.RandomDomStrength
pDominionSide = pModule.DominionSide


# Imports
import App
import loadspacehelper
import MissionLib


# Ship detail def
def DS9SetEnemyShips():
        # 1 ship has to come at least        
        debug(__name__ + ", DS9SetEnemyShips")
        Value = 1

        # We select in between 5 ships, 1 at least has to come lol
        SelectRandomShipNumber = GetRandomRate(Value)

        # Grab the system name from the set file
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()
        import Custom.DS9FX.DS9FXShips

        if pDominionSide == 1:

                if pRandomDomStrength == 2:
                    
                        if SelectRandomShipNumber == 1:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                        elif SelectRandomShipNumber == 2:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))


                        elif SelectRandomShipNumber == 3:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker3))



                        elif SelectRandomShipNumber == 4:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker4))


                        elif SelectRandomShipNumber == 5:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker4))


                                # Create the Attacking ship
                                Att5 = "Attacker 5"
                                pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att5, "Random 5 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att5)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                                pAttacker5 = App.ShipClass_Cast(Attacker5)

                                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker5))


                elif pRandomDomStrength == 1:
                    
                        if SelectRandomShipNumber == 1:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                        elif SelectRandomShipNumber == 2:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))


                        elif SelectRandomShipNumber == 3:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker3))



                        elif SelectRandomShipNumber == 4:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker4))


                        elif SelectRandomShipNumber == 5:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker4))


                                # Create the Attacking ship
                                Att5 = "Attacker 5"
                                pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att5, "Random 5 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att5)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI

                                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                                pAttacker5 = App.ShipClass_Cast(Attacker5)

                                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyRandomAttackFleetAI.CreateAI(pAttacker5))



                
                else:
                    
                        if SelectRandomShipNumber == 1:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                        elif SelectRandomShipNumber == 2:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


                        elif SelectRandomShipNumber == 3:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))



                        elif SelectRandomShipNumber == 4:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


                        elif SelectRandomShipNumber == 5:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


                                # Create the Attacking ship
                                Att5 = "Attacker 5"
                                pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att5, "Random 5 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetFriendlyGroup().AddName(Att5)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                                pAttacker5 = App.ShipClass_Cast(Attacker5)

                                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))

        else:
                if pRandomDomStrength == 2:
                    
                        if SelectRandomShipNumber == 1:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                        elif SelectRandomShipNumber == 2:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


                        elif SelectRandomShipNumber == 3:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))



                        elif SelectRandomShipNumber == 4:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


                        elif SelectRandomShipNumber == 5:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


                                # Create the Attacking ship
                                Att5 = "Attacker 5"
                                pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att5, "Random 5 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att5)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                                pAttacker5 = App.ShipClass_Cast(Attacker5)

                                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))


                elif pRandomDomStrength == 1:
                    
                        if SelectRandomShipNumber == 1:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                        elif SelectRandomShipNumber == 2:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


                        elif SelectRandomShipNumber == 3:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))



                        elif SelectRandomShipNumber == 4:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


                        elif SelectRandomShipNumber == 5:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionBC, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


                                # Create the Attacking ship
                                Att5 = "Attacker 5"
                                pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att5, "Random 5 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att5)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                                pAttacker5 = App.ShipClass_Cast(Attacker5)

                                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))



                
                else:
                    
                        if SelectRandomShipNumber == 1:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                        elif SelectRandomShipNumber == 2:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))


                        elif SelectRandomShipNumber == 3:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))



                        elif SelectRandomShipNumber == 4:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


                        elif SelectRandomShipNumber == 5:
                                # Create the Attacking ship
                                Att1 = "Attacker 1"
                                pAtt1 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att1, "Random 1 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att1)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker1 = MissionLib.GetShip("Attacker 1", DS9Set) 

                                pAttacker1 = App.ShipClass_Cast(Attacker1)

                                pAttacker1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker1))

                                # Create the Attacking ship
                                Att2 = "Attacker 2"
                                pAtt2 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att2, "Random 2 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att2)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker2 = MissionLib.GetShip("Attacker 2", DS9Set) 

                                pAttacker2 = App.ShipClass_Cast(Attacker2)

                                pAttacker2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker2))

                                # Create the Attacking ship
                                Att3 = "Attacker 3"
                                pAtt3 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att3, "Random 3 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att3)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker3 = MissionLib.GetShip("Attacker 3", DS9Set) 

                                pAttacker3 = App.ShipClass_Cast(Attacker3)

                                pAttacker3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker3))


                                # Create the Attacking ship
                                Att4 = "Attacker 4"
                                pAtt4 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att4, "Random 4 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att4)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker4 = MissionLib.GetShip("Attacker 4", DS9Set) 

                                pAttacker4 = App.ShipClass_Cast(Attacker4)

                                pAttacker4.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker4))


                                # Create the Attacking ship
                                Att5 = "Attacker 5"
                                pAtt5 = loadspacehelper.CreateShip(Custom.DS9FX.DS9FXShips.DS9FXDominionFighter, DS9Set, Att5, "Random 5 Location")

                                # Add it to a enemy group
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pMission.GetEnemyGroup().AddName(Att5)

                                # Assign AI
                                import Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI

                                Attacker5 = MissionLib.GetShip("Attacker 5", DS9Set) 

                                pAttacker5 = App.ShipClass_Cast(Attacker5)

                                pAttacker5.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXRandomAttackFleetAI.CreateAI(pAttacker5))


# We randomize number selection with this little def
def GetRandomRate(Number):
    
        debug(__name__ + ", GetRandomRate")
        return App.g_kSystemWrapper.GetRandomNumber(4) + Number
    

# Force BC to assign an AI
def CreateAI(pShip):
	debug(__name__ + ", CreateAI")
	pPlayer = MissionLib.GetPlayer()

        Random = lambda fMin, fMax : App.g_kSystemWrapper.GetRandomNumber((fMax - fMin) * 1000.0) / 1000.0 - fMin
        # Range values used in the AI.
        fInRange = 150.0 + Random(-25, 20)

	#########################################
	# Creating PlainAI Intercept at (279, 253)
	pIntercept = App.PlainAI_Create(pShip, "Intercept")
	pIntercept.SetScriptModule("Intercept")
	pIntercept.SetInterruptable(1)
	pScript = pIntercept.GetScriptInstance()
	pScript.SetTargetObjectName(pPlayer.GetName())
	# Done creating PlainAI Intercept
	#########################################
	#########################################
	# Creating ConditionalAI ConditionIntercept at (148, 273)
	## Conditions:
	#### Condition HaveToIntercept
	pHaveToIntercept = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fInRange, pPlayer.GetName(), pShip.GetName())
	## Evaluation function:
	def EvalFunc(bHaveToIntercept):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bHaveToIntercept:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionIntercept = App.ConditionalAI_Create(pShip, "ConditionIntercept")
	pConditionIntercept.SetInterruptable(1)
	pConditionIntercept.SetContainedAI(pIntercept)
	pConditionIntercept.AddCondition(pHaveToIntercept)
	pConditionIntercept.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionIntercept
	#########################################
	#########################################
	# Creating PlainAI Follow at (280, 181)
	pFollow = App.PlainAI_Create(pShip, "Follow")
	pFollow.SetScriptModule("FollowObject")
	pFollow.SetInterruptable(1)
	pScript = pFollow.GetScriptInstance()
	pScript.SetFollowObjectName(pPlayer.GetName())
	pScript.SetRoughDistances(10,20,30)
	# Done creating PlainAI Follow
	#########################################
	#########################################
	# Creating ConditionalAI PlayerInSameSet at (164, 201)
	## Conditions:
	#### Condition InSet
	pInSet = App.ConditionScript_Create("Conditions.ConditionAllInSameSet", "ConditionAllInSameSet", pShip.GetName(), pPlayer.GetName())
	## Evaluation function:
	def EvalFunc(bInSet):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInSet:
			# Player is in the same set as we are.
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pPlayerInSameSet = App.ConditionalAI_Create(pShip, "PlayerInSameSet")
	pPlayerInSameSet.SetInterruptable(1)
	pPlayerInSameSet.SetContainedAI(pFollow)
	pPlayerInSameSet.AddCondition(pInSet)
	pPlayerInSameSet.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI PlayerInSameSet
	#########################################
	#########################################
	# Creating CompoundAI FollowWarp at (281, 125)
	import AI.Compound.FollowThroughWarp
	pFollowWarp = AI.Compound.FollowThroughWarp.CreateAI(pShip, pPlayer.GetName())
	# Done creating CompoundAI FollowWarp
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (47, 125)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (139, 132)
	pPriorityList.AddAI(pConditionIntercept, 1)
	pPriorityList.AddAI(pPlayerInSameSet, 2)
	pPriorityList.AddAI(pFollowWarp, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (6, 188)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
