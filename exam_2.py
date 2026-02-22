"""N = int(input("Enter the number of times you want to run the program: "))
Count = 1
a=0
b=0
c=0
d=0
e=0
while (Count<=N):
    month = int(input("Enter the month in number(B/W 1-12):"))
    if month==3:
        print("The crops grown in this month are Wheat and Onion")
        a+=1
        b+=1
    elif month==10:
        print("The crops grown in this month are Rice and Soybean")
        d+=1
        e+=1
    elif month==4:
        print("the crops grown in this month is Wheat")
        a+=1
    elif month==2:
        print("The crops grown in this month is Onion")
        b+=1
    elif month==5 and month==6:
        print("The crops grown in this month are Watermelon")
        c+=1
    elif month==9:
        print("The crops grown in this month are Rice")
        d+=1
    elif month==11:
        print("The crops grown in this month is Soybean")
        e+=1
    else:
        print("There are no crops grown in this month")
    Count+=1
print("The number of times Wheat is grown is: ",a)
print("the number of times Onion is grown is: ",b)
print("The number of times Watermelon is grown is: ",c)
print("The number of times Rice is grown is: ",d)
print("The number of times Soybean is grown is: ",e)"""