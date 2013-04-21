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
	pass

if __name__ == '__main__':
	main()