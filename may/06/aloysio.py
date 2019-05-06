# Aloysio


def sol(arr):
    for i in range(len(arr)):
        while len(arr) >= arr[i] > 0 and arr[i] != i + 1:
            swp = arr[i] -1
            arr[i], arr[swp] = arr[swp], arr[i]

    for i in range(len(arr)):
        if arr[i] - 1 != i:
            return i + 1
    return len(arr) + 1


if __name__ == "__main__":
    print(sol(list(map(int, input().split()))))
