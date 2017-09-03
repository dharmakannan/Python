#!C:\Python27\python
def Selection_Sort(l1):
	k=0
	while k<len(l1):
		for i in range(k,len(l1)):
			if i+1<len(l1) and l1[k]>l1[i+1]:
				l1[k],l1[i+1]=l1[i+1],l1[k]
		print l1
		k+=1
	return l1
			
def main():
	input_list=input("Create a list with varying nos\n")
	res_list=Selection_Sort(input_list)
	print("The Selection Sorted list is {}".format(res_list))
	
if __name__=="__main__":
	main()