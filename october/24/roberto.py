import random

def evaluate(p):
	r = random.random()
	i = 0
	r -= p[i]
	while (r > 0 and i < len(p)-1):
		i += 1
		r -= p[i]
	return i

def markov(m, starting_state, num_steps):
	n = len(m)
	count = [0] * n
	t = starting_state
	for i in range(num_steps):
		p = m[t]
		t = evaluate(m[t])
		count[t] += 1
	return count

starting_state = int(input())
n = int(input())
m = [[0]*n for i in range(n)]
for i in range(n):
	m[i] = [float(x) for x in input().split()]
num_steps = int(input())

print(markov(m, starting_state, num_steps))
