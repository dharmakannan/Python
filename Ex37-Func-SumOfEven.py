#!C:\Python27\python
def SumOfEven(n):
	i=0
	sum=0
	while i<=n:
		if i%2==0:
			sum+=i
		i+=1
	return sum

n=input("Enter the No range to add\n")
res=SumOfEven(n)
print("Sum of Even no in given range %d is %d" %(n,res))

