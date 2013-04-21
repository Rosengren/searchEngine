import sys

from storeData import storeData
from dummyData import dummyData

"""
searchData
prompts user to search internet
returns relevant websites

Version 1.0.0 Kevin Rosengren

-- NEED TO IMPLEMENT WEIGHTED SEARCH --
-- ALLOW FOR MULTIPLE KEYWORD INPUTS --
"""


class searchData:

	def __init__(self):
		self.data = dummyData()
		self.stData = dummyData().getDummyData()
		search = None
		print self.stData.

		while (search != "q"):

			# prompt user with search term
			search = raw_input("Search data (only one keyword): ")
			self.stData.searchData(search)

		pass

if __name__ == '__main__':
	searchData()