#Q1.Missing in each sets:
# set_1 = {1,2,3,4,5,6}
# set_2 = {3,4,5,6,7,8}
# print("The differnce w.r.t to set1 is:",set_1.difference(set_2))  #w.r.t set1 as compared to set2
# print("The differnce w.r.t to set2 is: ",set_2.difference(set_1)) #w.r.t set2 as compared to set1

#Q2.to find unique words :
# words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']

# frequency = {}
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
# unique_words = list(frequency.keys())
# print("Unique Words:", unique_words)
# print("Frequency of occurrence:", frequency)

#Q3. To remove intersection between second and first set
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {4, 5, 6, 7, 8}
# print(set_1.difference(set_2))

#Q4.Superset
# num1 =  {1, 2, 3, 4, 5, 7}
# num2 =  {2, 4}
# num3 =  {5, 4}
# i = 1
# j = 1
# k = 1
# for i in range(0,i):
#     p1 = num1.issuperset(num2)
#     if(p1==True):
#         print("Num1 is superset of Num2")
#         print("True")
#     else:
#         print("it is not a superset")
#         print("False")
# for j in range(0,j):
#     p2 = num2.issuperset(num3)
#     if(p2==True):
#         print("Num2 is superset of Num3")
#         print("True")
#     else:
#         print("it is not a superset")
#         print("False")
# for k in range(0,k):
#     p3 = num3.issuperset(num2)
#     if(p3==True):
#         print("Num3 is superset of Num2")
#         print("True")
#     else:
#         print("it is not a superset")
#         print("False")

#Q5.to check for common elements
# set_1 = {1, 2, 3}
# set_2 = {4, 5, 6}
# i=0
# j=0
# for i in range(0,3):
#     p1 = set_1.isdisjoint(set_2)
#     if (p1 == True):
#        print("Set 1 and Set 2 have no elements in common: True")
#     else:
#        print("Set 1 and Set 2 have elements in common: False")
# for j in range(0,3):
#     p2 = set_2.isdisjoint(set_1)
#     if (p2 == True):
#        print("Set 2 and Set 1 have no elements in common: True")
#     else:
#        print("Set 2 and Set 1 have elements in common: False")

#Q6.Testing
# set = {1,3,5,7,9,11}
# value = int(input("Enter the value u want to check: "))
# if value in set:
#     print("The value is present in the given set")
# else:
#     print("The value is not present in the given set")

#Q7.Write a python program to find the length of a set with and without using len function
# set_1 = {2,3,5,10,15,20}
# #Using len() function
# print("Length of the set using len() function is:", len(set_1))

#  #Without using len() function
# count = 0
# for item in set_1:  
#     count += 1
# print("Length of the set without using len() function is:", count)

#Q8 to check for subset:
# x =   {'mango', 'apple'}
# y =  {'mango', 'orange'}
# z =  {'mango'} 
# for _ in range(0,1):
#     p1 = z.issubset(x)
#     if (p1 == True):
#       print("Set Z is a subset of Set X: True")
#     else:
#       print("Set Z is not a subset of Set X: False")
# for _ in range(0,1):
#     p2 = z.issubset(y)
#     if (p2 == True):
#        print("Set Z is a subset of Set Y: True")
#     else:
#        print("Set Z is not a subset of Set Y: False")

# #Q9.event:
# dinner_guests = {'Alice', 'Bob', 'Charlie', 'David'}
# afterparty_guests = {'Charlie', 'David', 'Eve', 'Frank'}
# #1. People attending both events
# print(dinner_guests.intersection(afterparty_guests))
# #2. People attending only dinner
# print(dinner_guests.difference(afterparty_guests))
# #3. People attending only afterparty 
# print(afterparty_guests.difference(dinner_guests))
# #4. people who are unique
# print(dinner_guests.union(afterparty_guests))

# #Q10. students attendence
# day_1 = {'Alice', 'Bob', 'Charlie', 'David'}
# day_2 = {'Charlie', 'David', 'Eve', 'Frank'}
# #1. attending both the days
# print(day_1.intersection(day_2))
# #2. atleast one day absent
# print(day_1.symmetric_difference(day_2))
# #3. Present all days checking:
# print(day_1.issubset(day_2))

# #programming courses
# python = {'Alice', 'Bob', 'Charlie', 'David'}
# java = {'Charlie', 'David', 'Eve', 'Frank'}
# #Q1.both courses
# print(python.intersection(java))
# #Q2.only python
# print(python.difference(java))
# #Q3.Unique students
# print(python.union(java))

