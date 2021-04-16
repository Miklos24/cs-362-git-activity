print("Enter a number: ", end='')
x = int(input())

print("Here are the divisors: ")
print([i for i in range(1, x + 1) if x % i == 0])