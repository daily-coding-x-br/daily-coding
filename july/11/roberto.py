def nthPerfectNumber(n): # if perfect number < 100
	if (n == 1):
		return 19
	if (n <= 9):
		return 10*n + (10 - n)

def nthPerfectNumber2(remaining, current=19): # if perfect numbr < 1000
	if (remaining == 0):
		return current
	units = current%10
	tens = (current%100)//10
	sum = units + tens
	if (remaining <= units):
		return current - 1*units - 10*tens + 10*(remaining) + 1*(sum - remaining)
	hundreds = (current%1000)//100
	if (hundreds < 9):
		current = current - 1*units - 10*tens - 100*hundreds + 100*(hundreds + 1) + 10*0 + 1*(sum - 1)
		return nthPerfectNumber2(remaining - units - 1, current)

n = int(input())
print(nthPerfectNumber2(n))
