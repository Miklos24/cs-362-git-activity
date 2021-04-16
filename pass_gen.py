import random
import string

CHARS = string.ascii_lowercase

def gen_password(length):
    return ''.join(random.choice(CHARS) for i in range(length))


print("Input the length of password you'd like: ", end='')
length = int(input())
password = gen_password(length)
print("Here's your password - don't forget it!")
print(password)