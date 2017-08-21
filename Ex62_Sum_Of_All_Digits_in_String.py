#!C:\Python27\python
def SumOfAllDigits(input_str):
	sum=0
	i=0
	while i<len(input_str):
		if input_str[i].isdigit():
			sum+=int(input_str[i])
		i+=1
	return sum

	
def main():
	input_str=input("Enter the Alpha-Numeric string\n")
	res=SumOfAllDigits(input_str)	
	print("Sum of All Digits in Alpha-Numeric string {} is {}".format(input_str,res))
	
	
if __name__=="__main__":
	main()