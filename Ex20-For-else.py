#!C:\Python27\python
for x in range (1,10):
	print (x)
else:
	print ("Loop executed completely")

#In below code "else" statement will not be executed due to "Jump-break" statement
for x in range (1,10):
	print (x)
	if x%7==0:
		break
else:
	print ("Loop executed completely")