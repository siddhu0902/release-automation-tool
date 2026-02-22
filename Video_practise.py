#Video_8
"""
first_name = input("Enter your first name: ")
last_name = input("Enter last name: ")
full_name = first_name+ ' ' +last_name
print("Hello",full_name)"""

"""
Prime number:
Start a loop: 2 ---- 16 ---> check if num is div b/1 2 to 15. 
if not divisible - prime
if divisible - not prime

logic:
Take a number
Start a loop from 2 to number-1
check if num is div in loop
if div - not prime,else,prime

"""
"""
number = int(input("Enter a number: "))
count = 0
i = 2
while(i<number-1):
    if number%i==0:
        count = count+1
    i = i+1
if count ==0:
    print("It is a prime number")
else:
    print("It is not a prime number")
"""

#Video_9
#Tuple practise
#Always index starts from zero(0)
"""
data = (10,20,-40)
for k in data:
    print(k)
"""
#Slicing tuple : to extract values between two positions
"""
a = (100,200,300,400)
b = a[1:]
print(b)  #(200,300,400)
"""
#Delete tuple = del()
#Concatenation = joining multiple tuples into single tuples
"""
a1 = (10,20)
a2 = (30,40)
a3 = a1 + a2  #Concatenation
print(a3)
"""

#Sorted() = it sorts the values in ascending order
"""
x = (2,8,1,6)
print(sorted(x))  #1,2,6,8
"""

#Descending order
"""
x = (2,1,8,6)
print(x,reverse = True)  #8,6,2,1
"""

#sum() = it retuns the total sum of values
"""
a = (10,20,30)
k = sum(a)
print(k)  #60
"""
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

#SETS:{} = collection of data
"""
data = {10,20,"Jhon"}
for k in data:
    print(k)  #Always string comes first and remaing values next - Jhon,10,20
"""

#add() = adds an element to the set
#clear() = removes all the elements from the set
#copy() = creates a copy of the set     
#difference() = returns the difference between two or more sets
#difference_update() = removes the elements found in another set from the current set
#discard() = removes the specified element from the set
#intersection() = returns the intersection of two sets
#intersection_update() = removes the elements that are not common to both sets
#isdisjoint() = returns True if two sets have no elements in common
#issubset() = returns True if all elements of a set are present in another set
#issuperset() = returns True if a set contains all elements of another set
#pop() = removes and returns an arbitrary element from the set
#remove() = removes the specified element from the set
#symmetric_difference() = returns the symmetric difference of two sets
#symmetric_difference_update() = updates a set with the symmetric difference of itself and another set
#union() = returns the union of two sets
#update() = updates a set with the union of itself and another set

