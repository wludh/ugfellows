import urllib.request
from bs4 import BeautifulSoup
from sys import argv
import re

# defines url and filename bk, sec, and ch
book_num = input('Book # (dd): ')
section_lett = input('Part Letter (a|b|c): ')
ch_num = input("Chapter # (ddd): ")
filenameHTML = "bk{}_sec({})_ch{}_1.html".format(book_num,section_lett,ch_num)

url = "http://www.sacred-texts.com/hin/m{}/m{}{}{}.htm".format(book_num,book_num,section_lett,ch_num)
# downloads and writes raw html to a file
html = urllib.request.urlopen(url).read()
html_refined = str(html)
print("Printing raw HTML...")
print(html_refined)
target = open("original_chapters\\"+filenameHTML,'w+')
target.write(html_refined)
target.close()
# opens file from last step, and deletes all <a> tags and contents (most of the clutter)
# prints result to text document
# was: a_filter.py
soup = BeautifulSoup(open(filenameHTML), "html.parser")
for tag in soup.find_all('a'):
    tag.replaceWith(' ')


finaltext = "bk{}_sec({})_ch{}_2.txt".format(book_num,section_lett,ch_num)

to_print = soup.get_text()
to_print.strip()
print("Now printing version 2, with <a> tags removed...")
print(to_print)
target = open("original_chapters\\"+finaltext,'w+')
target.write(to_print)
target.close()

finishedtext = "bk{}_sec({})_ch{}.txt".format(book_num,section_lett,ch_num)
target = open("cleaned_chapters\\"+finishedtext, "w")

target2 = open(finaltext, 'r')
for line in target2:
    print("No <a> Tags>>\n",line)
    result = re.sub(r'\\n', ' ', line)
    result2 = re.sub(r'\\',' ', result)
    result3 = re.sub('Footnotes.*','', result2)
    print("Completed>>\n",result3)
    target.write(result3)
target.close()
