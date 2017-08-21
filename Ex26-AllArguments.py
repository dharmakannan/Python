#!C:\Python27\python
def Add(a,b,c=20):# Default Arguments
	return a+b+c
print Add(10,10)# Positional Arguments
print Add(10,b=30) # Keyword Arguments
print Add(b=10,a=20)
print Add(1,c=200,b=100)
#print Add(b=30,20) # Will not work. As positional Argument should be always first followed by "Keyword Arguments". 
#Also all the agruments coming after "Keyword Arguments" should all be keyword Arguments.
#print Add(1,b=20,100)# Will not work because once "Keyword Arguments" started then all the next agruments after it should be "Keyword Arguments"