import urlparse
import urllib
from bs4 import BeautifulSoup

start_site = "http://math.stackexchange.com"

# create a stack for breadeth first search
url_stack = [start_site]
# a list of sites already visited, that will be checked against sites that are
#   going to be visited
visited_url = [start_site]

while len(url_stack) > 0:
    
    try:
        html= urllib.urlopen(url_stack[0]).read()
        req = urllib2.Request(html, headers={'User-Agent' : "Magic Browser"})
    except:
        print url_stack[0]
        
    link = BeautifulSoup(html).findAll('a',href = True)
    
    url_stack.pop(0)
    print len(url_stack)
    
    for tag in link:
        tag['href'] = urlparse.urljoin(start_site,tag['href'])
        
        if start_site in tag['href'] and tag['href'] not in visited_url:
                url_stack.append(tag['href'])
                visited_url.append(tag['href'])

print visited_url
                
        
    