#!C:\Python27\python
#Sequence statement
dd,mm,yy=input("Enter DD,MM,YY numbers with comma separated\n") # multi Assignment
if dd>0 and dd<32:
	if mm>0 and mm<13:
		if yy>0:
			#print("Yours DD=%d mm=%d yy=%d"%(dd,mm,yy))
			print("Date {}/{}/{} is Valid".format(dd,mm,yy))
		else:
			print("Yours yy=%d is invalid Year"%yy)
	else:
		print("Yours mm=%d is invalid Month" %mm)
else:
	print("Yours dd=%d is invalid Date"%dd)
