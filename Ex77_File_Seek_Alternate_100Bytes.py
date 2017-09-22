#!C:\Python27\python
def Read_10(fd):
	while True:
		data=fd.read(10)
		print data
		if data=="":
			break
		fd.seek(10,1)
	

def Seek_Alternate_Ten(filename):
	fd=open(filename)
	Read_10(fd)
	fd.seek(10,0)
	Read_10(fd)
		   
def main():
	filename=input("Enter filename:\n")
	Seek_Alternate_Ten(filename)
	
	
if __name__=="__main__":
	main()