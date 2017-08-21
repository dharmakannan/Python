#!C:\Python27\python
def SumNonSix(x,y):
	sum=0
	for i in range(x,y+1):
		if i%6!=0:
			sum+=i
	return sum

def main():
	lb,ub=input("Enter lower & upper range\n")
	res=SumNonSix(lb,ub)
	print("Sum of no in given range {}to{} which are not mutiply by 6 is {}".format(lb,ub,res))

if __name__=="__main__":
	main()
	