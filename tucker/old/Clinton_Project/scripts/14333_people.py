from bs4 import BeautifulSoup
from sys import argv
script, filename = argv
soup = BeautifulSoup(open("14333.html"))


refined = soup.find_all("span", class_="inlinemeta")
refined_string = str(refined)
for text in refined:
    print (refined)
target = open(filename,'w')
target.write(refined_string)
target.close()
