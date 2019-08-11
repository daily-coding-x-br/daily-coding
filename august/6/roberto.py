def getPermutations(l, using=set()):
	if (len(using) == len(l)):
		return [[]]
	result = []
	for i in range(len(l)):
		if l[i] not in using:
			using.add(l[i])
			perms = getPermutations(l, using)
			using.remove(l[i])
			for perm in perms:
				result.append([l[i]] + perm)
	return result

l = [int(x) for x in input().split()]
print(getPermutations(l))
