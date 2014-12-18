#First obtain and open the file
fileName = raw_input("Please input the file name: ")
if fileName.find('.txt.') == -1:
    fileName = fileName + '.txt'
f = open(fileName, 'r')

# container for all the DNA strings
DNA = []
DNAStrand = ""

for line in f:
    if line.find("Rosalind_") < 0:
        DNAStrand = DNAStrand + line.strip()
    elif len(DNAStrand) > 0:
        DNA.append(DNAStrand)
        DNAStrand = ""
DNA.append(DNAStrand)

length = len(DNA[0])
# dictionary containing an array for each base
profile = {}
bases = ['A', 'C', 'G', 'T']
for i in range(len(bases)):
    positions = []
    for j in range(length):
        positions.append(0)
    profile[bases[i]] = positions

# Update the profile based on the DNA strings
for strand in range(len(DNA)):
    for position in range(len(DNA[strand])):
        profile[DNA[strand][position]][position] = profile[DNA[strand][position]][position] + 1
# Find the consensus on the common ancestor
consensus = ""
highest = 0
mostCommon = ""

for position in range(length):
    for row in range(len(DNA)):
        if profile[DNA[row][position]][position] > highest:
            highest = profile[DNA[row][position]][position]
            mostCommon = DNA[row][position]
    consensus = consensus + mostCommon
    highest = 0
    mostCommon = ""

print consensus
for strand in profile:
    output =  strand + ": "
    for position in range(len(profile[strand])):
        output = output + str(profile[strand][position]) + " "
    print output
