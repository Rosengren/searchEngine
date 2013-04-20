# subpage

class pageLink:

	pageCount = 0
	pageURL = ""
	pageTags = []

	def __init__(self, url, pageTags):
		self.pageCount = 1
		self.pageURL = url

	def addTag(self, tag):
		self.pageTags.append(tag)

	def getTags(self):
		return self.pageTags

	def incCount(self):
		self.pageCount += 1

	def getCount(self):
		return self.pageCount

	def getURL(self):
		return self.pageURL


