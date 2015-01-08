# First obtain and open the file
fileName = raw_input("Please input the file name: ")
if fileName.find('.txt.') == -1:
    fileName = fileName + '.txt'
f = open(fileName, 'r')

# Find the complementary base utilizing dictionary
complementBase = {"A":"T", "C":"G", "G":"C", "T":"A"}
secondStrand = ""
for strand in f:
    for base in strand:
        if base != "\n":
            secondStrand = complementBase[base] + secondStrand 
print secondStrand
