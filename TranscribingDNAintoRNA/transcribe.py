# First obtain and open the file
fileName = raw_input("Please input the file name: ")
if fileName.find('.txt.') == -1:
    fileName = fileName + '.txt'
f = open(fileName, 'r')

for line in f:
    line = line.replace("T","U")
    print line
