print("Welcome to tip calculator! ")
bill_amount = input("What is your bill amount? ")
tip_amount = input("How much tip you would like to give? 10, 12 or 15 percent? ")
number_of_people = input("How many people to split the bill? ")

tip_amount = float(bill_amount) * (float(tip_amount) / 100)
bill_with_tip = float(bill_amount) + tip_amount
divided_bill = bill_with_tip / int(number_of_people)

divided_bill = round(divided_bill, 2)
print("Each will pay: " + str(divided_bill))