from BeautifulSoup import BeautifulSoup as soupy
import urllib
import re

html = urllib.urlopen('https://twitter.com/Evils_Paradise').read()
soup = soupy(html)

x = soup.find("meta", {"name":"description"})['content']

filter = re.findall(r'"(.*?)"',x)
tweet =  filter[0] 
print tweet
