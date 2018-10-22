import requests
import os.path
import json
import datetime

class userClass:
#holds userInformation used to grab from api
	def __init__(self, region, summonerName, apiKey):
		self.__region = set_region(region)
		self.__summonerName = set_summonerName(summonerName)
		self.__apiKey = set_apiKey(apiKey)
		self.__path = set_path('./')
		self.__summonerURL = __get_summonerURL(region, summonerName,apiKey)
		self.__matchURL = None
		self.__summonerId = None

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


	#functions
	def requestSummonerData():
		#for later : check if all conditions are met
		response = requests.get(get_summonerURL())



