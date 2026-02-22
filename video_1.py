units = int(input("Enter total monthly units: "))
if units<200:
    bill = 1000
    print(bill)
elif units>=201 and units<500:
    bill = 1500+ .102*units
    print(bill)
elif units>=501 and units<750:
    bill = 2250+ .15*units
    print(bill)
else:
    initial_bill1 = 5000 + .185*units
    initial_bill2 = .02*initial_bill1
    bill = initial_bill1 + initial_bill2
    print(bill)