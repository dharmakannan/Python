#!C:\Python27\python
def from_keys(d1,value='none'):
	list1=[]
	for key in d1:
		list1.append(key)
	if isinstance(value,list):
		if len(value)<len(list1):
			i=0
			while i<len(value):
				d1[list1[i]]=value[i]
				i+=1
			while i<len(list1):
				d1[list1[i]]='none'
				i+=1
		
		elif len(value)>len(list1):
			i=0
			while i<len(list1)-1:
				d1[list1[i]]=value[i]
				i+=1
			d1[list1[i]]=value[i:]
		
		else:
			i=0
			while i<len(list1):
				d1[list1[i]]=value[i]
				i+=1
		
	else:
		for key in d1:
			d1[key]=value
	return d1
		
def main():
	student={"Name":"Dharma","S.No":123,"Company":"Qlogic","pincode":"411015"}
	print student
	print from_keys(student)
	print from_keys(student,5)
	print from_keys(student,["kannan",456,"Cavium",511015])
	print from_keys(student,["James",789])
	print from_keys(student,["Gary",943,"EMC",811015,"USA","Aliso Vejo"])
	
	
	
	
if __name__=="__main__":
	main()