from collections import heapq

def running_medians(arr):
    smaller = []
    bigger = []

    n = 0
    for num in arr:
        if not bigger or num < bigger[0]:
            heapq.heappush(smaller, -num)
        else:
            heapq.heappush(bigger, num)
        n += 1

        if n % 2 == 0:
            print("{:}".format((bigger[0]-smaller[0])/2))
        else:
            