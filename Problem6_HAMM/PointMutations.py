# First obtain and open the file
fileName = raw_input("Please input the file name: ")
if fileName.find('.txt.') == -1:
    fileName = fileName + '.txt'
f = open(fileName, 'r')

# Read the first and second line

firstDNAStrand = f.readline().rstrip('\n')
secondDNAStrand = f.readline().rstrip('\n')

# Both strands should be of equal length
hammingDistance = 0
for character in range(len(firstDNAStrand)):
    if firstDNAStrand[character] != secondDNAStrand[character]:
        hammingDistance = hammingDistance + 1
print hammingDistance
