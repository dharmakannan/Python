#!C:\Python27\python
lb,ub=input("Enter the Lower Bound & Upper Bound range\n")
even=0
odd=0
for x in range(lb,ub+1):
	if x%2==0:
		even+=x
	else:
		odd+=x
print("The sum of Even of nos in User entered range {} to {} is {}".format(lb,ub,even))
print("The sum of Odd of nos in User entered range {} to {} is {}".format(lb,ub,odd))
	