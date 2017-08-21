#!C:\Python27\python

def ExtendList(l2,l3):
	j=0
	while j<len(l3):
		if type(l3[j])!=list:
			l2.append(l3[j])
		else:
			ExtendList(l2,l3[j])
		j+=1

def NeutralizeList(l1):
	i=0
	l2=[]
	while i<len(l1):
		if type(l1[i])!=list:
			l2.append(l1[i])
		else:
			ExtendList(l2,l1[i])
		i+=1
	print l2
	
def main():
	l1=input("Enter Nested list to be converted into single list\n")
	NeutralizeList(l1)

if __name__=="__main__":
	main()