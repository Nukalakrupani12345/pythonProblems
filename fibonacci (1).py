def fibonacci():
	fibm1 = 1
	fibm2 = 2
	fibm3 =  fibm1 + fibm2
	sume = 0
	while fibm1 < 4000000:
		if iseven(fibm1):
			sume = sume + fibm1
		fibm1 = fibm2
		fibm2 = fibm3
		fibm3 = fibm1 + fibm2
	return sume
def iseven(num):
	return num % 2 == 0		
print(fibonacci())

