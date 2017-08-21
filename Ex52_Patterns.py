#!C:\Python27\python
def Pattern1(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
			print"*",  # "," is needed to hold the cursor otherwise it will go to the next line
		print

def Pattern2(n):
	for i in range(1,n+1):
		for j in range(1,n+2-i):
			print"*",
		print

def Pattern3(n):
	for i in range(1,n+1):
		for j in range(1,n-i+1): # "j" loop is used for spaces
			print" ",# space & "," to hold the cursor
		for k in range(1,i+1): # "k" loop is used to print "*"
			print"*", # "," is needed to hold the cursor otherwise it will go to the next line
		print

def Pattern4(n):
	for i in range(1,n+1):
		for j in range(1,i+1-1):
			print" ",
		for k in range(1,n+2-i):
			print"*",
		print

def Pattern5(n):
	for i in range(1,n+1):
		for j in range(1,n+1-i):
			print" ",
		for k in range(1,i*2):
			print"*",
		print	
		
def Pattern6(n):
	for i in range(n,0,-1):
		for j in range(0,n-i):
			print" ",
		for k in range(1,i*2-1+1):
			print"*",
		print
		
def main():
	pat=input("Choose the Patter to display\n1.Pattern1\n2.Pattern2\n3.Pattern3\n4.Pattern4\n5.Pattern5\n6.pattern6\n")
	n=input("Enter the no of rows to be diplayed in your specified Pattern format\n")
	if pat==1:
		Pattern1(n)
	elif pat==2:
		Pattern2(n)
	elif pat==3:
		Pattern3(n)
	elif pat==4:
		Pattern4(n)
	elif pat==5:
		Pattern5(n)
	elif pat==6:
		Pattern6(n)
	else:
		print("Entered Pattern choice is invalid")
	
if __name__=="__main__":
	main()