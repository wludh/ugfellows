from sys import argv
#defines the argument variables that need to be given
script, filename = argv
#defines 'txt' as command open(given value for file)
txt = open(filename)
#prints text, % defined as filename, prints a reading of the text
print ("Here's your file, sir. %r:" % filename)
print (txt.read())
#gives prompt
print ("Type the file name again")
#defines file_again as an input by the user
file_again = input("> ")
#txt_again defined as opening file specified in file_again
txt_again = open(file_again)
#prints reading of file defined as file_again, opened by txt_again
print (txt_again.read())
close_all= txt.close
print (close_all)
