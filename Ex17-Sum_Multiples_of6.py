#!C:\Python27\python
lb,ub=input("Enter the Lower Bound, Upper Bound separated by commas\n")
sum=0
for x in range (lb,ub+1):
	if x%6!=0:
		continue
	sum+=x
print("Sum of multiples of 6 from range {} to {}={}".format(lb,ub,sum))