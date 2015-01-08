import GCFinder

# First obtain and open the file
fileName = raw_input("Please input the file name: ")
if fileName.find('.txt.') == -1:
    fileName = fileName + '.txt'
f = open(fileName, 'r')

gcfinder = GCFinder.GCFinder(f)
gcfinder.store()
strand, topGC = gcfinder.find()
print strand, topGC * 100
