#!C:\Python27\python
def add(a,b=10):
	return a+b
res=add(100,200)
print("Result without default argument=%d"%res)
res=add(100)
print("Result with Default Argument=%d"%res)