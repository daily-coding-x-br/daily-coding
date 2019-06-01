# Not sure if optimal, I've never seen this one before
# O(n*log n) runtime and O(n) space complexity
import heapq

def trapped_water(walls):
    total_water = 0
    index_left = {}
    height_left = []
    
    water_level = 0
    for i, right in enumerate(walls):
        if right > water_level:
            while height_left:
                left = height_left[0]
                if left <= right:
                    total_water += (i - index_left[left] - 1) * (left - water_level)
                    water_level = left
                    heapq.heappop(height_left)

                else:
                    total_water += (i - index_left[left] - 1) * (right - water_level)
                    break

            water_level = 0
            index_left[right] = i
            heapq.heappush(height_left, right)

    return total_water


if __name__ == "__main__":
    walls = list(map(int, input().split()))

    print(trapped_water(walls))