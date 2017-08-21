#!C:\Python27\python
def SumAllNos():
	sum=0
	while(1):
		n=input("Enter the No to add\n0 to Exit\n")
		if n==0:
			break
		sum+=n
	return sum

res=SumAllNos()
print("Sum of All entered nos is %d" %res)

