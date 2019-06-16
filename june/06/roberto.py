def dutchFlag(l):
	start = 0
	middle = 0
	end = len(l) - 1
	while (middle <= end):
		if (l[middle] == 'R'):
			l[start], l[middle] = l[middle], l[start]
			start += 1
			middle += 1
		elif (l[middle] == 'G'):
			middle += 1
		else: # (l[middle] == 'B'):
			l[middle], l[end] = l[end], l[middle]
			end -= 1
	return l

l = input().split()
print(dutchFlag(l))
