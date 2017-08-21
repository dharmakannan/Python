#!C:\Python27\python
def Consective_Char_Count(input_str):
	output_str=""
	i=0
	while i<len(input_str):
		ch=input_str[i]
		count=1
		while i+1<len(input_str) and ch==input_str[i+1]:
			count+=1
			i+=1
		output_str+=ch
		if count>1:
			output_str+=str(count)
		i+=1
	return output_str
	
	
def main():
	input_str=input("Enter the Consective Repatitive string\n")
	res=Consective_Char_Count(input_str)	
	print("Converted string Consective Repatitive String {}= {}".format(input_str,res))
	
if __name__=="__main__":
	main()