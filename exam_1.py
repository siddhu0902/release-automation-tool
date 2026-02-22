N = int(input("Enter the number of times you want to run the program: "))
Count = 1
a=0
b=0
c=0
d=0
e=0
while Count<=N:
    temp = int(input("Enter the temperature in celsius: "))
    if 60<temp<=122:
        print("The bacteria is Hyperthermophile and Thermophile")
        a+=1
        b+=1
    elif 45<temp<=60:
        print("The bacteria is Thermophile")
        b+=1
    elif 20<=temp<=45:
        print("The bacteria is Mesophile and psychotroph")
        d+=1
        c+=1
    elif temp==0:
        print("the bacteria is Psychotroph")
        d+=1
    elif 10>=temp>=-15:
        print("The bacteria is Psychrophile")
        e+=1
    else:
        print("There is no bacteria in this range")
    Count+=1
print("The number of Hyperthermophile bacteria is: ",a)
print("The number of Thermophile bacteria is: ",b)  
print("The number of Mesophile bacteria is: ",c)  
print("The number of Psychotroph bacteria is: ",d)
print("The number of Psychrophile bacteria is: ",e)


#turns = 0
#x = 3
#while turns<22:
#    x = x*3
#    turns =turns+3
#print("The value of x after 22 turns is: ",x)
#print(turns)

# prints rows of '*' increasing by one each row
"""n = int(input("How many rows? "))
for i in range(1, n + 1):
    print('*' * i))"""

"""n = int(input("Rows at peak? "))
if n > 0:
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)
n = int(input("Start from how many stars? "))
for i in range(n, 0, -1):
    print('*' * i)"""


