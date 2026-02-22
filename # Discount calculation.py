# Discount calculation

number_of_customers = int(input("Enter the number of customers:"))
customer_iterator = 0

#Outer loop
while(customer_iterator < number_of_customers): 
    number_of_items = int(input("Enter the number of items:"))

    # Initialize / reset variable to 0
    item_iterator = 0
    bill_amount = 0
    net_amount = 0

    # Inner loop
    while(item_iterator<number_of_items):
        bill_amount = bill_amount + int(input("Enter the price for the item:"))
        item_iterator = item_iterator + 1

    if(bill_amount>5000):
        net_amount = bill_amount-bill_amount*30/100
    elif(bill_amount>3000):
        net_amount = bill_amount-bill_amount*20/100
    elif(bill_amount>1500):
        net_amount = bill_amount-bill_amount*15/100
    elif(bill_amount>1000):
        net_amount = bill_amount-bill_amount*10/100
    else:
        net_amount = bill_amount
        print("Not eligible for discount")
    
    print("Final bill amount is:", net_amount)
    customer_iterator = customer_iterator + 1