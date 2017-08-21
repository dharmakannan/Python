#!C:\Python27\python
'''def EvenOdd(x,y):
	even=0
	odd=0
	if y>x:
		for i in range(x,y+1):
			if i%2!=0:
				odd+=i
			else:
				even+=i
	else:
		print("Invalid I/P: %d is greater than %d" %(x,y))
	return even,odd
	
if __name__=="__main__":		
	lb,ub=input("Enter lower & upper range\n")
	even,odd=EvenOdd(lb,ub)
	print("Sum of Even no in given range {2} to {1} is {0}".format(even,ub,lb))
	print("Sum of Odd no in given range {2} to {1} is {0}".format(odd,ub,lb))'''
	
	
#Same program using while
print("Outside of main\n",__name__)
def EvenOdd(x,y):
	even=0
	odd=0
	while (x<=y):
		if x%2==0:
			even+=x
		else:
			odd+=x
		x+=1
	return even,odd
		
def main():
	lb,ub=input("Enter lower & upper range\n")
	even,odd=EvenOdd(lb,ub)
	print("Sum of Even no in given range {2} to {1} is {0}".format(even,ub,lb))
	print("Sum of Odd no in given range {2} to {1} is {0}".format(odd,ub,lb))

if __name__=="__main__":		
	main()
