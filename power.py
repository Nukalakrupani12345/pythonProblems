def sumOfDigits(num):
    sume = 0
    while num != 0:
        rem = num % 10
        sume = sume + rem
        num = num // 10
    return sume
print(sumOfDigits(2**1000))
