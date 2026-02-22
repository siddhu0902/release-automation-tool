#Sorting
#Bubble Sort:
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 swapped = True
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#         if not swapped:
#             return
# arr=[64,34,25,12,22,11,90]
# bubbleSort(arr)
# print("The sorted array is: ")
# for i in range(len(arr)):
#     print("% d"% arr[i],end=" ")

#Insertion Sort
# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         current = arr[i]     # Element to be placed correctly
#         j = i - 1
#         # Shift elements greater than current to the right
#         while j >= 0 and arr[j] > current:
#             arr[j + 1] = arr[j]
#             j -= 1
#         # Place current element at its correct position
#         arr[j + 1] = current

#     return arr  


# arr = [12, 11, 13, 5, 6]
# sorted_arr = insertion_sort(arr)
# print(sorted_arr)


#Selection_Sort:
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[j],arr[min_index] = arr[min_index],arr[j]
#     return arr

# arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
# print("The array before sorting:")
# print(arr)
# sorted_arr = selection_sort(arr)
# print("The array after sorting:")
# print(sorted_arr)

#Selecting
# def linear_search(list,target):
#     for i in range(len(list)):
#         if list[i] == target:
#             return i
#     return -1
# list = [5,3,7,2,9,1]
# target = 7
# result = linear_search(list,target)
# print(result)

