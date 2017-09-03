#!C:\Python27\python
student={"Name":"Dharma","Company":"QLogic"}
print type(student)
print student["Name"]
print student["Company"]
student["Name"]="Kannan"
print student["Name"]
print student["Company"]
student["marks"]=100
print student
for key in student: # iterating in Dictionary
	print key,student[key]
print student.has_key("marks")
print student.items()
for value in student.itervalues():
	print value
z=dict.fromkeys(student,2)
print z
