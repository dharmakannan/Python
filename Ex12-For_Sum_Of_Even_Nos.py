#!C:\Python27\python
'''for x in range(101):
	print x'''
n=input("Enter the Upper Bound range\n")
sum=0
for x in range(2,n+1,2):
	sum+=x
print("Sum of Even nos upto %d is %d" %(n,sum))