def sumGeneration():
    for i in range(1, 100):
        sume = 0
        for j in range(1, i + 1):
            sume = sume + j
        count = numberOfFactors(sume)
        if count > 500:
            return sume
def numberOfFactors(sume):
    count = 1
    for factor in range(1, sume//2+1):
        if sume % factor == 0:
            count += 1
    return count
print(sumGeneration())
