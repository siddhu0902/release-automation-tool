#if a number is divisible by 3 and 5 both by using nested if else

number = int(input("Enter first number: "))

if number/3==0:
    if number/5==0:
        print("The number is divisible by both 3 and 5")
    else:
        print("The number is not divisible by both 3 and 5")
    
else:
    if number/5==0:
        print("The number is not divisible by both 3 and 5")
    else:
        print("The number is not divisible by both 3 and 5")
        