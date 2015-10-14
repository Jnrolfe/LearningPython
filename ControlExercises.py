#ControlExercises.py
#by James Rolfe
#This program shows how to use various control statements in Python3

'''
userInput = input('Enter 1 or 2: ')

if userInput == "1":
	print ("Hello World")
	print ("How are you?")
elif userInput == "2":
	print("Python3")
else:
	print("stuff")

#declaring enum or list
pets = ['cats', 'dogs', 'rabbits', 'hamsters']


#for loop iterates through pets enum
for a in pets:
	print(a)

#will print all integers from 0 to 20
for i in range(21):
	print(i)

#will print all EVEN integers from 0 to 20 
for i in range(0,21,2):
	print (i)

#var declaration
j = 0
for i in range(5):
	j += 2 #adds 2 to j
	print ('\ni = ', i, ', j = ', j)
	if j == 6:
		continue #skips rest of block
	print('I will be skipped if j = 6')
'''

try:
	answer = 1/0
	print(answer)
except:
	print('ERROR')