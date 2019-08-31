def canBePalindrome(s, k):
	def helper(s, start, end, k):
		if (k < 0):
			return False
		if (start > end):
			return k >= 0
		if (s[start] == s[end]):
			return helper(s, start+1, end-1, k)
		else:
			return helper(s, start, end-1, k-1) or helper(s, start+1, end, k-1)

	return helper(s, 0, len(s)-1, k)

s = input()
k = int(input())
print(canBePalindrome(s, k))
