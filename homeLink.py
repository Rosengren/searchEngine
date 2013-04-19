from pageLink import pageLink

# Homelink containing subpages

class homeLink:

	linkCount = 0
	linkTags = []
	homeURL = ""
	pageLinks = {}

	def __init__(self, url):
		self.homeURL = url

	def addTag(self, tag):
		self.linkTags.append(tag);

	def getURL(self):
		return self.homeURL

	def getTags(self):
		return self.linkTags

	def getCount(self):
		return self.linkCount

	def incCount(self):
		self.linkCount += 1

	def addPage(self, pageURL, pageTags):

		page = pageLink(pageURL, pageTags)

		if pageURL in self.pageLinks:
			self.pageLinks[pageURL].incCount()
		else:
			self.pageLinks[pageURL] = page

		addTag(pageTags)

	# def incPage(self, page):
	# 	if page.getURL() in self.pageLinks:
	# 		self.pageLinks[page.getURL()] += 1

	def getPageLinks(self):
		return self.pageLinks