def minCoins(n):
	coins = [25, 10, 5, 1]
	result = 0
	for coin in coins:
		result += n//coin
		n %= coin
	return result

n = int(input())
print(minCoins(n))
