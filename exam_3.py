#Multiplication Table
"""N = int(input("Enter the Limit: "))
i = 1
while i<=N:
    j = 1
    while j<=10:
        print(i,"X",j,"=",i*j)
        j = j+1
    i = i+1"""

#Prime numbers
"""c = "true"
n = int(input("Enter a number: "))
for i in range(2,n):
    if n%i==0:
        c = "false"
if c == "true":
    print("it is a prime number")
else:
    print("it is not a prime number")"""

#Generate a Pattern - 2
"""n = int(input("Rows at peak? "))
if n > 0:
    for i in range(1, n + 1):
        print('*' * i)"""

#Generate a Pattern - 1
"""n = int(input("Rows at peak? "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()"""

#Generate a Pattern - 3
"""n = int(input("Rows at peak? "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()"""

#Generate a Pattern - 4
"""rows = int(input("Enter number of rows: "))
for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    for j in range(i + 1):
        print((i + j) % 2, end=' ')
    print()"""

#Class of students
"""num = int(input("Enter a number: "))
for n in range(1, num + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")
    else:
        print(n, "is not a prime number")"""

#Question_6
"""n = int(input("Rows at peak? "))
for i in range (1,n+1) :
     for j in range (0,i) :
         print(j , end=" ")
     print()
for i in range (n-1,0,-1) :
     for j in range (0,i) :
         print(j , end=" ")
     print()"""

#question_7"""
"""company_total = 0
for d in range(1, 5):
    dept_total = 0
    for e in range(1, 6):
        wage = int(input(f"Department {d} Employee {e} wage: "))
        weekly = wage * 6
        print("Weekly salary:", weekly)
        dept_total += weekly
    print("Department total:", dept_total)
    company_total += dept_total

print("Company total payroll:", company_total)"""

#question_8
"""hostel_total = 0
for floor in range(1,4):
    floor_total = 0
    for room in range(1,11):
        rent = int(input(f"Floor {floor} Room {room} rent:"))
        floor+=rent
        print("Total rent of floor",floor,"is: ",floor_total)
        hostel_total+=floor_total
print("Total rent of hostel is: ",hostel_total) """

#question_9
"""travel_wage = 0
for day in range(1,6):
    seats_wage = 0
    for seat in range(1,11):
        wage = int(input(f"Day {day} Seat {seat} wage: "))
        seats_wage+=wage
        print("Total wage of day",day,"is: ",seats_wage)
        travel_wage+=seats_wage
print("Total wage of travel agency is: ",travel_wage)"""

#question_10
"""supermarket = 0
for branch in range(1,5):
    branch_total = 0
    for item in range(1,6):
        item_price = int(input(f"Branch {branch} Item {item} price:"))
        weekly = item_price*7
        print("weekly price of item",item,"is: ",weekly)
        branch_total+=weekly
    supermarket+=branch_total
    print("Total price of branch",branch,"is: ",branch_total)
print("Total price of supermarket is: ",supermarket)"""
