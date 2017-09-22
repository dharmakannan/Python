#!C:\Python27\python
'''def Longest_line(filename):
	length=0
	fd=open(filename)
	if fd!=None:
		lines=fd.readlines()
		for line in lines:
			line=line.strip("\n") # to remove "\n" at the end of each line
			if len(line)>length:
				longest_line=line
				length=len(line)
			
	return longest_line'''

def Longest_Shortestline(filename):
	fd=open(filename)
	if fd!=None:
		line=fd.readline()
		max_line=line
		short_line=line
		while line!="":
			line=fd.readline()
			if line=="":
				break
			if len(line)>len(max_line):
				max_line=line
			
			if len(line)<len(short_line):
				short_line=line
				
	return max_line,short_line
	

def main():
	filename=input("Enter the Filename\n")
	max_line,short_line=Longest_Shortestline(filename)
	print("The Longest line in given file {} is '{}'".format(filename,max_line))
	print("The Shortest line in given file {} is '{}'".format(filename,short_line))
	
if __name__=="__main__":
	main()