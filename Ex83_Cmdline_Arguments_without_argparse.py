#!C:\Python27\python
import sys
def Copy_Files(src_file,dest_file):
	print ("Source File={} and Destination File={}".format(src_file,dest_file))

def main(args):
	print args
	print type(args)
	s_index=args.index("-s")
	src_file=args[s_index+1]
	d_index=args.index("-d")
	dest_file=args[d_index+1]
	Copy_Files(src_file,dest_file)
		
if __name__=="__main__":
	main(sys.argv[1:])