def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact
def sumOfDigits():
    print("enter number ")
    fact = factorial(int(input()))
    result = 0
    while fact != 0:
        rem = fact % 10
        result += rem
        fact = fact // 10
    return result
print("sum of digits of factorial of number is :",sumOfDigits())
