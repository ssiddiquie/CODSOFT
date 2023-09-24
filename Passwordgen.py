import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "1234567890"
sym = "`~!@#$%^&*()_+[]{}|\:;'?/>.,<"

upp, lowe, symb, num = True, True, True, True

pss = ""
if upp:
    pss += uppercase
if lowe:
    pss += lowercase
if symb:
    pss += sym
if num:
    pss += numbers
try:
    x = int(input("Input password length: "))
    y = int(input("Input number of password variations needed"))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()
for i in range(y):
    password = "".join(random.sample(pss, x))
    print(password)
