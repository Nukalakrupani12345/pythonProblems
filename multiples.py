def multiples():
	sume = 0
	i = 1
	while i < 1000:
		if i % 3 == 0 or i % 5 == 0:
			sume = sume + i
		i = i + 1
	return sume
print(multiples())
