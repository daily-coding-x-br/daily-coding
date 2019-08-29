def squareAndSort(l):
	right = 0
	while (right < len(l) and l[right] < 0):
		right += 1
	left = right - 1
	square = [x**2 for x in l]
	result = []
	while (left >= 0 and right < len(l)):
		if (square[right] < square[left]):
			result.append(square[right])
			right += 1
		else:
			result.append(square[left])
			left -= 1
	while (left >= 0):
		result.append(square[left])
		left -= 1
	while (right < len(l)):
		result.append(square[right])
		right += 1
	return result

l = [int(x) for x in input().split()]
print(squareAndSort(l))
