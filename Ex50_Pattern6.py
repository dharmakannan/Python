#!C:\Python27\python
def Pattern6(n):
	for i in range(n,0,-1):
		for j in range(0,n-i):
			print" ",
		for k in range(1,i*2-1+1):
			print"*",
		print
	
def main():
	n=input("Enter the no of rows to be printed in Pattern6 format\n")
	Pattern6(n)

if __name__=="__main__":
	main()