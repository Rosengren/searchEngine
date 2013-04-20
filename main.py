import sys


from pageLink import pageLink
from homeLink import homeLink
from storeData import storeData
from storeData import storeData

stData = storeData()
homeL = homeLink("http://www.google.com")
pageL = pageLink("http://www.google.com/avengers", ['python', 'C++'])
		
def main():

	stData.addPage("http://www.google.com/avengers", ['jello', 'python'])
	print stData.getSearchData()
	homeL = stData.getLink("http://www.google.com/")
	print homeL.getPageLinks()
	# print urlData.getLink("http://www.google.com").getURL()
	# pageURL = "http://www.google.com/avengers"
	# page = pageURL.split(".com/")[1]
	# page = pageURL.split(pageURL.split(".com/")[1])[0]
	# print page	
	pass

if __name__ == '__main__':
	main()