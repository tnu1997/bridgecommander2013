##############################################################################
#	Filename:	LoadTacticalSounds.py
#
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#
#	This contains the code to load tactical sounds.
#
#	Created:	9/12/00 -	DLitwin
#	Edited:		6/14-06 -	Bryan Cook
##############################################################################
import App

# Dasher42's sound plugin support
import Foundation

###############################################################################
#	LoadSounds()
#
#	Load sounds that are needed throughout the game, in tactical.
#
#	Args:	none
#
#	Return:	none
###############################################################################
def LoadSounds(mode = Foundation.MutatorDef.StockSounds):
	pGame = App.Game_GetCurrentGame()
	for i in mode.sounds.values():
		pGame.LoadSound(i.fileName,	i.name,	App.TGSound.LS_3D).SetVolume(i.volume)
	
	pGame.LoadSound("sfx/enter warp.wav",				"Enter Warp",			App.TGSound.LS_3D).SetVolume(3.0)
	pGame.LoadSound("sfx/exit warp.wav",				"Exit Warp",			App.TGSound.LS_3D).SetVolume(6.0)
	pGame.LoadSound("sfx/warp flash.wav",				"Warp Flash",			0)

# NanoFX Sounds added with good volume levels!
	pGame.LoadSound("sfx/Explosions/shieldhit1.WAV",		"Explosion 1",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit2.WAV",		"Explosion 2",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit3.WAV",		"Explosion 3",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit4.WAV",		"Explosion 4",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit5.WAV",		"Explosion 5",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit6.WAV",		"Explosion 6",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit7.WAV",		"Explosion 7",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit8.WAV",		"Explosion 8",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit9.WAV",		"Explosion 9",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit10.WAV",		"Explosion 10",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit11.WAV",		"Explosion 11",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit12.WAV",		"Explosion 12",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit13.WAV",		"Explosion 13",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit14.WAV",		"Explosion 14",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit15.WAV",		"Explosion 15",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit16.WAV",		"Explosion 16",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit17.WAV",		"Explosion 17",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit18.WAV",		"Explosion 18",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit19.WAV",		"Explosion 19",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit20.WAV",		"Explosion 20",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit21.WAV",		"Explosion 21",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit22.WAV",		"Explosion 22",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit23.WAV",		"Explosion 23",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit24.WAV",		"Explosion 24",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit25.WAV",		"Explosion 25",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit26.WAV",		"Explosion 26",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/shieldhit27.WAV",		"Explosion 27",			App.TGSound.LS_3D).SetVolume(8.0)
	

	pGame.LoadSound("sfx/Explosions/explo1.WAV","Death Explosion 1",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo2.WAV","Death Explosion 2",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo3.WAV","Death Explosion 3",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo4.WAV","Death Explosion 4",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo5.WAV","Death Explosion 5",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo6.WAV","Death Explosion 6",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo7.WAV","Death Explosion 7",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo8.WAV","Death Explosion 8",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo9.WAV","Death Explosion 9",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo10.WAV","Death Explosion 10",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo11.WAV","Death Explosion 11",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo12.WAV","Death Explosion 12",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo13.WAV","Death Explosion 13",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo14.WAV","Death Explosion 14",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo15.WAV","Death Explosion 15",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo16.WAV","Death Explosion 16",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo17.WAV","Death Explosion 17",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo18.WAV","Death Explosion 18",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo19.WAV","Death Explosion 19",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo20.WAV","Death Explosion 20",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo21.WAV","Death Explosion 21",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo22.WAV","Death Explosion 22",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo23.WAV","Death Explosion 23",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo24.WAV","Death Explosion 24",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo25.WAV","Death Explosion 25",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo26.WAV","Death Explosion 26",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo27.WAV","Death Explosion 27",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo28.WAV","Death Explosion 28",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo29.WAV","Death Explosion 29",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo30.WAV","Death Explosion 30",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo31.WAV","Death Explosion 31",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo32.WAV","Death Explosion 32",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo33.WAV","Death Explosion 33",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo34.WAV","Death Explosion 34",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo35.WAV","Death Explosion 35",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo36.WAV","Death Explosion 36",	App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explo37.WAV","Death Explosion 37",	App.TGSound.LS_3D).SetVolume(10.0)
	
	pGame.LoadSound("sfx/Explosions/explolarge1.WAV","Big Death Explosion 1",App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explolarge2.WAV","Big Death Explosion 2",App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explolarge3.WAV","Big Death Explosion 3",App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explolarge4.WAV","Big Death Explosion 4",App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explolarge5.WAV","Big Death Explosion 5",App.TGSound.LS_3D).SetVolume(10.0)
	pGame.LoadSound("sfx/Explosions/explolarge6.WAV","Big Death Explosion 6",App.TGSound.LS_3D).SetVolume(10.0)
	
	pGame.LoadSound("sfx/Explosions/collision1.wav",	"Collision 1",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/collision2.wav",	"Collision 2",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/collision3.wav",	"Collision 3",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/collision4.wav",	"Collision 4",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/collision5.wav",	"Collision 5",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/collision6.wav",	"Collision 6",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/collision7.wav",	"Collision 7",			App.TGSound.LS_3D).SetVolume(8.0)
	pGame.LoadSound("sfx/Explosions/collision8.wav",	"Collision 8",			App.TGSound.LS_3D).SetVolume(8.0)


###############################################################################
#	GetRandomSound
#
#	Get a random sound from the given list of sound names.  This tries
#	not to return the same sound more than once every 3 calls.
#
#	Args:	lsSoundList	- A list of sound names to choose from (such
#						  as g_lsDeathExplosions, below)
#
#	Return:	One of the sounds in lsSoundList
###############################################################################
g_dRecentSounds = {}
def GetRandomSound(lsSoundList):
	global g_dRecentSounds
	try:
		lRecent = g_dRecentSounds[lsSoundList]
	except KeyError:
		lRecent = []
		g_dRecentSounds[lsSoundList] = lRecent

	# Randomly choose a sound from lsSoundList that isn't in lRecent.
	lsAvailableSounds = list(lsSoundList[:])
	for sSound in lRecent:
		lsAvailableSounds.remove(sSound)
	if not lsAvailableSounds:
		lsAvailableSounds = lsSoundList

	sSound = lsAvailableSounds[ App.g_kSystemWrapper.GetRandomNumber( len(lsAvailableSounds) ) ]

	# If there's more than 1 sound in the Recent Sounds list, remove the oldest one.
	if len(lRecent) > 1:
		lRecent.pop(0)
	# Add sSound to the list.
	lRecent.append(sSound)

	return sSound

g_lsDeathExplosions = (
	"Death Explosion 1",
	"Death Explosion 2",
	"Death Explosion 3",
	"Death Explosion 4",
	"Death Explosion 5",
	"Death Explosion 6",
	"Death Explosion 7",
	"Death Explosion 8",
	"Death Explosion 9",
	"Death Explosion 10",
	"Death Explosion 11",
	"Death Explosion 12",
	"Death Explosion 13",
	"Death Explosion 14",
	"Death Explosion 15",
	"Death Explosion 16",
	"Death Explosion 17",
	"Death Explosion 18",
	"Death Explosion 19",
	"Death Explosion 20",
	"Death Explosion 21",
	"Death Explosion 22",
	"Death Explosion 23",
	"Death Explosion 24",
	"Death Explosion 25",
	"Death Explosion 26",
	"Death Explosion 27",
	"Death Explosion 28",
	"Death Explosion 29",
	"Death Explosion 30",
	"Death Explosion 31",
	"Death Explosion 32",
	"Death Explosion 33",
	"Death Explosion 34",
	"Death Explosion 35",
	"Death Explosion 36",
	"Death Explosion 37",
	)

g_lsBigDeathExplosions = (
	"Big Death Explosion 1",
	"Big Death Explosion 2",
	"Big Death Explosion 3",
	"Big Death Explosion 4",
	"Big Death Explosion 5",
	"Big Death Explosion 6",
	)

g_lsWeaponExplosions = (
	"Explosion 1",
	"Explosion 2",
	"Explosion 3",
	"Explosion 4",
	"Explosion 5",
	"Explosion 6",
	"Explosion 7",
	"Explosion 8",
	"Explosion 9",
	"Explosion 10",
	"Explosion 11",
	"Explosion 12",
	"Explosion 13",
	"Explosion 14",
	"Explosion 15",
	"Explosion 16",
	"Explosion 17",
	"Explosion 18",
	"Explosion 19",
	"Explosion 20",
	"Explosion 21",
	"Explosion 22",
	"Explosion 23",
	"Explosion 24",
	"Explosion 25",
	"Explosion 26",
	"Explosion 27",
	)

g_lsCollisionSounds = (
	"Collision 1",
	"Collision 2",
	"Collision 3",
	"Collision 4",
	"Collision 5",
	"Collision 6",
	"Collision 7",
	"Collision 8",
	)