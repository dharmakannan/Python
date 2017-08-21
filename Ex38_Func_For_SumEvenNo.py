#!C:\Python27\python
import Ex40_Func_MutiplesOfNon6
print Ex40_Func_MutiplesOfNon6.SumNonSix(5,10) # Calling Function from other program using import that program & calling that function
def ForSumEven(n):
	sum=0
	for x in range(2,n+1,2):
		sum+=x
	return sum
	
def main():
	n=input("Enter the No range to sum it\n")
	res=ForSumEven(n)
	print("Sum of Even no is in given range %d is %d" %(n,res))
	
if __name__=="__main__":
	main()