from homeLink import homeLink

"""
storeData
stores all homeLinks and related pageLinks in dictionary

# version 1.0.1 Kevin Rosengren

"""

class storeData:

	def __init__(self):
		self.webBase = {}


	def addPage(self, pageURL, pageTags):

		try:
			page = pageURL.split(pageURL.split(".com/")[1])[0]
		except Exception, e:
			page = pageURL

		#page = pageURL.split(pageURL.split(".com/")[1])[0]
		
		# if homeLink already in webBase, add new page
		if page in self.webBase:
			self.webBase[page].addPage(pageURL, pageTags)
			return True
		
		# create homeLink
		newLink = homeLink(page)
		self.webBase[page] = newLink
		
		# if the pageURL is not a homeLink, add pageLink
		if page != pageURL:
			self.webBase[page].addPage(pageURL, pageTags)

		return True

	"""
	getLink
	returns the Link object to a specified URL

	# param 	string URL
	# return 	Link Object or None
	"""
	def getLink(self, homeURL):

		if homeURL in self.webBase:
			return self.webBase[homeURL]

		return None

	"""
	containsURL
	determines if URL is within the database

	# param	 	strin page
	# return 	True or False
	"""
	def containsURL(self, page):
		if page in self.webBase:
			return True
		
		return False

	"""
	getSearchData
	returns entire web database

	# param 	None
	# return 	dictionary database
	"""
	def getSearchData(self):

		return self.webBase


	def searchData(self, keyword):

		for home in self.webBase:

			if keyword in self.webBase[home].getTags():
				print self.webBase[home].getURL()
				print "-----------------------"
				self.webBase[home].searchPages(keyword)



