def histogram(l):
	m_index = 0
	m = l[0]
	for i in range(len(l)):
		if (l[i] > m):
			m_index = i
			m = l[i]

	# left side
	left_max_index = 0
	i = 0
	left_sum = 0
	while (i < m_index):
		if (l[i] > l[left_max_index]):
			left_max_index = i
		left_sum += l[left_max_index] - l[i]
		i += 1

	# right side
	right_max_index = len(l) - 1
	i = len(l) - 1
	right_sum = 0
	while (i > m_index):
		if (l[i] > l[right_max_index]):
			right_max_index = i
		right_sum += l[right_max_index] - l[i]
		i -= 1

	return left_sum + right_sum

l = [int(x) for x in input().split()]
print(histogram(l))
