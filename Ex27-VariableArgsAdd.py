#!C:\Python27\python
def VariableAgrsAdd(*args):
	print(type(args))
	for x in args:
		print(x)
VariableAgrsAdd(1,2)
VariableAgrsAdd(1,2,3)
VariableAgrsAdd(1,2,3,4,8,2,6,10)