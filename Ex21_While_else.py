#!C:\Python27\python
x=1
while x!=10:
	print(x)
	x+=1
else:
	print ("Loop executed completely")

#In below code "else" statement will not be executed due to "Jump-break" statement
x=1
while x!=0:
	if x%10==0:
		break
	print(x)
	x+=1
else:
	print ("Loop executed completely")
