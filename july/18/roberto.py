def getMergedIntervals(intervals):
	starts = [interval[0] for interval in intervals]
	ends = [interval[1] for interval in intervals]
	starts.sort()
	ends.sort()
	result = []
	count = 0
	current = 0, 0
	while (ends):
		if (len(starts) == 0):
			current = current[0], ends[-1]
			result.append(current)
			break
		if (starts[0] < ends[0]):
			if (count == 0):
				current = starts[0], 0
			count += 1
			starts.pop(0)
		else:
			count -= 1
			if (count == 0):
				current = current[0], ends[0]
				result.append(current)
			ends.pop(0)
	return result

intervals = []
n = int(input())
for i in range(n):
	s, e = [int(x) for x in input().split()]
	intervals.append((s, e))
print(getMergedIntervals(intervals))
