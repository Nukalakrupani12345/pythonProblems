def fibonacci(index):
    if index == 1 or index == 2:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)
def getFiboIndex():
    for i in range(1, 100000):
        fibonacciNumber = fibonacci(i)
        count = 0
        while fibonacciNumber != 0:
            count += 1
            fibonacciNumber = fibonacciNumber // 10
        if count == 1000:
            return i
print(getFiboIndex())

