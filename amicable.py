def amicable():
    result = 0
    for i in range(1, 10000):
        sume = sumOfFactors(i)
        if sumOfFactors(sume) == i and sume != i:
            result = result + i
    return result
def sumOfFactors(num):
    sume = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sume = sume + i
    return sume
print(amicable())
