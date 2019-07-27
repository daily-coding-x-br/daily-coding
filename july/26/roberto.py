def logic(x, y, b):
	return (b&1)*x + (not (b&1))*y

x, y, b = [int(x) for x in input().split()]
print(logic(x, y, b))
