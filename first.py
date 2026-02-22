n1 = int(input("Enter first number: "))
n2 = int(input("Enter Second number:"))
n3 = int(input("Enter Third number:"))

if n1<n2 and n1<n3:
    print("The first number is the lowest number")
elif n2<n1 and n2<n3:
    print("The third number is the lowest number")
else:
    print("The second number is the lowest number")

    