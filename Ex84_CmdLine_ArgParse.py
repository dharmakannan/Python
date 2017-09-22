#!C:\Python27\python
import argparse
import shutil
def Copy_Files(src_file,dest_file,no_of_lines):
	s_fd=open(src_file)
	d_fd=open(dest_file,"w")
	if no_of_lines!=0:
		i=0
		while i<no_of_lines:
			line=s_fd.readline()
			d_fd.write(line)
			i+=1
	else:
		shutil.copyfileobj(s_fd,d_fd)
	d_fd.flush()
	s_fd.close()
	
def main():
	parser=argparse.ArgumentParser()
	parser.add_argument("-s","--srcfile",type=str,help="Source File name",)
	parser.add_argument("-d","--destfile",type=str,help="Destination File name")
	parser.add_argument("-l","--length",type=int,help="No of lines to copy")
	args=parser.parse_args()
	#print args
	Copy_Files(args.s,args.d,args.l)
		
if __name__=="__main__":
	main()