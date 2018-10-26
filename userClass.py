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
		return self.__summonerName

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

	def getFromJSON(self):
		with open(self.get_fileName(),'r') as fp:
			return json.load(fp)

	def pushToJSON(self,userJSON):

		#if Botgame just return
		if userJSON is None:
			return

		oldData = self.retrieveData()
		#combining the old file and the new data together
		#update, had problem with below line of code adding duplicate keys. Need to expirement further
		#updatedData = {**oldData, **userJSON}

		for players in userJSON:
			if oldData == None:
				oldData = {}
			
			oldData[str(players)] = userJSON[players]

		with open(self.get_fileName(),'w') as fp:
			json.dump(oldData,fp)

	def retrieveData(self):
		#Checking if file already exists
		if(os.path.isfile(self.get_fileName())):
			oldData = self.getFromJSON()
		else:
			oldData = {}
		return oldData;

	def getParticipants(self):

		now = datetime.datetime.now()
		self.__currentTime = str(now.strftime("%Y-%m-%d/%H-%S"))

		fullResponse = self.requestMatchData()
		Participant = {}

		#Cleaning JSON file of useless items
		#Putting clean JSON into Participant
		for summoner in fullResponse['participants']:
			
			#Does not let bots nor the original user through
			if(summoner['bot'] == False and str(summoner['summonerId']) != self.get_summonerId()):
				
				#saving all the info under the date in which it was pulled
				#Participant[str(summoner['summonerId'])] = []



				#clear JSON of all junk we don't need
				del summoner['perks']
				del summoner['gameCustomizationObjects']
				del summoner['spell1Id']
				del summoner['spell2Id']
				del summoner['bot']
				del summoner['profileIconId']
				summoner['date'] = self.__currentTime

				
				Participant[str(summoner['summonerId'])]= summoner

		return Participant

	def checkParticipant(self, Participant):


		oldData = self.retrieveData()

		#if empty
		if oldData is None:
			pass

		#if in old data
		elif Participant in oldData:
			print("found player")
			print(oldData[Participant])
			#else
		else:
			print("not found")


	def __init__(self, region, summonerName, apiKey):
		self.set_region(region)
		self.set_summonerName(summonerName)
		self.set_apiKey(apiKey)
		self.set_path("./")
		self.set_fileName()
		self.__set_summonerURL(region, summonerName,apiKey)
		self.set_summonerId(summonerName)
		self.__set_matchURL(region, self.get_summonerId(), apiKey)
		self.__currentTime = 0

