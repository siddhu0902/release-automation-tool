#Linear Search:
list = [1,3,2,4,6,45,21,435,23]
def linear_search(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

print(linear_search,(21))

#Binary search:

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def binary_search(array,N):
    low = 0
    high = len(array)-1
    position = -1

    while low <=high:
        mid = (low+high)//2
        if N == array[mid]:
            position = mid
            return position
        elif(N<=array[mid]):
            high = mid + 1
        else:
            low = mid-1
    return position
print(binary_search,(13))