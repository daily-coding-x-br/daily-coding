import math

# O(n) time, O(n) space
def fib(n, d={}):
	if (n in d): return d[n]
	if (n == 1 or n == 0):
		return 1
	d[n] = fib(n-1) + fib(n-2)
	return d[n]

# O(n) time, O(1) space
def fib2(n):
	a0 = 1
	a1 = 1
	for i in range(n-1):
		a0, a1 = a1, a1 + a0
	return a1

# O(1) time, O(1) space (Only accurate until n = 69)
def fib3(n):
	return round((((1+math.sqrt(5))/2)**(n+1) - ((1-math.sqrt(5))/2)**(n+1))/math.sqrt(5))

# O(n) time, O(n) space
def solution(n, l, d={}):
	if (n in d): return d[n]
	if (n < 0):
		return 0
	if (n == 1 or n == 0):
		return 1
	result = 0
	for i in range(len(l)):
		result += solution(n - l[i], l)
	d[n] = result
	return d[n]


n = int(input())
l = [int(x) for x in input().split()]
print(solution(n, l))
