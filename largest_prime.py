def prime(n):
	large = 0
	i = 1
	while i < n:
		if  n % i == 0:
			if i > large and isprime(i):
				large = i
		i = i + 1
	return large
def isprime(x):
	count = 0
	for i in range(2, x // 2 + 1):
		if x % i == 0:
			return False
	return True
	
print(prime(13195))
			
