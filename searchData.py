from homeLink import homeLink

# Database containing all homeLinks

class searchData:

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

	def getDatabase(self):

		return self.webBase
