from bs4 import BeautifulSoup
from sys import argv
script, filename = argv
soup = BeautifulSoup(open("14333.html"))
# need to rewrite script to cycle through each email, instead of entering
# them above manually

refined = soup.find_all("div", class_="tab-content")
refined_string = str(refined)
for text in refined:
    print (refined)
target = open(filename,'w')
target.write(refined_string)
target.close()
