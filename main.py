import sys
# modified


from pageLink import pageLink
from homeLink import homeLink
from searchData import searchData

urlData = searchData()
homeL = homeLink("http://www.google.com")
pageL = pageLink("http://www.google.com/avengers")
		
def main():

	if True:
		pageURL = "http://www.google.com/avengers"
		page = pageURL.split(".com/")[1]
		page = pageURL.split(pageURL.split(".com/")[1])[0]
		print page
	# urlData.addLink(homeL)
	# homeL.addPage(pageL)
	# print homeL.getPageLinks()
	# print urlData.getLink("http://www.google.com").getURL()
	# print urlData.getDatabase()
	# homeL2 = urlData.getLink("http://www.google.com")
	pass

if __name__ == '__main__':
	main()