#!C:\Python27\python
def Babble(inputstr,replacestr):
	return inputstr[0]+inputstr[1:].replace(inputstr[0],replacestr)

def main():
	inputstr=input("Enter the input string\n")
	replacestr=input("Enter the replace string\n")
	res=Babble(inputstr,replacestr)
	print("The Converted string of {} by replace str {}={}".format(inputstr,replacestr,res))
	

if __name__=="__main__":
	main()