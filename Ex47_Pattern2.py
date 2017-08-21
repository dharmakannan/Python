#!C:\Python27\python
def Pattern2(n):
	for i in range(1,n+1):
		for j in range(1,n+2-i):
			print"*",
		print
			
def main():
	n=input("Enter the no of Rows to be printed in Pattern2 format\n")
	Pattern2(n)
	
if __name__=="__main__":
	main()