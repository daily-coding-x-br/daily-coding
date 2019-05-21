# This one is tricky

from collections import deque


def max_k_subarrays(k, arr):
    q = deque()

    # Initialize window with the first k elements
    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)

    # Slide the deque through the array
    for i in range(k, len(arr)):
        # The front is the maximum for this window
        print(arr[q[0]])

        # Slide the window to the right
        if q and q[0] <= i - k:
            q.popleft()

        # Add the new element respecting the invariant
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)

    # Print the maximum for the last window
    print(arr[q[0]])


if __name__ == "__main__":
    k = int(input())
    arr = list(map(int, input().split()))

    max_k_subarrays(k, arr)
    