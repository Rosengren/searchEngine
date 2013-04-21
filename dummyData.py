import string
import random
from storeData import storeData

"""
dummyData
"""

NUMBER_OF_HOMEPAGES = 5 	# total homepages generated
NUMBER_OF_SUBPAGES = 2 		# total subpages generated
WEBSITE_LENGTH = 8 			# length of website string

## Set of page Tags ##
TAGS_1 = set(['car','house','plane','tree'])
TAGS_2 = set(['python','c++','java'])
TAGS_3 = set(['safari','explorer','chrome','opera'])
ALLTAGS = [TAGS_1,TAGS_2,TAGS_3]

class dummyData:

	def __init__(self):

		self.storeData = storeData()
		self.homeLinks = []
		self.generatePages()

	def stringGen(self, size):
		# create character string from a to z
		chars = string.ascii_lowercase

		# return randomly generated string
		return ''.join(random.choice(chars) for x in range(size))

	def generatePages(self):

		# Add 100 homepages with 8 subpages to storeData
		for i in range(1, NUMBER_OF_HOMEPAGES):

			# generate random link & add to storeData
			linkURL = "http://www" + self.stringGen(WEBSITE_LENGTH) + ".com/"
			#print linkURL
			#newLink = self.storeData.addPage(linkURL, ALLTAGS[random.randint(0,2)])

			for k in range(1, NUMBER_OF_SUBPAGES):

				# generate random page & add to storeData
				pageURL = linkURL + self.stringGen(WEBSITE_LENGTH)
				newPage = self.storeData.addPage(pageURL,ALLTAGS[random.randint(0,2)])
				#print "\t" + pageURL

	def getDummyData(self):
		# return generated data
		return self.storeData
