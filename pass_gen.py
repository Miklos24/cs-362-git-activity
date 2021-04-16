import random
import string

print("Input the length of password you'd like: ", end='')
length = int(input())
chars = string.ascii_lowercase
password = ''.join(random.choice(chars) for i in range(length))
print("Here's your password - don't forget it!")
print(password)