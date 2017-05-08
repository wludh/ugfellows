import urllib.request
from bs4 import BeautifulSoup
from sys import argv
script, filenameHTML = argv

html = urllib.request.urlopen('http://www.sacred-texts.com/hin/m12/m12a068.htm').read()
html_refined = str(html)
print(html_refined)
target = open(filenameHTML,'w+')
target.write(html_refined)
target.close()
