s = input("Enter your string: ")
result = ""
count = 0

for c in s:
    if c.isupper():
        result += c.lower()
    elif c.islower():
        result += c.upper()
    else:
        result += c
        count += 1

print("Swapped case string:", result)
print("Count of non-alphabetic symbols:", count)

"""import asyncio

async def double_after_delay(x):
    await asyncio.sleep(1)   # non-blocking sleep
    return x * 2

async def main():
    print("Starting")
    result = await double_after_delay(5)   # pause here until double_after_delay finishes
    print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())"""


list1 = [1,3,5,7]
list2 = [2,4,6,8]
merged_list = []
i = 0
j = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1
while i < len(list1):       
    merged_list.append(list1[i])
    i += 1
while j < len(list2):
    merged_list.append(list2[j])
    j += 1
print("The merged sorted list is: ",merged_list)
