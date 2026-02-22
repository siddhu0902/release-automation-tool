#without using lists
#Q1. find the largest and smallest elements in a list
#Without lists
"""
list = [1,2,3,4,5]
largest = list[0]
smallest = list[0]
for i in list:
    if i>largest:
        largest = i
    elif i<smallest:
        smallest = i
print("Largest element is: ",largest)
print("Smallest element is: ",smallest)
"""
#with lists
"""
list = [1,2,3,4,5]
list.sort()
print("Largest element is: ",list[-1])
print("Smallest element is: ",list[0])
"""

#Q2. reverse the list, preferbly in place
#Without using lists
""" Error
list = [1,2,3,4,5]
reversed_list = []
j = 0
for i in range(len(list)-1,-1, -1):
    reversed_list[j]=list[i]
    j+=1
print(reversed_list)"""

#With using lists
"""
list = [1,2,3,4,5]
reversed_list = []
for i in range(len(list)-1,-1,-1):
    reversed_list.append(list[i])
    print(reversed_list)
"""
#Q3. Check whether an element occurs in a list and how many times it occurs in a list
#Without using lists
"""
list = [1,2,3,4,5,1,2,1,6,7,2,4,5]
element = int(input("Enter the element to be searched:"))
count = 0
for i in list:
    if i == element:
        count+=1
if count>0:
    print(f"Element {element} is present in the list and it occurs {count} times")
else:
    print(f"Element {element} is not present in the list")
"""

#With using lists
"""
list = [1,2,3,4,5,1,2,1,6,7,2,4,5]
element = int(input("Enter the element to be searched: "))
count = list.count(element)
if count>0:
    print(f"Element {element} is present in the list and it occurs {count} times")
else:
    print(f"Element {element} is not present in the list")"""

#Q4. Find the elements in odd positions in a list
#Without using lists
"""
list = [1,2,3,4,5,6,7,8,9,10,11]
odd_elements = []
for i in range(len(list)):
    if i%2 != 0:
        odd_elements.append(list[i])
print("Elements in odd positions are: ",odd_elements)
"""

#With using lists
"""
list = [1,2,3,4,5,6,7,8,9,10,11]
odd_elements = [] 
for i in range(1,len(list),2):
    odd_elements.append(list[i])
print("Elements in odd positions are: ",odd_elements)
"""

#Q5.Test whether a list is a palindrome or not
#Without using lists
"""
list = [1,2,3,2,1]
reversed_list = []
for i in range(len(list)-1,-1,-1):
    reversed_list.append(list[i])
if list == reversed_list:
    print("The list is a palindrome")   
else:
    print("The list is not a palindrome")
"""

#With using lists
"""
list = [1,2,3,2,1]
reversed_list = list[::-1]
if list == reversed_list:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")  
"""

#Q6.Compute the sum of the numbers in a list
#Without using lists
"""
list = [1,2,3,4,5]
sum = 0
for i in list:
    sum+=i
print("The sum of the numbers in the list is: ",sum)
"""
#With using lists
"""
list = [1,2,3,4,5]
sum = sum(list)
print("The sum of the numbers in the list is: ",sum)
"""

#Q7.Concatenate two lists
#With using lists
"""
list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = []
for i in list1:
    concatenated_list.append(i)
for j in list2:
    concatenated_list.append(j)
print("The concatenated list is: ",concatenated_list)
"""

#Without using lists
"""
list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = list1 + list2
print("The concatenated list is: ",concatenated_list)
"""

#Q8.To combine two lists alternatively taking elements
#Without using lists
"""
list1 = [1,3,5]
list2 = [2,4,6]
combined_list = []
for i in range(len(list1)):
    combined_list.append(list1[i])
    combined_list.append(list2[i])
print("The combined list is: ",combined_list)
"""

#With using lists
"""
names = ['Alice', 'Bob', 'Charlie']
scores = [88, 92, 75]
result = zip(names, scores)
print(list(result))  
"""

#Q9.to merge two sorted lists into a new list
#Without using lists

#With using list
"""
list1 = [1,3,5,7]
list2 = [2,4,6,8]
merged_list = sorted(list1 + list2)
print("The merged sorted list is: ",merged_list)
"""

#Q10. Rotate a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. Try
#     solving this without creating a copy of the list. How many swap or move operations do you need?

#Without using lists
"""
list = [1,2,3,4,5,6]    
k = 2
n = len(list)
for i in range(k):
    first_element = list[0]
    for j in range(n-1):
        list[j] = list[j+1]
    list[n-1] = first_element
"""

#With using list
"""
list = [1,2,3,4,5,6]
k = 2
rotated_list = list[k:] + list[:k]
print("The rotated list is: ",rotated_list)
"""

#Q11.Write a function that takes a number and returns a list of it's digits
#Without lists
