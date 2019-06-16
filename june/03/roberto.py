def arbitrage(a):
	n = len(a)
	for i in range(n):
		for j in range(i+1, n):
			if (a[i][j] * a[j][i] != 1):
				return True

	for i in range(1, n):
		for j in range(1, n):
			if (a[i][j] != a[0][j] * a[i][0]):
				return True

	return False



n = int(input())
a = []
for i in range(n):
	a.append([int(x) for x in input().split()])
print(arbitrage(a))
