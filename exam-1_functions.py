# def calculate(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# a=9
# b=8
# if(a>b):
#     print("First number is greater than the other")
# else:
#     print("Second number is greater than the other")
# calculate(a,b)

# def calculate(a,b):
#     mean = (a*b)/(a+b)
#     if(a>b):
#         print("The first number is greater than the second number")
#     else:
#         print("The second number is greater than the first number")
#     print(mean)
# a=5
# b=6
# calculate(a,b)
# c=9
# d=6
# calculate(c,d)

#Pass = if u want to write the code later in the function
# def isLesser(a,b):
#     pass

# def average(a=9,b=1):
#     print("the average is ",+(a+b)/2)
# average(4,6)          ## when the value is not given in default
# average()             ##when value is given in default
# average(1,5)          ##When value is given in default but u want to overide it

# def name(fname,mname="siddharth",lname="reddy"):
#     print("Hello",fname,mname,lname)
# name("Chowdavaram")

# def average(*numbers):
#     sum=0
#     print(type(numbers))
#     for i in numbers:
#         sum = sum+i
#     print("Average is ",sum/len(numbers))

# average(5,6)

##for cheking which data structure u r using type print(type(urname))

##Practise
#Factorial
# def factorial(n):
#     if n<0:
#         return
#     result = 1
#     for i in range(1,n+1):
#         result *= 1
#     return result
# print(factorial(5))

#prime numbers
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n*0.5)+1):
#         if(n%i==0):
#             return False
#     return True
# print(is_prime(6))
# print(is_prime(11))

#fibonaci
# def fibonacci(n):
#     fib = []
#     a,b=0,1
#     for _ in range(n):
#         fib.append(a)
#         a,b = b,a+b
#     return fib

# print(fibonacci(7))

# x=10
# def test():
#     x=5
# test()
# print(x)

#Practise
