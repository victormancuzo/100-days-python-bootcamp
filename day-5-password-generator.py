import random
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = "!#$%&()*+"

print("Welcome to the PyPassword Generator!\n")

num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

password_chars = []

for _ in range(num_letters):
    password_chars.append(random.choice(LETTERS))

for _ in range(num_numbers):
    password_chars.append(random.choice(NUMBERS))

for _ in range(num_symbols):
    password_chars.append(random.choice(SYMBOLS))

random.shuffle(password_chars)

password = "".join(password_chars)
print(f"Your password is: {password}")
