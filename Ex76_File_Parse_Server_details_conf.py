#!C:\Python27\python
				
def  File_Parse_Config_File(filename):
	result_dict={}
	fd=open(filename)
	if fd!=None:
		lines=fd.readlines()
		Section_details={}
		Section_name=""
		Section_found=False
		for line in lines:
			#print line
			if line.startswith("#"):
				continue
			if line.startswith("["):
				if Section_found==True:
					result_dict[Section_name]=Section_details
					Section_found=False
					
				if Section_found==False:
					Section_name=line[1:-2]
					Section_found=True
					Section_details={}
								
			elif Section_found==True:
				config_line=line.split("=")
				#print config_line
				if "#" in config_line[1]:
					config_line[1]=config_line[1].split("#")[0]
				Section_details[config_line[0]]=config_line[1].strip()
		else:
			result_dict[Section_name]=Section_details
				
	return result_dict	

def main():
	file_name=input("Enter the config file name\n")
	result=File_Parse_Config_File(file_name)
	print result
	
if __name__=="__main__":
	main()

