def longestIncreasingSubsequence(l, i=0, d={}): # longest increasing subsequence starting at i
	if i == len(l) - 1:
		return [l[i]]
	if i in d:
		return d[i]
	longest = 1, [l[i]]
	for j in range(i+1, len(l)):
		if l[i] <= l[j]:
			include = [l[i]] + longestIncreasingSubsequence(l, j, d)
			if len(include) >= longest[0]:
				longest = len(include), include
	d[i] = longest[1]
	return d[i]

def solution(l): # because longest increasing subsequence doesn't necessarily start at first element
	d = {}
	subsequences = [longestIncreasingSubsequence(l, i, d) for i in range(len(l))]
	result = []
	for subsequence in subsequences:
		if (len(subsequence) > len(result)):
			result = subsequence
	return result

l = [int(x) for x in input().split()]
print(solution(l))

# [0, 4, 6, 9, 13, 15] is another solution
