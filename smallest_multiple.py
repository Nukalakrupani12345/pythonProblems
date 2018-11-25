def smallest():
	for i in range(1, 3000):
		count = 0
		for j in range(2, 11):
			if i % j != 0:
				count = 1
				continue
		if count == 0:
			return i
print(smallest())
