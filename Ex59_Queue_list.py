#!C:\Python27\python

def IsQueueEmpty(l1):
	if l1==[]:
		return True
	else:
		return False
		
def IsQueueFull(l1):
	if len(l1)>=4:
		return True
	else:
		return False
	
def DisplayQueue(l1):
	print("Current Queue={}\n".format(l1))

def EnQueue(l1):
	if not IsQueueFull(l1):
		no=input("Enter the element to Add into the Queue\n")
		l1.append(no)
	else:
		print("Sorry!!! Can't Add element as Queue is Full\n")
	return l1
	
def DQueue(l1):
	if not IsQueueEmpty(l1):
		print("Removed element from front of the Queue is {}".format(l1.pop(0)))
	else:
		print("Sorry!!! Can't remove as Queue is Empty\n")
	
def Front(l1):
	if not IsQueueEmpty(l1):
		print("Current Front element in the Queue={}".format(l1[0]))
	else:
		print("Sorry!!! Can't Front as Queue is Empty\n")
	
def menu(l1):
	while True:
		choice=input("Choose the Queue Operation\n1.enQueue\n2.dQueue\n3.IsQueueFull\n4.IsQueueEmpty\n5.Front\n6.Display\n8.Exit\n")
		
		if choice==1:
			EnQueue(l1)
			
		elif choice==2:
			DQueue(l1)
			
		elif choice==3:
			if IsQueueFull(l1):
				print("Queue is Full\n")
			else:
				print("Queue is not Full\n")
		
		elif choice==4:
			if IsQueueEmpty(l1):
				print("Queue is Empty\n")
			else:
				print("Queue is not Empty\n")
			
		elif choice==5:
			Front(l1)
			
		elif choice==6:
			DisplayQueue(l1)
		
		elif choice==8:
			print("Exiting the Menu\n")
			break
		else:
			print("You entered invalid choice\n")
			
def main():
	l1=input("Create a Queue\n")
	menu(l1)
	
if __name__=="__main__":
	main()
