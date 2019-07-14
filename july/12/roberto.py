import random

def rand7():
	return random.randint(0, 6)

def rand5():
	r = rand7()
	return r if r < 5 else rand5()

l = [0]*5
for i in range(50000):
	l[rand5()] += 1
print(l)
