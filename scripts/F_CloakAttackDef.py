import Foundation

ShipDef = Foundation.ShipDef
Federation = Foundation.Federation

class CloakAttackDef(ShipDef):
	def __init__(self, abbrev, species, dict):
		dict['race'] = Federation
		ShipDef.__init__(self, abbrev, species, dict)
	def StrFriendlyAI(self):
		return 'CloakFriendlyAttack'
	def StrEnemyAI(self):
		return 'CloakAttack'
		