#Arrays : It is a colection of items stored at contigous memory locations
# It makes it easier to calculate the position of each element by simply addingg offset to a base value, i.e., the mwmory location of the first element of the array
"""
#Array created by importing an array module
import array as arr   #Importing "array" for array creations
a = arr.array('i',[1,2,3])      #creating an array with integer type
print("The new created array is: ")     #Printing original copy
for i in range(0,3):
    print(a[i],end=" ")
"""
#1. Program to find the sum of all elements in an array
import array as a
b = a.array('i',[1,2,3])
#sum = 
