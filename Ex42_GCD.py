#!C:\Python27\python
def GCD(no1,no2):
	while(no1!=no2):
		if no1>no2:
			no1=no1-no2
		else:
			no2=no2-no1
	return no1

def main():
	no1,no2=input("Enter two nos to get the GCD value\n")
	res=GCD(no1,no2)
	print("The GDC of %d and %d is %d"%(no1,no2,res))

if __name__=="__main__":
	main()