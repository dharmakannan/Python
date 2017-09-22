#!C:\Python27\python
'''def Compare_Dicts(d1,d2):
	if type(d1)!=dict and type(d2)!=dict:
		return False
	if len(d1)!=len(d2):
		return False
	count=0
	for key in d1.keys():
		if key in d2.keys():
			if d1[key]==d2[key]:
				count+=1
				continue
			else:
				break
		else:
			break
	if count==len(d1):
		return True
	else:
		return False'''
		
def Compare_Dicts(d1,d2):
	retrival=True
	if type(d1)!=dict or type(d2)!=dict:
		retrival=False
	else:
		if len(d1)!=len(d2):
			retrival=False
		else:
			for key in d1.keys():
				if key in d2.keys() and d1[key]==d2[key]:
					continue
				retrival=False
				break
	return retrival
		
def main():
	dict1=input("Enter elements for Dictionary 1\n")
	dict2=input("Enter elements for Dictionary 2\n")
	#dict1={"Name":"Dharma","Work":"Qlogic"}
	#dict2={"Name":"Dharma","Work":"Qlogic"}
	if Compare_Dicts(dict1,dict2):
		print("{} and {} are same".format(dict1,dict2))
	else:
		print("{} and {} are NOT same".format(dict1,dict2))

	
if __name__=="__main__":
	main()
	
