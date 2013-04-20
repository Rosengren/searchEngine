
"""
pageLink
subPage object containing the URL, page count, and page getTags
of a single sub page

Version 1.0.0 Kevin Rosengren
"""

class pageLink:

	def __init__(self, url, pageTags):
		self.pageCount = 1
		self.pageURL = url
		self.pageTags = pageTags

	def getTags(self):
		return self.pageTags

	def incCount(self):
		self.pageCount += 1

	def getCount(self):
		return self.pageCount

	def getURL(self):
		return self.pageURL


