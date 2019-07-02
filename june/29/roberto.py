def rotatedBinarySearch(l, k):
	low = 0
	high = len(l) - 1
	while (low <= high):
		mid = (low + high)//2
		if (l[mid] == k):
			return mid
		if (l[mid] < l[high]):
			if (l[mid] < k and k <= l[high]):
				low, high = mid + 1, high
			else:
				low, high = low, mid - 1
		else: # (l[mid] >= l[high]):
			if (l[low] <= k and k < l[mid]):
				low, high = low, mid - 1
			else:
				low, high = mid + 1, high
	return None

l = [int(x) for x in input().split()]
k = int(input())
print(rotatedBinarySearch(l, k))
