#!C:\Python27\python
name,rat=input("Enter the Employee name & his Appraisal Rating\n")
if rat==5:
	print("Employee {} Appraisal rating {} is Exceptional".format(name,rat))
elif rat>=4 and rat<5:
	print("Employee {} Appraisal rating {} is Excellent".format(name,rat))
elif rat>=3 and rat<4:
	print("Employee {} Appraisal rating {} is Good".format(name,rat))
elif rat>=2 and rat<3:
	print("Employee {} Appraisal rating {} is Improvement".format(name,rat))
elif rat<2:
	print("Employee {} Appraisal rating {} is poor".format(name,rat))
else:
	print("Your entered input {} is invalid".format(rat))
