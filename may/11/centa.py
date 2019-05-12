# Use dynamic programming!
#
# Let L[i] be the largest sum of non-adjacent elements on the subarray 
# arr[0:i] and I[i] be the largest sum of non-adjacent elements on the
# subarray arr[0:i] including the last element (index i-1). Then:
#
# I[i] = arr[i-1] + L[i-2]
#
# L[i] = max(I[i], L[i-1])
#
# with B[0] = 0 and B[1] = arr[0].
# Note that it is only necessary to store the last two values of B, so
# this solution has O(1) space complexity and O(n) runtime.

def largest_non_adjacent_sum(arr):
    L0 = 0
    L1 = arr[0]

    for i in range(2, len(arr)+1):
        L1, L0 = max(arr[i-1] + L0, L1), L1
    
    return L1


if __name__ == "__main__":
    # get array from input
    arr = list(map(int, input().split()))

    # get answer
    ans = largest_non_adjacent_sum(arr)

    # print answer
    print(ans)
