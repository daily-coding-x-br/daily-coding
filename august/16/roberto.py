def canReach(l, i=0, mem={}):
	if (i == len(l)-1):
		return True
	if i in mem:
		return mem[i]
	for j in reversed(range(l[i])):
		if (canReach(l, i+1+j, mem)):
			mem[i] = True
			return mem[i]
	mem[i] = False
	return mem[i]

l = [int(x) for x in input().split()]
print(canReach(l))
