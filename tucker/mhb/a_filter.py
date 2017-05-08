from bs4 import BeautifulSoup
from sys import argv
script, htmlfile, finalhtml = argv

soup = BeautifulSoup(open(htmlfile), "html.parser")
for tag in soup.find_all('a'):
    tag.replaceWith(' ')

to_print = soup.get_text()
to_print.strip()
print(to_print)
target = open(finalhtml,'w+')
target.write(to_print)
target.close()
