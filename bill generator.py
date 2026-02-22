#Calculate a different discounts based on the gross bill made
Count = 0
while(Count<5):
 customer = input("Enter customer name: ")
 bill_amount = int(input("Enter gross bill amount: "))
 discount = 0
 if bill_amount > 1000 and bill_amount <= 1500:
    discount = bill_amount*0.10
    net = bill_amount - discount
 elif bill_amount > 1500 and bill_amount <= 2000:
    discount = bill_amount*0.15
    net = bill_amount - discount
 elif bill_amount >2000 and bill_amount <= 5000:
    discount = bill_amount*0.20
    net = bill_amount - discount
 elif bill_amount > 5000:
    discount = bill_amount*0.30
    net = bill_amount - discount
 else:
    net = bill_amount
 print("Customer Name: ", customer)
 print("Gross Bill Amount: ", bill_amount)
 print("Discount: ", discount)
 print("Net Bill Amount: ", net)
Count = Count+1 