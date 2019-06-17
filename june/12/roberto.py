def getItinerary(flights, start):
	path = [start]
	vertices = set()
	neighbors = {}
	available = {}
	for origin, destination in flights:
		available[(origin, destination)] = True
		vertices.add(origin)
		vertices.add(destination)
		if origin not in neighbors:
			neighbors[origin] = []
		neighbors[origin].append(destination)
	for origin in neighbors:
		neighbors[origin].sort()

	def getPath(origin, i=0):
		if (i == len(flights)):
			return True

		for destination in neighbors[origin]:
			if not available[(origin, destination)]: continue
			path.append(destination)
			available[(origin, destination)] = False
			if getPath(destination, i+1):
				return True
			available[(origin, destination)] = True
			path.pop()
		return False

	if getPath(start):
		return path
	else:
		return "null"

n = int(input())
flights = []
for i in range(n):
	origin, destination = input().split()
	flights.append((origin, destination))
start = input()
print(getItinerary(flights, start))
