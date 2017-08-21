#!C:\Python27\python

def Pattern3(n):
	for i in range(1,n+1):
		for j in range(1,n-i+1): # "j" loop is used for spaces
			print" ",# space & "," to hold the cursor
		for k in range(1,i+1): # "k" loop is used to print "*"
			print"*", # "," is needed to hold the cursor otherwise it will go to the next line
		print

def main():
	no=input("Enter the no of rows for pattern to be printed\n")
	Pattern3(no)

if __name__=="__main__":
	main()