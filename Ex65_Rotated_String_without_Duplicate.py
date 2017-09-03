#!C:\Python27\python
def RotatedString(first_str,validate_str):
	if len(first_str)!=len(validate_str):
		return False
	str_list=[]
	temp_str=first_str
	while True:
		temp_str=temp_str[-1]+temp_str[:len(temp_str)-1]
		str_list.append(temp_str)
		if temp_str==first_str:
			break
	print("All possible Rotated combination of input string is {}".format(str_list))
	#print validate_str in str_list
	return validate_str in str_list
					
def main():
	first_str=input("Enter the first string\n")
	validate_str=input("Enter the second string to check whether its a Rotated String of first or not\n")
	if RotatedString(first_str,validate_str):
		print("Validate string {} is rotated string of first string {}".format(validate_str,first_str))
	else:
		print("Validate string {} is NOT rotated string of first string {}".format(validate_str,first_str))
	
if __name__=="__main__":
	main()