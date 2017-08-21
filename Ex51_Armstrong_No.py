#!C:\Python27\python
def SumOfCubesOfDigit(no):
	no1=no
	rem=0
	res=0
	while(no1!=0):
		rem=no1%10
		res=res+rem**3
		no1=no1/10
	print("Sum of Cubes of Digits of no {} is {}".format(no,res))
	return res
	
def Armstrong(no):
	armno=SumOfCubesOfDigit(no)
	if armno==no:
		print("Entered no %d is Armstrong no"%no)
	else:
		print("Entered no %d is not Armstrong no"%no)

def main():
	no=input("Enter the no to check its Armstrong no or not\n")
	Armstrong(no)
	
if __name__=="__main__":
	main()