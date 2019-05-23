def solution(n1, n2):
	len1 = getLength(n1)
	len2 = getLength(n2)
	l, s = (n1, n2) if len1 > len2 else (n2, n1)
	lenl, lens = max(len1, len2), min(len1, len2)
	travl = l
	travs = s
	for i in range(lenl - lens):
		travl = travl.next()

	for i in range(lens):
		if (travl == travs):
			return travl
		travl, travs = travl.next(), travs.next()

	return travl

def getLength(n1):
	trav = n1
	result = 0
	while (trav):
		trav = trav.next()
		result += 1
	return result
