def justify(l, k):
	result = []
	start = 0
	while (start < len(l)):
		line = []
		count = 0
		spaces = 0
		i = start
		count += len(l[i])
		i += 1
		while (i < len(l) and count + len(l[i]) + 1 <= k):
			count += len(l[i]) + 1
			i += 1
			spaces += 1
		if (spaces == 0):
			result.append([l[start] + " " * (k - len(l[start]))])
			start += 1
			continue
		div = (k - count)//spaces
		rest = (k - count)%spaces
		line.append(l[start])
		start += 1
		for _ in range(rest):
			line.append(" " * (2 + div))
			line.append(l[start])
			start += 1
		for _ in range(spaces - rest):
			line.append(" " * (1 + div))
			line.append(l[start])
			start += 1
		result.append("".join(line))
	return result

k = int(input())
l = input().split()
print(justify(l, k))
