def maxProfit(l, k):
	visited = [False] * len(l)
	result = 0
	for j in range(k):
		lowest = -1
		buy, sell = -1, -1
		for i in range(len(l)):
			if visited[i]:
				continue
			lowest = i if lowest == -1 or l[i] < l[lowest] else lowest
			buy, sell = (lowest, i) if (buy, sell) == (-1, -1) or l[i] - l[lowest] > l[sell] - l[buy] else (buy, sell)
		result += l[sell] - l[buy]
		visited[sell] = True
		visited[buy] = True
	return result

l = [int(x) for x in input().split()]
k = int(input())
print(maxProfit(l, k))
