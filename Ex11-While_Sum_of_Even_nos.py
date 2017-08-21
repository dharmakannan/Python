#!C:\Python27\python
n=input("Enter the value of n to display its sum of Even nos\n")
sum=0
i=0
while i<=n:
	if i%2==0:
		sum+=i
	i+=1
print("Sum of Even nos of %d from 0 is %d"%(n,sum))