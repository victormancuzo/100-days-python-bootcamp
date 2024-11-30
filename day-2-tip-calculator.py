print('Welcome to the Tip Calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give: 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

total_tip = bill * tip / 100
# split_total = round((bill + total_tip) / people, 2)
split_total = round((bill + total_tip) / people)

print(f'Each person should pay: ${split_total:.2f}')