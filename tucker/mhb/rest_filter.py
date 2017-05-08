from bs4 import BeautifulSoup
from sys import argv
import re
script, inputfile = argv

txtfile = open(inputfile).read()
result = re.sub(r"\n", ' ', txtfile )
print(result)
