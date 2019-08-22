def swap(a):
	return ((0b10101010 & a) >> 1) | ((0b01010101 & a) << 1)

x = int(input())
print(swap(x))
