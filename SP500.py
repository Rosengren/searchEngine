#!/usr/bin/python

import urllib2
from threading import Thread
import time

# list of ticker prices
tickerPrices = []

# Get top 500 ticker symbols from wikipedia
def fetchCompanies():

	# list of ticker symbols
	tickerList = []

	# get HTML code
	url = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	htmlCode = urllib2.urlopen(req).read()

	# break up html into lines
	htmlLines = htmlCode.splitlines()
	lookingFor = '<td><a rel="nofollow" class="external text"'

	# find all ticker symbols and add them to tickerList
	for s in htmlLines:
		if lookingFor in s and 'reports' not in s:
			r = s.split('">')[1].split('</a></td>')
			tickerList.append(r[0].lower())

	return tickerList

# Define a function for the thread
def fetchTickerValues(tickerList):

	# Iterate through tickerList
	for ticker in tickerList:

		try:
			# send request for html
			urlRequest = urllib2.Request('http://finance.yahoo.com/q?s=' + ticker)

			# get html and store in htmlCode
			htmlCode = urllib2.urlopen(urlRequest).read()

			# set parameters for finding the price
			first = '<span id="yfs_l84_' + ticker + '">'
			last = '</span>'
			
			# find index of first and last tags
			start = htmlCode.index( first ) + len( first )
			end = htmlCode.index( last, start )

			# get ticker price
			tickerPrice = htmlCode[start:end]
			tickerPrices.append((ticker, tickerPrice))
		
		except Exception as e:
		   print 'Exception: at ticker: ' + ticker
		   print e 

# run threads for scraping sites
def runThreads(siteList, threadLength):

	# list of threads
	threads = []

	try:
		for i in range(0, len(siteList), threadLength):
			t = Thread(target=fetchTickerValues, args =[companyList[i:i+threadLength]])
			t.start()
			threads.append(t)
	except:
		print "Error: unable to start thread"

	# Wait for all threads to complete
	for t in threads:
	    t.join()

def main():

	# Fetch List of Ticker Symbols
	companyList = fetchCompanies()

	# start clock
	start = time.time()

	#run threads
	runThreads(companyList, 50)

	# stop clock
	elapsed = (time.time() - start)
	
	# print some info
	print tickerPrices
	print 'Number of tickers: ', len(tickerPrices)
	print 'time elapsed: ', elapsed

if __name__ == '__main__':
	main()