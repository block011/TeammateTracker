import requests
import os.path
import json
import datetime

class userClass:
#holds userInformation used to grab from api

	#setters
	def set_region(self,region):
		self.__region = region
		

	def set_summonerName(self,summonerName):
		self.__summonerName = summonerName

	def set_apiKey(self,apiKey):
		self.__apiKey = apiKey

	def set_path(self, path):
		#for future check if path is valid
		self.__path = path

	def __set_summonerURL(self,region, summonerName, apiKey):
		self.__summonerURL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + apiKey

	def __set_matchURL(self, region, summonerId, apikey):
		self.__matchURL = "https://" + region + ".api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + summonerId + "?api_key=" + apikey
	
	def set_summonerId(self, summonerName):
		#for future check if empty with ID constant
		response = self.requestSummonerData()
		self.__summonerId = str(response['id'])

	def set_fileName(self):
		#for later : check if all variables are valid
		filePathName = self.get_path() + "/" + self.get_summonerName() + ".json"
		self.__fileName = filePathName

		

	#getters
	def get_region(self):
		return self.__region

	def get_summonerName(self):
		return self.__region

	def get_apiKey(self):
		return self.__apiKey

	def get_path(self):
		return self.__path

	def get_summonerURL(self):
		return self.__summonerURL

	def get_matchURL(self):
		return self.__matchURL

	def get_summonerId(self):
		return self.__summonerId

	def get_fileName(self):
		return self.__fileName


	#functions
	def updateUser(self, region, summonerName, apiKey):
		self.set_region(region)
		self.set_summonerName(summonerName)
		self.set_apiKey(apiKey)
		self.set_path('./')
		self.set_fileName()
		self.__summonerURL = __set_summonerURL(region, summonerName,apiKey)
		self.__summonerId = set_summonerId(summonerName)
		self.__matchURL = __set_matchURL(region, get_summonerId(), apiKey)


	def requestSummonerData(self):
		#for later : check if all conditions are met
		response = requests.get(self.get_summonerURL())
		return response.json()

	def requestMatchData(self):
		#for later : check if all conditions are met
		response = requests.get(self.get_matchURL())
		return response.json()

	def pushtoJSON(userJSON):

		#Checking if file already exists
		if(os.path.isfile(self.get_fileName())):
			oldData = getFromJSON(self.get_fileName())
		else:
			oldData = {}

		#combining the old file and the new data together
		updatedData = {**oldData, **userJSON}

		with open(self.get_fileName(),'w') as fp:
			json.dump(updatedData,fp)

	def getParticipants(self):

		now = datetime.datetime.now()
		currentTime = str(now.strftime("%Y-%m-%d-%S"))

		fullResponse = self.requestMatchData()
		Participant = {}

		#Cleaning JSON file of useless items
		#Putting clean JSON into Participant
		for summoner in fullResponse['participants']:
			
			#Does not let bots nor the original user through
			if(summoner['bot'] == False and str(summoner['summonerId']) != self.get_summonerId()):
				
				#saving all the info under the date in which it was pulled
				Participant[str(summoner['summonerId'])] = {}
				Participant[str(summoner['summonerId'])][currentTime] = summoner

				#clear JSON of all junk we don't need
				del Participant[str(summoner['summonerId'])][currentTime]['perks']
				del Participant[str(summoner['summonerId'])][currentTime]['gameCustomizationObjects']
				del Participant[str(summoner['summonerId'])][currentTime]['spell1Id']
				del Participant[str(summoner['summonerId'])][currentTime]['spell2Id']
				del Participant[str(summoner['summonerId'])][currentTime]['bot']
				del Participant[str(summoner['summonerId'])][currentTime]['profileIconId']
				del Participant[str(summoner['summonerId'])][currentTime]['summonerId']

		return Participant




	def __init__(self, region, summonerName, apiKey):
		self.set_region(region)
		self.set_summonerName(summonerName)
		self.set_apiKey(apiKey)
		self.set_path("./")
		self.set_fileName()
		self.__set_summonerURL(region, summonerName,apiKey)
		self.set_summonerId(summonerName)
		self.__set_matchURL(region, self.get_summonerId(), apiKey)

