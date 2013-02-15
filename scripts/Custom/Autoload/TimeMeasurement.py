####################################################################################################
#  TimeMeasurement.py  v0.5    by Fernando Aluani aka USS Frontier
#######
#  This script, when loaded by BC will start to count the real world time, that's because BC's python TIME module
#  isn't reliable. 
#############################################################################################################

import App

class Clock:
	def __init__(self):
		import time
		lt = time.localtime(time.time())
		#lt = [year, month, day, hour, minute, second, weekday, yearday, isDST]
		self.Year = lt[0]
		self.Month = lt[1]
		self.Day = lt[2]
		self.Hour = lt[3]
		self.Minute = lt[4]
		self.Second = lt[5]
		self.WeekDay = lt[6]
		self.YearDay = lt[7]
		self.IsDST = lt[8]
		self.l31months = [1, 3, 5, 7, 8, 10, 12]
		self.l30months = [4, 6, 9, 11]
		self.Refresher = RefreshEventHandler(self.Update, 0.1)
	def Update(self, pObject, pEvent):
		self.Second = self.Second + self.Refresher.Delay
		if self.Second > 59:
			self.Second = 0
			self.Minute = self.Minute + 1
		if self.Minute > 59:
			self.Minute = 0
			self.Hour = self.Hour + 1
		if self.Hour > 23:
			self.Hour = 0
			self.Day = self.Day + 1
			self.YearDay = self.YearDay + 1
			self.WeekDay = self.WeekDay + 1
		if self.WeekDay > 6:
			self.WeekDay = 0
		if self.Day > 31 and self.Month in self.l31months:
			self.Day = 1
			self.Month = self.Month + 1
		if self.Day > 30 and self.Month in self.l30months:
			self.Day = 1
			self.Month = self.Month + 1
		if self.Day > 28 and self.Month == 2:
			self.Day = 1
			self.Month = self.Month + 1
		if self.Month > 12:
			self.Month = 1
			self.Year = self.Year + 1
			self.YearDay = 1
	def ReUpdateByTIME(self):
		import time
		lt = time.localtime(time.time())
		#lt = [year, month, day, hour, minute, second, weekday, yearday, isDST]
		self.Year = lt[0]
		self.Month = lt[1]
		self.Day = lt[2]
		self.Hour = lt[3]
		self.Minute = lt[4]
		self.Second = lt[5]
		self.WeekDay = lt[6]
		self.YearDay = lt[7]
		self.IsDST = lt[8]
	def GetTimeStruct(self):
		return (self.Year, self.Month, self.Day, self.Hour, self.Minute, self.Second, self.WeekDay, self.YearDay, self.IsDST)
	def GetMonthString(self, month = None):
		monthDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
		if month == None:
			return monthDict[self.Month]
		else:
			if month in monthDict.keys():
				return monthDict[month]
			else:	return "invalid month"
	def GetWeekDayString(self, weekday = None):
		weekDayDict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday",}
		if weekday == None:
			return weekDayDict[self.WeekDay]
		else:
			if weekday in weekDayDict.keys():
				return weekDayDict[weekday]
			else:	return "invalid week day"
	def GetTimeString(self):
		sHMS = str(self.Hour) + ":" + str(self.Minute) + ":" + str(self.Second)
		sDMY = str(self.Day) + "/" + self.GetMonthString() + "/" + str(self.Year)
		s = sHMS + " of " + sDMY + ", " + self.GetWeekDayString()
		return s

	def __getstate__(self):
		dState = {}
		return dState

	def __setstate__(self, dict):
		__init__()


class RefreshEventHandler:
	def __init__(self, sFunc, nDelay = 0.1, sMode = 'NORMAL'):
		self.ModeDict = {'UNSTOPPABLE': App.TimeSliceProcess.UNSTOPPABLE, 'CRITICAL': App.TimeSliceProcess.CRITICAL, 'NORMAL': App.TimeSliceProcess.NORMAL, 'LOW': App.TimeSliceProcess.LOW}
		self.ID = "NON-GRAVITYFX RefreshEventHandler"
		self.CLASS = 'Refresh Event Handler'
		self.Function = sFunc
          	self.Delay = nDelay
		self.StartRefreshHandler(sMode)
	def Refresh(self, pObject = None, pEvent = None):
		self.Function(pObject, pEvent)			
	def EditHandler(self, sType, nValue):
		if sType == "Delay":
			self.Delay = nValue
			self._Refresher.SetDelay(self.Delay)
		elif sType == "Priority":
			if nValue == 'UNSTOPPABLE' or nValue == 'CRITICAL' or nValue == 'NORMAL' or nValue == 'LOW':
				self._Refresher.SetPriority(self.ModeDict[nValue])
			else:
				print "Value", nValue, " given to RefreshEventHandler", self.ID, " EditHandler(", sType, ") is invalid."
		elif sType == "Function":
			self.Function = nValue
		else:
			print "Type", sType, " given to RefreshEventHandler", self.ID, " EditHandler(", sType, ") is invalid."
	def StartRefreshHandler(self, sMode):
		self._Refresher = App.PythonMethodProcess()
		self._Refresher.SetInstance(self)
		self._Refresher.SetFunction("Refresh")
		self._Refresher.SetDelay(self.Delay)
		self._Refresher.SetPriority(self.ModeDict[sMode])
	def StopRefreshHandler(self):
		if self._Refresher:
			self._Refresher.__del__()
			self._Refresher = None
	def __repr__(self):	return "<"+self.ID+">"



Clock = Clock()
