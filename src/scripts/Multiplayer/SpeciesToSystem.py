from bcdebug import debug
import App

# types for initializing objects create from C.
UNKNOWN		= 0
MULTI1 		= 1
MULTI2 		= 2
MULTI3 		= 3
MULTI4 		= 4
MULTI5 		= 5
MULTI6		= 6
MULTI7 		= 7
ALBIREA 	= 8
POSEIDON	= 9
ALIOTH		= 10
ARTRUS		= 11
ASCELLA		= 12
BELARUZ		= 13
BEOL		= 14
BIRANU		= 15
CEBALRAI	= 16
CHAMBANA	= 17
GEBLE		= 18
ITARI		= 19
NEPENTHE	= 20
OMEGADRACONIS	= 21
ONA		= 22
PRENDEL		= 23
SAVOY		= 24
SERRIS		= 25
TEVRON		= 26
TEZLE		= 27
VESUVI		= 28
VOLTAIR		= 29
XIENTRADES	= 30
YILES		= 31
BANZAI          = 32
ARENAA          = 33
BEYONDTHEGALAXY = 34
BOREALIS        = 35
EARTH           = 36
BRIARPATCH      = 37
CALUFRAX        = 38
KHAN            = 39
CJONES          = 40
SMOKERING       = 41
GASGIANT        = 42
KRONOS          = 43
ROMULUS         = 44
ROSS_128        = 45
VULCAN          = 46
SIRIUS_B        = 47
UNIVERSE        = 48
COMET           = 49
JUNKYARD        = 50
NURSERY         = 51
RAINBOW         = 52
STRING          = 53
THEGALAXY       = 54
WOLF359         = 55
BETELGEUSE      = 56
PLEIDES         = 57
PROCYON         = 58
SYSTEMJ25       = 59
VATRIS          = 60
BAQIS           = 61
REDGIANT        = 62
GALAXYEDGE      = 63
KASTRA          = 64
ARCTURUS        = 65
CANOPUS         = 66
HEKARAS         = 67
TATHIS          = 68
BADLANDS        = 69
KAVISALPHA      = 70
SOL             = 71
VOID            = 72
CARDASSIA	= 73

MAX_SYSTEMS = 74

# Setup tuple
kSpeciesTuple = (
	(UNKNOWN		, None),
	(MULTI1			, "Multi1"),
	(MULTI2			, "Multi2"),
	(MULTI3			, "Multi3"),
	(MULTI4			, "Multi4"),
	(MULTI5			, "Multi5"),
	(MULTI6			, "Multi6"),
	(MULTI7			, "Multi7"),
	(ALBIREA		, "Albirea"),
	(POSEIDON		, "Poseidon"),
	(ALIOTH			, "Alioth"),
	(ARTRUS			, "Artrus"),
	(ASCELLA		, "Ascella"),
	(BELARUZ		, "Belaruz"),
	(BEOL			, "Beol"),
	(BIRANU			, "Biranu"),
	(CEBALRAI		, "Cebalrai"),
	(CHAMBANA		, "Chambana"),
	(GEBLE			, "Geble"),
	(ITARI			, "Itari"),
	(NEPENTHE		, "Nepenthe"),
	(OMEGADRACONIS		, "OmegaDraconis"),
	(ONA			, "Ona"),
	(PRENDEL		, "Prendel"),
	(SAVOY			, "Savoy"),
	(SERRIS			, "Serris"),
	(TEVRON			, "Tevron"),
	(TEZLE			, "Tezle"),
	(VESUVI			, "Vesuvi"),
	(VOLTAIR		, "Voltair"),
	(XIENTRADES		, "XiEntrades"),
	(YILES			, "Yiles"),
        (BANZAI                 , "Banzai"),
        (ARENAA                 , "ArenaA"),
        (BEYONDTHEGALAXY        , "BeyondTheGalaxy"),
        (BOREALIS               , "Borealis"),
        (EARTH                  , "Earth"),
        (BRIARPATCH             , "BriarPatch"),
        (CALUFRAX               , "Calufrax"),
        (KHAN                   , "Khan"),
        (CJONES                 , "CJones"),
        (SMOKERING              , "SmokeRing"),
        (GASGIANT               , "GasGiant"),
        (KRONOS                 , "Kronos"),
        (ROMULUS                , "Romulus"),
        (ROSS_128               , "Ross_128"),
        (VULCAN                 , "Vulcan"),
        (SIRIUS_B               , "Sirius_B"),
        (UNIVERSE               , "Universe"),
        (COMET		        , "Comet"),
        (JUNKYARD		, "Junkyard"),
        (NURSERY		, "Nursery"),
        (RAINBOW		, "Rainbow"),
        (STRING		        , "String"),
        (THEGALAXY		, "TheGalaxy"),
        (WOLF359		, "Wolf359"),
        (BETELGEUSE		, "Betelgeuse"),
        (PLEIDES		, "Pleides"),
        (PROCYON		, "Procyon"),
        (SYSTEMJ25		, "SystemJ25"),
        (VATRIS 		, "Vatris"),
        (BAQIS  		, "Baqis"),
        (REDGIANT		, "RedGiant"),
        (GALAXYEDGE		, "GalaxyEdge"),
        (KASTRA 		, "Kastra"),
        (ARCTURUS		, "Arcturus"),
        (CANOPUS		, "Canopus"),
        (HEKARAS		, "Hekaras"),
        (TATHIS 		, "Tathis"),
        (BADLANDS		, "Badlands"),
        (KAVISALPHA		, "KavisAlpha"),
        (SOL                    , "Sol"),
        (VOID                    , "Void"),
	(CARDASSIA                    , "Cardassia"),
        
        (MAX_SYSTEMS	, None))



def CreateSystemFromSpecies (iSpecies):
	debug(__name__ + ", CreateSystemFromSpecies")
	if (iSpecies <= 0 or iSpecies >= MAX_SYSTEMS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	pcScript = pSpecTuple [1]

	# import the module.
	pModule = __import__("Systems." + pcScript + "." + pcScript)

	# call CreateMenu function to create the system and setup warp menus
	pCourseMenu = pModule.CreateMenus ()
	pStartingSet = pCourseMenu.InitializeAllSets ()

	return pStartingSet

def GetScriptFromSpecies (iSpecies):
	debug(__name__ + ", GetScriptFromSpecies")
	if (iSpecies <= 0 or iSpecies >= MAX_SYSTEMS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	return pSpecTuple [1]
	



	
