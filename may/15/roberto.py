def solution(s, k):
	start = 0
	end = 0
	d = {}
	maximum = (0, 0)
	while (start < len(s)):
		while (end < len(s) and len(d) <= k):
			d[s[end]] = 1 + (d[s[end]] if s[end] in d else 0)
			end += 1
		if (end - start > maximum[1] - maximum[0]):
			maximum = start, end
		d[s[start]] -= 1
		if (d[s[start]] == 0): del(d[s[start]])
		start += 1
	return s[maximum[0]:maximum[1]-1]

s = input()
k = int(input())
print(solution(s, k))
