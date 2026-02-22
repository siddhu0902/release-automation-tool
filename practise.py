#calculator

Count = 0
while(Count <5):
    number_1 = int(input("Enter a number:"))
    number_2 = int(input("Enter a number:"))
    choice = input("Enter the opration you would like to perform (+,_,*,/):")
    if choice =='+':
        print("The sum is:", number_1+number_2)
    elif choice == '-':
        print("The difference is:",number_1-number_2)
    elif choice =='*' :
        print("The product is:", number_1*number_2)
    elif choice == '/':
        print("The quotient is:", number_1/number_2)

    else:
        print("invalid operation")
    Count = Count+1
    print("You have used", Count, "out of 5 calculations")            