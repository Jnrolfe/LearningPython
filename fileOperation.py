#fileOperation.py
#by James Rolfe
#this file demonstrates reading from a file in python3
'''
f = open ('myfile.txt', 'r')

firstLine = f.readline()
secondLine = f.readline()
print (firstLine, end = '') #gets rid of \n
print (secondLine) #still has implied \n

#loop iteration through text file
for line in f:
	print(line, end = '')
print() #adds return, equivalent to \n

f.close()#closes file to conserve resources

f = open ('myfile.txt', 'a')#opens file under precendent to APPEND any additions
#to already existing text in the file
# a = APPEND
# w = WRITE (will overwrite all existing text)
# r = READ (will throw error if you try to write to)
# r+ = both WRITE and READ

f.write('\nThis sentence will be appended.')
f.write('\nPython is Fun!')

f.close()
'''

inputFile = open('myfile.txt', 'r')
outputFile = open ('myOutputFile.txt', 'w')

msg = inputFile.read(10)#only reads 10 char at a time, includes spaces
i = 0

while len(msg):#len = string length function
	outputFile.write(msg + '\n')#return added to show string length of 10 in output file
	msg = inputFile.read(10 + i)#travese through text file 10 at a time
	i += 1

inputFile.close()
outputFile.close()