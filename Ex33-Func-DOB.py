#!C:\Python27\python
def DateOfBirth(dd,mm,yy):
	if dd>0 and dd<32:
		if mm>0 and mm<13:
			if yy>0:
				print("Entered Date of birth {}/{}/{} is Valid".format(dd,mm,yy))
			else:
				print("Entered Year {} is invalid".format(yy))
		else:
			print("Entered Month{} is invalid".format(mm))
	else:
		print("Entered Date{} is invalid".format(dd))

dd,mm,yy=int(input("Enter the Date, Month & Year of birth separated by commans\n"))

DateOfBirth(dd,mm,yy)