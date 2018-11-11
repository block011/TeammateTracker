import psutil
import schedule
import time

from userClass import *

class LeagueScheduler:

	#Setters
	def set_processName(self, processName):
		self.__processName = processName

	def __set_inGame(self, inGame):
		self.__inGame = inGame


	#Getters
	def get_processName(self):
		return self.__processName

	def get_inGame(self):
		return self.__inGame
	
	def updateUser(self, user):
		self.__user = user



	def isProcessRunning(self):
		if (self.get_processName() in (p.name() for p in psutil.process_iter())):
			return True
		return False

	def checkProcess(self):

		#finds process once and doesnt run again until next
		if(self.isProcessRunning() and self.get_inGame()):
			pass		
		elif(self.isProcessRunning()):
			self.__set_inGame(True)
			participants = self.__user.getParticipants()
			for summoner in participants:

				self.__user.checkParticipant(summoner)

			self.__user.pushToJSON(participants)
		else:
			self.__set_inGame(False)
	
	def __init__(self,userClass):
		self.set_processName("League of Legends.exe")
		self.updateUser(userClass)
		self.__set_inGame(False)
