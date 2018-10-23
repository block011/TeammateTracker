from userClass import userClass 

class LeagueScheduler:

	#Setters
	def set_processName(self, processName):
		self.__processName = processName

	def __set_inGame(self, inGame):
		self.__inGame = inGame


	#Getters
	def get_processName(self):
		return self.__process

	def get_inGame(self):
		return self.__inGame
	
	def updateUser(self, user):
		self.__user = user



	def isProcessRunning(self):
		if (self.get_processName() in (p.name() for p in psutil.process_iter())):
			return True
		return False

	def checkProcess():

		if(isProcessRunning(self)):
			print("FoundProcess")
			#response = user.getParticipants
			#for user in response:
			#	user.pushToJSON(response[user])
		else:
			print("didNotFindProcess")
	
	def __init__(self,userClass):
		set_processName("League of Legends.exe")
		updateUser(user)
		__set_inGame(False)