def calc_divisors(x):
    return [i for i in range(1, x + 1) if x % i == 0]

print("Enter a number: ", end='')
x = int(input())

divisors = calc_divisors(x)
print("Here are the divisors: ")
print(divisors)