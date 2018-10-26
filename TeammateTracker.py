#imports
import psutil
import schedule
import time

from userClass import *
from LeagueScheduler import *



def main():
	processName = "League of Legends.exe"
	
	region = "na1"
	userName = "hi im mateo"
	apiKey = "RGAPI-85fa05d8-746a-446e-a1c8-63509d55a5a7"

	user = userClass(region, userName, apiKey)

	scheduler = LeagueScheduler(user)
	schedule.every(5).seconds.do(scheduler.checkProcess)

	while (True):
		schedule.run_pending()
		time.sleep(5)





if __name__ == "__main__":
	main()