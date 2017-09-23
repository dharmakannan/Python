#!C:\Python27\python
import tempfile
def Temp_Function():
	tmp_file=tempfile.NamedTemporaryFile(mode='w+b',dir="C:\Users\dkannan\Documents\Study_Material\Python\Exercises",prefix="Ex89_tmp",suffix=".txt",delete=False)
	tmp_file.write("Hello")
	print tmp_file.tell()
	tmp_file.seek(0,0)
	print tmp_file.read()

def main():
	Temp_Function()
	
if __name__=="__main__":
	main()