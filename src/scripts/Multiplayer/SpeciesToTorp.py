from bcdebug import debug
import App

# types for initializing torps create from C.
UNKNOWN = 0
DISRUPTOR = 1
PHOTON = 2
QUANTUM = 3
ANTIMATTER = 4
CARDTORP = 5
KLINGONTORP = 6
POSITRON = 7
PULSEDISRUPT = 8
FUSIONBOLT = 9
CARDASSIANDISRUPTOR = 10
KESSOKDISRUPTOR = 11
PHASEDPLASMA = 12
POSITRON2 = 13
PHOTON2 = 14
ROMULANCANNON = 15
ACHMICROQUANTUM = 16
CARDASSIANXTORP = 17
BORGMINI2 = 18
BREENTORPEDOXL = 19
BREENTORPEDO = 20
DOMCANNON2 = 21
DURPHASEQUANTUM = 22
DUMMY = 23
DOMFUSIONBOLT = 24
DISRUPTORSDV = 25
DYFUTILE = 26
DYBORGTORPEDO = 27
SMALLPULSE = 28
MPNEGHVARTORP = 29
ENERGYDISSIPATOR = 30
MICROQUANTUM = 31
LCRAPTOR = 32
MPNEGHVARPULSE = 33
KVORTTORP = 34
KVORTPULSE = 35
KAZONTORPEDO = 36
GATLING = 37
ORIONMISSILE = 38
DOMTORPEDO = 39
PHASEQUANTUM = 40
PULSEPHASER = 41
PHALANTIUM = 42
PHOTONMULTTARGET = 43
PHOTONMULT = 44
PHOTON2MULTTARGET = 45
PHOTON2MULT = 46
PRETOS = 47
POSITRON2 = 48
POLERON = 49
VOYAGERTORP = 50
TRICOBALT = 51
STATIONPHOTON = 52
ROMULANTORPEDO = 53
ROMPLASMAMED = 54
ROMPLASMALIGHT = 55
ROMPLASMAHEAVY = 56
REMANPULSE = 57
REMANPHOTON = 58
RAPIDQUANTUM = 59
ROMPLASMAPULSE = 60
ROMPHASEDDISRUPTOR = 61
VENTUREPHOTON = 62
FIREHAWKBLAST = 63
DEATHCHANT = 64
IONSTORM = 65
REPULSIONWAVE = 66
DISRUPTOR2 = 67
BORGNANITES = 68
SONABTORP = 69
BORGDISRUPTOR = 70
BORGHAIL = 71
BORGMINI = 72
BORGPULSE = 73
BORGTORPEDO = 74
CACARDTORP = 75
CAGREENKLINGONTORP = 76
CAREDKLINGONTORP = 77
CAPHASEQUANTUM = 78
CAQUANTUMX = 79
CAZZPOLARON = 80
DGBORGTORP = 81
DGBORGTORPEDO = 82
DGDIAMONDTORP = 83
DGGRAVIMETRIC = 84
DGGRAVIMETRIC2 = 85
REMANCANNONXI = 87
SHIELDDISRUPTOR = 88
ULTRIUMBURST = 89
VALDOREDISRUPTOR = 90
WARBIRDCANNON = 91
BORGCANNON = 92
ZZ_BREENTORP = 93
ZZ_POLARONTORP = 94
ZZ_ROMTORPTNG = 95
CASONA = 96
CASONAPHOTON = 97
PHOTON3 = 98
PHOTON4 = 99
CAROMULANHEAVY = 100
TACHYON = 101
SHUTTLEDISRUPTOR = 102
KLINGONBASEDISRUPTOR = 103
KLINGONBASETORP = 104
MIRADORNTORP = 105
MIRADORNDISRUPTOR = 106
MERCHANT = 107
SFPBUGTORP = 108
IONTORP = 109
CAJUNK = 110
COWPTORP = 111
DFBORGTORPEDO = 112

MAX_TORPS = 113


# Setup tuples
kSpeciesTuple = ((UNKNOWN, None),
        (DISRUPTOR, "Disruptor"),
        (PHOTON, "PhotonTorpedo"),
        (QUANTUM, "QuantumTorpedo"),
        (ANTIMATTER, "AntimatterTorpedo"),
        (CARDTORP, "CardassianTorpedo"),
        (KLINGONTORP, "KlingonTorpedo"),
        (POSITRON, "PositronTorpedo"),
        (PULSEDISRUPT, "PulseDisruptor"),
        (FUSIONBOLT, "FusionBolt"),
        (CARDASSIANDISRUPTOR, "CardassianDisruptor"),
        (KESSOKDISRUPTOR, "KessokDisruptor"),
        (PHASEDPLASMA, "PhasedPlasma"),
        (POSITRON2, "PositronTorpedo2"),
        (PHOTON2, "PhotonTorpedo2"),
        (ROMULANCANNON, "RomulanCannon"),
        (ACHMICROQUANTUM, "MicroQuantum"),
        (CARDASSIANXTORP, "CardassianXTorpedo"),
        (BORGMINI2, "Borgmini2"),
        (BREENTORPEDOXL, "BreenTorpedoXL"),
        (BREENTORPEDO, "BreenTorpedo"),        
        (DOMCANNON2, "DomCannon2"),
        (DURPHASEQUANTUM, "Dur_PhaseQuantum"),
        (DUMMY, "Dummy"),
        (DOMFUSIONBOLT, "DomFusionBolt"),
        (DISRUPTORSDV, "Disruptor SDV"),
        (DYFUTILE, "DYfutile"),
        (DYBORGTORPEDO, "DYborgtorpedo"),
        (SMALLPULSE, "SmallPulse"),
        (MPNEGHVARTORP, "MPneghvartorp"),
        (ENERGYDISSIPATOR, "Energy Dissipator"),
        (MICROQUANTUM, "MicroQuantum"),
        (LCRAPTOR, "LCRaptor"),
        (MPNEGHVARPULSE, "MPneghvarpulse"),
        (KVORTTORP, "KvortTorpedo"),
        (KVORTPULSE, "KvortPulse"),
        (KAZONTORPEDO, "KazonTorpedo"),
        (GATLING, "Gatling"),
        (ORIONMISSILE, "Orionmissile"),
        (DOMTORPEDO, "DomTorpedo"),
        (PHASEQUANTUM, "PhaseQuantum"),
        (PULSEPHASER, "PulsePhaser"),
        (PHALANTIUM, "Phalantium"),
        (PHOTONMULTTARGET, "PhotonTorpedoMultipleTarget"),
        (PHOTONMULT, "PhotonTorpedoMultiple"),
        (PHOTON2MULTTARGET, "PhotonTorpedo2MultipleTarget"),
        (PHOTON2MULT, "PhotonTorpedo2Multiple"),
        (PRETOS, "preTOS"),
        (POSITRON2, "PositronTorpedo2"),
        (POLERON, "PoleronJLH"),
        (VOYAGERTORP, "VoyagerTorpedo"),
        (TRICOBALT, "TricobaltTorpedo"),
        (STATIONPHOTON, "StationPhotonTorpedo"),
        (ROMULANTORPEDO, "RomulanTorp"),
        (ROMPLASMAMED, "RomulanPlasmaMedium"),
        (ROMPLASMALIGHT, "RomulanPlasmaLight"),
        (ROMPLASMAHEAVY, "RomulanPlasmaHeavy"),
        (REMANPULSE, "RemanClass1Pulse"),
        (REMANPHOTON, "RemanClass1Photon"),
        (RAPIDQUANTUM, "RapidQuantum"),
        (ROMPLASMAPULSE, "RomulanPlasmaPulse"),
        (ROMPHASEDDISRUPTOR, "RomulanPhasedDisruptor"),
        (VENTUREPHOTON, "VentureScoutPhoton"),
        (FIREHAWKBLAST, "FirehawkBlast"),
        (DEATHCHANT, "DeathChant"),
        (IONSTORM, "IonStorm"),
        (REPULSIONWAVE, "RepulsionWave"),
        (DISRUPTOR2, "Disruptor2"),
        (BORGNANITES, "BorgNanites"),
        (SONABTORP, "SonaBTORP"),
        (BORGDISRUPTOR, "BorgDisruptor"),
        (BORGHAIL, "BorgHail"),
        (BORGMINI, "BorgMini"),
        (BORGPULSE, "BorgPulse"),
        (BORGTORPEDO, "BorgTorpedo"),
        (CACARDTORP, "CACardassianTorpedo"),
        (CAGREENKLINGONTORP, "CAKlingonTorpedoGreen"),
        (CAREDKLINGONTORP, "CAKlingonTorpedoRed"),
        (CAPHASEQUANTUM, "CAPhaseQuantum"),
        (CAQUANTUMX, "CAQuantumX"),
        (CAZZPOLARON, "CAZZ_PolaronTorp"),
        (DGBORGTORP, "DGBorgTorp"),
        (DGBORGTORPEDO, "DGBorgTorpedo"),
        (DGDIAMONDTORP, "DGDiamondTorp"),
        (DGGRAVIMETRIC, "DGGravimetric"),
        (DGGRAVIMETRIC2, "DGGravimetric2"),
        (REMANCANNONXI, "RemanCannonXI"),
        (SHIELDDISRUPTOR, "ShieldDisruptor"),
        (ULTRIUMBURST, "UltriumBurst"),
        (VALDOREDISRUPTOR, "ValdoreDisruptorCube"),
        (WARBIRDCANNON, "WarbirdCannon"),
        (BORGCANNON, "BorgCannon"),
        (ZZ_BREENTORP, "ZZ_BreenTorp"),
        (ZZ_POLARONTORP, "ZZ_PolaronTorp"),
        (ZZ_ROMTORPTNG, "ZZ_RomTorpTNG"),
        (CASONA, "CASona"),
        (CASONAPHOTON, "CASonaPhoton"),
        (PHOTON3, "PhotonTorpedo3"),
        (PHOTON4, "PhotonTorpedo4"),
        (CAROMULANHEAVY, "CARomulanHeavy"),
        (TACHYON, "CATachyon"),
        (SHUTTLEDISRUPTOR, "ShuttlePulseDisruptor"),
        (KLINGONBASEDISRUPTOR, "KlingbaseDisruptor"),
        (KLINGONBASETORP, "Liklingbasetorp"),
        (MIRADORNTORP, "MiradornTorpedo"),
        (MIRADORNDISRUPTOR, "MiradornDisruptor"),
        (MERCHANT, "Merchant"),
        (SFPBUGTORP, "SFPBugTorpedo"),
        (IONTORP, "CAIonTorpedo"),
	(CAJUNK, "CAJunkTorpedo"),
	(COWPTORP, "cOWPTorpedo"),
	(DFBORGTORPEDO, "DFBorgTorpedo"),

        (MAX_TORPS, None))

def CreateTorpedoFromSpecies (iSpecies):
	debug(__name__ + ", CreateTorpedoFromSpecies")
	if (iSpecies <= 0 or iSpecies >= MAX_TORPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	pcScript = pSpecTuple [1]

	pTorp = App.Torpedo_Create (pcScript)
	return pTorp

def GetScriptFromSpecies (iSpecies):
	debug(__name__ + ", GetScriptFromSpecies")
	if (iSpecies <= 0 or iSpecies >= MAX_TORPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	return pSpecTuple [1]
	
def InitObject (self, iType):
	# Get the script
	debug(__name__ + ", InitObject")
	pcScript = GetScriptFromSpecies (iType)
	if (pcScript == None):
		return 0

	# call create function to initialize the torp.
	mod = __import__("Tactical.Projectiles." + pcScript)
	mod.Create(self)	

	self.UpdateNodeOnly ()

	return 1;
	
