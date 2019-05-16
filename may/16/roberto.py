def y(x):
	return (1 - x**2)**.5

def pi(n):
	X = [x/n for x in range(n)] # x in [0, 1-1/n]
	area = 0
	for i in range(len(X)-1):
		# area += y(X[i])/n # Rectangle
		area += (y(X[i])+y(X[i+1]))/(2*n) # Trapezium
	return 4*area

def solution(N):
	for n in range(N):
		print(pi(n))

N = int(input())
solution(N)
# N >= 360, for 3 decimal cases accuracy
