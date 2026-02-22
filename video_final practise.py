#Lists
# k = ['apple','mango','banana']
# k[1] = 'orange'
# print(k)

#append() = it adds an element at the end of the list
#clear() = it removes all the elements from the list
#copy() = it creates a copy of the list
#count() = it counts the number of occurences of an element in the list
#extend() = it adds the elements of a list to the end of another list
#index() = it returns the index of the first occurence of an element in the list
#insert() = it adds an element at the specified position in the list
#pop() = it removes the element at the specified position in the list
#remove() = it removes the first occurence of an element in the list
#reverse() = it reverses the order of the elements in the list
#sort() = it sorts the elements of the list in the ascending order
#len() = it returns the length of the list

#Converting list into dictionary:
# zip() - convert into dictionary format
# {"key":"value"}
#dict() - convert list into dictionary

# roll_num = [101,102,104]
# student_name = ["sid","dad","mom"]
# dictionary_format = zip(roll_num,student_name)
# d = dict(dictionary_format)
# for k in d:
#     print(k,"=",d[k])

#Function
#very important
# def sum():
#     x=10
#     y=20
#     print(x+y)
# sum()             #→calling the value

# def sum(x,y):
#     print(x+y)
# x = int(input("enter first value: "))
# y = int(input("Enter second value: "))
# sum(x,y)

# def sum(x,y,z):
#     print(z-(x+y))
# sum(z=30,x=20,y=100)

# sum = lambda x,y,z : print(z-(x+y))
# sum(10,20,90)         #→one line function


# def happy_birthday(name,age):
#     print(f"Happy birthday to you {name}")
#     print(f"u r {age}")
#     print("happy birthday")
#     print()
# happy_birthday("sid",20)
# happy_birthday("mom",30)
# happy_birthday("dad",35)

# def display_invoice(username,amount,duedate):
#     print(f"Hello {username}")
#     print(f"your bill of ${amount:.2f} is due: {duedate}")
# display_invoice("Sid",100.01,"09/02")           #.2f is used for using definition upto two decimal places


#return - statement used to end a function and send a result back
# def add(x,y):
#     z = x+y
#     return z
# def subtract(x,y):
#     z = x-y
#     return z
# def multiply(x,y):
#     z = x*y
#     return z
# def divide(x,y):
#     z = x/y
#     return z
# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

# def creat_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
# full_name = creat_name("sid","reddy")
# print(full_name)

# def greet(name):
#      print(f"hi {name}")

# def get_greeting(name):
#     return f"hi {name}"
# message = get_greeting("Sid")
# print(greet("sid"))

#Parameter optional
# def increment(number,by=1):
#     return number + by
# print(increment(2,5))

#number of arguments
# def multiply(*numbers):
#     total = 1
#     for number in numbers:    #->for tuples   
#         total *= number
#     return total

# print(multiply(2,3,4,5))

#** to pass multiple inputs but use what we want
# def save_user(**user):
#     print(user["id"])
#     print(user["name"])
#     print(user["age"])
# save_user(id=1,name="Sid",age=22)           #→dictionary

# Scope
# message = "a"

# def greet(name):
#     message = "b"

# greet("Sid")
# print(message)

#fizz buz algorithm
# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0: 
#         return "Buzz"
#     return input
# print(fizz_buzz(5))
# print(fizz_buzz(3))
# print(fizz_buzz(15))
# print(fizz_buzz(7))