# This is a Plugin for GravityFX, made with the GravityFX Plugin Tool

PluginType = "GravTorpedo"

Lifetime = 10.00000

GravFXlib = __import__('Custom.GravityFX.GravityFXlib')
Mass = GravFXlib.GetMassByMaxDistance(10)

#the above function GetMassByMaxDistance, returns the mass of a obj that would have the given distance as the max grav force 
#distance. 

SoundDelay = 5.0

ColorRed = 0/255.0
ColorGreen = 0/255.0
ColorBlue = 180/255.0
ColorAlpha = 0.1000000000
