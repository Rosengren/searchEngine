import unittest

"""
unitTest
tests every object and their related functions

version 1.0.0 Kevin Rosengren
"""


from pageLink import pageLink
from homeLink import homeLink
from storeData import storeData

""" Constants """

HOMEPAGE_ONE = "http://www.google.com/"
HOMEPAGE_TWO = "http://www.youtube.com/"
SUBPAGE = "http://www.google.com/subPage"
SUBTAGS = set(['python','c++','java'])
HOMETAGS = set(['games', 'videos', 'photos'])
EXTRA_TAGS = set(['apple','orange','banana'])
COUNT_INCREMENTS = 10

""""""""""""""""""

class TestSearchEngine(unittest.TestCase):

	def setUp(self):

		# create & init objects
		self.homePage_one = homeLink(HOMEPAGE_ONE)
		self.homePage_two = homeLink(HOMEPAGE_TWO)
		self.subPage = pageLink(SUBPAGE, SUBTAGS)
		self.stData = storeData()

	""" Basic Class Testing """
	def test_pageLink(self):

		# test get functions
		self.test_pageLink_get()

		# test pageCount function
		self.test_pageLink_pageCount()


	def test_homeLink(self):

		# test get functions
		self.test_homeLink_get()

		# test adding sub pages
		self.test_homeLink_addPage()

		# test adding tags to home page
		self.test_homeLink_addTags()

	def test_storeData(self):

		# test get functions
		self.test_storeData_get()

		# test adding home pages
		self.test_storeData_addPage()


	def test_pageLink_get(self):

		# test page count
		self.assertEqual(self.subPage.getCount(), 1)

		# test  page tags
		self.assertEqual(self.subPage.getTags(), SUBTAGS)

		# test page URL
		self.assertEqual(self.subPage.getURL(), SUBPAGE)

	def test_pageLink_pageCount(self):

		# assert page only visited once
		self.assertEqual(self.subPage.getCount(), 1)

		for n in range(1, COUNT_INCREMENTS):
			self.subPage.incCount()

		# assert page count is accurate
		self.assertEqual(self.subPage.getCount(), COUNT_INCREMENTS)


	def test_homeLink_get(self):

		# test homepage URL
		self.assertEqual(self.homePage_one.getURL(), HOMEPAGE_ONE)

		# test homepage count
		self.assertEqual(self.homePage_one.getCount(), 1)

		# test homepage tags
		self.assertEqual(self.homePage_one.getTags(), set([]))

		# test homepage sub-pages
		self.assertEqual(self.homePage_two.getPageLinks(), {})


	def test_homeLink_addPage(self):

		# add subpage to homepage
		self.homePage_two.addPage(self.subPage.getURL(), SUBTAGS)
		
		# assert subpage object added to homepage
		self.assertNotEqual(self.homePage_two.getPageLinks(), None)


	def test_homeLink_addTags(self):

		# add tags to homepage
		self.homePage_one.addTags(HOMETAGS)

		# assert tags were added to homepage
		self.assertEqual(self.homePage_one.getTags(), HOMETAGS)

	def test_storeData_get(self):

		# test getting homeLink by passing URL
		self.assertEqual(self.stData.getLink(HOMEPAGE_ONE), None)

		# test getting homepage dict.
		self.assertEqual(self.stData.getSearchData(), {})

	def test_storeData_addPage(self):

		# add sub page to database
		self.stData.addPage(self.subPage.getURL(), SUBTAGS)

		# assert homePage was added
		self.assertTrue(self.stData.containsURL(HOMEPAGE_ONE))
		self.assertFalse(self.stData.containsURL(HOMEPAGE_TWO))

		# assert contains function
		self.assertNotEqual(self.stData.getLink(HOMEPAGE_ONE), None)
		# assert homePage contains subpage
		self.assertNotEqual(self.stData.getLink(HOMEPAGE_ONE).getPageLink(SUBPAGE),None)

if __name__ == '__main__':

	searchTest = unittest.TestLoader().loadTestsFromTestCase(TestSearchEngine)
	unittest.TextTestRunner(verbosity=10).run(searchTest)