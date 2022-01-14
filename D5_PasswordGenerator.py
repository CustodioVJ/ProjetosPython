import random

letters = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '&', '*']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("Welcome to the password generator!!\n")

letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like?\n"))
number = int(input("How many numbers would you like?\n"))

log_word  = []

for l in range(letter):
    log_word += random.choice(letters)
for s in range(symbol):
    log_word += random.choice(symbols)
for n in range(number):
    log_word += random.choice(numbers)

random.shuffle(log_word)

password = ""

for x in log_word:
    password += x

print(f"Here is your password: {password}")