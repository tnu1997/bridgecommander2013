import App

def LoadRacesIcons(RacesIcons = None):
	if not RacesIcons:
		RacesIcons = App.g_kIconManager.CreateIconGroup("RacesIcons")
		App.g_kIconManager.AddIconGroup(RacesIcons)

	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Sona.tga')
	RacesIcons.SetIconLocation(1, kTextureHandle, 0, 0, 128, 128)

	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/8472.tga')
	RacesIcons.SetIconLocation(2, kTextureHandle, 0, 0, 128, 128)

	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Ferengi.tga')
	RacesIcons.SetIconLocation(3, kTextureHandle, 0, 0, 128, 128)
        
	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Borg.tga')
	RacesIcons.SetIconLocation(4, kTextureHandle, 0, 0, 128, 128)
        
        kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Romulan.tga')
	RacesIcons.SetIconLocation(5, kTextureHandle, 0, 0, 128, 128)

	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Dominion.tga')
	RacesIcons.SetIconLocation(6, kTextureHandle, 0, 0, 128, 128)

	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Federation.tga')
	RacesIcons.SetIconLocation(7, kTextureHandle, 0, 0, 128, 128)

	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Klingon.tga')
	RacesIcons.SetIconLocation(8, kTextureHandle, 0, 0, 128, 128)

	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Cardassian.tga')
	RacesIcons.SetIconLocation(9, kTextureHandle, 0, 0, 128, 128)

	kTextureHandle = RacesIcons.LoadIconTexture('Data/Icons/Races/Breen.tga')
	RacesIcons.SetIconLocation(10, kTextureHandle, 0, 0, 128, 128)
