# O(n) runtime and O(1) space complexity
#
# Push every positive integer smaller than n (ther array size)
# to its position on the queue.
# Notice that the smallest positive integer that is not on the
# array cannot be bigger than n+1. 
# Do a second pass on the array and return the first element 
# that is not equal to its index.
#
# by: Centa

def smallest_integer_not_present(arr):
    n = len(arr)
    arr.append(-1) # so that the index n is reachable

    for i in range(n):
        tmp = arr[i]
        while (tmp <= n) and (tmp > 0) and (tmp != arr[tmp]):
            arr[tmp], tmp = tmp, arr[tmp] # swap

    for i in range(1, n+1):
        if arr[i] != i:
            return i
    
    return n+1 # the arr is [1, 2, 3, ..., n]


if __name__ == "__main__":
    # read array from stdin
    arr = list(map(int, input().split()))

    # get the answer
    ans = smallest_integer_not_present(arr)

    # print the answer
    print(ans)
