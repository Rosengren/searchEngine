import urllib
import re
import csv

# look at celery for threads

all_companies = []
# method find_companies() crawls CNN page and brings in the names of all the 
#  companies in the S&P 500. it takes the webpage as an input and outputs the 
#   sympol of the companie
def find_companies(page):
    start_link = page.find('href="http://money.cnn.com/quote/quote.html?')
    
    if start_link == -1:
            return None,0
    else:
        start_quote = page.find('symb=', start_link) + 5
        end_quote = page.find('"', start_quote)
        
        company_name = page[start_quote:end_quote]
        all_companies.append(company_name)
        return company_name, end_quote
    
# crawls page and finds all companies that are on the page.
#  takes the web page as an input
def find_all_companies(page):
    while True:
        companie,endpos = find_companies(page)
        if companie:
            print companie
            page = page[endpos:]
        else:
            break 
        
def get_stock_price(stocks_list):
    
    for i in stocks_list:
        html = urllib.urlopen('http://ca.finance.yahoo.com/q?s='+i)
        htmlopen = html.read()
        yahoo_stock_price = '<span id="yfs_l84_'+ i.lower() +'">(.+?)</span>'
        pattern = re.compile(yahoo_stock_price) 
        price = re.findall(pattern, htmlopen)
        print 'the price of ' + i +' is: ' + price[0]
    
# -------- MAIN ----------------

# open up the web page and read it
i = 1
while i<=34:
    print 'http://money.cnn.com/data/markets/sandp/?page='+ str(i)
    html = urllib.urlopen('http://money.cnn.com/data/markets/sandp/?page='+ str(i))
    web_page = html.read()
    find_all_companies(web_page)
    i= i+1

print all_companies
get_stock_price(all_companies[:5])