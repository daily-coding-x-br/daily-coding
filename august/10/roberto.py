def getMinimumSteps(points):
	result = 0
	for i in range(len(points)-1):
		next, prev = points[i+1], points[i]
		dx = abs(next[0] - prev[0])
		dy = abs(next[1] - prev[1])
		result += max(dx, dy)
	return result

n = int(input())
points = []
for i in range(n):
	points.append([int(x) for x in input().split()])
print(getMinimumSteps(points))
