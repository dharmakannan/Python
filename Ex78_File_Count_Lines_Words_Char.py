#!C:\Python27\python
def Count_Lines_Words_Char(filename):
	count_line=0
	count_word=0
	count_char=0
	fd=open(filename)
	if fd!=None:
		lines=fd.readlines()
		for line in lines:
			count_line+=1
			line_list=line.split()
			for word in line_list:
				count_word+=1
				count_char+=len(word)
				
	return count_line,count_word,count_char		
			
	
def main():
	filename=input("Enter the Filename from which Lines,Words & Char to be counted\n")
	count_line,count_word,count_char=Count_Lines_Words_Char(filename)
	print("File has {} no of lines,{} no of words and {} no of char".format(count_line,count_word,count_char))

if __name__=="__main__":
	main()
	