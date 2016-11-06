# Sets first argument to filename
filename = ARGV.first

# Open var filename as file object txt
txt = open(filename)

# Read and print file contents
puts "Here's your file #{filename}:"
print txt.read

# Input file name
print "Type the filename again: "
file_again = $stdin.gets.chomp

# Open file
txt_again = open(file_again)

# Read and print file
print txt_again.read
