import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

box = []

for n in range(nr_letters):
    random_letter = random.choice(letters)  # choose a letter from the list
    box.append(random_letter)  # insert the letter randomly generated into the list called box

for n in range(nr_symbols):
    random_symbol = random.choice(symbols)
    box.append(random_symbol)

for n in range(nr_numbers):
    random_number = random.choice(numbers)
    box.append(random_number)

random.shuffle(box)  # Answer to hard version - any other way?
final_password = ''.join(box) # any other way to print all the elements from list without , or space?
print(f"Your password could be {final_password}")