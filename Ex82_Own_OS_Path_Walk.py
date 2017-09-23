#!C:\Python27\python
import os.path

def Norm_Case(file_path):
	pass

def Norm_Path(file_path):
	pass

def menu():
	file_path=input("Enter the file name with or without Path")
	while True:
		choice=input("Enter the method to perform\n1.NormCase\2.NormPath\n8.Exit\n")
		if choice==1:
			Norm_Case(file_path)
		elif choice==2:
			Norm_Path(file_path)
		elif choice==8:
			break
		else:
			print("Entered Invalid choice")
	
def main():
	menu()
	
if __name__=="__main__":
	main()
