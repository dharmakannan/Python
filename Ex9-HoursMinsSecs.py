#!C:\Python27\python
hh,min,secs=input("Enter the Hours,Minutes & Seconds separated by commas\n")
if hh>0 and hh<25:
	if min>0 and min <61:
		if secs>0 and secs <61:
			print("Your Entered Time format {}:{}:{} is valid".format(hh,min,secs))		
		else:
			print("Entered Secs=%d is invalid"%secs)
	
	else:
		print("Entered Minutes=%d is invalid"%min)

else:
	print("Entered Hour=%d is invalid"%hh)