# create a calculator that can add, subtract, multiply, and divide two numbers
Count = 0
while(Count<5):
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter a number: "))
    choice = input("Enter an operation (+, -, *, /): ")
    if choice == "+":
       print("The result is: ", number_1 + number_2)
    elif choice == "-":
       print("The result is: ", number_1 - number_2)
    elif choice == "*":
       print("The result is: ", number_1 * number_2)   
    elif choice == "/":
       print("the result is: ", number_1 / number_2)

    else:
       print("Invalid operation")    
    Count = Count+1
    print("You have used the calculator ", Count, " times")
 
        