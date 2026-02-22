#Lists - mutable(can modify the list in the code)
# courses = ["his","math","physics","science"]
# print(courses)
# print(courses[0])
# print(courses[1])
# print(courses[2])
# print(courses[3])
# print(course[0:2])
# courses.insert(0,'Art')
# courses.pop(1)
# courses.sort(reverse=True)
# courses.reverse()
# courses.sort()
# print(courses.index("his"))
# print("math" in courses)
# print(courses)
'''
for index,item in enumerate(courses,start=1):       #enumerate() function is used to add a counter to an iterable (such as a list, tuple, or string) and return the data as an enumerate object  
    print(index,item)                         #Item is just for indentation and we can use any word in place off item. it just makes the list written in new line
                                            #start =1 just strts the index from 1 in print box
'''


#Tuples - immutable(can't modify the tuple in the code)
# tuple_1 = ('History','Math','Physics','science','biology')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)


#Problems
# def reverse_list(lst):
#     rev = []
#     for i in range(len(lst) - 1, -1, -1):
#         rev.append(lst[i])
#     return rev
# print(reverse_list([1, 2, 3, 4]))

# def remove_common(lst):
#     unique = []
#     for i in lst:
#         if i not in unique:
#             unique.append(i)
#     return unique
# print(remove_common([1, 2, 2, 3, 4, 3]))

