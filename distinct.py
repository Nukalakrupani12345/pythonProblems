def distinctPowers():
    liste = []
    count = 0
    liste = []
    for i in range(2, 101):
        for j in range(2, 101):
            if (i ** j) not in liste:
                liste.append(i ** j)
                count += 1
    return count
print(distinctPowers())
