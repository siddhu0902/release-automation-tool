# #Functions
# def function(fname):
#     print(fname + " Redfnes")
# function("Emil")
# function("Tobias")
# function("Linus")

# def sum():
#     x=10
#     y=20
#     print(x+y)
# sum()

# def sum(x,y):
#     print(x+y)
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# sum(x,y)

#Calculator
# def add(num_1, num_2):
#     print("The sum is:", num_1 + num_2)

# def subtract(num_1, num_2):
#     print("The subtraction is:", num_1 - num_2)

# def multiply(num_1, num_2):
#     print("The multiplication is:", num_1 * num_2)

# def divide(num_1, num_2):
#     if num_2 != 0:
#         print("The division is:", num_1 / num_2)
#     else:
#         print("Cannot divide by zero")

# count = 0
# while count < 5:
#     num_1 = int(input("Enter first number: "))
#     num_2 = int(input("Enter second number: "))
#     a = input("Enter the sign (+, -, *, /): ")

#     if a == "+":
#         add(num_1, num_2)
#     elif a == "-":
#         subtract(num_1, num_2)
#     elif a == "*":
#         multiply(num_1, num_2)
#     elif a == "/":
#         divide(num_1, num_2)
#     else:
#         print("Invalid operation")

#     count += 1

#Number of Arguments
'''
def my_function(fname,Mname,lname):
    print(fname + " "+ Mname + " " +lname)
my_function("Siddharth","Reddy","Chowdavaram")
'''

#Use of **kwargs
'''
def my_function(**kid):
    print("His last name is: " + kid["lname"])
my_function(fname = "Siddharth" , lname = "Reddy")
'''

#Use of *args
'''
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Siddharth","Nayan","Reddy")
'''

'''
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Zimbambwe")
'''
'''
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
my_function(fruits)
'''
'''
def f1():
    s = 'Welcome to Amrita'

    def f2():
        print(s)

    f2()
f1()
'''
#Return statement in python function
'''
def square_value(num):
    return num**2
print(square_value(2))
print(square_value(-4))
'''

#Pass by reference and pass by value
'''
def myFun(x):
    x[0] = 20
lst = [10,11,12,13,14,15]
myFun(lst)
print(lst)
'''

