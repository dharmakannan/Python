#!C:\Python27\python
def Union(l1,l2):
	l3=[]
	for i in l1:
		if i not in l3:
			l3.append(i)
	for j in l2:
		if j not in l1:
			l3.append(j)
	return l3
	
def Intersection(l1,l2):
	l3=[]
	i=0
	while i<len(l2):
		if l2[i] in l1:
			l3.append(l2[i])
		i+=1
	return l3

def InverseIntersection(l1,l2):
	l3=[]
	for i in l2:
		if i not in l1 and i not in l3:
			l3.append(i)
	for j in l1:
		if j not in l2 and j not in l3:
			l3.append(j)
	return l3
	
def main():
	l1=input("Enter List 1 \n")
	l2=input("Enter List 2 \n")
	res=Union(l1,l2)
	print("Union of l1 & l2 is {}".format(res))
	res=Intersection(l1,l2)
	print("Intersection of l1 & l2 is {}".format(res))
	res=InverseIntersection(l1,l2)
	print("InverseIntersection of l1 & l2 is {}".format(res))
	
if __name__=="__main__":
	main()