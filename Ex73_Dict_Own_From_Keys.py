#!C:\Python27\python
def from_keys(d1,value=None):
	#verify d1 is dictionary
	if type(d1)!=dict:
		return "{} is not a dictionary".format(d1)
	# verify if value is list
	result_dict={}
	if type(value)==list or type(value)==tuple:
		i=0
		length=len(d1.keys())
		for key in d1.keys():
			if  i+1==length and i+1!=len(value):
				result_dict[key]=value[i:]
			elif i<len(value):
				result_dict[key]=value[i]
				i+=1
			else:
				result_dict[key]=None
				
	else:
		for key in d1:
			result_dict[key]=value
	return result_dict
	
'''def from_keys(d1,value=None):
	#verify d1 is dictionary
	if type(d1)!=dict:
		return "{} is not a dictionary".format(d1)
	# verify if value is list
	result_dict={}
	if type(value)==list or type(value)==tuple:
		i=0
		for key in d1.keys():
			if i<len(value):
				result_dict[key]=value[i]
				i+=1
			else:
				result_dict[key]=None
			
		if len(value)>len(d1):
			result_dict[key]=value[i:]
	else:
		for key in d1:
			result_dict[key]=value
	return result_dict'''
	
		
		
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