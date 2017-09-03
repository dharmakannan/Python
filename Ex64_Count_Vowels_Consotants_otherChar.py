#!C:\Python27\python
def CountVowelsConsotants(input_str):
	count_c=0
	count_v=0
	count_ch=0
	i=0
	while i<len(input_str):
		if not input_str[i].isalpha():
			count_ch+=1
		elif input_str[i]=="a" or input_str[i]=="e" or input_str[i]=="i" or input_str[i]=="o" or input_str[i]=="u":
			count_v+=1
		else:
			count_c+=1
		i+=1
	return count_v,count_c,count_ch
		
def main():
	input_str=input("Enter the String containing Vowels, Consotants & other Char\n")
	count_v,count_c,count_ch=CountVowelsConsotants(input_str)
	print("Entered String {} have {} Vowels,{} Consotants & {} other Char".format(input_str,count_v,count_c,count_ch))
	
if __name__=="__main__":
	main()