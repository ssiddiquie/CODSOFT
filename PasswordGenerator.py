import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
numbers = "1234567890"
sym = "`~!@#$%^&*()_+[]{}|\:;'?/>.,<"

u = input("Do you want uppercase letters in your password (y/n): ")
if u == 'y':
    upp = True
else:
    upp = False
l = input("Do you want lowercase letters in your password (y/n): ")
if l == 'y':
    lowe = True
else:
    lowe = False
s = input("Do you want symbols in your password (y/n): ")
if s == 'y':
    symb = True
else:
    symb = False

n = input("Do you want numbers in your password (y/n): ")
if n == 'y':
    num = True
else:
    num = False


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
