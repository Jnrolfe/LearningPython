#myPythonFunctions.py
#By James Rolfe
#this file contains the functions used in the mathGame.py file

from random import randint
from os import remove, rename

#passMe = "hi"

def getUserPoint(userName):
	try:
		inputFile = open('userScores.txt', 'r')#attempt to open file, read-only
		for line in inputFile:#iterate over each line
			content = line.split(',')#split the line into two separate strings excluding the comma
			if content[0] == userName:#check username
				inputFile.close()
				return content[1]#return user score associated with user name
		print("user name not found")
		inputFile.close()
		return '-1'
	except IOError:
		print('ERROR 404: userScores.txt not found')
		newFile = open('userScores.txt', 'w')#makes new file
		print('userScores.txt created')
		newFile.close()

def updateUserPoints(newUser, userName, score):
	if newUser == True: #see if new user
		outputFile = open('userScores.txt', 'a')#open file to append, create new file if not found
		outputFile.write('\n' + userName + ", " + score)#append name and score to end of file
		outputFile.close()
	else:
		tmpFile = open('userScores.tmp', 'w')#open file to write only
		outputFile = open('userScores.txt', 'a')#open file to append, create if doesn't exist <<< this is avoids the error of trying to read from a file that doesn't it
		outputFile.close()
		outputFile = open('userScores.txt', 'r')#re-open file to read
		for line in outputFile:
			content = line.split(",")
			if content[0] = userName:#check if the username is correct
				content[1] = score
				line = content[0] + ', ' + content[1]#rebuild the line
				tmpFile.write(line)#copy new updated line to temp file
			else:
				tmpFile.write(line)#if the name doesn't match, just copy the line to the temp file
		tmpFile.close()
		outputFile.close()

		remove('userScores.txt')
		rename('userScores.tmp', 'userScores.txt')

#declare operator and operand lists
operandList = [0, 0, 0, 0, 0]
operatorList = ["", "", "", ""]
operatorDict = {1:"+", 2:"-", 3:"*", 4:"**"}

#replace declared list with random values
for i in operandList:
	operandList[i] = randint(1, 9)

#replace
for i in operatorList:
	if i == 0:
		operatorList[i] = operatorDict[randint(1, 4)]
	elif operatorList[i-1] == operatorDict[4]:
		operandList[i] = operatorDict[randint(1,3)]
	else:				
		operatorList[i] = operatorDict[randint(1, 4)]

questionString = ""

for i in operatorList:
	questionString = questionString + operandList[i] + operatorList[i]
questionString = questionString + operatorList[-1]
#what = getUserPoint(passMe)