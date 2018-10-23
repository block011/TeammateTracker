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


	#functions
	def updateUser(self, region, summonerName, apiKey):
		self.__region = set_region(region)
		self.__summonerName = set_summonerName(summonerName)
		self.__apiKey = set_apiKey(apiKey)
		self.__path = set_path('./')
		self.__fileName = set_fileName()
		self.__summonerURL = __get_summonerURL(region, summonerName,apiKey)
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

	#def pushtoJSON()




	def __init__(self, region, summonerName, apiKey):
		self.set_region(region)
		self.set_summonerName(summonerName)
		self.set_apiKey(apiKey)
		self.set_path("./")
		self.set_fileName()
		self.__set_summonerURL(region, summonerName,apiKey)
		self.set_summonerId(summonerName)
		self.__set_matchURL(region, self.get_summonerId(), apiKey)

