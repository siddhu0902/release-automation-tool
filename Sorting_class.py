# #Sorting:
# #O(n) = linear search
# #O(logn) = binary search
# # O(n^2) = bubble Sort
# #Bubble Sort:

# def buubleSort(arr):
#     n = len(arr)
#     swapped = False

#     for i in range(n-1):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:           #If we use arr[j] < arr[j+1] the sorting will be done reversed manner and we get the values in descending order
#                 swapped = True
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#         if not swapped:
#             return

# arr = [24,6,12,34,86,52,65,87,35,76,39]
# buubleSort(arr)
# print("Sorted Array is: ")
# for i in range(len(arr)):
#     print("% d"%arr[i], end="")

# # Selection Sort
# def selectionSort(array, size):
#     for ind in range(size):
#         min_index = ind
#         for j in range(ind + 1, size):
# # select the minimum element in every iteration
#             if array[j] < array[min_index]:
#                 min_index = j
# # swapping the elements to sort the array
#         (array[ind], array[min_index]) = (array[min_index], array[ind])
# arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
# size = len(arr)
# print('The array before sorting in Ascending Order by selection sort is:')
# print(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)