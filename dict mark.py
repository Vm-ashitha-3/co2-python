dict1={}
x=int(input("enter the limit of students"))
for i in range(0,x):
   key=int(input("enter the student roll no:"));
   value1=int(input("enter the mark of 1st student:"));
   value2=int(input("enter the mark of 2nd student:"));
   value3=int(input("enter the mark of 3rd student:"));
   value4=int(input("enter the mark of 4th student:"));
   value5=int(input("enter the mark of 5th students:"));
   dict1[key]=value1,value2,value3,value4,value5
print(dict1)
