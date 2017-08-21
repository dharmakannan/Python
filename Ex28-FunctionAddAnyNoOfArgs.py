#!C:\Python27\python
def VariableArgsAdd(*args):
	sum=0
	for x in args:
		sum+=x
	return sum

res=VariableArgsAdd(1,2)
print(res)
res=VariableArgsAdd(1,2,3)
print(res)
res=VariableArgsAdd(1,2,3,4,8,2,6,10)
print(res)
	