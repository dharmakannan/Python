#!C:\Python27\python

def CountString(inputstr,searchstr):
	count=0
	index=0
	while index!=-1:
		index=inputstr.find(searchstr)
		if index!=-1:
			count+=1
			inputstr=inputstr[index+1:]
	return count

def main():
	inputstr=input("Enter the Input String\n")
	searchstr=input("Enter the Search String\n")
	res=CountString(inputstr,searchstr)
	print res
	
if __name__=="__main__":
	main()