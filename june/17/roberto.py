# O(n^2) time, O(1) space
def longestPalindromicContiguousSubstring(s):
	result = (0, 0)
	# odd length palindromes:
	for mid in range(len(s)):
		low = mid
		high = mid
		while (0 <= low and high < len(s) and s[low] == s[high]):
			low -= 1
			high += 1
		low += 1
		if (high - low > result[1] - result[0]):
			print("long: " + s[result[0]:result[1]])
			result = low, high
	# even length palindromes:
	for mid in range(len(s)):
		low = mid
		high = mid + 1
		while (0 <= low and high < len(s) and s[low] == s[high]):
			low -= 1
			high += 1
		low += 1
		if (high - low > result[1] - result[0]):
			result = low, high
			print("long even: " + s[result[0]:result[1]])
	return s[result[0]:result[1]]

l = input()
print(longestPalindromicContiguousSubstring(l))
