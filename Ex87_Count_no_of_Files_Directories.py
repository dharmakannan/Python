#!C:\Python27\python
import os
count_fpy=0
count_ftxt=0
count_fconf=0
count_fpyc=0
count_dir=0
def Count_Files_Directories(arg,directories,files):
	global count_fpy
	global count_ftxt
	global count_fconf
	global count_fpyc
	global count_dir
	for file in files:
		if file.endswith(".py"):
			count_fpy+=1
		elif file.endswith(".txt"):
			count_ftxt+=1
		elif file.endswith(".conf"):
			count_fconf+=1
		elif file.endswith(".pyc"):
			count_fpyc+=1
		else:
			count_dir+=1


def main():
	dir_path=input("Enter the Directory path to Count the files & directories\n")
	os.path.walk(dir_path,Count_Files_Directories,format)
	print("The given Directory {} have {} no of python files,{} no of Text files,{} no of Conf files,{} no of Pyc files & {} no of Directories".format(dir_path,count_fpy,count_ftxt,count_fconf,count_fpyc,count_dir))

if __name__=="__main__":
	main()