#!C:\Python27\python
def webname(str):
	return str[4:-4]

url=input("Enter the URL from which domain name to be extracted\n")
dname=webname(url)
print("The extracted domain name from your entered {} url is {}".format(url,dname))


