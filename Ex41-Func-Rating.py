#!C:\Python27\python
def Rating(rat):
	if rat==5:
		print("Rating is Exceptional")
	elif rat>=4 and rat<5:
		print("Rating is Excellent")
	elif rat>=3 and rat<4:
		print("Rating is Good")
	elif rat>=2 and rat<3:
		print("Rating is Improvement")
	elif rat>=1 and rat<2:
		print("Rating is Poor")
	else:
		print("Entered Rating value is invalid")

rat=input("Enter the Rating of the Employee\n")
Rating(rat)