#First obtain and open the file
fileName = raw_input("Please input the file name: ")
if fileName.find('.txt.') == -1:
    fileName = fileName + '.txt'
f = open(fileName, 'r')

# the first string is s and the second one is t
s = f.readline().rstrip()
t = f.readline().rstrip()
start = s.find(t)
positions = ""
while start > 0:
    positions = positions + str(start + 1) + " "
    start = s.find(t, start + 1)
    
print positions
