def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
def sumOfCurious():
    result = 0
    for i in range(3, 50000):
        sume = 0
        temp = i
        while temp != 0:
            rem = temp % 10
            sume = sume + factorial(rem)
            temp = temp // 10
        if i == sume:
            result = result + i
    return result
print(sumOfCurious())
