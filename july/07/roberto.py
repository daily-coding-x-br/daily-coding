import random
p = 0.8

def toss_biased():
	r = random.random() # float in [0, 1)
	return 1 if r < p else 0

def toss_unbiased():
	while (True):
		r1 = toss_biased()
		r2 = toss_biased()
		if (r1 == 1 and r2 == 0): return 1
		if (r1 == 0 and r2 == 1): return 0

n = 5000000
sum = 0
for i in range(n):
	sum += toss_unbiased()

print(sum/n)
