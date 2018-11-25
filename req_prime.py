def prime():
	count1 = 0
	for i in range(2, 20):
		count = 0
		for j in range(2, i // 2 + 1):
			if i % j == 0:
				count = 1
				continue
		if count == 