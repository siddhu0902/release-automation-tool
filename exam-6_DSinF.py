# #List → Dictionary
# def Count_frequency(lst):
#     freq = {}
#     for item in lst:
#         if item in freq:
#             freq[item] +=1
#         else:
#             freq[item] = 1
#     return freq
# numbers = [1,2,3,3,2,1,1]
# print(Count_frequency(numbers))

# # List → Set → List
# def remove_duplicates(lst):
#     sets = set(lst)
#     lists = list(sets)
#     return lists
# nums = [1,1,2,3,4,4]
# print(remove_duplicates(nums))

# #To find largest and Smallest elements
# def find_largest_smallest(lst):
#     largest = lst[0]
#     smallest = lst[0]
#     for num in lst:
#         if num > largest:
#             largest = num
#         if num < smallest:
#             smallest = num
#     return largest , smallest
# values = [10,5,2,4,6,7]
# print(find_largest_smallest(values))

# #To merge two dictionaries
# def merge_dicts(d1, d2):
#     merged = d1.copy()
#     merged.update(d2)
#     return merged

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# print(merge_dicts(dict1, dict2))

# #to check if an element exist in a list
# def element_exists(lst, element):
#     if element in lst:
#         return True
#     else:
#         return False

# numbers = [10, 20, 30, 40]
# print(element_exists(numbers, 20))
# print(element_exists(numbers, 50))



def fun(n):
    if n>10:
        return n -1
    else:
        return fun(fun(n+2))
