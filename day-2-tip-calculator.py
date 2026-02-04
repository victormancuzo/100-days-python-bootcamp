print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give (in %): 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

total_bill = bill + (bill * tip / 100)
split_total = round(total_bill / people, 2)

print(f"Each person should pay: ${split_total:.2f}")
