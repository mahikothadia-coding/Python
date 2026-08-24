import random

letters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
numbers = "0123456789"
symbols = "£$%^&*@~#?><"

password = " "

#5 letters
for i in range (5):
    password += random.choice(letters)

#3 numbers
# for i in range (3):
    password += random.choice(numbers)

# 2 symbols
for i in range (2):
    password += random.choice(symbols)    

password = list(password)
random.shuffle (password)

print("Generated password:  ", "".join(password))