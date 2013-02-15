###########################################################################################################################
###########################################################################################################################
##    THE   LOGGER SCRIPT         
##			by Fernando Aluani aka USS Frontier
## License:
## 	- You can't change this file, but you may distribute it with your mod if you use it on your mod,
##	  and credit must be given to me.
#####################################################################################
##  With this script, and the LogCreator class contained in this script, you can easily make a log of what happens when 
##  your code is used in-game and then automaticaly print the log to a file you define with a delay between each print that
##  you also define OR automaticaly print the log to a file when the game ends (tho bear in mind that the handler for the
##   App.ET_QUIT event will only be created when a LogCreator is created after the initialization of BC's Menu, otherwise,
##   a annoying bug would happen).
##  After creating the LogCraetor obj, with a single function you add a string to the log. The LogCreator automaticaly
##  arranges the strings added by the time(hour:min:sec weekday day/month/year) when they were added.
#########
# WARNING: after some tests, i discovered that BC's python Time module doesn't work correctly, dunno why...
#		it doesn't return the exact time, resulting that sometimes it return the same time over and over again...
###########################################################################################################################
###############################################################################################
#@@@@@@ initializing/creating the LogCreator
######
# 	- initialize: LogCreator(name, path) 
#     	       name --> the name of the LogCreator obj you're making, if not given, the LogCreator class will use the
#				    path as the name
#			 path --> the filepath (with the file extension) to the file in which the log will be printed
#  Example on how to use:
#	import Logger
#	pLogger = Logger.LogCreator("Mod X", "script\Custom\ModXlog.txt", 5.0)
#	pLogger.LogString("just started the Mod X logger")      --- See functions below
#
# TIP: you'll probably want to make a single LogCreator obj for a single script or a single class
#################################################################################################################
#@@@@@@@ The functions of the LogCreator :
######
#	-LogString(string)
#		- This is the function you'll most probaly use only. It is used to add a string to the log. Also, the LogCreator 
#		  will automaticaly arrange the strings added by the time when they were added.
#		Arguments:
#		> string --> the string to be added to the log
#	-GetTime()
#		- Used internally the the LogCreator to arrange the log by time. This returns the exact time now in the form 
#		   hour:minutes:seconds weekday day/month/year
#	-Dump()
#		- This is also used internally to print the log to the file specified when creating the LogCreator obj.
#	-SetFilePath(path)
#		- Use this to change the file path in which the log will be printed.
#		Arguments:
#		> path --> the new file path. Example: "scripts\Custom\MyLog.txt"
#	-SetAutoDelay(value)
#		- Use this to change the delay between each automatic print of the LogCreator obj if when creating it you had 
#		  set it to automaticaly print the log.
#		Arguments:
#		> value --> the new delay value. must be a float or integer, in seconds.
######################################################################################################################
import App
import nt

LogCreatorsQUITlist = []
QUIThandlerCreated = 0

class  LogCreator:
	def __init__(self, name, path):
		global LogCreatorsQUITlist, QUIThandlerCreated
		try:
			GravFXlib = __import__('Custom.GravityFX.GravityFXlib')
			if name == None:
				ID = GravFXlib.GetUniqueID(path+" LogCreator")
			else:
				ID = GravFXlib.GetUniqueID(name+" LogCreator")
		except:
			if name == None:
				ID = path+" LogCreator"
			else:
				ID = name+" LogCreator"
		self.LCID = ID
		self.CLASS = "Log Creator"
		self.FilePath = path
		self.WasFileCreated = 0
		self.NotQuitted = 1
		self.CurrentTime = ""
		if QUIThandlerCreated == 0:
			pTopWindow = App.TopWindow_GetTopWindow()
			if pTopWindow:
				pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
				if pOptionsWindow:
					pOptionsWindow.AddPythonFuncHandlerForInstance(App.ET_QUIT, __name__+".LoggerQuitHandler")
					QUIThandlerCreated = 1
		LogCreatorsQUITlist.append(self)		
	def LogString(self, s):
		sTime = self.GetTime()
		if self.WasFileCreated == 0:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
			nt.write(file, "#This is the dump of the LogCreator: "+str(self)+ "\n")
			nt.write(file, "#This log file was created on: "+sTime+ "\n########################################\n")
			self.WasFileCreated = 1
		else:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_APPEND)
		if sTime != self.CurrentTime:
			nt.write(file, "## -------------------- ##"+ "\n")
			nt.write(file, "####################\n#######>>>"+str(sTime)+ "\n")
			self.CurrentTime = sTime
		nt.write(file, "#>>>"+str(s)+ "\n")
		nt.close(file)
	def LogError(self, s):
		sTime = self.GetTime()
		if self.WasFileCreated == 0:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
			nt.write(file, "#This is the dump of the LogCreator: "+str(self)+ "\n")
			nt.write(file, "#This log file was created on: "+sTime+ "\n########################################\n")
			self.WasFileCreated = 1
		else:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_APPEND)
		if sTime != self.CurrentTime:
			nt.write(file, "## -------------------- ##"+ "\n")
			nt.write(file, "####################\n#######>>>"+str(sTime)+ "\n")
			self.CurrentTime = sTime
		nt.write(file, "< --------------------------------------- >\n<----------------- ERROR ----------------->\n")
		nt.write(file, "-----> "+str(s)+ "\n")
		nt.write(file, "<--------------- END ERROR --------------->\n< --------------------------------------- >\n")
		nt.close(file)
	def LogImportant(self, s):
		sTime = self.GetTime()
		if self.WasFileCreated == 0:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
			nt.write(file, "#This is the dump of the LogCreator: "+str(self)+ "\n")
			nt.write(file, "#This log file was created on: "+sTime+ "\n########################################\n")
			self.WasFileCreated = 1
		else:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_APPEND)
		if sTime != self.CurrentTime:
			nt.write(file, "## -------------------- ##"+ "\n")
			nt.write(file, "####################\n#######>>>"+str(sTime)+ "\n")
			self.CurrentTime = sTime
		nt.write(file, "< =========================================== >\n<================= IMPORTANT =================>\n")
		nt.write(file, "-----> "+str(s)+ "\n")
		nt.write(file, "<=============== END IMPORTANT ===============>\n< =========================================== >\n")
		nt.close(file)
	def LogException(self, et, s = ""):
		sTime = self.GetTime()
		if self.WasFileCreated == 0:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
			nt.write(file, "#This is the dump of the LogCreator: "+str(self)+ "\n")
			nt.write(file, "#This log file was created on: "+sTime+ "\n########################################\n")
			self.WasFileCreated = 1
		else:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_APPEND)
		if sTime != self.CurrentTime:
			nt.write(file, "## -------------------- ##"+ "\n")
			nt.write(file, "####################\n#######>>>"+str(sTime)+ "\n")
			self.CurrentTime = sTime
		nt.write(file, "< ------------------------------------------- >\n<----------------- EXCEPTION ----------------->\n")
		if s != "":
			nt.write(file, str(s) + "\n")
		nt.write(file, "Traceback of Error: "+str(et[0])+": "+str(et[1])+ "\n")
		if et[2]:
			tl = GetTracebackList(et[2])
		else:
			tl = []
		for tline in tl:
			sline = "Script: \""+str(tline[0])+"\", Line "+str(tline[1])+", in the function \""+str(tline[2])+"\"."
			nt.write(file, sline + "\n")
		nt.write(file, "<--------------- END EXCEPTION --------------->\n< ------------------------------------------- >\n")
		nt.close(file)
	def GetTime(self):
		try:
			Time = __import__('Custom.Autoload.TimeMeasurement')
			return Time.Clock.GetTimeString()
		except:
			import time
			return time.asctime(time.localtime(time.time()))
	def DumpEnd(self):
		if self.WasFileCreated and self.NotQuitted:
			file = nt.open(self.FilePath, nt.O_WRONLY|nt.O_APPEND)
			nt.write(file, "########################################\n# "+self.GetTime()+"\n#Ending of log dump - User is quiting the game\n########################################\n")
			nt.close(file)
			self.NotQuitted = 0
	def __repr__(self):
		return "<"+self.LCID+">"

###################################################################################################
# The Dummy Logger
#  - This can be used to make a dummy logger, incase your script creates or not a logger based on some setting
#    but your code is using the logger. So if the logger won't be created, just set it as this type of logger
#    so that your code won't require anything else than the LogCreator.LogString() lines.
##########
# Example:
#	import Logger
#	if UserWantsLogs == 1:
#		pLogger = Logger.LogCreator("Mod X", "script\Custom\ModXlog.txt", 5.0)
#	else:	
#		pLogger = Logger.DummyLogger()
#   ***then in the code that will be logged just use***
#	*code
#	pLogger.LogString(string)
#	*code
#####
# Note that you can also use LogError(string), LogImportant(string) and LogException(exception, string =None)
###################################################################################################
class DummyLogger:
	def __init__(self):
		self.CLASS = "Dummy Log Creator"
	def LogString(self, string):
		pass
	def LogError(self, string):
		pass
	def LogImportant(self, string):
		pass
	def LogException(self, et, string = ""):
		pass
	def DumpEnd(self):
		pass
	def GetTime(self):
		pass

#####################################
#  just to test if LogCreator.LogException is working
################################
logtest = None
itest = 30
refreshtest = None
def start():
	global logtest, refreshtest
	logtest = LogCreator("testando", "scripts\\Custom\\testando.txt")
	logtest.LogString("acabou d comecar")
	refreshtest = RefreshEventHandler(testupdate, 1.0)


def testupdate(pObject, pEvent):
	global itest, logtest, refreshtest
	try:
		itest = itest - 1
		xtest = 30 / itest
		logtest.LogString("The Value now is: "+str(xtest))
	except:
		import sys
		et = sys.exc_info()
		logtest.LogException(et)
		logtest.LogString("Finalizing refreshtest")
		refreshtest.StopRefreshHandler()

###################################################################################################
# LoggerQuitHandler
# - This is the handler for the game quit event, to print all logs.
#   Don't use it, don't mess with it.
###################################################################################################
def LoggerQuitHandler(pObject, pEvent):
	global LogCreatorsQUITlist
	pObject.CallNextHandler(pEvent)
	for LC in LogCreatorsQUITlist:
		LC.DumpEnd()

#######################################################
# I made this function based on the function "extract_tb" from the traceback module i found in my BC directory,
# that module isn't from stock BC, so i assume a mod has put it there, but i do not know which one...
# So i would like to thank and credit the person that made that module (because it is diferent than the traceback module 
# from python 2.4) for this function.
###
# the next function, "tb_lineno" is also from the module i mentioned, so i again thank and credit the person who did it.
# The next function is used by this function, and this function is used by LogCreator.LogException to get the traceback
# strings (script, line number, function name, line) from the given traceback object.
####################################################
def GetTracebackList(tb, limit = None):
	import sys
	if limit is None:
		if hasattr(sys, 'tracebacklimit'):
			limit = sys.tracebacklimit
	list = []
	n = 0
	while tb is not None and (limit is None or n < limit):
		f = tb.tb_frame
		lineno = tb_lineno(tb)
		co = f.f_code
		filename = co.co_filename
		name = co.co_name
		list.append((filename, lineno, name))
		tb = tb.tb_next
		n = n+1
	return list

#########
## I got this function from a module called "traceback" that i found in my BC directory, the following comment is what was
## commented above the function in that module
#####
# Calculate the correct line number of the traceback given in tb (even
# with -O on).
# Coded by Marc-Andre Lemburg from the example of PyCode_Addr2Line()
# in compile.c.
# Revised version by Jim Hugunin to work with JPython too.
#########
def tb_lineno(tb):
	c = tb.tb_frame.f_code
	if not hasattr(c, 'co_lnotab'):
		return tb.tb_lineno
	tab = c.co_lnotab
	line = c.co_firstlineno
	stopat = tb.tb_lasti
	addr = 0
	for i in range(0, len(tab), 2):
		addr = addr + ord(tab[i])
		if addr > stopat:
			break
		line = line + ord(tab[i+1])
	return line

#####################################################################################
##  LOGGER HELPER
#########
# This is a class i made to help me read logs (because some logs of mine were passing the 1000 pages mark...), this basicly
# shows you the whole log, the log stats (which and how many lines are), and also presents you with some useful functions
# to change the log file (like remove X times a S line from the log).
#####
# WARNING: IT IS MEANT (at least at the moment) TO BE USED IN THE PYTHON IDLE!!!
#	     if your log has many lines (like mine that had 60000), some functions may take a little while to finish.
###########################################################################################################################
###############################################################################################
#@@@@@@ initializing/creating the LoggerHelper
######
# 	- initialize: LoggerHelper(logfilename) 
#			 logfilename --> the filepath (with the file extension) to the log file
#################################################################################################################
#@@@@@@@ The functions of the LoggerHelper:
######
#	-PrintStats()
#		- This prints the stats of the log. whihc lines there are in it, and how many times they appear, and total lines
#		   in the log.
#	-GetLogStats()
#		- Used internally the the LoggerHelper by the PrintStats function, this returns a dict (keys: log strings,
#		   values: how many times the log string appears.
#	-PrintLog()
#		- Just prints the log.
#	-RemoveLines(line, times = 0)
#		- Use this to remove X times the given line from the log, with X being the given times.
#		Arguments:
#		> line --> the line that you want to remove.
#		> times --> how many times to remove the given line. if 0, removes all lines that are the given line.
#	-RereadLogFile()
#		- This just re-reads the log file, to updates the LoggerHelper's data.
#	-UpdateLogFile()
#		- This updates the log file with the data from the LoggerHelper, incase you removed any lines from the log
#		  using the RemoveLines function, this will save these changes to the log file.
######################################################################################################################
class LoggerHelper:
	def __init__(self, logfilename):
		self.Log = []
		self.LogFileName = logfilename
		self.RereadLogFile()
	def PrintStats(self):
		d = self.GetLogStats()
		for s in d.keys():
			print s, " // Times =", d[s]
		print "--------------"
		print "TOTAL Lines =", len(self.Log)
	def GetLogStats(self):
		d = {}
		for s in self.Log:
			if not d.has_key(s):
				d[s] = 0
			d[s] = d[s] + 1
		return d
	def PrintErrors(self):
		errors = self.GetErrors()
		for s in errors.keys():
			print s, " // Times =", errors[s]
	def GetErrors(self):
		geterror = 0
		errors = {}
		for s in self.Log:
			if s == "<--------------- END ERROR --------------->":
				geterror = 0
			if geterror == 1:
				if not errors.has_key(s):
					errors[s] = 0
				errors[s] = errors[s] + 1
			if s == "<----------------- ERROR ----------------->":
				geterror = 1
		return errors
	def PrintImportants(self):
		importants = self.GetImportants()
		for s in importants.keys():
			print s, " // Times =", importants[s]
	def GetImportants(self):
		getimp = 0
		imps = {}
		for s in self.Log:
			if s == "<=============== END IMPORTANT ===============>":
				getimp = 0
			if getimp == 1:
				if not imps.has_key(s):
					imps[s] = 0
				imps[s] = imps[s] + 1
			if s == "<================= IMPORTANT =================>":
				getimp = 1
		return imps
	def PrintLog(self):
		for s in self.Log:
			print s
	def RemoveLines(self, line, times = 0):
		x = 0
		il = []
		for i in range(len(self.Log)):
			s = self.Log[i]
			if s == line:
				il.append(s)
				x = x+1
			if times != 0 and x >= times:
				break
		for s in il:
			self.Log.remove(s)
	def RereadLogFile(self):
		import string
		logfile = file(self.LogFileName, "r")
		l = logfile.readlines()
		logfile.close()
		self.Log = []
		for s in l:
			cs = string.split(s, "\n")[0]
			self.Log.append(cs)
	def UpdateLogFile(self):
		logfile = file(self.LogFileName, "w")
		for s in self.Log:
			logfile.write(s+"\n")
		logfile.close()

###################################################################################################
# RefreshEventHandler
# - This is the class that creates a refresh event handler. it automaticaly calls the given function
#   with the given delay time between each call with the given priority
# I originally made it for GravityFX, but i redistribute it with some other scripts so that they do not require GravityFX
# to work.
# And as i'm lazy now, i won't write it's explanation here... if you want, see the LogCreator class, it uses this. Or
# check the GravityFXlib script, it contains the original explanation of this.
###################################################################################################
IndexID = 1
class RefreshEventHandler:
	def __init__(self, sFunc, nDelay = 0.1, sMode = 'NORMAL'):
		global IndexID
		self.ModeDict = {'UNSTOPPABLE': App.TimeSliceProcess.UNSTOPPABLE, 'CRITICAL': App.TimeSliceProcess.CRITICAL, 'NORMAL': App.TimeSliceProcess.NORMAL, 'LOW': App.TimeSliceProcess.LOW}
		try:
			GravFXlib = __import__('Custom.GravityFX.GravityFXlib')
			ID = GravFXlib.GetUniqueID("RefreshEventHandler")
		except:
			ID = "RefreshEventHandler_"+str(IndexID)
			IndexID = IndexID + 1
		self.ID = ID
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
		elif sType == "Function":
			self.Function = nValue
	def StartRefreshHandler(self, sMode):
		self._Refresher = App.PythonMethodProcess()
		self._Refresher.SetInstance(self)
		self._Refresher.SetFunction("Refresh")
		self._Refresher.SetDelay(self.Delay)
		self._Refresher.SetPriority(self.ModeDict[sMode])
	def StopRefreshHandler(self):
		self._Refresher.__del__()
		self._Refresher = None
	def __repr__(self):
		return "<"+self.ID+">"
