from homeLink import homeLink

# Database containing all homeLinks

class storeData:

	webBase = {}
	def __init__(self):
		self.webBase = {}

	def addLink(self, link):

		if link.getURL() not in self.webBase:
			self.webBase[link.getURL()] = link
			return 1

		return 0

	def getLink(self, homeURL):

		if homeURL in self.webBase:
			return self.webBase[homeURL]

		return None

	def containsURL(self, page):
		if page in self.webBase:
			return True
		
		return False

	def getSearchData(self):

		return self.webBase

	def addPage(self, pageURL, pageTags):
		page = pageURL.split(pageURL.split(".com/")[1])[0]

		if page in self.webBase:
			self.webBase[page].addPage(pageURL, pageTags)
			return True
		else:
			newLink = homeLink(page)
			self.webBase[page] = newLink
			self.webBase[page].addPage(pageURL, pageTags)
			return True

		return False

