def collatz():
    maxi = 0
    for i in range(2, 10000000):
        count = 0
        temp = i
        while temp != 1:
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = 3 * temp + 1
            count += 1
        if count > maxi:
            maxi = count
            number = i
    return number
print(collatz())	
