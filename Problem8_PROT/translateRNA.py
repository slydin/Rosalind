import csv
#First obtain and open the file
fileName = raw_input("Please input the file name: ")
if fileName.find('.txt.') == -1:
    fileName = fileName + '.txt'
f = open(fileName, 'r')
#set up the RNA codon table for protein translation
RNA_CODON_TABLE = {}
with open("RNA_CODON_TABLE.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=' ')
    for row in reader:
        RNA_CODON_TABLE[row['Codon']] = row['AA']

# with the RNA Codon Table we can now translate RNA to proteins
# first check if the total length of the string is divisible by 3
protein = ""
codon = ""
gene = ""
for line in f:
    gene = gene + line.rstrip('\n')

for i in range(len(gene)):
    if i % 3 == 0 and i != 0:
        protein = protein + RNA_CODON_TABLE[codon]
        codon = ""
    codon = codon + line[i]
        
print protein
