#imports
import psutil
import schedule
import time

from userClass import *



def main():
	processName = "League of Legends.exe"
	
	region = "na1"
	userName = "us economy"
	apiKey = "RGAPI-343570c7-c17c-4537-939d-9f2e6f34a6f3"

	user = userClass(region, userName, apiKey)

	schedule.every(5).seconds.do(checkProcess, user, processName)

	while (True):
		schedule.run_pending()
		time.sleep(5)





if __name__ == "__main__":
	main()