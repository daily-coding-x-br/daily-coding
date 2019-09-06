def rotate(l, k):
	n = len(l)
	visited = [False] * n
	for i in range(n):
		if (visited[i]):
			continue
		j = i
		temp = l[j]
		while (not visited[j%n]):
			l[j%n] = l[(j + k)%n]
			visited[j%n] = True
			j += k
		l[(j-k)%n] = temp
	return

l = [int(x) for x in input().split()]
k = int(input())
rotate(l, k)
print(l)
