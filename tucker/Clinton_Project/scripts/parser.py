from bs4 import BeautifulSoup
from sys import argv
script, html_file, filename = argv
#will parse email partially. certain tags will remain above and below email
#need html to cycle through each html doc in folder
#need filename to be defined 
soup = BeautifulSoup(open(html_file))


refined = soup.find_all("div", class_="tab-content")
refined_string = str(refined)
for text in refined:
    print (refined)
target = open(filename,'w+')
target.write(refined_string)
target.close()
