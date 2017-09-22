#!C:\Python27\python
import ConfigParser

'''def Config_Parser_Write(config_obj):
	config_obj.add_section("SERVER-1")
	config_obj.set("SERVER-1","ip","172.28.39.87")
	config_obj.set("SERVER-1","port","3450")
	config_obj.set("SERVER-1","Test_Cases",["Top","meminfo"])
	config_obj.add_section("SERVER-2")
	config_obj.set("SERVER-2","ip","172.28.40.15")
	config_obj.set("SERVER-2","port","3450")
	config_obj.set("SERVER-2","Test_Cases",["Middle"])
	config_obj.add_section("SERVER-3")
	config_obj.set("SERVER-3","ip","172.28.41.118")
	config_obj.set("SERVER-2","port","3450")
	config_obj.set("SERVER-3","Test_Cases",["Last","Add Delete","LoadUnload"])
	with open("Config.conf","w") as configfile:
		config_obj.write(configfile)'''
		
def Config_Parser_Parse(config_obj,filename):
	config_obj.read(filename)
	Sections_List=config_obj.sections()
	outer_dict={}
	for Section in Sections_List:
		list1=config_obj.options(Section)
		i=0
		inner_dict={}
		while i<len(list1):
			value=config_obj.get(Section,list1[i]).split("#")[0]
			inner_dict[list1[i]]=value
			i+=1
		outer_dict[Section]=inner_dict
	return outer_dict
	

def main():
	filename=input("Enter the filename\n")
	config_obj=ConfigParser.ConfigParser()
	#Config_Parser_Write(config_obj)
	#print Config_Parser_Parse(config_obj)
	print Config_Parser_Parse(config_obj,filename)
	
if __name__=="__main__":
	main()