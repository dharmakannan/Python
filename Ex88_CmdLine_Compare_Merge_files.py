#!C:\Python27\python
import argparse
import shutil
import os.path
def Compare_Files(src_file,dest_file):
	sfd=open(src_file)
	dfd=open(dest_file)
	if sfd!=None and dfd!=None:
		l1=sfd.readlines()
		l2=dfd.readlines()
		if len(l2)==len(l1):
			if l1==l2:
				return True
			else:
				return False
		else:
			return False
	sfd.close()
	dfd.close()
	
def Merge_Files(src_file,dest_file):
	fd1=open(src_file)
	fd2=open(dest_file)
	fd3=open("Merged_file.conf","w")
	shutil.copyfileobj(fd1,fd3)
	shutil.copyfileobj(fd2,fd3)
	fd1.close()
	fd2.close()
	fd3.close()

def File_Operations(src_file,dest_file):
	if Compare_Files(src_file,dest_file):
			print("Contents in Files {} and {} are Same.So no need to Merge it".format(src_file,dest_file))
	else:
			print("Contents in Files {} and {} are NOT Same, Hence Merging these two files".format(src_file,dest_file))
			Merge_Files(src_file,dest_file)
	
def main():
	parser=argparse.ArgumentParser()
	parser.add_argument("-f1",type=str,help="File 1 Name")
	parser.add_argument("-f2",type=str,help="File 2 Name")
	args=parser.parse_args()
	if os.path.exists(args.f1) and os.path.exists(args.f2):
		File_Operations(args.f1,args.f2)
	else:
		print("Error:File not exists")
			
if __name__=="__main__":
	main()