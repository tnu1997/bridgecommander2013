from bcdebug import debug
import App

# This function returns the name of the mission to be displayed in the file
# dialog.  The return must be a TGString
def GetMissionName():
	debug(__name__ + ", GetMissionName")
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/MultiplayerMissions.tgl")

	pString = pDatabase.GetString("Mission10")

	App.g_kLocalizationManager.Unload(pDatabase)

	return pString

# This function returns the description of the mission to be displayed in the
# host dialog.  The return must be a TGString
def GetMissionDescription():
	debug(__name__ + ", GetMissionDescription")
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/MultiplayerMissions.tgl")

	pString = pDatabase.GetString("Mission10 Description")

	App.g_kLocalizationManager.Unload(pDatabase)

	return pString

# This function returns a short version of the mission name for the join game browser
def GetMissionShortName():
	debug(__name__ + ", GetMissionShortName")
	pDatabase = App.g_kLocalizationManager.Load("data/TGL/MultiplayerMissions.tgl")

	pString = pDatabase.GetString("Mission10 Short Name")

	App.g_kLocalizationManager.Unload(pDatabase)

	return pString