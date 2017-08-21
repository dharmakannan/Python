#!C:\Python27\python
def FiveArgs(a,b,c=10,d=1,e=1):
	return a,b,c,d,e

print FiveArgs(10,30)
print FiveArgs(10,b=20)
print FiveArgs(b=30,a=10)
print FiveArgs(10,20,c=100,d=200,e=300)
print FiveArgs(e=300,d=100,a=10,b=20,c=100)