#!C:\Python27\python
def Reverse(no):
	rev=0
	rem=0
	while no!=0:
		rem=no%10 #1234%10=4
		rev=rev*10+rem #0*10+4=4
		no=no/10#1234/10=123 for Python 3.5 put "no//10"
	return rev
def Palindrome(no):
	rev=Reverse(no)
	if no==rev:
		print("%d is Palindrome"%no)
	else:
		print("%d is not Palindrome"%no)
	
def main():
	no=input("Enter the no to be Reversed\n")
	res=Reverse(no)
	print("The Reverse no of %d is %d" %(no,res))
	Palindrome(no)
	
if __name__=="__main__":
	main()
