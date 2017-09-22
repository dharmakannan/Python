#!C:\Python27\python
import os
import shutil
def Make_Archive_Files(arg,directories,files):
	for file in files:
		base_path=os.path.join(directories,file)
		shutil.make_archive(base_path,arg,directories,file)
	
def main():
	dir_path=input("Enter the Directory Path to create Archives of all files\n")
	format=input("Enter the Archive format to create\n")
	os.path.walk(dir_path,Make_Archive_Files,format)
	
if __name__=="__main__":
	main()