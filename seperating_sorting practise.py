# #Bubble sort
# def bubbleSort(arr):
#     n = len(arr)
#     swapped = False
#     for i in range(n-1):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 swapped = True
#                 arr[j] , arr[j+1] = arr[j+1] , arr[j]
#             if not swapped:
#                 return None

# arr = [20,14,25,45,60,12,9]
# bubbleSort(arr)
# print("Sorted array is: ")
# for i in range(len(arr)):
#     print("% d" % arr[i], end="")

# #Selection sort
# def SelectionSort(array,size):
#     for i in range(size):
#         min_index = i
#         for j in range(i+1,size):
#             if array[j] < array[min_index]:
#                 array[j] , array[min_index] = array[min_index] , array[j]

# arr = [20,14,25,45,60,12,9]
# size = len(arr)
# print("The array before sorting in ascending order by selection sort is: ")
# print(arr)
# SelectionSort(arr,size)
# print("The array after sorting in ascending order using selection sort is: ")
# print(arr)

# #Insertion Sort
# def insertionSort(arr):
#     n = len(arr)
#     if n<=1:
#         return
#     for i in range(1,n):
#         key = arr[i]
#         j = i-1
#         while j>=0 and key < arr[i]:
#             arr[j+1] = arr[j]
#             j -=1
#         arr[j+1] = key
# arr =[20,14,25,45,50,12,9]
# insertionSort(arr)
# print("The new corrected ascending order using insertion sort is: ")
# print(arr)


# #Linear Search
# list  = [20,14,25,45,50,12,9]
# def linearlist(list,target):
#     for i in range(0,len(list)):
#         if list[i] == target:
#             return i
#     return None
# print(linearlist(45))