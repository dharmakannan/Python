#!C:\Python27\python
def Not_Bad(inputstr,replacestr):
	start_index=inputstr.find("not")
	end_index=inputstr.find("bad")
	return inputstr.replace(inputstr[start_index:end_index+3],replacestr)
	

def main():
	inputstr=input("Enter the String to be converted\n")
	replacestr=input("Enter the Replace String\n")
	print Not_Bad(inputstr,replacestr)


if __name__=="__main__":
	main()


