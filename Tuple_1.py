"""T = (2,3,4,5,6)
print("Tuple before adding new element")
print(T)
L = list(T)
L.append(int(input("Enter new element: ")))
T = tuple(L)
print("Tuple after adding new element")
print(T)"""

#print('Amrita','School','of','Engineering',sep='**')

#n = "Sid"
#print(f'Hello {n}. Welcome to Amrita University!')

"""thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrent","watermelon"]
print(thislist)"""

"""thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist.append("orange")
print(thislist)"""

"""thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist.insert(1,"watermelon")
print(thislist)"""

"""thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist.pop(2)
print(thislist)"""

#below two codes are same but in different ways
"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)"""

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)"""

"""
append() = it adds an element at the end of the list
clear() = it removes all the elements from the list
copy() = it creates a copy of the list
count() = it counts the number of occurences of an element in the list
extend() = it adds the elements of a list to the end of another list
index() = it returns the index of the first occurence of an element in the list
insert() = it adds an element at the specified position in the list
pop() = it removes the element at the specified position in the list
remove() = it removes the first occurence of an element in the list
reverse() = it reverses the order of the elements in the list
sort() = it sorts the elements of the list in the ascending order
"""


"""list = [1,2,3,4,5]
i = list.reverse()
print(list)"""

"""
fruits = ("apple","banana","cherry")
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)
"""