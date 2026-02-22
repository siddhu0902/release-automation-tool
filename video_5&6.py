#30/7/2025
#write a program to display first 20 even numbers

#IMP: for i in range(1,21):
#    if i%2==0:
#        print(i)

#1)To display first 30 fibonacci numbers
#a=0
#b=1
#count=0
# while count<30:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     count+=1

#2)To find sum of numbers b/w 50 to 70
#for i in range(50,71):
#    sum=0
#    sum=sum+i
#print(sum)

#3)To check if the number is prime or not
#num = int(input("Enter a number: "))
#if num >  1:
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            break

#4)To take name and display vowels in it
#name = input("Enter your name:")
#vowels = "aeiouAEIOU"
#for i in name:
#    if i in vowels:
#        print(i,"These is the vowel in your name")

#5)To take 3 digit numbers and find sum of its digits
#num = int(input("Enter a 3 Digit number: "))
#sum = 0
#while num > 0:
#    digit = num % 10
#    sum += digit
#    num //= 10   
#print("Sum of digits:", sum)

#6)To find the sum of first 25 odd numbers
#for i in range(1,50,2):
#    sum=0
#    sum=sum+i   
#print(sum)

#7)To find factor
#num = int(input("Enter a number: "))
#print("The factors of", num, "are:")
#for i in range(1, num+1):
#    if num % i ==0:
#        print(i, end=" ")

#8)To display following pattern:  
#  *
#  **
#  ***
#  ****
#  *****
#for i in range(1,6):
#    for j in range(i):
#        print("*",end="")
#    print("")