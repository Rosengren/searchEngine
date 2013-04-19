# method Controls flow of links

import sys

from searchData import searchData
from homeLink import homeLink
from pageLink import pageLink

class storeData:

	siteData = searchData()

	def __init__(self, arg):
		self.arg = arg

	def addPage(self, pageURL, pageTags):
		page = pageURL.split(pageURL.split(".com/")[1])[0]

		if page in self.siteData:
			self.siteData[page].addPage(pageURL, pageTags)
			return True
		else:
			newLink = homeLink(page)
			self.siteData[page] = newLink
			self.siteData[page].addPage(pageURL, pageTags)
			return True

		return False

