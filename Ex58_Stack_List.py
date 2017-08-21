#!C:\Python27\python

def IsStackEmpty(l1):
	if l1==[]:
		return True
	else:
		return False
		
def IsStackFull(l1):
	if len(l1)>=4:
		return True
	else:
		return False
	
def DisplayStack(l1):
	print("Current Stack={}\n".format(l1))

def Push(l1):
	if not IsStackFull(l1):
		no=input("Enter the element to Push into the stack\n")
		l1.append(no)
	else:
		print("Sorry!!! Can't Add element as Stack is Full\n")
	return l1
	
def Pop(l1):
	if not IsStackEmpty(l1):
		print("Removed element from Top of the stack is {}".format(l1.pop()))
	else:
		print("Sorry!!! Can't remove as Stack is Empty\n")
	
def Peep(l1):
	if not IsStackEmpty(l1):
		print("Current Top element in the stack={}".format(l1[len(l1)-1]))
	else:
		print("Sorry!!! Can't Peep as Stack is Empty\n")
	
'''def DeleteStack(l1):
	del(l1)
	print("Stack Deleted succesfully\n")'''

def menu(l1):
	while True:
		choice=input("Choose the Stack Operation\n1.Push\n2.Pop\n3.IsStackFull\n4.IsStackEmpty\n5.Peep\n6.Display\n7.Delete\n8.Exit\n")
		
		if choice==1:
			Push(l1)
			
		elif choice==2:
			Pop(l1)
			
		elif choice==3:
			if IsStackFull(l1):
				print("Stack is Full\n")
			else:
				print("Stack is not Full\n")
		
		elif choice==4:
			if IsStackEmpty(l1):
				print("Stack is Empty\n")
			else:
				print("Stack is not Empty\n")
			
		elif choice==5:
			Peep(l1)
			
		elif choice==6:
			DisplayStack(l1)
		
		elif choice==7:
			#DeleteStack(l1)
			del(l1)
			print("Stack deleted succesfully\n")
			
		elif choice==8:
			print("Exiting the Menu\n")
			break
		else:
			print("You entered invalid choice\n")
			
def main():
	l1=input("Create a Stack\n")
	menu(l1)
	
if __name__=="__main__":
	main()
