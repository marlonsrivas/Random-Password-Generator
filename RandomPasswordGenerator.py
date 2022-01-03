#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
inletters = int(input("How many letters would you like in your password?\n"))
insymbols = int(input(f"How many symbols would you like?\n"))
innumbers = int(input(f"How many numbers would you like?\n"))

password = []
rpassword = []

for letter in range(1,inletters+1):
    select = int(random.randint(0,len(letters)))
    lett = letters[select-1]
    password.append(lett)

for symbol in range(1,insymbols+1):
    sel = int(random.randint(0,len(symbols)))
    sym = symbols[sel-1]
    password.append(sym)

for number in range(1,innumbers+1):
    sel1 = int(random.randint(0,len(numbers)))
    num = numbers[sel1-1]
    password.append(num)

random.shuffle(password)
passwordchar = ""

for char in password:
    passwordchar += char
print(passwordchar)
