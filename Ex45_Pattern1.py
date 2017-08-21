#!C:\Python27\python
'''def Pattern1(no):
	i=1
	while i<=no:
		print ("*"*i)
		i+=1'''
def Pattern1(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
			print"*",  # "," is needed to hold the cursor otherwise it will go to the next line
		print

def main():
	no=input("Enter the no of rows for pattern to be printed\n")
	Pattern1(no)

if __name__=="__main__":
	main()