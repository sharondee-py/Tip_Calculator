#This is a tip calculator that splits the bill among a number of people.
#It takes the total bill amount, the desired tip percentage, and the number of people to split the bill.
#It then calculates and prints the amount each person should pay.

print("Welcome to the Tip Calculator!")
bill_amount = float(input("What was the total bill? P"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_as_decimal = tip_percentage / 100
total_tip_amount = bill_amount * tip_as_decimal
total_bill = bill_amount + total_tip_amount
bill_per_person = total_bill / number_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: P{final_amount}")