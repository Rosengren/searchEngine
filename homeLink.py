from pageLink import pageLink

# Homelink containing subpages
class homeLink:

	def __init__(self, url):
		self.homeURL = url
		self.linkCount = 1
		self.linkTags = set([])
		self.pageLinks = {}

	def getURL(self):
		return self.homeURL

	def getTags(self):
		return self.linkTags

	def getCount(self):
		return self.linkCount

	def getPageLinks(self):
		return self.pageLinks

	def incCount(self):
		self.linkCount += 1

	def addTags(self, tags):

		for tag in tags:
			self.linkTags.add(tag)

	def addPage(self, pageURL, pageTags):

		# increment Homepage Count
		self.incCount()

		# create pageLink object
		page = pageLink(pageURL, pageTags)

		# inc. pageLink if already in dict.
		if pageURL in self.pageLinks:
			self.pageLinks[pageURL].incCount()

		# else add pageLink to dict.
		else:
			self.pageLinks[pageURL] = page
		
		# add Tags to homeLink
		self.addTags(pageTags)

