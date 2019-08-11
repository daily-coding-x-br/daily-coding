def addToDictionary(end, start, x):
	if x-1 in start:
		start[x] = start[x-1]
	if x+1 in end:
		end[x] = end[x+1]
	end[start[x]] = end[x]
	start[end[x]] = start[x]

def longestConsecutiveSequence(l):
	end = {}
	start = {}
	for x in l:
		end[x], start[x] = x, x
	for x in l:
		addToDictionary(end, start, x)
	result = 0
	for element in end:
		result = max(end[element] - element + 1, result)
	return result

l = [int(x) for x in input().split()]
print(longestConsecutiveSequence(l))
