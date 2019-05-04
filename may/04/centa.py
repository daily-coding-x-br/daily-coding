# O(n) runtime and O(n) space complexity
# same ideia as the cpp one

def problem_2(arr):
    n = len(arr)

    left = [1 for _ in range(n)]
    right = [1 for _ in range(n)]

    for i in range(n-1):
        left[i+1] = arr[i]*left[i]

    for i in range(n-1, 0, -1):
        right[i-1] = arr[i]*right[i]

    return [left[i]*right[i] for i in range(n)]


if __name__ == "__main__":
    # read array from input
    arr = list(map(int, input().split()))

    # get the answer
    ans = problem_2(arr)

    # print the answer
    print(ans)
