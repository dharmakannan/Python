#!C:\Python27\python
#Sequence statement
num1,num2=input("Enter 2 numbers with comma separated\n") # multi Assignment
print("%d-%d is %d" %(num1,num2,(num1-num2)))
#Selection
result=0
num1,num2=input("Enter 2 numbers with comma separated\n") # multi Assignment
if num1>num2:
	result=num1-num2
else:
	result=num2-num1
print("result=%d"%result)
#Elif & Nested IF
a,b,c=input("Enter 3 numbers with comma separated\n") # multi Assignment
if a>b:
	print("Hello")
elif a>c:
	print("Bye")
else:
	print("Catch")
#Nested IF
'''if a>b:
	if a>c:
		print a
	else:
		print c
elif:'''
		
