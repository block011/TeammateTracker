#imports
import psutil
import schedule
import time

from userClass import userClass


#LeagueClientUxRender
def isProcessRunning(processName):
	if (processName in (p.name() for p in psutil.process_iter())):
		return True
	return False

def checkProcess(user, processName):

	if(isProcessRunning(processName)):
		print("FoundProcess")
		#response = user.getParticipants
		#for user in response:
		#	user.pushToJSON(response[user])
	else:
		print("didNotFindProcess")

def test():
	print("Test")

def main():
	processName = "League of Legends.exe"
	
	region = "na1"
	userName = "us economy"
	apiKey = "RGAPI-343570c7-c17c-4537-939d-9f2e6f34a6f3"

	user = userClass(region, userName, apiKey)
	#players = user.getParticipants()

	schedule.every(5).seconds.do(checkProcess, user, processName)

	while (True):
		schedule.run_pending()
		time.sleep(5)

	#user.pushtoJSON(players)




if __name__ == "__main__":
	main()