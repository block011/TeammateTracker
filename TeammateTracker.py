#imports
from userClass import userClass




def main():
	region = "na1"
	userName = "us economy"
	apiKey = "RGAPI-343570c7-c17c-4537-939d-9f2e6f34a6f3"
	user = userClass(region, userName, apiKey)
	print(user.getParticipants())




if __name__ == "__main__":
	main()