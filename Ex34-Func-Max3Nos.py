#!C:\Python27\python
def max3nos(no1,no2,no3):
	if no1>no2 and no1>no3:
		print("{} is greater no of 3 nos".format(no1))
	elif no2>no3:
		print("{} is greater no of 3 nos".format(no2))
	else:
		print("{} is greater no of 3 nos".format(no3))

def min3nos(no1,no2,no3):
	if no1<no2 and no1<no3:
		print("{} is minimum no of 3 nos".format(no1))
	elif no2<no3:
		print("{} is minimum no of 3 nos".format(no2))
	else:
		print("{} is minimum no of 3 nos".format(no3))
		
n1,n2,n3=input("Enter 3 nos separated by commas\n")
max3nos(n1,n2,n3)
min3nos(n1,n2,n3)