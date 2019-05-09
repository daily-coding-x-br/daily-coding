def countDecodings(s, d = {}, i = 0):
	if (i in d):
		return d[i]
	if (i == len(s) - 1 or i == len(s)):
		d[i] = 1
	elif (int(s[i:i + 2]) <= 26):
		d[i] = countDecodings(s, d, i+1) + countDecodings(s, d, i+2)
	else: #(int(s[i:i + 2]) > 26)
		d[i] = countDecodings(s, d, i+1)
	return d[i]

s = input()
print(countDecodings(s))
