#!C:\Python27\python
def RotatedString(first_str,validate_str):
	if len(first_str)!=len(validate_str):
		return False
			
	return validate_str in first_str+first_str
		
def main():
	first_str=input("Enter the first string\n")
	validate_str=input("Enter the second string to check whether its a Rotated String of first or not\n")
	if RotatedString(first_str,validate_str):
		print("Validate string {} is rotated string of first string {}".format(validate_str,first_str))
	else:
		print("Validate string {} is NOT rotated string of first string {}".format(validate_str,first_str))
	
if __name__=="__main__":
	main()