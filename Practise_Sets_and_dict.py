#Sets
#Q1.
"""
set_1 = {1,2,3,4,5,6}
set_2 = {3,4,5,6,7,8}
i=0
j=0
for i in range(0,6):
    p1 = set_1.issubset(set_2)
    if (p1 == False):
       a = set_1.intersection(set_2)
       print(set_1-a)
for j in range(0,6):
    p2 = set_2.issubset(set_1)
    if (p2 == False):
       b = set_2.intersection(set_1)
       print(set_2-b)
"""
"""
set_1 = {1,2,3,4,5}
set_2 = {6,7,8}
i=0
j=0
for i in range(0,5):
    p1 = set_1.issubset(set_2)
    if (p1 == False):
       a = set_1.intersection(set_2)
       print(set_1-a)
for j in range(0,3):
    p2 = set_2.issubset(set_1)
    if (p2 == False):
       b = set_2.intersection(set_1)
       print(set_2-b)
"""

#Q2
'''
words = {'Red','Green','Red','Blue','Red','Red','Green'}
i=0
a = words.count("Red","Green","Blue")
print(a)
'''

#Q3.
# set_1 = {1,2,3,4,5}
# set_2 = {4,5,6,7,8}
# a = set_1.difference(set_2)
# print(a)
# set_1 = {1,2,3,4,5}
# set_2 = {4,5,6,7,8}
# b = set_2.difference(set_1)
# print(b)

#Q4.
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

#Q5. 5.	Write a Python program to check if two given sets have no elements in common Original set elements:
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

#Q6.Write a python program to check if a given value is present in a set or not
# set_1 = {1,3,5,7,9,11}
# value = int(input("Enter the value to be checked: "))
# if value in set_1:
#     print("The value is present in the set")
# else:
#     print("The value is not present in the set")

#Q7.Write a python program to find the length of a set with and without using len function
# set_1 = {2,3,5,10,15,20}
# #Using len() function
# print("Length of the set using len() function is:", len(set_1))

#  #Without using len() function
# count = 0
# for item in set_1:  
#     count += 1
# print("Length of the set without using len() function is:", count)

#Q8. Write a python program to check if a set is a subset of another set using comparision operators and issubset():
# set_x = {'mango', 'apple'}
# set_y = {'mango', 'orange'} 
# set_z = {'mango'}
# i=0
# for i in range(0,1):
#     p1 = set_z.issubset(set_x)
#     if (p1 == True):
#        print("Set Z is a subset of Set X: True")
#     else:
#        print("Set Z is not a subset of Set X: False")
# for i in range(0,1):
#     p2 = set_z.issubset(set_y)
#     if (p2 == True):
#        print("Set Z is a subset of Set Y: True")
#     else:
#        print("Set Z is not a subset of Set Y: False")

#Q9.
'''
9.	You’re managing an event where some guests have RSVP’d for dinner and others for the afterparty. Given two sets — dinner_guests and afterparty_guests —
perfor the following task using sets:
'''
# dinner_guests = {'Alice', 'Bob', 'Charlie', 'David'}
# afterparty_guests = {'Charlie', 'David', 'Eve', 'Frank'}
# #1. Find people attending both events.
# both_parties = dinner_guests.intersection(afterparty_guests)
# print("People attending both parties",both_parties)
# #2. Find people attending only dinner.
# only_dinner = dinner_guests.difference(afterparty_guests)
# print("People attending only dinner" , only_dinner)
# #3. Find people attending only the afterparty.
# only_afterparty = afterparty_guests.difference(dinner_guests)
# print("People attending only afterparty", only_afterparty)
# #4. Find the total unique guests across both events
# unique_guests = dinner_guests.union(afterparty_guests)
# print("Total unique guests" , unique_guests)
'''
Q10. In a class, students mark attendance using an online system. day1 and day2 
contain names of students who attended on those days.
'''
# day_1 = {'Alice', 'Bob', 'Charlie', 'David'}
# day_2 = {'Charlie', 'David', 'Eve', 'Frank'}
#1.Find students who attended both days
# both_days = day_1.intersection(day_2)
# print("Students hwo atended both days", both_days)
#2.find students who missed at least one day
# missed_one_day = day_1.symmetric_difference(day_2)
# print("Students who missed at least one day", missed_one_day)
#3.check if all students from day_1 also attended day_2
# all_day1_in_day2 = day_1.issubset(day_2)
# print("All students from day 1 attended day 2:", all_day1_in_day)

'''
11.You collected a list of emails from a survey form but some are duplicates.
Given a list of email strings, use a set to remove duplicates and display the unique email addresses.
'''
# emails = ['iamsiddhu@gmail.com','thisisgaming@gmail.com','fku@gmail.com','siddhu0902.c@gmail.com','fku@gmail.com','hi@gmail.com']
# unique_emails = set(emails)
# print("Unique email addresses:", unique_emails)

'''
Q12.A library keeps track of which books are currently checked out and which are 
    reserved. Given the sets checked_out and reserved, find which books are:
'''
# checked_out = {'Book A', 'Book B', 'Book C'}
# reserved = {'Book C', 'Book D', 'Book E'}
#q1.currently unavailable (either checked out or reserved).
# unavailable_books = checked_out.union(reserved)
# print("Currently unavailable books : ",unavailable_books)
#q2.only reserved but not checked out.
# only_reserved = reserved.difference(checked_out)  
# print("Only reserved books : ",only_reserved)
#q3.checked out multiple members(if you store as sets per user).
# member1_checked_out = {'Book A', 'Book B'}
# member2_checked_out = {'Book B', 'Book C'}
# multiple_checked_out = member1_checked_out.intersection(member2_checked_out)
# print("Books checked out by multiple members : ",multiple_checked_out)

'''
13.	You’re managing online courses. Each course has a set of enrolled students.
 Given two sets, python_students and java_students:
'''
# python_students = {'Alice', 'Bob', 'Charlie', 'David'}
# java_students = {'Charlie', 'David', 'Eve', 'Frank'}
# Q1.students enrolled in both platforms
# both_courses = python_students.intersection(java_students)
# print("In both course: ",both_courses)
#Q2. find students who took only python
# only_python = python_students.difference(java_students)
# print("only Python: ",only_python)
#Q3.Total number of unique students
# unique_students = python_students.union(java_students)
# print("Unique students: ",unique_students)
#Q4.check if all python students are in java also
# if (python_students.issubset):
#     print("True")
# else:
#     print("false")

'''
14.	Your analyzing social media data for a celebrity.
 Given two sets: instagram_followers and twitter_followers
'''
# instagram_followers = {'Alice', 'Bob', 'Charlie', 'David'}
# twitter_followers = {'Charlie', 'David', 'Eve', 'Frank'}
#Q1.find follower in both platforms
# both_platforms = instagram_followers.intersection(twitter_followers)
# print("Both platforms: ",both_platforms)
#Q2.find followers exclusive to instagram
# exclusive = instagram_followers.difference(twitter_followers)
# print("only instagram",exclusive)
#Q3.follow atleast one account
# unique_followers = instagram_followerr.union(twitter_followers)
# print("Unique followers: ",unique_followers)

#Dictionaries
