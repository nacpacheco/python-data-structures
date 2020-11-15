# O(N)
def factorial_recursive(number):
    if number == 1:
        return 1
    else:
        return number * factorial_recursive(number-1)

# O(N)
def factorial_iteractive(number):
    factorial = 1
    for num in range(number,1,-1):
        factorial = num * factorial
    return factorial


print(factorial_recursive(1))
print(factorial_iteractive(1))