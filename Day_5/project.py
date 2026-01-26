# PyPassword Generator!
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "@", "?", "¿", "¡"]

print("Welcome to the PyPassword Generator!")
input_letters = int(input("How many letters would you like in your password?\n"))
input_symbols = int(input("How many symbols would you like?\n"))
input_numbers = int(input("How many numbers would you like?\n"))
password_length = input_letters + input_symbols + input_numbers

password_list = []
for i in range(0, password_length):
    if input_letters > 0:
        password_list.append(random.choice(letters))
        input_letters -= 1
    elif input_symbols > 0:
        password_list.append(random.choice(symbols))
        input_symbols -= 1
    elif input_numbers > 0:
        password_list.append(random.choice(numbers))
        input_numbers -= 1

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
