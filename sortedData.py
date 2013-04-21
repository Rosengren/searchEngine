import sys

from storeData import storeData

"""
sortedData
stores the storeData according to website popularity

Version 1.0.0 Kevin Rosengren
"""


class storeData:
	"""docstring for storeData"""
	def __init__(self, dictionaryData):
		self.dictData = dictionaryData
		self.tagData = {}
		self.allTags = set([])
		pass


	def buildTagData(self):

		# get all Tags from storeDats
		for homeLink in dictionaryData:
			self.allTags.add(homeLink.getTags)

		# build dictionary with all tags
		for homeLink in dictionaryData:
			for pageLink in homeLink:
				
				



	def searchData(self):
