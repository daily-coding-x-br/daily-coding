import heapq

def running_medians(arr):
    smaller = []
    bigger = []

    for num in arr:
        # Insert
        if not bigger or num >= bigger[0]:
            heapq.heappush(bigger, num)
        else:
            heapq.heappush(smaller, -num)

        # Rebalance
        if len(bigger) > len(smaller) + 1:
            tmp = heapq.heappop(bigger)
            heapq.heappush(smaller, -tmp)
        elif len(smaller) > len(bigger) + 1:
            tmp = -heapq.heappop(smaller)
            heapq.heappush(bigger, tmp)

        # Print current median
        if len(smaller) > len(bigger):
            print("{:}".format(-smaller[0]))
        elif len(smaller) < len(bigger):
            print("{:}".format(bigger[0]))
        else:
            print("{:}".format((bigger[0]-smaller[0])/2))


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    running_medians(arr)