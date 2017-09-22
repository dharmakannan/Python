#!C:\Python27\python
'''def Avg_State_Petrol(filename):
	fd=open(filename)
	total_col1=0
	total_col2=0
	total_col3=0
	num_lines=0
	if fd!=None:
		line=fd.readline()
		state=line.split()
		lines=fd.readlines()
		for line in lines:
			num_lines+=1
			x_list=line.split()
			total_col1+=int(x_list[1])
			total_col2+=int(x_list[2])
			total_col3+=int(x_list[3])
		avg_state1=total_col1/num_lines
		avg_state2=total_col2/num_lines
		avg_state3=total_col3/num_lines
	print("Avg Petrol price of {}={}".format(state[1],avg_state1))
	print("Avg Petrol price of {}={}".format(state[2],avg_state2))
	print("Avg Petrol price of {}={}".format(state[3],avg_state3))'''
	
def Avg_State_Petrol(filename):
	fd=open(filename)
	total_col1=0
	total_col2=0
	total_col3=0
	num_lines=0
	if fd!=None:
		line=fd.readline()
		state=line.split()
		state.remove(state[0])
		print state
		lines=fd.readlines()
		for line in lines:
			num_lines+=1
			x_list=line.split()
			x_list.remove(x_list[0])
			print x_list
			i=0
			for x in x_list:
				list[i]=[]
				list[i].append(x)
			print list[1]
				
				
			
			'''total_col1+=int(x_list[1])
			total_col2+=int(x_list[2])
			total_col3+=int(x_list[3])
		avg_state1=total_col1/num_lines
		avg_state2=total_col2/num_lines
		avg_state3=total_col3/num_lines
	print("Avg Petrol price of {}={}".format(state[1],avg_state1))
	print("Avg Petrol price of {}={}".format(state[2],avg_state2))
	print("Avg Petrol price of {}={}".format(state[3],avg_state3))'''
	
def main():
	filename="Petrol_States_Avg.txt"
	Avg_State_Petrol(filename)

if __name__=="__main__":
	main()