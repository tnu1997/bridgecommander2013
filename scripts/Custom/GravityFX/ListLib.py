################################################################
#######  ListLib Script ###################
################################################################
#################        by Fernando Aluani aka USS Frontier
############################################################
# A little library to help using lists and dicts with objects
####################################################################
import App
import MissionLib

#################################################################################
### List Object related functions
#
# i made these functions because i was tired of having to make lists with Objs IDs because damn BC can't remove a instance
# from a list of instances... And then having to make another 2 to 4 lines of code just to recover that Obj from a ID
# So i made these functions that helps us with handling instances lists.
#################################################################

def GetObjIndexInList(obj, list):
	index = 0
	for item in list:
		if item.GetObjID() == obj.GetObjID():
			return index
		index = index + 1
	else:
		#given obj is not in given list...
		return None

def DeleteObjFromList(obj, list):
	index = GetObjIndexInList(obj, list)
	if index == None:
		return
	del list[index]
	return

def IsObjInList(obj, list):
	for item in list:
		if item.GetObjID() == obj.GetObjID():
			return 1
	else:
		return 0

######################################################################
### Same as above, but for Dicts
#################################################################
def GetObjIndexInDict(obj, dict):
	for item in dict.keys():
		value = dict[item]
		if value.GetObjID() == obj.GetObjID():
			return item
	else:
		#given obj is not in given dict...
		return None

def DeleteObjFromDict(obj, dict):
	index = GetObjIndexInDict(obj, dict)
	if index == None:
		return
	del dict[index]
	return

def IsObjInDict(obj, dict):
	for item in dict.keys():
		value = dict[item]
		if value.GetObjID() == obj.GetObjID():
			return 1
	else:
		return 0