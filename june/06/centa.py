def segregate_rgb(arr):
    n = len(arr)
    r_count, b_count = 0, 0

    i = 0
    while i < n - b_count:
        if arr[i] == 'B':
            arr[n - b_count - 1], arr[i] = arr[i], arr[n - b_count - 1]
            b_count += 1
        if arr[i] == 'R':
            arr[r_count], arr[i] = arr[i], arr[r_count]
            r_count += 1
        i += 1
        
    return arr


if __name__ == "__main__":
    arr = input().split()

    print(segregate_rgb(arr))
