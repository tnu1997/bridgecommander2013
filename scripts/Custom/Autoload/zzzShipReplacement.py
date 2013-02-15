# GPL - Defiant <erik@defiant.homedns.org>

import Foundation
import StaticDefs

#mode = Foundation.MutatorDef("Default Replacement")

def GetBridge(self):
    return 'SovereignBridge'


Foundation.ShipDef.GetBridge = GetBridge
#import Custom.Ships.Defiant
Foundation.MutatorDef.Stock.startShipDef = Foundation.ShipDef.Sovereign

#Foundation.OverrideDef.DefaultReplacement = Foundation.OverrideDef("DefaultReplacement", "Foundation.MutatorDef.Stock.startShipDef", "Foundation.ShipDef.Defiant", dict = { "modes": [ mode ] } )
#Foundation.OverrideDef.DefaultReplacement = Foundation.OverrideDef("DefaultReplacement", "Foundation.ShipDef.GetBridge", __name__ + "GetBridge", dict = { "modes": [ mode ] } )
