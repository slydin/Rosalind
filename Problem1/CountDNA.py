# First obtain and open the file
fileName = raw_input("Please input the file name: ")
if fileName.find('.txt') == -1:
    fileName = fileName + '.txt'
f = open(fileName,'r')
# Go through every line and aggregate the sugar base totals
bases = {'A':0,'C':0,'G':0,'T':0}
for line in f:
    for character in line:
        if character != '\n':
            bases[character] = bases[character] + 1
print bases['A'], bases['C'], bases['G'], bases['T']

