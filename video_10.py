#Video_10 starts
#convert list into dictionary
#zip() : Convert into dictionary format : {"key":"Value"}
"""
roll_number = [101,102]
student_name = ["Divya","Sid"]
dict_format = zip(roll_number,student_name)
d = dict(dict_format)
for k in d:
    print(k,"=",d[k])
"""

#Functions:
#Two types:  User defined functions and Built-in functions
"""
1)User defined:
→Functions without parameters
→functions with parameters
→keyword based functions
→lambda function
→default functions
"""

#Without parameters:
"""
def sum():
    x=10
    y=20
    print(x+y)
sum() 
"""

#With parameters:
"""
def sum(x,y):
    print(x+y)
x = int(input("Enter first value:"))
y = int(input("Enter second value: "))
sum(x,y)
"""

#Keywords functions
"""
def sum(x,y,z):
    print(z-(x+y))
sum(z=100,x=50,y=10)
"""

#Lambda function
sum = lambda x,y : print(x,y)
sum(10,20)  # calling a function
 #10th video ends
 