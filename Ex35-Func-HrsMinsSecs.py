#!C:\Python27\python
def ValidTime(hh,mins,secs):
	if hh>0 and hh<25:
		if mins>0 and mins<61:
			if secs>0 and secs<61:
				print("Entered Time {}:{}:{} is valid".format(hh,mins,secs))
			else:
				print("Entered Secs value {} is invalid".format(secs))
		else:
			print("Entered Mins value {} is invalid".format(mins))
	else:
		print("Entered Hours value {} is invalid".format(hh))

hh,mins,secs=input("Enter Hours, Mins & secs values separated by commas\n")
ValidTime(hh,mins,secs)