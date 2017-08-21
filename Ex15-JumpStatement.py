#!C:\Python27\python
n=input("Enter the input Range\n")
sum=0
for i in range(1,n+1):
	if i%5==0:
		continue
	sum+=i
print("The sum of all nos of %d apart multiples of 5 is %d"%(n,sum))
#Break Statement
sum1=0
for i in range(1,n+1):
	if i%5==0:
		break
	sum1+=i
print("The sum of all nos of %d using BREAK statement of 5 is %d"%(n,sum1))
