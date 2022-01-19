import random

length = input("Input Password Length:")

print(" ")
#weak pasword
password = ''
lowercase = 'abcdefghijklmnopqrstuvwxyz'

for i in range(int(length)):
    randGen = random.choice(lowercase)
    password = password + randGen
print("Low Strength Password:" + password + " | Lowercase Only")

#
print(" ")

password2 = ''
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(length)):
    randGen = random.choice(lowercase + uppercase)
    password2 = password2 + randGen
print("Medium Strength Password:" + password2 +
      " | Lowercase & Uppercase Only")

print(" ")

password3 = ''
number = '123456789'
for i in range(int(length)):
    randGen = random.choice(lowercase + uppercase + number)
    password3 = password3 + randGen
print("High Strength Password:" + password3 +
      " | Lowercase & Uppercase & Numbers Only")

print(" ")

password4 = ''
symbol = '!@#$%^&*\/.,><-=[}]{`~'
for i in range(int(length)):
    randGen = random.choice(lowercase + uppercase + number + symbol)
    password4 = password4 + randGen
print("Really High Strength Password:" + password4 +
      " | Lowercase & Uppercase & Numbers & Symbols Only")
print("")
