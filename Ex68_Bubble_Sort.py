#!C:\Python27\python
def Bubble_Sort(l1):
	for x in range(len(l1)-1,0,-1):
		for i in range(x):
			if l1[i]>l1[i+1]:
				l1[i],l1[i+1]=l1[i+1],l1[i]
	return l1
	
def main():
	input_list=input("Create a list with varying nos\n")
	res_list=Bubble_Sort(input_list)
	print("The Bubble Sorted list is {}".format(res_list))
	
if __name__=="__main__":
	main()