def palindrome():
	large = 0
	for i in range(100, 1000):
		for j in range(i + 1, 1000):
			if reverse(i * j) == i *j:
				if i * j > large:
					large = i * j
	return large
def reverse(num):
	rev = 0
	while num > 0:
		rem = num % 10
		rev = rev * 10 + rem
		num = num // 10
	return rev
print(palindrome())
