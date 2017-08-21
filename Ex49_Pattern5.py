#!C:\Python27\python
def Pattern5(n):
	for i in range(1,n+1):
		for j in range(1,n+1-i):
			print" ",
		for k in range(1,i*2):
			print"*",
		print		

def main():
	n=input("Enter the no of rows to be printed in Pattern5 format\n")
	Pattern5(n)
	
if __name__=="__main__":
	main()