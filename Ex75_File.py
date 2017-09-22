#!C:\Python27\python
fd=open("File.txt")
lines=fd.readlines()
dict_file={}
for line in lines:
	key,value=line.split("=")
	dict_file[key]=value.strip()
	
print dict_file
	