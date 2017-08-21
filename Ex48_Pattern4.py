#!C:\Python27\python
def Pattern4(n):
	for i in range(1,n+1):
		for j in range(1,i+1-1):
			print" ",
		for k in range(1,n+2-i):
			print"*",
		print

def main():
	n=input("Enter the no of rows to be printed in Pattern4 formar\n")
	Pattern4(n)
	
if __name__=="__main__":
	main()