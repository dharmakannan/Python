#!C:\Python27\python
x=10
def foo():
	global x
	x=100
	print ("inside function x=%d" %x)

if __name__=="__main__":
	print x
	foo()
	print x